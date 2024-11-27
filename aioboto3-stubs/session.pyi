"""
Type annotations for aioboto3.session module.

Copyright 2024 Vlad Emelianov
"""

from types import TracebackType
from typing import Any, Generic, TypeVar

from aioboto3.resources.base import AIOBoto3ServiceResource
from aioboto3.resources.factory import AIOBoto3ResourceFactory
from aiobotocore.client import AioBaseClient
from aiobotocore.config import AioConfig
from aiobotocore.credentials import AioCredentials
from botocore.hooks import BaseEventHooks
from botocore.loaders import Loader
from botocore.session import Session as BotocoreSession

class Session:
    def __init__(
        self,
        aws_access_key_id: str | None = ...,
        aws_secret_access_key: str | None = ...,
        aws_session_token: str | None = ...,
        region_name: str | None = ...,
        botocore_session: BotocoreSession | None = ...,
        profile_name: str | None = ...,
    ) -> None:
        self._session: BotocoreSession
        self.resource_factory: AIOBoto3ResourceFactory
        self._loader: Loader

    @property
    def profile_name(self) -> str: ...
    @property
    def region_name(self) -> str: ...
    @property
    def events(self) -> BaseEventHooks: ...
    @property
    def available_profiles(self) -> list[str]: ...
    def _setup_loader(self) -> None: ...
    def get_available_services(self) -> list[str]: ...
    def get_available_resources(self) -> list[str]: ...
    def get_available_partitions(self) -> list[str]: ...
    def get_available_regions(
        self,
        service_name: str,
        partition_name: str = ...,
        allow_non_regional: bool = ...,
    ) -> list[str]: ...
    def get_credentials(self) -> AioCredentials | None: ...
    def _register_default_handlers(self) -> None: ...
    def client(  # type: ignore [override]
        self,
        service_name: str,
        region_name: str | None = ...,
        api_version: str | None = ...,
        use_ssl: bool | None = ...,
        verify: str | bool | None = ...,
        endpoint_url: str | None = ...,
        aws_access_key_id: str | None = ...,
        aws_secret_access_key: str | None = ...,
        aws_session_token: str | None = ...,
        config: AioConfig | None = ...,
    ) -> AioBaseClient: ...
    def resource(
        self,
        service_name: str,
        region_name: str | None = ...,
        api_version: str | None = ...,
        use_ssl: bool | None = ...,
        verify: bool | str | None = ...,
        endpoint_url: str | None = ...,
        aws_access_key_id: str | None = ...,
        aws_secret_access_key: str | None = ...,
        aws_session_token: str | None = ...,
        config: AioConfig | None = ...,
    ) -> ResourceCreatorContext[AIOBoto3ServiceResource]: ...

_AIOBoto3ServiceResource = TypeVar("_AIOBoto3ServiceResource", bound=AIOBoto3ServiceResource)

class ResourceCreatorContext(Generic[_AIOBoto3ServiceResource]):
    def __init__(
        self,
        session: Session,
        service_name: str,
        region_name: str,
        api_version: str,
        use_ssl: bool,
        verify: bool,
        endpoint_url: str,
        aws_access_key_id: str,
        aws_secret_access_key: str,
        aws_session_token: str,
        config: AioConfig,
        resource_model: Any,
    ) -> None: ...
    async def __aenter__(self) -> _AIOBoto3ServiceResource: ...
    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> None: ...
