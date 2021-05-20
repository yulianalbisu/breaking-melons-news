const { Container, Row, Col } = ReactBootstrap;

const AboutUs = () => {

    return (
        <Container>
            <Row>
                <h3>About Us</h3>
            </Row>
            <Row>
                <p>Some really exciting and fun facts about us!</p>
                <p>We love melons so much, it's almost weird! Actually, definitely weird. :D</p>
            </Row>
            <Row>
                <Col>
                    <img className="about-img" src="/static/images/yulianapic.jpg" alt="Yuliana"/>
                </Col>
                <Col>
                    <img className="about-img" src="/static/images/melissapic.jpg" alt="Melissa"/>
                </Col>
                <Col>
                    <img className="about-img" src="/static/images/christinapic.jpg" alt="Christina"/>
                </Col>
                <Col>
                    <img className="about-img" src="/static/images/emilypic.jpg" alt="Emily"/>
                </Col>
            </Row>
            <Row>
                <Col>
                    <img className="about-img" src="/static/images/catpic.jpg" alt="cat"/>
                </Col>
            </Row>
        </Container>
    )
};