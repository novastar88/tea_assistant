import Container from 'react-bootstrap/Container';
import Spinner from 'react-bootstrap/Spinner';

function Loading() {
	return (
		<Container className="mt-3">
			<p>Loading</p>
			<Spinner animation="border" size="lg" />
		</Container>
	);
}

export default Loading;
