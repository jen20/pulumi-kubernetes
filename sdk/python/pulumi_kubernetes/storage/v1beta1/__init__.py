# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .CSIDriver import *
from .CSIDriverList import *
from .CSINode import *
from .CSINodeList import *
from .CSIStorageCapacity import *
from .CSIStorageCapacityList import *
from .StorageClass import *
from .StorageClassList import *
from .VolumeAttachment import *
from .VolumeAttachmentList import *
from ._inputs import *
from . import outputs

def _register_module():
    import pulumi
    from ... import _utilities


    class Module(pulumi.runtime.ResourceModule):
        _version = _utilities.get_semver_version()

        def version(self):
            return Module._version

        def construct(self, name: str, typ: str, urn: str) -> pulumi.Resource:
            if typ == "kubernetes:storage.k8s.io/v1beta1:CSIDriver":
                return CSIDriver(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "kubernetes:storage.k8s.io/v1beta1:CSIDriverList":
                return CSIDriverList(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "kubernetes:storage.k8s.io/v1beta1:CSINode":
                return CSINode(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "kubernetes:storage.k8s.io/v1beta1:CSINodeList":
                return CSINodeList(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "kubernetes:storage.k8s.io/v1beta1:CSIStorageCapacity":
                return CSIStorageCapacity(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "kubernetes:storage.k8s.io/v1beta1:CSIStorageCapacityList":
                return CSIStorageCapacityList(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "kubernetes:storage.k8s.io/v1beta1:StorageClass":
                return StorageClass(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "kubernetes:storage.k8s.io/v1beta1:StorageClassList":
                return StorageClassList(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "kubernetes:storage.k8s.io/v1beta1:VolumeAttachment":
                return VolumeAttachment(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "kubernetes:storage.k8s.io/v1beta1:VolumeAttachmentList":
                return VolumeAttachmentList(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("kubernetes", "storage.k8s.io/v1beta1", _module_instance)

_register_module()
