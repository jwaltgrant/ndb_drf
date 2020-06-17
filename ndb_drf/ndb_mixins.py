from __future__ import annotations
import typing
from rest_framework import mixins


class NDBDestroyModelMixin(mixins.DestroyModelMixin):
    def perform_destroy(self, instance: ndb.Model):
        instance.key.delete()


if typing.TYPE_CHECKING:
    from google.cloud import ndb