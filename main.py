import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run(app="app:main", reload=True, port=8080)