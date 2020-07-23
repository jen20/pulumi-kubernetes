# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from ... import _utilities, _tables
from ... import core as _core
from ... import meta as _meta

__all__ = [
    'OverheadArgs',
    'RuntimeClassArgs',
    'SchedulingArgs',
]

@pulumi.input_type
class OverheadArgs:
    def __init__(__self__, *,
                 pod_fixed: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        Overhead structure represents the resource overhead associated with running a pod.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] pod_fixed: PodFixed represents the fixed resource overhead associated with running a pod.
        """
        pulumi.set(__self__, "podFixed", pod_fixed)

    @property
    @pulumi.getter(name="podFixed")
    def pod_fixed(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        PodFixed represents the fixed resource overhead associated with running a pod.
        """
        ...

    @pod_fixed.setter
    def pod_fixed(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        ...


@pulumi.input_type
class RuntimeClassArgs:
    def __init__(__self__, *,
                 handler: pulumi.Input[str],
                 api_version: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input['_meta.v1.ObjectMetaArgs']] = None,
                 overhead: Optional[pulumi.Input['OverheadArgs']] = None,
                 scheduling: Optional[pulumi.Input['SchedulingArgs']] = None):
        """
        RuntimeClass defines a class of container runtime supported in the cluster. The RuntimeClass is used to determine which container runtime is used to run all containers in a pod. RuntimeClasses are (currently) manually defined by a user or cluster provisioner, and referenced in the PodSpec. The Kubelet is responsible for resolving the RuntimeClassName reference before running the pod.  For more details, see https://git.k8s.io/enhancements/keps/sig-node/runtime-class.md
        :param pulumi.Input[str] handler: Handler specifies the underlying runtime and configuration that the CRI implementation will use to handle pods of this class. The possible values are specific to the node & CRI configuration.  It is assumed that all handlers are available on every node, and handlers of the same name are equivalent on every node. For example, a handler called "runc" might specify that the runc OCI runtime (using native Linux containers) will be used to run the containers in a pod. The Handler must conform to the DNS Label (RFC 1123) requirements, and is immutable.
        :param pulumi.Input[str] api_version: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
        :param pulumi.Input[str] kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
        :param pulumi.Input['_meta.v1.ObjectMetaArgs'] metadata: More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
        :param pulumi.Input['OverheadArgs'] overhead: Overhead represents the resource overhead associated with running a pod for a given RuntimeClass. For more details, see https://git.k8s.io/enhancements/keps/sig-node/20190226-pod-overhead.md This field is alpha-level as of Kubernetes v1.15, and is only honored by servers that enable the PodOverhead feature.
        :param pulumi.Input['SchedulingArgs'] scheduling: Scheduling holds the scheduling constraints to ensure that pods running with this RuntimeClass are scheduled to nodes that support it. If scheduling is nil, this RuntimeClass is assumed to be supported by all nodes.
        """
        pulumi.set(__self__, "handler", handler)
        pulumi.set(__self__, "apiVersion", 'node.k8s.io/v1beta1')
        pulumi.set(__self__, "kind", 'RuntimeClass')
        pulumi.set(__self__, "metadata", metadata)
        pulumi.set(__self__, "overhead", overhead)
        pulumi.set(__self__, "scheduling", scheduling)

    @property
    @pulumi.getter
    def handler(self) -> pulumi.Input[str]:
        """
        Handler specifies the underlying runtime and configuration that the CRI implementation will use to handle pods of this class. The possible values are specific to the node & CRI configuration.  It is assumed that all handlers are available on every node, and handlers of the same name are equivalent on every node. For example, a handler called "runc" might specify that the runc OCI runtime (using native Linux containers) will be used to run the containers in a pod. The Handler must conform to the DNS Label (RFC 1123) requirements, and is immutable.
        """
        ...

    @handler.setter
    def handler(self, value: pulumi.Input[str]):
        ...

    @property
    @pulumi.getter(name="apiVersion")
    def api_version(self) -> Optional[pulumi.Input[str]]:
        """
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
        """
        ...

    @api_version.setter
    def api_version(self, value: Optional[pulumi.Input[str]]):
        ...

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[str]]:
        """
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
        """
        ...

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[str]]):
        ...

    @property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input['_meta.v1.ObjectMetaArgs']]:
        """
        More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
        """
        ...

    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input['_meta.v1.ObjectMetaArgs']]):
        ...

    @property
    @pulumi.getter
    def overhead(self) -> Optional[pulumi.Input['OverheadArgs']]:
        """
        Overhead represents the resource overhead associated with running a pod for a given RuntimeClass. For more details, see https://git.k8s.io/enhancements/keps/sig-node/20190226-pod-overhead.md This field is alpha-level as of Kubernetes v1.15, and is only honored by servers that enable the PodOverhead feature.
        """
        ...

    @overhead.setter
    def overhead(self, value: Optional[pulumi.Input['OverheadArgs']]):
        ...

    @property
    @pulumi.getter
    def scheduling(self) -> Optional[pulumi.Input['SchedulingArgs']]:
        """
        Scheduling holds the scheduling constraints to ensure that pods running with this RuntimeClass are scheduled to nodes that support it. If scheduling is nil, this RuntimeClass is assumed to be supported by all nodes.
        """
        ...

    @scheduling.setter
    def scheduling(self, value: Optional[pulumi.Input['SchedulingArgs']]):
        ...


@pulumi.input_type
class SchedulingArgs:
    def __init__(__self__, *,
                 node_selector: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tolerations: Optional[pulumi.Input[List[pulumi.Input['_core.v1.TolerationArgs']]]] = None):
        """
        Scheduling specifies the scheduling constraints for nodes supporting a RuntimeClass.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] node_selector: nodeSelector lists labels that must be present on nodes that support this RuntimeClass. Pods using this RuntimeClass can only be scheduled to a node matched by this selector. The RuntimeClass nodeSelector is merged with a pod's existing nodeSelector. Any conflicts will cause the pod to be rejected in admission.
        :param pulumi.Input[List[pulumi.Input['_core.v1.TolerationArgs']]] tolerations: tolerations are appended (excluding duplicates) to pods running with this RuntimeClass during admission, effectively unioning the set of nodes tolerated by the pod and the RuntimeClass.
        """
        pulumi.set(__self__, "nodeSelector", node_selector)
        pulumi.set(__self__, "tolerations", tolerations)

    @property
    @pulumi.getter(name="nodeSelector")
    def node_selector(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        nodeSelector lists labels that must be present on nodes that support this RuntimeClass. Pods using this RuntimeClass can only be scheduled to a node matched by this selector. The RuntimeClass nodeSelector is merged with a pod's existing nodeSelector. Any conflicts will cause the pod to be rejected in admission.
        """
        ...

    @node_selector.setter
    def node_selector(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        ...

    @property
    @pulumi.getter
    def tolerations(self) -> Optional[pulumi.Input[List[pulumi.Input['_core.v1.TolerationArgs']]]]:
        """
        tolerations are appended (excluding duplicates) to pods running with this RuntimeClass during admission, effectively unioning the set of nodes tolerated by the pod and the RuntimeClass.
        """
        ...

    @tolerations.setter
    def tolerations(self, value: Optional[pulumi.Input[List[pulumi.Input['_core.v1.TolerationArgs']]]]):
        ...


