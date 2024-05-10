'use client';

import Container from 'react-bootstrap/Container';
import Form from 'react-bootstrap/Form';
// import InputGroup from 'react-bootstrap/InputGroup';
// import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/Row';
import { create } from 'zustand';
// import { useShallow } from 'zustand/react/shallow';
import { useEffect } from 'react';

const sideBarState = create(() => ({
	order_by: null,
	direction: null,
	rating_max: 10,
	rating_min: 1,
	blocked_statuses: [],
	statuses: [],
}));

function orderByChange() {
	const a = document.getElementById('order_by_selector');
	sideBarState.setState({ order_by: a.value });
	console.log(sideBarState.getState());
}

function directionChange() {
	const a = document.getElementById('direction_selector');
	sideBarState.setState({ direction: a.value });
}

function ratingMaxChange() {
	const a = document.getElementById('rating_max_selector');
	sideBarState.setState({ rating_max: a.value });
}

function ratingMinChange() {
	const a = document.getElementById('rating_min_selector');
	sideBarState.setState({ rating_min: a.value });
}

function handleStatus(id, state) {
	let inArray = state.blocked_statuses.includes(id);

	if (inArray == true) {
		let itemIndex = state.blocked_statuses.indexOf(id);
		let tempArray = state.blocked_statuses;
		tempArray.splice(itemIndex, 1);

		sideBarState.setState({ blocked_statuses: tempArray });
	} else {
		let tempArray = state.blocked_statuses;
		tempArray.push(id);
		sideBarState.setState({ blocked_statuses: tempArray });
	}
}

export default function Sidebar() {
	const sbsState = sideBarState((state) => state);

	useEffect(() => {
		fetch(`${process.env.NEXT_PUBLIC_API_FULL_URL}resources/status/all`, {
			method: 'GET',
			headers: {
				'Content-type': 'application/json; charset=UTF-8',
				Authorization: `Token ${process.env.NEXT_PUBLIC_API_USER_TOKEN}`,
			},
		})
			.then((response) => response.json())
			.then((data) => sideBarState.setState({ statuses: data }));
	}, []);

	return (
		<Container className="bg-light border border-dark rounded">
			<Row className="pb-3 pt-1 border border-dark rounded">
				<Form>
					<Form.Label>Sortuj po polu</Form.Label>
					<Form.Select
						defaultValue={'id'}
						id="order_by_selector"
						onChange={() => orderByChange()}>
						<option value={'id'}>ID</option>
						<option value={'rating'}>Ocena</option>
						<option value={'last_used'}>Ostatnio użyte</option>
						<option value={'status'}>Status</option>
						<option value={'shop'}>Sklep</option>
						<option value={'created_at'}>Data dodania</option>
						<option value={'amount'}>g/ml</option>
					</Form.Select>
				</Form>
				<Form>
					<Form.Label className="mt-2">Kierunek</Form.Label>
					<Form.Select
						defaultValue={'asc'}
						id="direction_selector"
						onChange={() => directionChange()}>
						<option value={'asc'}>Rosnąco</option>
						<option value={'desc'}>Malejąco</option>
					</Form.Select>
				</Form>
			</Row>
			<Row className="mt-3 pt-1 border border-dark rounded">
				<Form>
					<Form.Label>Ocena max</Form.Label>
					<Form.Range
						min={1}
						max={10}
						step={1}
						defaultValue={10}
						id="rating_max_selector"
						onChange={() => ratingMaxChange()}
					/>
					<Form.Label>Aktualna wartość: {sbsState.rating_max}</Form.Label>
				</Form>
			</Row>
			<Row className="mt-3 pt-1 border border-dark rounded">
				<Form>
					<Form.Label>Ocena min</Form.Label>
					<Form.Range
						min={1}
						max={10}
						step={1}
						defaultValue={1}
						id="rating_min_selector"
						onChange={() => ratingMinChange()}
					/>
					<Form.Label>Aktualna wartość: {sbsState.rating_min}</Form.Label>
				</Form>
			</Row>
			<Row className="pb-2 mt-3 pt-1 border border-dark rounded">
				<Form>
					<Form.Label>Statusy</Form.Label>
					{sbsState.statuses.map((item, index) => {
						return (
							<Form.Check
								key={index}
								label={item.name}
								id={`status_item-${item.id}`}
								type="checkbox"
								defaultChecked={true}
								onChange={() => {
									handleStatus(item.id, sbsState);
								}}
							/>
						);
					})}
				</Form>
			</Row>
		</Container>
	);
}
