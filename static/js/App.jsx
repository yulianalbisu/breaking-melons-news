const { Container, Row, Col } = ReactBootstrap;
const { useState, useEffect } = React;

const App = () => {
  const [news, setNews] = useState([]);
  const [index, setIndex] = useState(0);

  const handleSelect = (selectedIndex, e) => {
    setIndex(selectedIndex);
  };

  useEffect(() => {
    fetch("/api/news", {
      method: "GET",
    })
      .then((response) => response.json())
      .then((newsData) => setNews(newsData))
      .catch((error) => {
        console.error("Error:", error);
      });
  }, []);

  return (
    <Container>
      <Container>
        <Row>
          <Col>
            <Carousel activeIndex={index} onSelect={handleSelect}></Carousel>
          </Col>
        </Row>
      </Container>
    </Container>
  );
};

ReactDOM.render(<App />, document.querySelector("#root"));
