from __future__ import annotations
import typing
from rest_framework.generics import GenericAPIView
from django.http import Http404
from .lazy_query import LazyQuery

class NDBGenericAPIView(GenericAPIView):
    """
    Generic API View that allows for use with Google NDB
    
    It is recomended to define the `model_class` property on the class
    as that alows for using query filtering rather that looping over key results
    for the implementation of `get_object`
    """

    lookup_field = 'key'
    model_class = None

    def get_queryset(self):
        """
        Get the list of items for this view.
        This must be an iterable, and may be a queryset.
        Defaults to using `self.queryset`.
        This method should always be used rather than accessing `self.queryset`
        directly, as `self.queryset` gets evaluated only once, and those results
        are cached for all subsequent requests.
        You may want to override this if you need to provide different
        querysets depending on the incoming request.
        (Eg. return a list of items that is specific to the user)
        """
        assert self.queryset is not None, (
            "'%s' should either include a `queryset` attribute, "
            "or override the `get_queryset()` method."
            % self.__class__.__name__
        )

        return self.queryset

    def _get_with_model(self, key: ndb.Key):
        """
        Get the Object by filtering with the model class
        This is the optimal implementation to use
        """
        queryset = LazyQuery.create(self.get_queryset())
        queryset.filter(self.model_class.key == key)
        return queryset.get()

    def _get_with_loop(self, key: ndb.Key):
        """
        Fetch the keys of the results of the query set
        Then loop over, attempting to find a match of the key,
        return the object if key is found in query set results
        """
        queryset = LazyQuery.create(self.get_queryset())
        for _key in self.get_queryset():
            if _key == key:
                return _key.get()

    def get_object(self) -> ndb.Model:
        """
        Get NDB Model intance from the query set
        :raises: 404 if key is not in the query set
        :return: ndb.Model
        """
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        assert lookup_url_kwarg in self.kwargs, (
            'Expected view %s to be called with a URL keyword argument '
            'named "%s". Fix your URL conf, or set the `.lookup_field` '
            'attribute on the view correctly.' %
            (self.__class__.__name__, lookup_url_kwarg)
        )
        lookup_key = self.kwargs.get(lookup_url_kwarg)
        if isinstance(lookup_key, (bytes, str)):
            lookup_key = ndb.Key(urlsafe=lookup_key)
        
        obj = None
        
        if self.model_class:
            obj = self._get_with_model(lookup_key)
        else:
            obj = self._get_with_loop(lookup_key)
        if not obj:
            raise Http404
        
        self.check_object_permissions(self.request, obj)

        return obj

if typing.TYPE_CHECKING:
    from google.cloud import ndb
