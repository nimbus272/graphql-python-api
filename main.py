from flask import Flask
from flask_graphql import GraphQLView
from .database import Movie, Director, Base, engine, session
from .schemas import schema



app = Flask(__name__)

@app.route('/init')
def initialize_db():
    Base.metadata.create_all(bind=engine)
    
    director1 = Director(name="Jonathan Demme")
    movie1 = Movie(title="Silence of the Lambs", runtime=118, rating=8)
    movie1.director = director1
    director2 = Director(name="Quentin Tarantino")
    movie2 = Movie(title="Once Upon a Time in Hollywood", runtime=160, rating=7)
    movie2.director = director2
    movie3 = Movie(title="Kill Bill", runtime=111, rating=8)
    movie3.director = director2
    director3 = Director(name="Wes Anderson")
    movie4 = Movie(title="The Royal Tenenbaums", runtime=109, rating=7)
    movie4.director = director3
    movie5 = Movie(title="Fantastic Mr.Fox", runtime=87, rating=6)
    movie5.director = director3
    
    session.add_all([director1, director2, director3, movie1, movie2, movie3, movie4, movie5])
    session.commit()
    
    
    return {
        "status": "200"
    }

@app.route('/test')
def test_db():
    return session.query(Movie).all()

app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view(
        "graphql",
        schema=schema,
        graphiql=True,
    ),
)
