from fastapi import FastAPI
from .routes import router
from .graphql import gql_app

app = FastAPI(title="Query Engine API")
app.include_router(router)
app.mount("/graphql", gql_app)
