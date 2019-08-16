# *** WARNING: this file was generated by the Pulumi Kubernetes codegen tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
from typing import Optional

import pulumi
import pulumi.runtime
from pulumi import Input, ResourceOptions

from ... import tables, version


class Event(pulumi.CustomResource):
    """
    Event is a report of an event somewhere in the cluster. It generally denotes some state change
    in the system.
    """

    def __init__(self, resource_name, opts=None, action=None, deprecated_count=None, deprecated_first_timestamp=None, deprecated_last_timestamp=None, deprecated_source=None, event_time=None, metadata=None, note=None, reason=None, regarding=None, related=None, reporting_controller=None, reporting_instance=None, series=None, type=None, __name__=None, __opts__=None):
        """
        Create a Event resource with the given unique name, arguments, and options.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if not resource_name:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(resource_name, str):
            raise TypeError('Expected resource name to be a string')
        if opts and not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['apiVersion'] = 'events.k8s.io/v1beta1'
        __props__['kind'] = 'Event'
        if event_time is None:
            raise TypeError('Missing required property event_time')
        __props__['eventTime'] = event_time
        __props__['action'] = action
        __props__['deprecatedCount'] = deprecated_count
        __props__['deprecatedFirstTimestamp'] = deprecated_first_timestamp
        __props__['deprecatedLastTimestamp'] = deprecated_last_timestamp
        __props__['deprecatedSource'] = deprecated_source
        __props__['metadata'] = metadata
        __props__['note'] = note
        __props__['reason'] = reason
        __props__['regarding'] = regarding
        __props__['related'] = related
        __props__['reportingController'] = reporting_controller
        __props__['reportingInstance'] = reporting_instance
        __props__['series'] = series
        __props__['type'] = type

        if opts is None:
            opts = pulumi.ResourceOptions()
        if opts.version is None:
            opts.version = version.get_version()

        super(Event, self).__init__(
            "kubernetes:events.k8s.io/v1beta1:Event",
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(name: str, id: Input[str], opts: Optional[ResourceOptions] = None):
        opts = ResourceOptions(id=id) if opts is None else opts.merge(ResourceOptions(id=id))
        return Event(name, opts)

    def translate_output_property(self, prop: str) -> str:
        return tables._CASING_FORWARD_TABLE.get(prop) or prop

    def translate_input_property(self, prop: str) -> str:
        return tables._CASING_BACKWARD_TABLE.get(prop) or prop
