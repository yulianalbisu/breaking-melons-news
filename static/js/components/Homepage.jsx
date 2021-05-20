const { Container, Row, Col } = ReactBootstrap;

const Homepage=({news}) => {

    return (
        <Container>
            <Row>
            <Col>
                <NewsCarousel
                news={news}
                />
            </Col>
            </Row>
        </Container>
    );
};