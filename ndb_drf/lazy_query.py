from google.cloud import ndb


class LazyQuery:

    def __init__(self, query: ndb.Query):
        self.__query = query

    def __repr__(self):
        return self.__query.__repr__()

    @property
    def is_distinct(self):
        return self.__query.is_distinct

    def filter(self, *filters):
        return self.__query.filter(*filters)
    def order(self, *props):
        return self.__query.order(*props)
    def analyze(self):
        return self.__query.analyze()
    def bind(self, *positional, **keyword):
        return self.__query.bind(*positional, **keyword)
    def _to_property_orders(self, order_by):
        return self.__query._to_property_orders(order_by)
    def fetch(self, limit=None, **kwargs):
        return self.__query.fetch(limit=limit, **kwargs)
    def fetch_async(self, limit=None, **kwargs):
        return self.__query.fetch_async(limit=limit, **kwargs)
    def _option(self, name, given, options=None):
        return self.__query._option(name, given, options=options)
    def run_to_queue(self, queue, conn, options=None, dsquery=None):
        return self.__query.run_to_queue(queue, conn, options=options, dsquery=dsquery)

    def iter(self, **kwargs):
        return self.__query.iter(**kwargs)
    __iter__ = iter

    def map(self, callback, **kwargs):
        return self.__query.map(callback, **kwargs)
    def map_async(self, callback, **kwargs):
        return self.__query.map_async(callback, **kwargs)
    def get(self, **kwargs):
        return self.__query.get(**kwargs)
    def get_async(self, **kwargs):
        return self.__query.get_async(**kwargs)

    def count(self, limit=None, **kwargs):
        return self.__query.count(limit=limit, **kwargs)

    def count_async(self, limit=None, **kwargs):
        return self.__query.count_async(limit=limit, **kwargs)
    def fetch_page(self, page_size, **kwargs):
        return self.__query.fetch_page(page_size, **kwargs)
    def fetch_page_async(self, page_size, **kwargs):
        return self.__query.fetch_page_async(page_size, **kwargs)