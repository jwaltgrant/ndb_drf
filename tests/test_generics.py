from google.cloud import ndb

class TestModel(ndb.Model):
    field = ndb.StringProperty()

def test():
    t = TestModel()
    t.field = 'test'
    key = t.put()
    test = key.get()
    assert t == key