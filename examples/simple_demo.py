# -*- coding: utf-8 -*-
from pydantic import BaseModel, Field
from flaskapi4 import Info, Flaskapi, Tag


class Unauthorized(BaseModel):
    code: int = Field(-1, description="Status Code")
    message: str = Field("Unauthorized!", description="Exception Information")

info = Info(title="book API", version="1.0.0")
app = Flaskapi(__name__,
              info=info, responses={"401": Unauthorized})
# app.init_doc()
book_tag = Tag(name="book", description="Some Book")


class BookQuery(BaseModel):
    age: int
    author: str=''


@app.get("/test",)
def get_book(query:BookQuery) :
    """
    get all books
    """

    return BookQuery(age=1)


if __name__ == "__main__":
    app.init_doc()
    app.run(debug=True, port=5001)