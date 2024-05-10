'use client';

import Navbar from 'react-bootstrap/Navbar';

export default function Footer() {
	return (
		<Navbar
			className="bg-body-tertiary justify-content-center "
			fixed="bottom">
			<Navbar.Text size="sm">
				Created with autism by{' '}
				<a href="https://github.com/novastar88" target="_blank">
					novastar88
				</a>
			</Navbar.Text>
		</Navbar>
	);
}
