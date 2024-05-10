import Table from 'react-bootstrap/Table';

export default function MainTable({ tableData }) {
	return (
		<Table striped bordered hover>
			<thead>
				<tr>
					<th>id</th>
					<th>Nazwa</th>
					<th>Ocena</th>
					<th>Pojemnik</th>
					<th>Status</th>
					<th>Sklep</th>
					<th>Opis</th>
					<th>Ostatnio użyte</th>
					<th>g/ml</th>
					<th>Data dodania</th>
				</tr>
			</thead>
			<tbody>
				{tableData.map((item, index) => {
					return (
						<tr key={index}>
							<td>{item.id}</td>
							<td>{item.name}</td>
							<td>{item.rating}</td>
							<td>{item?.container_symbol}</td>
							<td>{item?.status.name}</td>
							<td>{item?.shop.name}</td>
							<td>{item?.short_description}</td>
							<td>{item?.last_used}</td>
							<td>{item?.amount}</td>
							<td>{item?.created_at}</td>
						</tr>
					);
				})}
			</tbody>
		</Table>
	);
}
