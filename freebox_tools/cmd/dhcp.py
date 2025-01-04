# -*- coding: utf-8 -*-
import typer
from typing import Any, Optional
import json
from freebox_tools.api.freebox_api import wrapCall, AsyncTyper
import yaml
from yaml import Loader

async def wrapDhcpCall(method: str, arg0: Optional[Any] = None, arg1: Optional[Any] = None, arg2: Optional[Any] = None):
    return await wrapCall("dhcp", method, arg0, arg1, arg2)

app = AsyncTyper(help="Manage DHCP")

@app.async_command(help="List DHCP dynamic leases")
async def dynamic_leases() -> list[Any]:
    result: Any = await wrapDhcpCall("get_dhcp_dynamic_leases")
    print(json.dumps(result, indent=2))
    return result

@app.async_command(help="List DHCP static leases")
async def static_leases() -> list[Any]:
    result: Any = await wrapDhcpCall("get_dhcp_static_leases")
    print(json.dumps(result, indent=2))
    return result
