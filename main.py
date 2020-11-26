from fastapi import FastAPI
import graphene
from starlette.graphql import GraphQLApp
from schema import Query, Mutation

app = FastAPI()
app.add_route(
    "/graphiql", GraphQLApp(schema=graphene.Schema(query=Query, mutation=Mutation))
)


@app.get("/")
def main():
    return {"Hello": "World"}