const { Card } = ReactBootstrap;
const { useState } = React;

const NewsCard = ({newsItem, newsInd}) => {

    const [cardHover, setCardHover] = useState("card-hidden");

    const cardClass = newsInd < 3 ? "big-news-card" : "small-news-card";

    const imageCardClass = newsInd < 3 ? "big-news-image" : "small-news-image";
    return (
        <Card className={`${cardClass} news-card`} onMouseOver={() => setCardHover("card-visible")} onMouseOut={() => setCardHover("card-hidden")}>
            <Card.Img src={newsItem.image} alt="Card image" fluid className={`card-image ${imageCardClass}`}/>
            <Card.ImgOverlay>
                <div className={cardHover}><a className="card-link" href={newsItem.direct_link}>{newsItem.direct_title}</a></div>
            </Card.ImgOverlay>
        </Card>
    );
};