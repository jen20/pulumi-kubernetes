# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from ... import _utilities, _tables
from . import outputs
from ... import meta as _meta

__all__ = [
    'FlowDistinguisherMethod',
    'FlowSchema',
    'FlowSchemaCondition',
    'FlowSchemaSpec',
    'FlowSchemaStatus',
    'GroupSubject',
    'LimitResponse',
    'LimitedPriorityLevelConfiguration',
    'NonResourcePolicyRule',
    'PolicyRulesWithSubjects',
    'PriorityLevelConfiguration',
    'PriorityLevelConfigurationCondition',
    'PriorityLevelConfigurationReference',
    'PriorityLevelConfigurationSpec',
    'PriorityLevelConfigurationStatus',
    'QueuingConfiguration',
    'ResourcePolicyRule',
    'ServiceAccountSubject',
    'Subject',
    'UserSubject',
]

@pulumi.output_type
class FlowDistinguisherMethod(dict):
    """
    FlowDistinguisherMethod specifies the method of a flow distinguisher.
    """
    @property
    @pulumi.getter
    def type(self) -> str:
        """
        `type` is the type of flow distinguisher method The supported types are "ByUser" and "ByNamespace". Required.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class FlowSchema(dict):
    """
    FlowSchema defines the schema of a group of flows. Note that a flow is made up of a set of inbound API requests with similar attributes and is identified by a pair of strings: the name of the FlowSchema and a "flow distinguisher".
    """
    @property
    @pulumi.getter(name="apiVersion")
    def api_version(self) -> Optional[str]:
        """
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
        """
        ...

    @property
    @pulumi.getter
    def kind(self) -> Optional[str]:
        """
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
        """
        ...

    @property
    @pulumi.getter
    def metadata(self) -> Optional['_meta.v1.outputs.ObjectMeta']:
        """
        `metadata` is the standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
        """
        ...

    @property
    @pulumi.getter
    def spec(self) -> Optional['outputs.FlowSchemaSpec']:
        """
        `spec` is the specification of the desired behavior of a FlowSchema. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
        """
        ...

    @property
    @pulumi.getter
    def status(self) -> Optional['outputs.FlowSchemaStatus']:
        """
        `status` is the current status of a FlowSchema. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class FlowSchemaCondition(dict):
    """
    FlowSchemaCondition describes conditions for a FlowSchema.
    """
    @property
    @pulumi.getter(name="lastTransitionTime")
    def last_transition_time(self) -> Optional[str]:
        """
        `lastTransitionTime` is the last time the condition transitioned from one status to another.
        """
        ...

    @property
    @pulumi.getter
    def message(self) -> Optional[str]:
        """
        `message` is a human-readable message indicating details about last transition.
        """
        ...

    @property
    @pulumi.getter
    def reason(self) -> Optional[str]:
        """
        `reason` is a unique, one-word, CamelCase reason for the condition's last transition.
        """
        ...

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        """
        `status` is the status of the condition. Can be True, False, Unknown. Required.
        """
        ...

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        `type` is the type of the condition. Required.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class FlowSchemaSpec(dict):
    """
    FlowSchemaSpec describes how the FlowSchema's specification looks like.
    """
    @property
    @pulumi.getter(name="distinguisherMethod")
    def distinguisher_method(self) -> Optional['outputs.FlowDistinguisherMethod']:
        """
        `distinguisherMethod` defines how to compute the flow distinguisher for requests that match this schema. `nil` specifies that the distinguisher is disabled and thus will always be the empty string.
        """
        ...

    @property
    @pulumi.getter(name="matchingPrecedence")
    def matching_precedence(self) -> Optional[float]:
        """
        `matchingPrecedence` is used to choose among the FlowSchemas that match a given request. The chosen FlowSchema is among those with the numerically lowest (which we take to be logically highest) MatchingPrecedence.  Each MatchingPrecedence value must be ranged in [1,10000]. Note that if the precedence is not specified, it will be set to 1000 as default.
        """
        ...

    @property
    @pulumi.getter(name="priorityLevelConfiguration")
    def priority_level_configuration(self) -> 'outputs.PriorityLevelConfigurationReference':
        """
        `priorityLevelConfiguration` should reference a PriorityLevelConfiguration in the cluster. If the reference cannot be resolved, the FlowSchema will be ignored and marked as invalid in its status. Required.
        """
        ...

    @property
    @pulumi.getter
    def rules(self) -> Optional[List['outputs.PolicyRulesWithSubjects']]:
        """
        `rules` describes which requests will match this flow schema. This FlowSchema matches a request if and only if at least one member of rules matches the request. if it is an empty slice, there will be no requests matching the FlowSchema.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class FlowSchemaStatus(dict):
    """
    FlowSchemaStatus represents the current state of a FlowSchema.
    """
    @property
    @pulumi.getter
    def conditions(self) -> Optional[List['outputs.FlowSchemaCondition']]:
        """
        `conditions` is a list of the current states of FlowSchema.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GroupSubject(dict):
    """
    GroupSubject holds detailed information for group-kind subject.
    """
    @property
    @pulumi.getter
    def name(self) -> str:
        """
        name is the user group that matches, or "*" to match all user groups. See https://github.com/kubernetes/apiserver/blob/master/pkg/authentication/user/user.go for some well-known group names. Required.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class LimitResponse(dict):
    """
    LimitResponse defines how to handle requests that can not be executed right now.
    """
    @property
    @pulumi.getter
    def queuing(self) -> Optional['outputs.QueuingConfiguration']:
        """
        `queuing` holds the configuration parameters for queuing. This field may be non-empty only if `type` is `"Queue"`.
        """
        ...

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        `type` is "Queue" or "Reject". "Queue" means that requests that can not be executed upon arrival are held in a queue until they can be executed or a queuing limit is reached. "Reject" means that requests that can not be executed upon arrival are rejected. Required.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class LimitedPriorityLevelConfiguration(dict):
    """
    LimitedPriorityLevelConfiguration specifies how to handle requests that are subject to limits. It addresses two issues:
     * How are requests for this priority level limited?
     * What should be done with requests that exceed the limit?
    """
    @property
    @pulumi.getter(name="assuredConcurrencyShares")
    def assured_concurrency_shares(self) -> Optional[float]:
        """
        `assuredConcurrencyShares` (ACS) configures the execution limit, which is a limit on the number of requests of this priority level that may be exeucting at a given time.  ACS must be a positive number. The server's concurrency limit (SCL) is divided among the concurrency-controlled priority levels in proportion to their assured concurrency shares. This produces the assured concurrency value (ACV) --- the number of requests that may be executing at a time --- for each such priority level:

                    ACV(l) = ceil( SCL * ACS(l) / ( sum[priority levels k] ACS(k) ) )

        bigger numbers of ACS mean more reserved concurrent requests (at the expense of every other PL). This field has a default value of 30.
        """
        ...

    @property
    @pulumi.getter(name="limitResponse")
    def limit_response(self) -> Optional['outputs.LimitResponse']:
        """
        `limitResponse` indicates what to do with requests that can not be executed right now
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class NonResourcePolicyRule(dict):
    """
    NonResourcePolicyRule is a predicate that matches non-resource requests according to their verb and the target non-resource URL. A NonResourcePolicyRule matches a request if and only if both (a) at least one member of verbs matches the request and (b) at least one member of nonResourceURLs matches the request.
    """
    @property
    @pulumi.getter(name="nonResourceURLs")
    def non_resource_urls(self) -> List[str]:
        """
        `nonResourceURLs` is a set of url prefixes that a user should have access to and may not be empty. For example:
          - "/healthz" is legal
          - "/hea*" is illegal
          - "/hea" is legal but matches nothing
          - "/hea/*" also matches nothing
          - "/healthz/*" matches all per-component health checks.
        "*" matches all non-resource urls. if it is present, it must be the only entry. Required.
        """
        ...

    @property
    @pulumi.getter
    def verbs(self) -> List[str]:
        """
        `verbs` is a list of matching verbs and may not be empty. "*" matches all verbs. If it is present, it must be the only entry. Required.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class PolicyRulesWithSubjects(dict):
    """
    PolicyRulesWithSubjects prescribes a test that applies to a request to an apiserver. The test considers the subject making the request, the verb being requested, and the resource to be acted upon. This PolicyRulesWithSubjects matches a request if and only if both (a) at least one member of subjects matches the request and (b) at least one member of resourceRules or nonResourceRules matches the request.
    """
    @property
    @pulumi.getter(name="nonResourceRules")
    def non_resource_rules(self) -> Optional[List['outputs.NonResourcePolicyRule']]:
        """
        `nonResourceRules` is a list of NonResourcePolicyRules that identify matching requests according to their verb and the target non-resource URL.
        """
        ...

    @property
    @pulumi.getter(name="resourceRules")
    def resource_rules(self) -> Optional[List['outputs.ResourcePolicyRule']]:
        """
        `resourceRules` is a slice of ResourcePolicyRules that identify matching requests according to their verb and the target resource. At least one of `resourceRules` and `nonResourceRules` has to be non-empty.
        """
        ...

    @property
    @pulumi.getter
    def subjects(self) -> List['outputs.Subject']:
        """
        subjects is the list of normal user, serviceaccount, or group that this rule cares about. There must be at least one member in this slice. A slice that includes both the system:authenticated and system:unauthenticated user groups matches every request. Required.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class PriorityLevelConfiguration(dict):
    """
    PriorityLevelConfiguration represents the configuration of a priority level.
    """
    @property
    @pulumi.getter(name="apiVersion")
    def api_version(self) -> Optional[str]:
        """
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
        """
        ...

    @property
    @pulumi.getter
    def kind(self) -> Optional[str]:
        """
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
        """
        ...

    @property
    @pulumi.getter
    def metadata(self) -> Optional['_meta.v1.outputs.ObjectMeta']:
        """
        `metadata` is the standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
        """
        ...

    @property
    @pulumi.getter
    def spec(self) -> Optional['outputs.PriorityLevelConfigurationSpec']:
        """
        `spec` is the specification of the desired behavior of a "request-priority". More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
        """
        ...

    @property
    @pulumi.getter
    def status(self) -> Optional['outputs.PriorityLevelConfigurationStatus']:
        """
        `status` is the current status of a "request-priority". More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class PriorityLevelConfigurationCondition(dict):
    """
    PriorityLevelConfigurationCondition defines the condition of priority level.
    """
    @property
    @pulumi.getter(name="lastTransitionTime")
    def last_transition_time(self) -> Optional[str]:
        """
        `lastTransitionTime` is the last time the condition transitioned from one status to another.
        """
        ...

    @property
    @pulumi.getter
    def message(self) -> Optional[str]:
        """
        `message` is a human-readable message indicating details about last transition.
        """
        ...

    @property
    @pulumi.getter
    def reason(self) -> Optional[str]:
        """
        `reason` is a unique, one-word, CamelCase reason for the condition's last transition.
        """
        ...

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        """
        `status` is the status of the condition. Can be True, False, Unknown. Required.
        """
        ...

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        `type` is the type of the condition. Required.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class PriorityLevelConfigurationReference(dict):
    """
    PriorityLevelConfigurationReference contains information that points to the "request-priority" being used.
    """
    @property
    @pulumi.getter
    def name(self) -> str:
        """
        `name` is the name of the priority level configuration being referenced Required.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class PriorityLevelConfigurationSpec(dict):
    """
    PriorityLevelConfigurationSpec specifies the configuration of a priority level.
    """
    @property
    @pulumi.getter
    def limited(self) -> Optional['outputs.LimitedPriorityLevelConfiguration']:
        """
        `limited` specifies how requests are handled for a Limited priority level. This field must be non-empty if and only if `type` is `"Limited"`.
        """
        ...

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        `type` indicates whether this priority level is subject to limitation on request execution.  A value of `"Exempt"` means that requests of this priority level are not subject to a limit (and thus are never queued) and do not detract from the capacity made available to other priority levels.  A value of `"Limited"` means that (a) requests of this priority level _are_ subject to limits and (b) some of the server's limited capacity is made available exclusively to this priority level. Required.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class PriorityLevelConfigurationStatus(dict):
    """
    PriorityLevelConfigurationStatus represents the current state of a "request-priority".
    """
    @property
    @pulumi.getter
    def conditions(self) -> Optional[List['outputs.PriorityLevelConfigurationCondition']]:
        """
        `conditions` is the current state of "request-priority".
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class QueuingConfiguration(dict):
    """
    QueuingConfiguration holds the configuration parameters for queuing
    """
    @property
    @pulumi.getter(name="handSize")
    def hand_size(self) -> Optional[float]:
        """
        `handSize` is a small positive number that configures the shuffle sharding of requests into queues.  When enqueuing a request at this priority level the request's flow identifier (a string pair) is hashed and the hash value is used to shuffle the list of queues and deal a hand of the size specified here.  The request is put into one of the shortest queues in that hand. `handSize` must be no larger than `queues`, and should be significantly smaller (so that a few heavy flows do not saturate most of the queues).  See the user-facing documentation for more extensive guidance on setting this field.  This field has a default value of 8.
        """
        ...

    @property
    @pulumi.getter(name="queueLengthLimit")
    def queue_length_limit(self) -> Optional[float]:
        """
        `queueLengthLimit` is the maximum number of requests allowed to be waiting in a given queue of this priority level at a time; excess requests are rejected.  This value must be positive.  If not specified, it will be defaulted to 50.
        """
        ...

    @property
    @pulumi.getter
    def queues(self) -> Optional[float]:
        """
        `queues` is the number of queues for this priority level. The queues exist independently at each apiserver. The value must be positive.  Setting it to 1 effectively precludes shufflesharding and thus makes the distinguisher method of associated flow schemas irrelevant.  This field has a default value of 64.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ResourcePolicyRule(dict):
    """
    ResourcePolicyRule is a predicate that matches some resource requests, testing the request's verb and the target resource. A ResourcePolicyRule matches a resource request if and only if: (a) at least one member of verbs matches the request, (b) at least one member of apiGroups matches the request, (c) at least one member of resources matches the request, and (d) least one member of namespaces matches the request.
    """
    @property
    @pulumi.getter(name="apiGroups")
    def api_groups(self) -> List[str]:
        """
        `apiGroups` is a list of matching API groups and may not be empty. "*" matches all API groups and, if present, must be the only entry. Required.
        """
        ...

    @property
    @pulumi.getter(name="clusterScope")
    def cluster_scope(self) -> Optional[bool]:
        """
        `clusterScope` indicates whether to match requests that do not specify a namespace (which happens either because the resource is not namespaced or the request targets all namespaces). If this field is omitted or false then the `namespaces` field must contain a non-empty list.
        """
        ...

    @property
    @pulumi.getter
    def namespaces(self) -> Optional[List[str]]:
        """
        `namespaces` is a list of target namespaces that restricts matches.  A request that specifies a target namespace matches only if either (a) this list contains that target namespace or (b) this list contains "*".  Note that "*" matches any specified namespace but does not match a request that _does not specify_ a namespace (see the `clusterScope` field for that). This list may be empty, but only if `clusterScope` is true.
        """
        ...

    @property
    @pulumi.getter
    def resources(self) -> List[str]:
        """
        `resources` is a list of matching resources (i.e., lowercase and plural) with, if desired, subresource.  For example, [ "services", "nodes/status" ].  This list may not be empty. "*" matches all resources and, if present, must be the only entry. Required.
        """
        ...

    @property
    @pulumi.getter
    def verbs(self) -> List[str]:
        """
        `verbs` is a list of matching verbs and may not be empty. "*" matches all verbs and, if present, must be the only entry. Required.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ServiceAccountSubject(dict):
    """
    ServiceAccountSubject holds detailed information for service-account-kind subject.
    """
    @property
    @pulumi.getter
    def name(self) -> str:
        """
        `name` is the name of matching ServiceAccount objects, or "*" to match regardless of name. Required.
        """
        ...

    @property
    @pulumi.getter
    def namespace(self) -> str:
        """
        `namespace` is the namespace of matching ServiceAccount objects. Required.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class Subject(dict):
    """
    Subject matches the originator of a request, as identified by the request authentication system. There are three ways of matching an originator; by user, group, or service account.
    """
    @property
    @pulumi.getter
    def group(self) -> Optional['outputs.GroupSubject']:
        ...

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        Required
        """
        ...

    @property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional['outputs.ServiceAccountSubject']:
        ...

    @property
    @pulumi.getter
    def user(self) -> Optional['outputs.UserSubject']:
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class UserSubject(dict):
    """
    UserSubject holds detailed information for user-kind subject.
    """
    @property
    @pulumi.getter
    def name(self) -> str:
        """
        `name` is the username that matches, or "*" to match all usernames. Required.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


