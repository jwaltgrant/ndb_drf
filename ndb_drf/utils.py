import typing
from google.cloud import ndb

def key_to_urlsafe(
    key: typing.Union[ndb.Key, str, bytes],
    _as: typing.Union[typing.Type[str], typing.Type[bytes]] = bytes
) -> typing.Union[str, bytes]:
    if isinstance(key, ndb.Key):
        key = key.urlsafe()
    else:
        assert ndb.Key(urlsafe=key), 'Key must be ndb.Key or url safe key'
    if _as is bytes:
        if isinstance(key, str):
            key = key.encode()
        return key
    else:
        assert _as is str, 'Valid return types are exclusively bytes or str'
        if isinstance(key, bytes):
            key = key.decode()
        return key

def key_to_ndb_key(
    key: typing.Union[ndb.Key, str, bytes]
) -> ndb.Key:
    if isinstance(key, ndb.Key):
        return key
    assert isinstance(key, (bytes, str)), 'Key must be either a String or Byte String'
    return ndb.Key(urlsafe=key)