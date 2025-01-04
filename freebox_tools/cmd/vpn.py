# -*- coding: utf-8 -*-
import typer
from typing import Any, Optional
import json
from freebox_tools.api.freebox_api import wrapCall, AsyncTyper
import yaml
from yaml import Loader

async def wrapVpnCall(method: str, arg0: Optional[Any] = None, arg1: Optional[Any] = None, arg2: Optional[Any] = None):
    return await wrapCall("vpn", method, arg0, arg1, arg2)

app = AsyncTyper(help="Manage VPNs")

@app.async_command(help="List VPNs")
async def list_servers() -> list[Any]:
    result: Any = await wrapVpnCall("get_server_list")
    print(json.dumps(result, indent=2))
    return result

@app.async_command(help="List clients VPNs")
async def list_clients() -> list[Any]:
    result: Any = await wrapVpnCall("get_client_list")
    print(json.dumps(result, indent=2))
    return result

@app.async_command(help="Get a VPN")
async def get_client(
    vpn_id: str = typer.Option(help="The VPN id"),
    ) -> Any:
    result: Any = await wrapVpnCall("get_client_config", vpn_id)
    print(json.dumps(result, indent=2))
    return result
