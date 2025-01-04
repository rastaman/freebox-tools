# -*- coding: utf-8 -*-
import typer
from typing import Any, Optional
import json
from freebox_tools.api.freebox_api import wrapCall, AsyncTyper
import yaml
from yaml import Loader

async def wrapProfileCall(method: str, arg0: Optional[Any] = None, arg1: Optional[Any] = None, arg2: Optional[Any] = None):
    return await wrapCall("profile", method, arg0, arg1, arg2)

app = AsyncTyper(help="Manage Profiles")

@app.async_command(help="List Profiles")
async def list_profiles() -> list[Any]:
    result: Any = await wrapProfileCall("get_profiles")
    print(json.dumps(result, indent=2))
    return result

# @app.async_command(help="Get a VPN")
# async def get_client(
#     vpn_id: str = typer.Option(help="The VPN id"),
#     ) -> Any:
#     result: Any = await wrapVpnCall("get_client_config", vpn_id)
#     print(json.dumps(result, indent=2))
#     return result
