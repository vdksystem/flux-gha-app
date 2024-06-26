import os

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name} from flux-gha-app demo project"}


@app.get("/get_node")
async def get_node():
    """Some docstring"""
    node = os.environ.get("NODE_NAME", "UNKNOWN")
    return {"message": f"Pod is running on {node}"}


@app.get("/release")
async def get_release():
    return {"message": f"Something about release"}


@app.get("/health")
async def health():
    return {"status": "OK"}

