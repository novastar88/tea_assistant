'use client';
import Container from 'react-bootstrap/Container';
import Button from 'react-bootstrap/Button';
import Alert from 'react-bootstrap/Alert';

export default function Error({ error, reset }) {
	return (
		<Container>
			<Alert variant="danger" className="mt-3">
				Error: {error.message}
			</Alert>
			<Button variant="primary" onClick={() => reset()}>
				Try again
			</Button>
		</Container>
	);
}
