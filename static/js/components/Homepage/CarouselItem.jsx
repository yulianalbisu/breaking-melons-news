const { Container, Row, Col } = ReactBootstrap;
const { useHistory } = ReactRouterDOM;

const CarouselItem = ({newsItem, viewNews, Carousel}) => {

    const months = ["Jan", "Feb", "March", "April", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"];

    let history = useHistory();

    const handleClickArticle = (news) => {
        viewNews(news)
        history.push(`/articles/${news.news_id}`)
      }

    return (
         <Container style={{backgroundImage: `url(${newsItem.picture_link})`}} className='carousel-div'>
                    <Row>
                      <Col xs={1}>
                        <div className='carousel-date-div'>
                          <div className='carousel-inner-date'>
                              {new Date(newsItem.date_post).getDate() + 1}
                          </div>
                          <div className='carousel-inner-date'>
                              {months[new Date(newsItem.date_post).getMonth()]}
                          </div>
                        </div>
                      </Col>
                      <Col xs={10}>
                        <img 
                        className="d-block w-100 carousel-picture"
                        src={newsItem.picture_link}
                        alt={newsItem.summary}
                        />
                        <Carousel.Caption className="carousel-caption-box">
                          <h3 className='carousel-item-title'><a className='carousel-item-title-link' onClick={() => handleClickArticle(newsItem)} href="#" className="carousel-link">{newsItem.title}</a></h3>
                          <p>{newsItem.summary}</p>
                        </Carousel.Caption>
                      </Col>
                    </Row>
        </Container>
    );
}