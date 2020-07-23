# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from ... import _utilities, _tables

__all__ = [
    'TokenReviewSpecArgs',
]

@pulumi.input_type
class TokenReviewSpecArgs:
    def __init__(__self__, *,
                 audiences: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
                 token: Optional[pulumi.Input[str]] = None):
        """
        TokenReviewSpec is a description of the token authentication request.
        :param pulumi.Input[List[pulumi.Input[str]]] audiences: Audiences is a list of the identifiers that the resource server presented with the token identifies as. Audience-aware token authenticators will verify that the token was intended for at least one of the audiences in this list. If no audiences are provided, the audience will default to the audience of the Kubernetes apiserver.
        :param pulumi.Input[str] token: Token is the opaque bearer token.
        """
        pulumi.set(__self__, "audiences", audiences)
        pulumi.set(__self__, "token", token)

    @property
    @pulumi.getter
    def audiences(self) -> Optional[pulumi.Input[List[pulumi.Input[str]]]]:
        """
        Audiences is a list of the identifiers that the resource server presented with the token identifies as. Audience-aware token authenticators will verify that the token was intended for at least one of the audiences in this list. If no audiences are provided, the audience will default to the audience of the Kubernetes apiserver.
        """
        ...

    @audiences.setter
    def audiences(self, value: Optional[pulumi.Input[List[pulumi.Input[str]]]]):
        ...

    @property
    @pulumi.getter
    def token(self) -> Optional[pulumi.Input[str]]:
        """
        Token is the opaque bearer token.
        """
        ...

    @token.setter
    def token(self, value: Optional[pulumi.Input[str]]):
        ...


