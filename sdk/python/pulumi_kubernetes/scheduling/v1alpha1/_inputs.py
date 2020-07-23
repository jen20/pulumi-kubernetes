# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from ... import _utilities, _tables
from ... import meta as _meta

__all__ = [
    'PriorityClassArgs',
]

@pulumi.input_type
class PriorityClassArgs:
    def __init__(__self__, *,
                 value: pulumi.Input[float],
                 api_version: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 global_default: Optional[pulumi.Input[bool]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input['_meta.v1.ObjectMetaArgs']] = None,
                 preemption_policy: Optional[pulumi.Input[str]] = None):
        """
        DEPRECATED - This group version of PriorityClass is deprecated by scheduling.k8s.io/v1/PriorityClass. PriorityClass defines mapping from a priority class name to the priority integer value. The value can be any valid integer.
        :param pulumi.Input[float] value: The value of this priority class. This is the actual priority that pods receive when they have the name of this class in their pod spec.
        :param pulumi.Input[str] api_version: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
        :param pulumi.Input[str] description: description is an arbitrary string that usually provides guidelines on when this priority class should be used.
        :param pulumi.Input[bool] global_default: globalDefault specifies whether this PriorityClass should be considered as the default priority for pods that do not have any priority class. Only one PriorityClass can be marked as `globalDefault`. However, if more than one PriorityClasses exists with their `globalDefault` field set to true, the smallest value of such global default PriorityClasses will be used as the default priority.
        :param pulumi.Input[str] kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
        :param pulumi.Input['_meta.v1.ObjectMetaArgs'] metadata: Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
        :param pulumi.Input[str] preemption_policy: PreemptionPolicy is the Policy for preempting pods with lower priority. One of Never, PreemptLowerPriority. Defaults to PreemptLowerPriority if unset. This field is alpha-level and is only honored by servers that enable the NonPreemptingPriority feature.
        """
        pulumi.set(__self__, "value", value)
        pulumi.set(__self__, "apiVersion", 'scheduling.k8s.io/v1alpha1')
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "globalDefault", global_default)
        pulumi.set(__self__, "kind", 'PriorityClass')
        pulumi.set(__self__, "metadata", metadata)
        pulumi.set(__self__, "preemptionPolicy", preemption_policy)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[float]:
        """
        The value of this priority class. This is the actual priority that pods receive when they have the name of this class in their pod spec.
        """
        ...

    @value.setter
    def value(self, value: pulumi.Input[float]):
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
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        description is an arbitrary string that usually provides guidelines on when this priority class should be used.
        """
        ...

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        ...

    @property
    @pulumi.getter(name="globalDefault")
    def global_default(self) -> Optional[pulumi.Input[bool]]:
        """
        globalDefault specifies whether this PriorityClass should be considered as the default priority for pods that do not have any priority class. Only one PriorityClass can be marked as `globalDefault`. However, if more than one PriorityClasses exists with their `globalDefault` field set to true, the smallest value of such global default PriorityClasses will be used as the default priority.
        """
        ...

    @global_default.setter
    def global_default(self, value: Optional[pulumi.Input[bool]]):
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
        Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
        """
        ...

    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input['_meta.v1.ObjectMetaArgs']]):
        ...

    @property
    @pulumi.getter(name="preemptionPolicy")
    def preemption_policy(self) -> Optional[pulumi.Input[str]]:
        """
        PreemptionPolicy is the Policy for preempting pods with lower priority. One of Never, PreemptLowerPriority. Defaults to PreemptLowerPriority if unset. This field is alpha-level and is only honored by servers that enable the NonPreemptingPriority feature.
        """
        ...

    @preemption_policy.setter
    def preemption_policy(self, value: Optional[pulumi.Input[str]]):
        ...


