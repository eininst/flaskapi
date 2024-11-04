from pydantic import BaseModel

from flaskapi4 import Info, Tag
from flaskapi4 import Flaskapi

info = Info(title="book API", version="1.0.0")
app = Flaskapi(__name__, info=info)

book_tag = Tag(name="book", description="Some Book")


class BookQuery(BaseModel):
    age: int
    author: str


class ResultData(BaseModel):
    code: int
    message: str
    data: dict


@app.get("/book/<name>", summary="get books", tags=[book_tag])
def get_book(name, query: BookQuery) -> ResultData:
    """
    to get all books
    """
    return {
        "code": 0,
        "message": "ok",
        "data": [
            {"bid": 1, "age": query.age, "author": query.author},
            {"bid": 2, "age": query.age, "author": query.author}
        ]
    }


if __name__ == "__main__":
    app.run(debug=True)