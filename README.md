# Django REST Framework extension to use Google App Engine NDB

Currently provides extensions of GenericAPIView, the Destroy and List Mixins
These are theoretically the only overrides needed to use DRF's Generic API Views

It is recommended to subclass from `NDBGenericAPIView` and to define the `model_class`
property for the most efficient implmentation of `get_object()`.

There is no serialization helpers yet, but I plan to make a `ModelSerialize` implementation for ndb Models

Example Use:
```
from google.cloud import ndb
from ndb_drf import ndb_viewsets
from rest_framework import mixins
from .serializers import SomeModelSerializer # Implementation coming

class SomeModel(ndb.Model):
    field = ndb.StringField()
    another = ndb.IntegerField()

class SomeModelViewSet(ndb_viewsets.NDBModelViewSet):
    model_class = SomeModel
    serialize_class = SomeModelSerializer

    def get_queryset(self):
        return SomeModel.query()
```
