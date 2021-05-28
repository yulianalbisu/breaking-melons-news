## Table of contents
* [General Information](#general-information)
* [Features](#features)
* [Technologies](#technologies)
* [Setup](#setup)

## General Information

## Project BitMelon Newsfeed
The Breaking Melon News app is a newsfeed designed to bring you the latest and greatest in melon news in a pleasing visual format. 
 
  
## API/datasets used
The application was made from web scrapping to fill the data inside the carousel, the articles by the author. On the cards, the information has been linked to Youtube Videos and formal blogs.
  
  
## Documentation

[Project Details](https://www.dropbox.com/scl/fi/udrfqakdxhbe64jstk529/%F0%9F%98%83-My-Paper-doc.paper?dl=0&oref=e&rlkey=96f9az5llr1ubj8ac2uavrlxi)
 
## Features

### Carousel
Front and center when you hit the homepage is a carousel created using React Bootstrap, which displays the most recent stories from our top melon reporter Meli Mellen. There are also some articles by Mel Melitopolski. 
![caption](/static/img/carousel.gif)

### Articles
User can view a list of articles than can move with a carousel design and can be clicked to be redirect to the article wanted. These stories are retrieved from our PostgreSQL database, and sent to the front end as JSON using an endpoint, where the state is updated. Once updated, each carousel item is dynamically rendered, and the carousel movement is controlled via state.
![App Screenshot](/static/img/articles.png)

### Link-Cards
Below the carousel, we have React Bootstrap cards which are used to display external news links, pulled from a different table than our internal articles. These cards have animations created using the animate.css library to streamline the process. This is used in conjunction with React, with the class name on each melon div controlled by state. When a mouseover event triggers, the class is changed and along with it the corresponding css animation. When the mouseout event triggers, the state and thus the class is updated again, returning it to its original invisible state.
![caption](/static/img/card.gif)

### About Us
Back on the homepage, we also use React Router Dom to go to an About Us page, which features our team 
![App Screenshot](/static/img/about-us.png)

### The Newsfeed
Carousel and cards together, making the melon news more interesting.
![App Screenshot](/static/img/integration.png)

## Nice to have
In a future sprint, we’d love to add the ability to create accounts and add comments to our articles. Once this was implemented, the next thing we’d like to add is the ability for our correspondents to post articles directly using their own accounts, distinguished from regular commenters with a specific role that is already built into the database. This would be more streamlined than adding directly to the database.


## Run Locally

Clone the project

```bash
  git clone https://github.com/yulianalbisu/breaking-melons-news/
```

Go to the project directory

```bash
  cd breaking-melons-news
```

```bash
  virtualenv env
```
```bash
  source env/bin/activate
```

Install requirements

```bash
  pip3 install requirements.txt
```

```bash
  sudo service postgresql 
```
Start the server

## Technologies
Technologies used on this project:
## Languages
* Python
* JavaScript (JSON)
* CSS
* React

## Frameworks & Libraries
* PostgresQL
* SQLAlchemy
* Flask
* Jinja
* React Bootstrap 


## Collaborators
- Emily Merline
- Melissa Rice
- Christina Babaya
- Yuliana Aldrich