import typing

from rest_framework import serializers
from google.cloud import ndb
from .utils import key_to_ndb_key, key_to_urlsafe


class URLSafeKeyField(serializers.Field):
    """
    Serializer Field to URL Safe Keys
    The internal data should be stored as a URL Safe Key string
    """

    @staticmethod
    def validate_key(key) -> ndb.Key:
        _key = None
        try:
            _key = key_to_ndb_key(key)
        except ValueError:
            pass  # Value error will lead to Validation Error being raised
        if not isinstance(_key, ndb.Key):
            raise serializers.ValidationError('Provided Key Could not be Parsed into NDB Key')
        return _key

    def to_internal_value(self, data) -> bytes:
        self.validate_key(data)
        if isinstance(data, str):
            data = data.encode()
        return data

    def to_representation(self, value) -> str:
        key = key_to_urlsafe(value, str)
        assert key is not None
        return key

class NDBKeyField(URLSafeKeyField):
    """
    Serialize Field for NDB Keys
    Output will be serialized as a URL Safe Key
    """
    def to_internal_value(self, data) -> ndb.Key:
        key = self.validate_key(data)
        isinstance(key, ndb.Key)
        return key

class NDBModelSerializer(serializers.Serializer):
    serializer_field_mapping = {
        ndb.KeyProperty: NDBKeyField,
        ndb.IntegerProperty: serializers.IntegerField,
        ndb.FloatProperty: serializers.FloatField,
        ndb.BooleanProperty: serializers.BooleanField,
        ndb.DateProperty: serializers.DateField,
        ndb.DateTimeProperty: serializers.DateTimeField,
        ndb.StringProperty: serializers.CharField,
        ndb.TextProperty: serializers.CharField,
        ndb.PickleProperty: serializers.CharField,
        ndb.BlobProperty: serializers.CharField,
        ndb.JsonProperty: serializers.JSONField
    }
