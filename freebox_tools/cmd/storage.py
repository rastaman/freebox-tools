# -*- coding: utf-8 -*-
import typer
from typing import Any, Optional
import json
from freebox_tools.api.freebox_api import wrapCall, AsyncTyper
import yaml
from yaml import Loader

async def wrapStorageCall(method: str, arg0: Optional[Any] = None, arg1: Optional[Any] = None, arg2: Optional[Any] = None):
    return await wrapCall("storage", method, arg0, arg1, arg2)

app = AsyncTyper(help="Manage Storage")

@app.async_command(help="Get config")
async def config() -> list[Any]:
    result: Any = await wrapStorageCall("get_config")
    print(json.dumps(result, indent=2))
    return result

@app.async_command(help="Get partitions")
async def partitions() -> list[Any]:
    result: Any = await wrapStorageCall("get_partitions")
    print(json.dumps(result, indent=2))
    return result

@app.async_command(help="Get a partition")
async def partition(
    partition_id: str = typer.Argument(help="The partition id"),
    ) -> Any:
    result: Any = await wrapStorageCall("get_partition", partition_id)
    print(json.dumps(result, indent=2))
    return result

@app.async_command(help="Check a partition")
async def check(
    partition_id: str = typer.Argument(help="The partition id"),
    ) -> Any:
    result: Any = await wrapStorageCall("check_partition", partition_id)
    print(json.dumps(result, indent=2))
    return result

@app.async_command(help="Get disks")
async def disks() -> list[Any]:
    result: Any = await wrapStorageCall("get_disks")
    print(json.dumps(result, indent=2))
    return result

@app.async_command(help="Get a disk")
async def disk(
    disk_id: str = typer.Argument(help="The disk id"),
    ) -> Any:
    result: Any = await wrapStorageCall("get_disk", disk_id)
    print(json.dumps(result, indent=2))
    return result

# enabled
# freebox-tools storage eject 2000 --state "{\"state\": \"disabled\"}"
@app.async_command(help="Eject a disk")
async def eject(
    disk_id: str = typer.Argument(help="The disk id"),
    state: str = typer.Option(help="The disk desired state", default="{\"state\": \"disabled\"}"),
    ) -> Any:
    result: Any = await wrapStorageCall("eject_disk", disk_id, state)
    print(json.dumps(result, indent=2))
    return result
