import Container from 'react-bootstrap/Container';
import Image from 'react-bootstrap/Image';
import Alert from 'react-bootstrap/Alert';
import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/Row';

function NotFound() {
	return (
		<Container className="mt-3">
			<Alert variant="warning">Nie znaleziono zasobu ;[</Alert>
			<Row>
				<Col sm={3} />
				<Col>
					<Image src="404.jpg" />
				</Col>
				<Col sm={3} />
			</Row>
		</Container>
	);
}

export default NotFound;
