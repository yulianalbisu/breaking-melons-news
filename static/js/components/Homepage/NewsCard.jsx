const { Card } = ReactBootstrap;
const { useState } = React;

const NewsCard = ({catMelon}) => {

    const [cardHover, setCardHover] = useState("card-hidden");

    return (
        <Card className="bg-dark text-white" onMouseOver={() => setCardHover("card-visible")} onMouseOut={() => setCardHover("card-hidden")}>
            <Card.Img src={catMelon.image} alt="Card cat image" />
            <Card.ImgOverlay>
                <div className={cardHover}><a href={catMelon.externalLink}>{catMelon.title}</a></div>
            </Card.ImgOverlay>
        </Card>
    );
};