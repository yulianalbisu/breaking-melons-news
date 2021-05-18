const { Container, Row, Col } = ReactBootstrap;
const { useState, useEffect } = React;

const App = () => {

    return (
        <Container>
            <Row>
                <Col>Col 1</Col>
                <Col>Col 2</Col>
            </Row>
        </Container>
    )
}

ReactDOM.render(<App />, document.querySelector('#root'));