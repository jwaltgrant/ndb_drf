import pytest
from rest_framework import serializers

from ndb_drf import ndb_serializers
from ndb_drf import utils

class TestURLSafeField:
    URL_SAFE = b'agZzfmZpcmVyDwsSBEtpbmQiBVRoaW5nDA'
    field = ndb_serializers.URLSafeKeyField()

    @pytest.mark.usefixtures("in_context")
    def test_to_internal(self):
        internal = self.field.to_internal_value(self.URL_SAFE)
        assert internal == self.URL_SAFE

    @pytest.mark.usefixtures('in_context')
    def test_to_rep(self):
        rep = self.field.to_representation(self.URL_SAFE)
        assert rep == self.URL_SAFE.decode()

    @pytest.mark.usefixtures('in_context')
    def test_validation_failure(self):
        with pytest.raises(serializers.ValidationError):
            internal = self.field.to_internal_value('bad_key')

class TestKeyField:
    URL_SAFE = b'agZzfmZpcmVyDwsSBEtpbmQiBVRoaW5nDA'
    field = ndb_serializers.NDBKeyField()

    @pytest.mark.usefixtures('in_context')
    def test_to_internal(self):
        internal = self.field.to_internal_value(self.URL_SAFE)
        ndb_key = utils.key_to_ndb_key(self.URL_SAFE)
        assert internal == ndb_key

    @pytest.mark.usefixtures('in_context')
    def test_to_rep(self):
        ndb_key = utils.key_to_ndb_key(self.URL_SAFE)
        rep = self.field.to_representation(ndb_key)
        assert rep == self.URL_SAFE.decode()

    @pytest.mark.usefixtures('in_context')
    def test_validation_error(self):
        with pytest.raises(serializers.ValidationError):
            internal = self.field.to_internal_value('still_bad')
