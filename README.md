# pydantic-mongodb

A tiny library to help working with Pydantic mongodb

##  Installing

```shell
pip install git+ssh://git@github.com/2read-online/pydantic-mongodb.git
```

## Usage example

```python
from pydantic_mongo import MongoModel


class TestModel(MongoModel):
    """A model for testing"""
    field: str



entry = TestModel(field='Some data')
mongo_collection.insert_one(entry.db())
```
