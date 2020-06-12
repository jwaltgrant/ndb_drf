from __future__ import annotations
import typing
from rest_framework import mixins
from rest_framework.response import Response
from .lazy_query import LazyQuery

class NDBDestroyModelMixin(mixins.DestroyModelMixin):
    def perform_destroy(self, instance: ndb.Model):
        instance.key.delete()

if typing.TYPE_CHECKING:
    from google.cloud import ndb