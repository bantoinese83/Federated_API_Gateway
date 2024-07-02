from fastapi import FastAPI
import graphene
from graphene_federation import build_schema, key, shareable
from starlette_graphene3 import GraphQLApp


@key(fields="id")
@shareable
class Post(graphene.ObjectType):
    id = graphene.ID(required=True)
    title = graphene.String()
    author_id = graphene.ID()


@key(fields="id")
@shareable
class User(graphene.ObjectType):
    id = graphene.ID(required=True)
    posts = graphene.List(Post)

    def resolve_posts(self, info):
        posts_data = {
            "1": {"id": "1", "title": "First Post", "author_id": "1"},
            "2": {"id": "2", "title": "Second Post", "author_id": "2"},
        }
        return [post for post in posts_data.values() if post["author_id"] == self.id]


class Query(graphene.ObjectType):
    post = graphene.Field(Post, id=graphene.ID(required=True))

    @staticmethod
    def resolve_post(parent, info, id):
        posts_data = {
            "1": {"id": "1", "title": "First Post", "author_id": "1"},
            "2": {"id": "2", "title": "Second Post", "author_id": "2"},
        }
        return posts_data.get(id)


schema = build_schema(Query, types=[User, Post])

app = FastAPI()
app.add_route("/graphql", GraphQLApp(schema=schema))

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001)
