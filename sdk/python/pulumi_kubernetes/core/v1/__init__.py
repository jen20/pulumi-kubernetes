# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from ._enums import *
from .Binding import *
from .ConfigMap import *
from .ConfigMapList import *
from .Endpoints import *
from .EndpointsList import *
from .EphemeralContainers import *
from .Event import *
from .EventList import *
from .LimitRange import *
from .LimitRangeList import *
from .Namespace import *
from .NamespaceList import *
from .Node import *
from .NodeList import *
from .PersistentVolume import *
from .PersistentVolumeClaim import *
from .PersistentVolumeClaimList import *
from .PersistentVolumeList import *
from .Pod import *
from .PodList import *
from .PodTemplate import *
from .PodTemplateList import *
from .ReplicationController import *
from .ReplicationControllerList import *
from .ResourceQuota import *
from .ResourceQuotaList import *
from .Secret import *
from .SecretList import *
from .Service import *
from .ServiceAccount import *
from .ServiceAccountList import *
from .ServiceList import *
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
            if typ == "kubernetes:core/v1:Binding":
                return Binding(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "kubernetes:core/v1:ConfigMap":
                return ConfigMap(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "kubernetes:core/v1:ConfigMapList":
                return ConfigMapList(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "kubernetes:core/v1:Endpoints":
                return Endpoints(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "kubernetes:core/v1:EndpointsList":
                return EndpointsList(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "kubernetes:core/v1:EphemeralContainers":
                return EphemeralContainers(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "kubernetes:core/v1:Event":
                return Event(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "kubernetes:core/v1:EventList":
                return EventList(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "kubernetes:core/v1:LimitRange":
                return LimitRange(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "kubernetes:core/v1:LimitRangeList":
                return LimitRangeList(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "kubernetes:core/v1:Namespace":
                return Namespace(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "kubernetes:core/v1:NamespaceList":
                return NamespaceList(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "kubernetes:core/v1:Node":
                return Node(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "kubernetes:core/v1:NodeList":
                return NodeList(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "kubernetes:core/v1:PersistentVolume":
                return PersistentVolume(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "kubernetes:core/v1:PersistentVolumeClaim":
                return PersistentVolumeClaim(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "kubernetes:core/v1:PersistentVolumeClaimList":
                return PersistentVolumeClaimList(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "kubernetes:core/v1:PersistentVolumeList":
                return PersistentVolumeList(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "kubernetes:core/v1:Pod":
                return Pod(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "kubernetes:core/v1:PodList":
                return PodList(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "kubernetes:core/v1:PodTemplate":
                return PodTemplate(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "kubernetes:core/v1:PodTemplateList":
                return PodTemplateList(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "kubernetes:core/v1:ReplicationController":
                return ReplicationController(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "kubernetes:core/v1:ReplicationControllerList":
                return ReplicationControllerList(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "kubernetes:core/v1:ResourceQuota":
                return ResourceQuota(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "kubernetes:core/v1:ResourceQuotaList":
                return ResourceQuotaList(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "kubernetes:core/v1:Secret":
                return Secret(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "kubernetes:core/v1:SecretList":
                return SecretList(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "kubernetes:core/v1:Service":
                return Service(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "kubernetes:core/v1:ServiceAccount":
                return ServiceAccount(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "kubernetes:core/v1:ServiceAccountList":
                return ServiceAccountList(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "kubernetes:core/v1:ServiceList":
                return ServiceList(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("kubernetes", "core/v1", _module_instance)

_register_module()
