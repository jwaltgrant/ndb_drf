import pytest

from google.cloud import ndb
from ndb_drf.utils import key_to_urlsafe

@pytest.mark.usefixtures("in_context")
def test_key_to_urlsafe():
    URL_SAFE = b'agZzfmZpcmVyDwsSBEtpbmQiBVRoaW5nDA'
    key = ndb.Key(urlsafe=URL_SAFE)
    assert key_to_urlsafe(key) == URL_SAFE
    assert key_to_urlsafe(key, str) == URL_SAFE.decode()
