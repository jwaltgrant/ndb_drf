import pytest
from google.cloud import ndb

class NDB_Mock:
    objects = {}

    @classmethod
    def save(cls, obj: _NDBModelMock):
        of_type = None
        cls.objects[key] = obj

    @classmethod
    def get(cls, key):
        return cls.objects.get(key, None)

    @classmethod
    def delete(cls, key):
        if key in cls.objects:
            del cls.objects[key]

class _NDBModelMock(ndb.Model):
    def put(self):
        self._pre_put_hook()
        NDB_Mock.save()

class Person(ndb.Model):
    age = ndb.IntegerProperty()
    first_name = ndb.StringProperty()
    last_name = ndb.StringProperty()
    parents_names = ndb.StringProperty(repeated=True) 


@pytest.fixture
def people():
    return [
        Person(age=27, first_name='Josh', last_name='Grant', parents_names=['Lloyd', 'Kerri']),
        Person(age=27, first_name='Olivia', last_name='Goodin,', parents_names=['Mark', 'Maria'])
    ]

