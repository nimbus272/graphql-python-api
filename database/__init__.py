import string, random
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, String, Integer, Column, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, scoped_session

Base = declarative_base()


sqlite_shared_name = "test_db_{}".format(random.sample(string.ascii_letters, k=4))
engine = create_engine("sqlite:///file:{}?mode=memory&cache=shared&uri=true".format(sqlite_shared_name), echo=True)

class Director(Base):
    __tablename__ = "director"
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    movies = relationship("Movie", backref="director")
    
    def __repr__(self):
        return f"<Director {self.name}>"

class Movie(Base):
    __tablename__ = "movie"
    id = Column(Integer(), primary_key=True)
    director_id = Column(Integer(), ForeignKey("director.id"))
    title = Column(String())
    runtime = Column(Integer())
    rating = Column(Integer())

    
    def __repr__(self):
        return f"<Movie {self.title}>"
    


session = scoped_session(sessionmaker(bind=engine, autocommit=False, autoflush=False))

Base.query = session.query_property()
    

    