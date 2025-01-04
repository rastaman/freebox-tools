# -*- coding: utf-8 -*-
import typer
from typing import Any, Optional
import json
from freebox_tools.api.freebox_api import wrapCall, AsyncTyper
import yaml
from yaml import Loader

async def wrapVmCall(method: str, arg0: Optional[Any] = None, arg1: Optional[Any] = None, arg2: Optional[Any] = None):
    return await wrapCall("vm", method, arg0, arg1, arg2)

app = AsyncTyper(help="Manage VMs")

@app.async_command(help="List VMs")
async def list_vms() -> list[Any]:
    result: Any = await wrapVmCall("get_config_all")
    print(json.dumps(result, indent=2))
    return result

@app.async_command(help="Get a VM")
async def get(
    vm_id: str = typer.Option(help="The VM id"),
    ) -> Any:
    result: Any = await wrapVmCall("get_config_vm", vm_id)
    print(json.dumps(result, indent=2))
    return result

@app.async_command(help="Start a VM")
async def start(
    vm_id: str = typer.Option(help="The VM id"),
    ) -> Any:
    result: Any = await wrapVmCall("start", vm_id)
    print(json.dumps(result, indent=2))
    return result

@app.async_command(help="Stop a VM")
async def stop(
    vm_id: str = typer.Option(help="The VM id"),
    ) -> Any:
    result: Any = await wrapVmCall("stop", vm_id)
    print(json.dumps(result, indent=2))
    return result

@app.async_command(help="Delete a VM")
async def delete(
    vm_id: str = typer.Option(help="The VM id"),
    ) -> Any:
    result: Any = await wrapVmCall("delete", vm_id)
    print(json.dumps(result, indent=2))
    return result

@app.async_command(help="Restart a VM")
async def restart(
    vm_id: str = typer.Option(help="The VM id"),
    ) -> Any:
    result: Any = await wrapVmCall("restart", vm_id)
    print(json.dumps(result, indent=2))
    return result

@app.async_command(help="Get VMs system info")
async def system_info() -> Any:
    result: Any = await wrapVmCall("get_system_info")
    print(json.dumps(result, indent=2))
    return result

@app.async_command(help="Get info on a VM disk")
async def disk_info(
    disk_path: str = typer.Argument(help="The VM disk path"),
    ) -> Any:
    result: Any = await wrapVmCall("disk_info", disk_path)
    print(json.dumps(result, indent=2))
    return result

@app.async_command(help="Create a VM disk")
async def disk_create(
    disk_path: str = typer.Option(help="The VM disk path"),
    size: str = typer.Option(help="The VM disk size in bytes"),
    disk_type: str = typer.Option(help="The VM disk type (raw or qcow2)", default="raw"),
    ) -> Any:
    result: Any = await wrapVmCall("disk_create", disk_path, size, disk_type)
    print(json.dumps(result, indent=2))
    return result

@app.async_command(help="Delete a VM disk task")
async def delete_task(
    task_id: str = typer.Argument(help="The VM disk task"),
    ) -> Any:
    result: Any = await wrapVmCall("delete_task", task_id)
    print(json.dumps(result, indent=2))
    return result

@app.async_command(help="Get a VM disk task")
async def get_task(
    task_id: str = typer.Argument(help="The VM disk task"),
    ) -> Any:
    result: Any = await wrapVmCall("get_task", task_id)
    print(json.dumps(result, indent=2))
    return result

@app.async_command(help="Get VMs system info")
async def disk_list() -> Any:
    result: Any = await wrapVmCall("disk_list")
    print(json.dumps(result, indent=2))
    return result

@app.async_command(help="Create a VM")
async def create(
    vm_file: str = typer.Option(help="The VM file definition"),
    ) -> Any:
    with open(vm_file, 'r') as stream:
        datas = yaml.load(stream, Loader=Loader)
        result: Any = await wrapVmCall("create", datas)
        print(json.dumps(result, indent=2))
        return result

@app.async_command(help="Update a VM")
async def update(
    vm_id: str = typer.Option(help="The VM id"),
    vm_file: str = typer.Option(help="The VM file definition"),
    ) -> Any:
    with open(vm_file, 'r') as stream:
        datas = yaml.load(stream, Loader=Loader)
        result: Any = await wrapVmCall("set_config", vm_id, datas)
        print(json.dumps(result, indent=2))
        return result
