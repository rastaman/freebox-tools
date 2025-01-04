from freebox_api import Freepybox
from functools import wraps
import asyncio
import typer
from collections.abc import Callable, Coroutine
from functools import wraps
from typing import Any, ParamSpec, TypeVar, Optional

freebox_config: dict[str,Any] = {}

async def get_api_from_config() -> Freepybox:
    api = Freepybox(
        token_file = freebox_config["token_file"],
        api_version = freebox_config["api_version"],
    )
    await api.open(host=freebox_config["freebox_host"], port=freebox_config["freebox_port"]) # type: ignore ## Because it return nothing and doesn't specify it
    return api

async def wrapCall(component: str, method: str, arg0: Optional[Any] = None, arg1: Optional[Any] = None, arg2: Optional[Any] = None):
    api = await get_api_from_config()
    comp = getattr(api, component)
    if arg2:
        result: Any = await getattr(comp, method)(arg0, arg1, arg2)
    elif arg1:
        result: Any = await getattr(comp, method)(arg0, arg1)
    elif arg0:
        result: Any = await getattr(comp, method)(arg0)
    else:
        result: Any = await getattr(comp, method)()
    await api.close()
    return result

P = ParamSpec("P")
R = TypeVar("R")

class AsyncTyper(typer.Typer):
    """Asyncronous Typer that derives from Typer.

    Use this when you have an asynchronous command you want to build, otherwise, just use Typer.
    """

    def async_command(  # type: ignore # Because we're being generic in this decorator, 'Any' is fine for the args.
        self,
        *args: Any,
        **kwargs: Any,
    ) -> Callable[
        [Callable[P, Coroutine[Any, Any, R]]],
        Callable[P, Coroutine[Any, Any, R]],
    ]:
        """An async decorator for Typer commands that are asynchronous."""

        def decorator(  # type: ignore # Because we're being generic in this decorator, 'Any' is fine for the args.
            async_func: Callable[P, Coroutine[Any, Any, R]],
        ) -> Callable[P, Coroutine[Any, Any, R]]:
            @wraps(async_func)
            def sync_func(*_args: P.args, **_kwargs: P.kwargs) -> R:
                return asyncio.run(async_func(*_args, **_kwargs))

            # Now use app.command as normal to register the synchronous function
            self.command(*args, **kwargs)(sync_func)

            # We return the async function unmodified, so its library functionality is preserved.
            return async_func

        return decorator
