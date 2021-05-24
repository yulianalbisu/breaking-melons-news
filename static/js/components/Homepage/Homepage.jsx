const { Container, Row, Col } = ReactBootstrap;

const Homepage=({news, externalNews, viewNews}) => {


    return (
        <Container fluid>
            <Row>
            <Col xs={{ span: 10, offset: 1 }}>
                <NewsCarousel
                news={news}
                viewNews={viewNews}
                />
            </Col>

            </Row>
            <Container>
            <Row className="d-flex justify-content-center">
                {externalNews.map((newsItem, newsInd) =>
                    <Col key={newsItem.external_news_id} xs={7} md={5} lg={4} xl={3} className="ml-4" >
                        <NewsCard
                        newsInd={newsInd}
                        newsItem={newsItem}
                        />
                    </Col>
                )}
            </Row>
            </Container>
        </Container>
    );
};