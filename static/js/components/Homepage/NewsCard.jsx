const { Card } = ReactBootstrap;
const { useState } = React;

const NewsCard = ({newsItem}) => {

    const [cardHover, setCardHover] = useState("card-hidden");

    return (
        <Card className="bg-dark text-white" onMouseOver={() => setCardHover("card-visible")} onMouseOut={() => setCardHover("card-hidden")}>
            <Card.Img src={newsItem.image} alt="Card cat image" />
            <Card.ImgOverlay>
                <div className={cardHover}><a href={newsItem.direct_link}>{newsItem.direct_title}</a></div>
            </Card.ImgOverlay>
        </Card>
    );
};