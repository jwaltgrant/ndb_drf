from google.cloud import ndb

class LazyQuery(ndb.Query):
    @staticmethod
    def create(query: ndb.Query):
        if isinstance(query, LazyQuery):
            return query
        assert isinstance(query, ndb.Query), 'Query must be either ndb.Query or Lazy Query'
        query.__class__ = LazyQuery
        return query

    def __iter__(self):
        return self.iter()