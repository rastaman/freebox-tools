import typer
from freebox_tools.cmd import vm, vpn, profile, contact, fw, dhcp, storage
from freebox_tools.api.freebox_api import freebox_config, AsyncTyper

def init_config(
    token_file: str = typer.Option(help="The token file to use", envvar="FREEBOX_TOKEN"),
    api_version: str = typer.Option(help="The API version", envvar="FREEBOX_API", default="v8"),
    freebox_host: str = typer.Option(help="The Freebox host", envvar="FREEBOX_HOST", default="mafreebox.freebox.fr"),
    freebox_port: str = typer.Option(help="The Feeebox port", envvar="FREEBOX_PORT", default=443)
    ):
    freebox_config["token_file"] = token_file
    freebox_config["api_version"] = api_version
    freebox_config["freebox_host"] = freebox_host
    freebox_config["freebox_port"] = freebox_port

app = AsyncTyper(callback=init_config)
app.add_typer(contact.app, name="contact")
app.add_typer(dhcp.app, name="dhcp")
app.add_typer(fw.app, name="fw")
app.add_typer(profile.app, name="profile")
app.add_typer(storage.app, name="storage")
app.add_typer(vm.app, name="vm")
app.add_typer(vpn.app, name="vpn")

if __name__ == '__main__':
    app()
