from enum import Enum


class ResourceTypes(str, Enum):
    file_hash_md5 = 'MD5',
    file_hash_sha1 = 'SHA1',
    file_hash_sha256 = 'SHA256',
    file_hash_sha512 = 'SHA512',
    url = 'url',
    ip = 'IP address',
    domain = 'domain',
    email = 'email',
    uuid = 'UUID',
    registry_path = 'registry path',
    revision_save_id = 'revision save ID'
