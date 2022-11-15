import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType
from ..database import Movie as MovieModel, Director as DirectorModel

class DirectorSchema(SQLAlchemyObjectType):
    class Meta:
        model=DirectorModel
        interfaces=(relay.Node, )
    
class MovieSchema(SQLAlchemyObjectType):
    class Meta:
        model=MovieModel
        interfaces=(relay.Node, )
        
class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_directors = SQLAlchemyConnectionField(DirectorSchema.connection)
    all_movies = SQLAlchemyConnectionField(MovieSchema.connection)
    
schema = graphene.Schema(query=Query)