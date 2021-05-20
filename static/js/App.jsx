const { Container, Row, Col, Carousel, Navbar } = ReactBootstrap;
const { NavLink, BrowserRouter, Switch, Route } = ReactRouterDOM;
const { useState, useEffect } = React;

const App = () => {

  

  const [news, setNews] = useState([]);

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



                  {/* <CarouselItem
                key={newsIndex}
                newsItem={newsItem}
                /> */}
  return (
  <BrowserRouter>
    <Container>
      <Navbar bg="light">
        <Navbar.Brand>
            <NavLink to="/">
            Breaking Melon News
            </NavLink>
          </Navbar.Brand>
        <NavLink to="/about-us">
          About Us
          </NavLink>
        </Navbar>
        <Switch>
          <Route exact path="/">
            <Homepage 
            news={news}
            />
          </Route>
          <Route path="/about-us">
            <AboutUs />
          </Route>
      </Switch> 
    </Container>
    </BrowserRouter>
  );
};

ReactDOM.render(<App />, document.querySelector("#root"));
