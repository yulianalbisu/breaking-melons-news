const { Container, Row, Col } = ReactBootstrap;

const Homepage=({news, externalNews}) => {

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
                {externalNews.map(newsItem =>
                    <Col key={newsItem.external_news_id} xs={3}>
                        <NewsCard
                        newsItem={newsItem}
                        />
                    </Col>
                )}
            </Row>

        </Container>
    );
};