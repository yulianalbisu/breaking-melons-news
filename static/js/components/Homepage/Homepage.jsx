const { Container, Row, Col } = ReactBootstrap;

const Homepage=({news, externalNews, viewNews}) => {


    return (
        <Container>
            <Row>
            <Col>
                <NewsCarousel
                news={news}
                viewNews={viewNews}
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