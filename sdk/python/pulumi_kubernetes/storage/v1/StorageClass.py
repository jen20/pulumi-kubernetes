# *** WARNING: this file was generated by the Pulumi Kubernetes codegen tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
from typing import Optional

import pulumi
import pulumi.runtime
from pulumi import Input, ResourceOptions

from ... import tables, version


class StorageClass(pulumi.CustomResource):
    """
    StorageClass describes the parameters for a class of storage for which PersistentVolumes can be
    dynamically provisioned.
    
    StorageClasses are non-namespaced; the name of the storage class according to etcd is in
    ObjectMeta.Name.
    """

    def __init__(self, resource_name, opts=None, allow_volume_expansion=None, allowed_topologies=None, metadata=None, mount_options=None, parameters=None, provisioner=None, reclaim_policy=None, volume_binding_mode=None, __name__=None, __opts__=None):
        """
        Create a StorageClass resource with the given unique name, arguments, and options.
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

        __props__['apiVersion'] = 'storage.k8s.io/v1'
        __props__['kind'] = 'StorageClass'
        if provisioner is None:
            raise TypeError('Missing required property provisioner')
        __props__['provisioner'] = provisioner
        __props__['allowVolumeExpansion'] = allow_volume_expansion
        __props__['allowedTopologies'] = allowed_topologies
        __props__['metadata'] = metadata
        __props__['mountOptions'] = mount_options
        __props__['parameters'] = parameters
        __props__['reclaimPolicy'] = reclaim_policy
        __props__['volumeBindingMode'] = volume_binding_mode

        if opts is None:
            opts = pulumi.ResourceOptions()
        if opts.version is None:
            opts.version = version.get_version()

        super(StorageClass, self).__init__(
            "kubernetes:storage.k8s.io/v1:StorageClass",
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(name: str, id: Input[str], opts: Optional[ResourceOptions] = None):
        opts = ResourceOptions(id=id) if opts is None else opts.merge(ResourceOptions(id=id))
        return StorageClass(name, opts)

    def translate_output_property(self, prop: str) -> str:
        return tables._CASING_FORWARD_TABLE.get(prop) or prop

    def translate_input_property(self, prop: str) -> str:
        return tables._CASING_BACKWARD_TABLE.get(prop) or prop
