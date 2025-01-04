# -*- coding: utf-8 -*-
import typer
from typing import Any, Optional
import json
from freebox_tools.api.freebox_api import wrapCall, AsyncTyper
import yaml
from yaml import Loader

async def wrapContactCall(method: str, arg0: Optional[Any] = None, arg1: Optional[Any] = None, arg2: Optional[Any] = None):
    return await wrapCall("contact", method, arg0, arg1, arg2)

app = AsyncTyper(help="Manage Contacts")

@app.async_command(help="List Contacts")
async def list_contacts() -> list[Any]:
    result: Any = await wrapContactCall("get_contact_list")
    print(json.dumps(result, indent=2))
    return result
