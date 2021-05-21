const { Container, Row, Col } = ReactBootstrap;

const AboutUs = () => {

    return (
        <Container>
            <Row>
                <h3 className="about-us">About Us</h3>
            </Row>
            <Row className="par">
                <p>Some really exciting and fun facts about us!</p>
                <p>We love melons so much, it's almost weird! Actually, definitely weird. :D</p>
            </Row>
            <Row>
                <Col xs={3}>
                    <img className="about-img" src="/static/images/yulianapic.jpg" alt="Yuliana"/>
                    <h5 className="padding-name title">Yuliana</h5>
                    <h6 className="subtitle">Chief Melon Analyst</h6>
                </Col>
                <Col xs={3}>
                    <img className="about-img" src="/static/images/melissapic.jpg" alt="Melissa"/>
                    <h5 className="padding-name title">Melissa</h5>
                    <h6 className="subtitle">Hybrid Melon</h6>
                </Col>
                <Col xs={3}>
                    <img className="about-img" src="/static/images/christinapic.jpg" alt="Christina"/>
                    <h5 className="padding-name title">Christina</h5>
                    <h6 className="subtitle">Specialist Melon-Quality Assurance</h6>
                </Col>
                <Col xs={3}>
                    <img className="about-img" src="/static/images/emilypic.jpg" alt="Emily"/>
                    <h5 className="padding-name title">Emily</h5>
                    <h6 className="subtitle">Melon Developer</h6>
                </Col>
            </Row>
            <Row>
                <Col xs={{ span:4, offset:4 }}>
                    <img className="about-img" src="/static/images/catpic.jpg" alt="cat"/>
                    <h5 className="padding-name title">Muffin</h5>
                    <h6 className="subtitle">Chief Fieldline Officer</h6>
                </Col>
            </Row>
        </Container>
    )
};