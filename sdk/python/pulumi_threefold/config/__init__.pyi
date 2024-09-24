# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

graphql_url: Optional[str]
"""
The graphql urls, example: https://graphql.grid.tf/graphql
"""

key_type: str
"""
The key type registered on substrate (ed25519 or sr25519).
"""

mnemonic: str
"""
The mnemonic of the user. It is very secret.
"""

network: str
"""
The network to deploy on.
"""

proxy_url: Optional[str]
"""
The proxy urls, example: https://gridproxy.grid.tf/
"""

relay_url: Optional[str]
"""
The relay urls, example: wss://relay.grid.tf
"""

rmb_timeout: Optional[str]
"""
The timeout duration in seconds for rmb calls
"""

substrate_url: Optional[str]
"""
The substrate url, example: wss://tfchain.grid.tf/ws
"""

