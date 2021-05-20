const { Container, Row, Col, Carousel } = ReactBootstrap;
const { useState } = React;
const NewsCarousel = ({news}) => {

    const [index, setIndex] = useState(0);

    const handleSelect = (selectedIndex, e) => {
      setIndex(selectedIndex);
    };
    
    const months = ["Jan", "Feb", "March", "April", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"];

    return (
         <Carousel activeIndex={index} onSelect={handleSelect}>
              {news.map((newsItem, newsIndex) => (
                <Carousel.Item key={newsIndex}>
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
                        <Carousel.Caption>
                          <h3 className='carousel-item-title'>{newsItem.title}</h3>
                          <p>{newsItem.summary}</p>
                        </Carousel.Caption>
                      </Col>
                    </Row>
                  </Container>
                </Carousel.Item>
              ))}
            </Carousel>
    );
};