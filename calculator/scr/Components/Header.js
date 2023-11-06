import React, { Component } from "react";
import {
  Navbar,
  Nav,
  Container,
  FormControl,
  Button,
  Form,
} from "react-bootstrap";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Natural from "../Pages/Natural";
import Integer from "../Pages/Integer";
import Rational from "../Pages/Rational";
import Polynum from "../Pages/Polynum";
import Test from "../Pages/Test";

export default class Header extends Component {
  render() {
    return (
      <div>
        <Navbar collapseOnSelect expand="md" bg="dark" variant="dark">
          <Container>
            <Navbar.Toggle aria-controls="responsive-navbar-nav" />
            <Navbar.Collapse id="responsive-navbar-nav">
              <Nav className="mr-auto">
                <Nav.Link href="/">Natural</Nav.Link>
                <Nav.Link href="/int"> Integer</Nav.Link>
                <Nav.Link href="/rat"> Rational</Nav.Link>
                <Nav.Link href="/poly"> Polynom</Nav.Link>
                <Nav.Link href="/test"> Test</Nav.Link>
              </Nav>
              <Form inline>
                <div style={{ display: "flex" }}>
                  <Button className="mr-sm-2" variant="outline-info">
                    Search
                  </Button>
                </div>
              </Form>
            </Navbar.Collapse>
          </Container>
        </Navbar>

        <Router>
          <Routes>
            <Route exact path="/" element={<Natural />} />
            <Route exact path="/int" element={<Integer />} />
            <Route exact path="/rat" element={<Rational />} />
            <Route exact path="/poly" element={<Polynum />} />
            <Route exact path="/test" element={<Test />} />
          </Routes>
        </Router>
      </div>
    );
  }
}
