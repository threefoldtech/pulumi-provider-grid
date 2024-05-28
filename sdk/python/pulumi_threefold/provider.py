# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ProviderArgs', 'Provider']

@pulumi.input_type
class ProviderArgs:
    def __init__(__self__, *,
                 key_type: Optional[pulumi.Input[str]] = None,
                 mnemonic: Optional[pulumi.Input[str]] = None,
                 network: Optional[pulumi.Input[str]] = None,
                 relay_url: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 rmb_timeout: Optional[pulumi.Input[str]] = None,
                 substrate_url: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Provider resource.
        :param pulumi.Input[str] key_type: The key type registered on substrate (ed25519 or sr25519).
        :param pulumi.Input[str] mnemonic: The mnemonic of the user. It is very secret.
        :param pulumi.Input[str] network: The network to deploy on.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] relay_url: The relay urls, example: wss://relay.dev.grid.tf
        :param pulumi.Input[str] rmb_timeout: The timeout duration in seconds for rmb calls
        :param pulumi.Input[str] substrate_url: The substrate url, example: wss://tfchain.dev.grid.tf/ws
        """
        if key_type is None:
            key_type = (_utilities.get_env('') or 'sr25519')
        if key_type is not None:
            pulumi.set(__self__, "key_type", key_type)
        if mnemonic is None:
            mnemonic = (_utilities.get_env('') or '')
        if mnemonic is not None:
            pulumi.set(__self__, "mnemonic", mnemonic)
        if network is None:
            network = (_utilities.get_env('') or '')
        if network is not None:
            pulumi.set(__self__, "network", network)
        if relay_url is not None:
            pulumi.set(__self__, "relay_url", relay_url)
        if rmb_timeout is not None:
            pulumi.set(__self__, "rmb_timeout", rmb_timeout)
        if substrate_url is not None:
            pulumi.set(__self__, "substrate_url", substrate_url)

    @property
    @pulumi.getter
    def key_type(self) -> Optional[pulumi.Input[str]]:
        """
        The key type registered on substrate (ed25519 or sr25519).
        """
        return pulumi.get(self, "key_type")

    @key_type.setter
    def key_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key_type", value)

    @property
    @pulumi.getter
    def mnemonic(self) -> Optional[pulumi.Input[str]]:
        """
        The mnemonic of the user. It is very secret.
        """
        return pulumi.get(self, "mnemonic")

    @mnemonic.setter
    def mnemonic(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mnemonic", value)

    @property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[str]]:
        """
        The network to deploy on.
        """
        return pulumi.get(self, "network")

    @network.setter
    def network(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network", value)

    @property
    @pulumi.getter
    def relay_url(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The relay urls, example: wss://relay.dev.grid.tf
        """
        return pulumi.get(self, "relay_url")

    @relay_url.setter
    def relay_url(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "relay_url", value)

    @property
    @pulumi.getter
    def rmb_timeout(self) -> Optional[pulumi.Input[str]]:
        """
        The timeout duration in seconds for rmb calls
        """
        return pulumi.get(self, "rmb_timeout")

    @rmb_timeout.setter
    def rmb_timeout(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "rmb_timeout", value)

    @property
    @pulumi.getter
    def substrate_url(self) -> Optional[pulumi.Input[str]]:
        """
        The substrate url, example: wss://tfchain.dev.grid.tf/ws
        """
        return pulumi.get(self, "substrate_url")

    @substrate_url.setter
    def substrate_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "substrate_url", value)


class Provider(pulumi.ProviderResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 key_type: Optional[pulumi.Input[str]] = None,
                 mnemonic: Optional[pulumi.Input[str]] = None,
                 network: Optional[pulumi.Input[str]] = None,
                 relay_url: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 rmb_timeout: Optional[pulumi.Input[str]] = None,
                 substrate_url: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a Threefold resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] key_type: The key type registered on substrate (ed25519 or sr25519).
        :param pulumi.Input[str] mnemonic: The mnemonic of the user. It is very secret.
        :param pulumi.Input[str] network: The network to deploy on.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] relay_url: The relay urls, example: wss://relay.dev.grid.tf
        :param pulumi.Input[str] rmb_timeout: The timeout duration in seconds for rmb calls
        :param pulumi.Input[str] substrate_url: The substrate url, example: wss://tfchain.dev.grid.tf/ws
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ProviderArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Threefold resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param ProviderArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProviderArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 key_type: Optional[pulumi.Input[str]] = None,
                 mnemonic: Optional[pulumi.Input[str]] = None,
                 network: Optional[pulumi.Input[str]] = None,
                 relay_url: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 rmb_timeout: Optional[pulumi.Input[str]] = None,
                 substrate_url: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ProviderArgs.__new__(ProviderArgs)

            if key_type is None:
                key_type = (_utilities.get_env('') or 'sr25519')
            __props__.__dict__["key_type"] = key_type
            if mnemonic is None:
                mnemonic = (_utilities.get_env('') or '')
            __props__.__dict__["mnemonic"] = None if mnemonic is None else pulumi.Output.secret(mnemonic)
            if network is None:
                network = (_utilities.get_env('') or '')
            __props__.__dict__["network"] = network
            __props__.__dict__["relay_url"] = pulumi.Output.from_input(relay_url).apply(pulumi.runtime.to_json) if relay_url is not None else None
            __props__.__dict__["rmb_timeout"] = rmb_timeout
            __props__.__dict__["substrate_url"] = substrate_url
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["mnemonic"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(Provider, __self__).__init__(
            'threefold',
            resource_name,
            __props__,
            opts)

    @property
    @pulumi.getter
    def key_type(self) -> pulumi.Output[Optional[str]]:
        """
        The key type registered on substrate (ed25519 or sr25519).
        """
        return pulumi.get(self, "key_type")

    @property
    @pulumi.getter
    def mnemonic(self) -> pulumi.Output[Optional[str]]:
        """
        The mnemonic of the user. It is very secret.
        """
        return pulumi.get(self, "mnemonic")

    @property
    @pulumi.getter
    def network(self) -> pulumi.Output[Optional[str]]:
        """
        The network to deploy on.
        """
        return pulumi.get(self, "network")

    @property
    @pulumi.getter
    def rmb_timeout(self) -> pulumi.Output[Optional[str]]:
        """
        The timeout duration in seconds for rmb calls
        """
        return pulumi.get(self, "rmb_timeout")

    @property
    @pulumi.getter
    def substrate_url(self) -> pulumi.Output[Optional[str]]:
        """
        The substrate url, example: wss://tfchain.dev.grid.tf/ws
        """
        return pulumi.get(self, "substrate_url")

