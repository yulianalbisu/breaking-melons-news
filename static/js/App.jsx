const { Container, Row, Col, Carousel, Navbar } = ReactBootstrap;
const { NavLink, BrowserRouter, Switch, Route } = ReactRouterDOM;
const { useState, useEffect } = React;

const App = () => {

  const [news, setNews] = useState([]);

  const [externalNews, setExternalNews] = useState([]);

  const [selectedNews, setSelectedNews] = useState({});
 
  useEffect(() => {
    fetch("/api/news", {
      method: "GET",
    })
      .then((response) => response.json())
      .then((newsData) => setNews(newsData))
      .catch((error) => {
        console.error("Error:", error);
      });
    fetch("/api/external-news", {
        method: "GET",
      })
        .then((response) => response.json())
        .then((externalNewsData) => setExternalNews(externalNewsData))
        .catch((error) => {
          console.error("Error:", error);
      });
  }, []);

  const viewNews = newsItem => {
    setSelectedNews(newsItem)
  }

  return (
  <BrowserRouter>
    <div>
      <Navbar bg="light" className="melon-navbar" sticky='top'>
        <Navbar.Brand>
            <img
            alt=""
            src="/static/images/watermelon.png"
            width="30"
            height="30"
            className="d-inline-block align-top"
          />{' '}
            <NavLink to="/" className="home-link">
            Breaking Melon News
            </NavLink>
          </Navbar.Brand>
        <NavLink to="/about-us" className="aboutus-link">
          About Us
          </NavLink>
        </Navbar>
        <Switch>
          <Route exact path="/">
            <Homepage 
            news={news}
            externalNews={externalNews}
            viewNews={viewNews}
            />
          </Route>
          <Route path="/about-us">
            <AboutUs />
          </Route>
          <Route path="/articles/:articleId">
            <NewsArticle newsItem={selectedNews} />
          </Route>
      </Switch> 
    </div>
    </BrowserRouter>
  );
};

ReactDOM.render(<App />, document.querySelector("#root"));
