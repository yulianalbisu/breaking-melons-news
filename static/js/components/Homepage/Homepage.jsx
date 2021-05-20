const { Container, Row, Col } = ReactBootstrap;

const Homepage=({news}) => {

    const catMelon = {
        title: "Why Does My Cat Like Canteloupe?",
        image: "https://www.farmersalmanac.com/wp-content/uploads/2020/11/cat-cantaloupe.jpeg",
        externalLink: "https://www.farmersalmanac.com/why-does-my-cat-like-cantaloupe-22108"
    }

    return (
        <Container>
            <Row>
            <Col>
                <NewsCarousel
                news={news}
                />
            </Col>

            </Row>
            <Row>
            <Col>
                <NewsCard
                catMelon={catMelon}
                />
            </Col>
            </Row>

        </Container>
    );
};