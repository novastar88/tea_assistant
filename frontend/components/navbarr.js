'use client';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';
import Form from 'react-bootstrap/Form';
import { Moon } from 'react-bootstrap-icons';
// import { useShallow } from 'zustand/react/shallow';

export default function Navbarr() {
	return (
		<Navbar expand="lg" className="bg-body-tertiary justify-content-start">
			<Navbar.Toggle aria-controls="basic-navbar-nav" />
			<Navbar.Collapse id="basic-navbar-nav">
				<Nav className="me-auto">
					<Nav.Link href="/" className="ms-2">
						Home
					</Nav.Link>
					<Nav.Link href="/browse">Browse</Nav.Link>
					<NavDropdown title="Edit" id="basic-nav-dropdown">
						<NavDropdown.Item href="/">Produkty</NavDropdown.Item>
					</NavDropdown>
				</Nav>
			</Navbar.Collapse>
			<Form.Check // prettier-ignore
				type="switch"
				id="darkmode-toggle"
				label="Dark Mode"
				className="me-2"
			/>
			<Moon />
		</Navbar>
	);
}
