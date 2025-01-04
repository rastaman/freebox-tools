# -*- coding: utf-8 -*-
import typer
from typing import Any, Optional
import json
from freebox_tools.api.freebox_api import wrapCall, AsyncTyper
import yaml
from yaml import Loader

async def wrapFwCall(method: str, arg0: Optional[Any] = None, arg1: Optional[Any] = None, arg2: Optional[Any] = None):
    return await wrapCall("fw", method, arg0, arg1, arg2)

app = AsyncTyper(help="Manage ports forwarding")

@app.async_command(help="List port forwarding configurations")
async def list_fw() -> list[Any]:
    result: Any = await wrapFwCall("get_all_port_forwarding_configuration")
    print(json.dumps(result, indent=2))
    return result

@app.async_command(help="Delete a FW")
async def delete_fw(
    fw_id: str = typer.Option(help="The FW id"),
    ) -> Any:
    result: Any = await wrapFwCall("delete_port_forwarding_configuration", fw_id)
    print(json.dumps(result, indent=2))
    return result

@app.async_command(help="Get a FW")
async def get_fw(
    fw_id: str = typer.Option(help="The FW id"),
    ) -> Any:
    result: Any = await wrapFwCall("get_port_forwarding_configuration", fw_id)
    print(json.dumps(result, indent=2))
    return result

@app.async_command(help="Add/create port forwarding configurations")
async def create(
    fw_file: str = typer.Option(help="The FW file definition"),    
) -> Any:
    with open(fw_file, 'r') as stream:
        datas = yaml.load(stream, Loader=Loader)
        result: Any = await wrapFwCall("create_port_forwarding_configuration", datas)
        print(json.dumps(result, indent=2))
        return result

@app.async_command(help="Update port forwarding configurations")
async def update(
    fw_id: int = typer.Option(help="The port forwarding configuration (FW) identifier"),
    fw_file: str = typer.Option(help="The FW file definition"),    
) -> Any:
    with open(fw_file, 'r') as stream:
        datas = yaml.load(stream, Loader=Loader)
        result: Any = await wrapFwCall("edit_port_forwarding_configuration", fw_id, datas)
        print(json.dumps(result, indent=2))
        return result

@app.async_command(help="List incoming port forwarding configurations")
async def list_ifw() -> list[Any]:
    result: Any = await wrapFwCall("get_all_incoming_port_configuration")
    print(json.dumps(result, indent=2))
    return result

@app.async_command(help="Get a IFW")
async def get_ifw(
    ifw_id: str = typer.Option(help="The IFW id"),
    ) -> Any:
    result: Any = await wrapFwCall("get_incoming_port_configuration", ifw_id)
    print(json.dumps(result, indent=2))
    return result

@app.async_command(help="Update incoming port configurations")
async def update_ifw(
    ifw_id: int = typer.Option(help="The incoming port configuration (IFW) identifier"),
    ifw_file: str = typer.Option(help="The IFW file definition"),    
) -> Any:
    with open(ifw_file, 'r') as stream:
        datas = yaml.load(stream, Loader=Loader)
        result: Any = await wrapFwCall("edit_incoming_port_configuration", ifw_id, datas)
        print(json.dumps(result, indent=2))
        return result

@app.async_command(help="Get the DMZ configurarution")
async def get_dmz() -> Any:
    result: Any = await wrapFwCall("get_dmz_configuration")
    print(json.dumps(result, indent=2))
    return result

@app.async_command(help="Update DMZ configuration")
async def update_dmz(
    dmz_file: str = typer.Option(help="The DMZ file definition"),    
) -> Any:
    with open(dmz_file, 'r') as stream:
        datas = yaml.load(stream, Loader=Loader)
        result: Any = await wrapFwCall("set_dmz_configuration", datas)
        print(json.dumps(result, indent=2))
        return result
    