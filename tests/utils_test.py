import pytest

from google.cloud import ndb
from ndb_drf.utils import key_to_urlsafe, key_to_ndb_key

class TestKeys:
    URL_SAFE = b'agZzfmZpcmVyDwsSBEtpbmQiBVRoaW5nDA'

    @pytest.mark.usefixtures("in_context")
    def test_key_to_urlsafe(self):
        key = ndb.Key(urlsafe=self.URL_SAFE)
        assert key_to_urlsafe(key) == self.URL_SAFE
        assert key_to_urlsafe(key, str) == self.URL_SAFE.decode()

    @pytest.mark.usefixtures('in_context')
    def test_urlsafe_to_key(self):
        keys = [self.URL_SAFE, self.URL_SAFE.decode(), ndb.Key(urlsafe=self.URL_SAFE)]
        for _key in keys:
            key = key_to_ndb_key(_key)
            assert isinstance(key, ndb.Key)
            assert key.kind() == 'Kind'
            assert key.project() == 'fire'


