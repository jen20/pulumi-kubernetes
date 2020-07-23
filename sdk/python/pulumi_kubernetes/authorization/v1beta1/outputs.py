# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from ... import _utilities, _tables
from . import outputs

__all__ = [
    'NonResourceAttributes',
    'NonResourceRule',
    'ResourceAttributes',
    'ResourceRule',
    'SelfSubjectAccessReviewSpec',
    'SelfSubjectRulesReviewSpec',
    'SubjectAccessReviewSpec',
    'SubjectAccessReviewStatus',
    'SubjectRulesReviewStatus',
]

@pulumi.output_type
class NonResourceAttributes(dict):
    """
    NonResourceAttributes includes the authorization attributes available for non-resource requests to the Authorizer interface
    """
    @property
    @pulumi.getter
    def path(self) -> Optional[str]:
        """
        Path is the URL path of the request
        """
        ...

    @property
    @pulumi.getter
    def verb(self) -> Optional[str]:
        """
        Verb is the standard HTTP verb
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class NonResourceRule(dict):
    """
    NonResourceRule holds information that describes a rule for the non-resource
    """
    @property
    @pulumi.getter(name="nonResourceURLs")
    def non_resource_urls(self) -> Optional[List[str]]:
        """
        NonResourceURLs is a set of partial urls that a user should have access to.  *s are allowed, but only as the full, final step in the path.  "*" means all.
        """
        ...

    @property
    @pulumi.getter
    def verbs(self) -> List[str]:
        """
        Verb is a list of kubernetes non-resource API verbs, like: get, post, put, delete, patch, head, options.  "*" means all.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ResourceAttributes(dict):
    """
    ResourceAttributes includes the authorization attributes available for resource requests to the Authorizer interface
    """
    @property
    @pulumi.getter
    def group(self) -> Optional[str]:
        """
        Group is the API Group of the Resource.  "*" means all.
        """
        ...

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Name is the name of the resource being requested for a "get" or deleted for a "delete". "" (empty) means all.
        """
        ...

    @property
    @pulumi.getter
    def namespace(self) -> Optional[str]:
        """
        Namespace is the namespace of the action being requested.  Currently, there is no distinction between no namespace and all namespaces "" (empty) is defaulted for LocalSubjectAccessReviews "" (empty) is empty for cluster-scoped resources "" (empty) means "all" for namespace scoped resources from a SubjectAccessReview or SelfSubjectAccessReview
        """
        ...

    @property
    @pulumi.getter
    def resource(self) -> Optional[str]:
        """
        Resource is one of the existing resource types.  "*" means all.
        """
        ...

    @property
    @pulumi.getter
    def subresource(self) -> Optional[str]:
        """
        Subresource is one of the existing resource types.  "" means none.
        """
        ...

    @property
    @pulumi.getter
    def verb(self) -> Optional[str]:
        """
        Verb is a kubernetes resource API verb, like: get, list, watch, create, update, delete, proxy.  "*" means all.
        """
        ...

    @property
    @pulumi.getter
    def version(self) -> Optional[str]:
        """
        Version is the API Version of the Resource.  "*" means all.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ResourceRule(dict):
    """
    ResourceRule is the list of actions the subject is allowed to perform on resources. The list ordering isn't significant, may contain duplicates, and possibly be incomplete.
    """
    @property
    @pulumi.getter(name="apiGroups")
    def api_groups(self) -> Optional[List[str]]:
        """
        APIGroups is the name of the APIGroup that contains the resources.  If multiple API groups are specified, any action requested against one of the enumerated resources in any API group will be allowed.  "*" means all.
        """
        ...

    @property
    @pulumi.getter(name="resourceNames")
    def resource_names(self) -> Optional[List[str]]:
        """
        ResourceNames is an optional white list of names that the rule applies to.  An empty set means that everything is allowed.  "*" means all.
        """
        ...

    @property
    @pulumi.getter
    def resources(self) -> Optional[List[str]]:
        """
        Resources is a list of resources this rule applies to.  "*" means all in the specified apiGroups.
         "*/foo" represents the subresource 'foo' for all resources in the specified apiGroups.
        """
        ...

    @property
    @pulumi.getter
    def verbs(self) -> List[str]:
        """
        Verb is a list of kubernetes resource API verbs, like: get, list, watch, create, update, delete, proxy.  "*" means all.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class SelfSubjectAccessReviewSpec(dict):
    """
    SelfSubjectAccessReviewSpec is a description of the access request.  Exactly one of ResourceAuthorizationAttributes and NonResourceAuthorizationAttributes must be set
    """
    @property
    @pulumi.getter(name="nonResourceAttributes")
    def non_resource_attributes(self) -> Optional['outputs.NonResourceAttributes']:
        """
        NonResourceAttributes describes information for a non-resource access request
        """
        ...

    @property
    @pulumi.getter(name="resourceAttributes")
    def resource_attributes(self) -> Optional['outputs.ResourceAttributes']:
        """
        ResourceAuthorizationAttributes describes information for a resource access request
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class SelfSubjectRulesReviewSpec(dict):
    @property
    @pulumi.getter
    def namespace(self) -> Optional[str]:
        """
        Namespace to evaluate rules for. Required.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class SubjectAccessReviewSpec(dict):
    """
    SubjectAccessReviewSpec is a description of the access request.  Exactly one of ResourceAuthorizationAttributes and NonResourceAuthorizationAttributes must be set
    """
    @property
    @pulumi.getter
    def extra(self) -> Optional[Mapping[str, List[str]]]:
        """
        Extra corresponds to the user.Info.GetExtra() method from the authenticator.  Since that is input to the authorizer it needs a reflection here.
        """
        ...

    @property
    @pulumi.getter
    def group(self) -> Optional[List[str]]:
        """
        Groups is the groups you're testing for.
        """
        ...

    @property
    @pulumi.getter(name="nonResourceAttributes")
    def non_resource_attributes(self) -> Optional['outputs.NonResourceAttributes']:
        """
        NonResourceAttributes describes information for a non-resource access request
        """
        ...

    @property
    @pulumi.getter(name="resourceAttributes")
    def resource_attributes(self) -> Optional['outputs.ResourceAttributes']:
        """
        ResourceAuthorizationAttributes describes information for a resource access request
        """
        ...

    @property
    @pulumi.getter
    def uid(self) -> Optional[str]:
        """
        UID information about the requesting user.
        """
        ...

    @property
    @pulumi.getter
    def user(self) -> Optional[str]:
        """
        User is the user you're testing for. If you specify "User" but not "Group", then is it interpreted as "What if User were not a member of any groups
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class SubjectAccessReviewStatus(dict):
    """
    SubjectAccessReviewStatus
    """
    @property
    @pulumi.getter
    def allowed(self) -> bool:
        """
        Allowed is required. True if the action would be allowed, false otherwise.
        """
        ...

    @property
    @pulumi.getter
    def denied(self) -> Optional[bool]:
        """
        Denied is optional. True if the action would be denied, otherwise false. If both allowed is false and denied is false, then the authorizer has no opinion on whether to authorize the action. Denied may not be true if Allowed is true.
        """
        ...

    @property
    @pulumi.getter(name="evaluationError")
    def evaluation_error(self) -> Optional[str]:
        """
        EvaluationError is an indication that some error occurred during the authorization check. It is entirely possible to get an error and be able to continue determine authorization status in spite of it. For instance, RBAC can be missing a role, but enough roles are still present and bound to reason about the request.
        """
        ...

    @property
    @pulumi.getter
    def reason(self) -> Optional[str]:
        """
        Reason is optional.  It indicates why a request was allowed or denied.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class SubjectRulesReviewStatus(dict):
    """
    SubjectRulesReviewStatus contains the result of a rules check. This check can be incomplete depending on the set of authorizers the server is configured with and any errors experienced during evaluation. Because authorization rules are additive, if a rule appears in a list it's safe to assume the subject has that permission, even if that list is incomplete.
    """
    @property
    @pulumi.getter(name="evaluationError")
    def evaluation_error(self) -> Optional[str]:
        """
        EvaluationError can appear in combination with Rules. It indicates an error occurred during rule evaluation, such as an authorizer that doesn't support rule evaluation, and that ResourceRules and/or NonResourceRules may be incomplete.
        """
        ...

    @property
    @pulumi.getter
    def incomplete(self) -> bool:
        """
        Incomplete is true when the rules returned by this call are incomplete. This is most commonly encountered when an authorizer, such as an external authorizer, doesn't support rules evaluation.
        """
        ...

    @property
    @pulumi.getter(name="nonResourceRules")
    def non_resource_rules(self) -> List['outputs.NonResourceRule']:
        """
        NonResourceRules is the list of actions the subject is allowed to perform on non-resources. The list ordering isn't significant, may contain duplicates, and possibly be incomplete.
        """
        ...

    @property
    @pulumi.getter(name="resourceRules")
    def resource_rules(self) -> List['outputs.ResourceRule']:
        """
        ResourceRules is the list of actions the subject is allowed to perform on resources. The list ordering isn't significant, may contain duplicates, and possibly be incomplete.
        """
        ...

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


