## Requirements

Python 3.9+

flaskapi4 is dependent on the following libraries:

- [Flask](https://github.com/pallets/flask) for the web app.
- [Pydantic](https://github.com/pydantic/pydantic) for the data validation.

## Installation

```bash
pip install -U flaskapi4
```

## A Simple Example

Here's a simple example, further go to the [Example](https://luolingchun.github.io/flask-openapi3/latest/Example/).

```python
from pydantic import BaseModel

from flaskapi4 import Info, Tag
from flaskapi4 import OpenAPI

info = Info(title="book API", version="1.0.0")
app = OpenAPI(__name__, info=info)

book_tag = Tag(name="book", description="Some Book")


class BookQuery(BaseModel):
    age: int
    author: str

class ResultData(BaseModel):
    code: int
    message: str
    data: dict
    
@app.get("/book", summary="get books", tags=[book_tag])
def get_book(query: BookQuery) -> ResultData:
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
```