from enum import Enum


class IOCTypes(str, Enum):
    Urls = 'extractedUrls',
    Domains = 'extractedDomains',
    IPs = 'extractedIPs',
    Emails = 'extractedEmails',
    MD5 = 'extractedHashesMD5',
    SHA1 = 'extractedHashesSHA1',
    SHA256 = 'extractedHashesSHA256',
    SHA512 = 'extractedHashesSHA512',
    UUIDs = 'extractedUUIDs',
    RegistryPathways = 'extractedRegistryPathways',
    RevisionSaveIDs = 'extractedRevisionSaveIDs'
