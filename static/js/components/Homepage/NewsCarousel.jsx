const { Container, Row, Col, Carousel } = ReactBootstrap;
const { useState } = React;
const NewsCarousel = ({news, viewNews}) => {

    const [index, setIndex] = useState(0);
    const handleSelect = (selectedIndex, e) => {
      setIndex(selectedIndex);
    };


    return (
         <Carousel activeIndex={index} onSelect={handleSelect}>
              {news.map((newsItem, newsIndex) => (
                <Carousel.Item key={newsIndex}>
                  <CarouselItem newsItem={newsItem} viewNews={viewNews}/>
                </Carousel.Item>
              ))}
            </Carousel>
    );
};