# Copyright 2012 Managed I.T.
#
# Author: Kiall Mac Innes <kiall@managedit.ie>
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


class Base(Exception):
    error_code = 500
    error_type = None
    error_message = None
    errors = None

    def __init__(self, *args, **kwargs):
        self.errors = kwargs.pop('errors', None)

        super(Base, self).__init__(*args, **kwargs)

        if len(args) > 0 and isinstance(args[0], basestring):
            self.error_message = args[0]


class Backend(Exception):
    pass


class NSD4SlaveBackendError(Backend):
    pass


class NotImplemented(Base, NotImplementedError):
    pass


class ConfigurationError(Base):
    error_type = 'configuration_error'


class CommunicationFailure(Base):
    error_code = 504
    error_type = 'communication_failure'


class NeutronCommunicationFailure(CommunicationFailure):
    """
    Raised in case one of the alledged Neutron endpoints fails.
    """
    error_type = 'neutron_communication_failure'


class NoServersConfigured(ConfigurationError):
    error_code = 500
    error_type = 'no_servers_configured'


class OverQuota(Base):
    error_code = 413
    error_type = 'over_quota'


class QuotaResourceUnknown(Base):
    error_type = 'quota_resource_unknown'


class InvalidObject(Base):
    error_code = 400
    error_type = 'invalid_object'


class BadRequest(Base):
    error_code = 400
    error_type = 'bad_request'


class NetworkEndpointNotFound(BadRequest):
    error_type = 'no_endpoint'
    error_code = 403


class InvalidOperation(BadRequest):
    error_code = 400
    error_type = 'invalid_operation'


class UnsupportedAccept(BadRequest):
    error_code = 406
    error_type = 'unsupported_accept'


class UnsupportedContentType(BadRequest):
    error_code = 415
    error_type = 'unsupported_content_type'


class InvalidDomainName(Base):
    error_code = 400
    error_type = 'invalid_domain_name'


class InvalidRecordSetName(Base):
    error_code = 400
    error_type = 'invalid_recordset_name'


class InvalidRecordSetLocation(Base):
    error_code = 400
    error_type = 'invalid_recordset_location'


class DomainHasSubdomain(Base):
    error_code = 400
    error_type = 'domain_has_subdomain'


class Forbidden(Base):
    error_code = 403
    error_type = 'forbidden'


class Duplicate(Base):
    error_code = 409
    error_type = 'duplicate'


class DuplicateQuota(Duplicate):
    error_type = 'duplicate_quota'


class DuplicateServer(Duplicate):
    error_type = 'duplicate_server'


class DuplicateTsigKey(Duplicate):
    error_type = 'duplicate_tsigkey'


class DuplicateDomain(Duplicate):
    error_type = 'duplicate_domain'


class DuplicateTLD(Duplicate):
    error_type = 'duplicate_tld'


class DuplicateRecordSet(Duplicate):
    error_type = 'duplicate_recordset'


class DuplicateRecord(Duplicate):
    error_type = 'duplicate_record'


class NotFound(Base):
    error_code = 404
    error_type = 'not_found'


class QuotaNotFound(NotFound):
    error_type = 'quota_not_found'


class ServerNotFound(NotFound):
    error_type = 'server_not_found'


class TsigKeyNotFound(NotFound):
    error_type = 'tsigkey_not_found'


class DomainNotFound(NotFound):
    error_type = 'domain_not_found'


class TLDNotFound(NotFound):
    error_type = 'tld_not_found'


class RecordSetNotFound(NotFound):
    error_type = 'recordset_not_found'


class RecordNotFound(NotFound):
    error_type = 'record_not_found'


class LastServerDeleteNotAllowed(BadRequest):
    error_type = 'last_server_delete_not_allowed'


class ResourceNotFound(NotFound):
    # TODO(kiall): Should this be extending NotFound??
    pass
