const { Container, Row, Col } = ReactBootstrap;

const NewsArticle = ({ newsItem }) => {
    return (
        <Container className='article-style'>
            <Row className='title-article'> 
               <h1> {newsItem.title} </h1>         
            </Row>
            <Row>
                <Col className='autor-article'>
                    {newsItem.user_name}
                </Col>
                <Col xs={2} className='date-box date-article'>
                    {newsItem.date_post.slice(0,-13)}
                </Col>
            </Row>
            <Row>
                <img className='image-article' src={newsItem.picture_link}/>
            </Row>
            <Row className='article-placeholder'>
                {newsItem.article_text.split("|").map((para, index) => 
                <div key={index}>
                    {para}
                </div>
                )}
            </Row>
        </Container>
    )
}