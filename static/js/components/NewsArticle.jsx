const { Container, Row, Col } = ReactBootstrap;

const NewsArticle = ({ newsItem }) => {
    return (
        <Containter>
            <Row>
                {newsItem.title}
            </Row>
            <Row>
                <Col>
                    {newsItem.user_name}
                </Col>
                <Col>
                    {newsItem.date_post}
                </Col>
            </Row>
            <Row>
                <img src={newsItem.picture_link}/>
            </Row>
            <Row>
                {newsItem.article_text.split("|").map((para, index) => 
                <div key={index}>
                    {para}
                </div>
                )}
            </Row>
        </Containter>
    )
}