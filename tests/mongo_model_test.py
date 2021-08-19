import pytest
from pydantic import ValidationError

from pydantic_mongo import MongoModel
from bson import ObjectId


class TestModel(MongoModel):
    field: str


ID = ObjectId()


def test__from_db():
    """Should create model from mongodb document
    """
    model = TestModel.from_db(dict(_id=ID, field='something'))

    assert model.id == ID
    assert model.field == 'something'


def test_to_db():
    """Should convert model to mongodb document
    """
    model = TestModel(id=ID, field='something')
    assert model.db() == dict(_id=ID, field='something')


def test_validation():
    with pytest.raises(ValidationError):
        TestModel(id='xxxxxxxx', field='something')
