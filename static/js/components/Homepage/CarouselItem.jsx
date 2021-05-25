const { Container, Row, Col } = ReactBootstrap;
const { useHistory } = ReactRouterDOM;

const CarouselItem = ({newsItem, viewNews}) => {

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
                          <div>
                              {new Date(newsItem.date_post).getDate() + 1}
                          </div>
                          <div>
                              {months[new Date(newsItem.date_post).getMonth()]}
                          </div>
                        </div>
                      </Col>
                      <Col xs={10}>
                        <img
                        className="d-block w-100"
                        src={newsItem.picture_link}
                        alt={newsItem.summary}
                        />
                        <div>
                          <h3 className='carousel-item-title'><a onClick={() => handleClickArticle(newsItem)} href="#" className="carousel-link">{newsItem.title}</a></h3>
                          <p>{newsItem.summary}</p>
                        </div>
                      </Col>
                    </Row>
        </Container>
    );
}