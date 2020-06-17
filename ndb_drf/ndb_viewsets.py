from rest_framework import viewsets
from . import ndb_generics, ndb_mixins


class NDBGenericViewSet(
    ndb_generics.NDBGenericAPIView,
    viewsets.GenericViewSet
):
    """
    Provide the necessary overrides to the Generic View Set
    """
    pass


class NDBModelViewSet(
    ndb_generics.NDBGenericAPIView,
    ndb_mixins.NDBDestroyModelMixin,
    viewsets.ModelViewSet
):
    """
    Provide the necessary overrides to the Model View Set
    """
    pass
