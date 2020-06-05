from __future__ import annotations
import typing
from rest_framework import mixins
from rest_framework.response import Response

class NDBDestroyModelMixin(mixins.DestroyModelMixin):
    def perform_destroy(self, instance: ndb.Model):
        instance.key.delete()

class NDBListModelMixin(mixins.ListModelMixin):
    """
    List a queryset.
    """
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset()).fetch()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

if typing.TYPE_CHECKING:
    from google.cloud import ndb