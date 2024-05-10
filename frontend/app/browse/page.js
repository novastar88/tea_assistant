import Table from 'react-bootstrap/Table';
import Container from 'react-bootstrap/Container';
import MainTable from '@/components/browse/mainTable';
import Sidebar from '@/components/browse/sidebar';
import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/Row';

export const dynamic = 'force-dynamic';

async function getTableData() {
	console.log(`${process.env.NEXT_PUBLIC_API_FULL_URL}resources/product/all`);
	const a = await fetch(
		`${process.env.NEXT_PUBLIC_API_FULL_URL}resources/product/all`,
		{
			method: 'GET',
			headers: {
				'Content-type': 'application/json; charset=UTF-8',
				// Authorization: `Token `,
				Authorization: `Token ${process.env.NEXT_PUBLIC_API_USER_TOKEN}`,
			},
		}
	);

	if (!a.ok) {
		throw new Error('fetching error');
	}

	return a.json();
}

async function Browser() {
	const tableData = await getTableData();

	return (
		<>
			<Container className="mt-3" fluid>
				<Row>
					<Col sm={2}>
						<Sidebar />
					</Col>
					<Col>
						<MainTable tableData={tableData} />
					</Col>
					<Col sm={1}></Col>
				</Row>
			</Container>
		</>
	);
}

export default Browser;
