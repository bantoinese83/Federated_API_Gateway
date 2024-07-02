from fastapi import FastAPI
import graphene
from graphene_federation import build_schema, key, shareable
from starlette_graphene3 import GraphQLApp


@key(fields="id")
@shareable
class User(graphene.ObjectType):
    id = graphene.ID(required=True)
    username = graphene.String()


class Query(graphene.ObjectType):
    user = graphene.Field(User, id=graphene.ID(required=True))

    @staticmethod
    def resolve_user(parent, info, id):
        users_data = {
            "1": {"id": "1", "username": "alice"},
            "2": {"id": "2", "username": "bob"},
        }
        return users_data.get(id)


schema = build_schema(Query)

app = FastAPI()
app.add_route("/graphql", GraphQLApp(schema=schema))

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
