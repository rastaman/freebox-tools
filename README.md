# Freebox tools

This is a **work in progress** python client tool for the Freebox API. Tests are done on a Freebox Delta. It rely on a PR sent from my fork of `freebox-api`, which extends another older fork that i don't recall yet, this means that at this time the project file reference the following dependency:

```txt
freebox-api = { git = "ssh://git@github.com/rastaman/freebox-api.git", branch = "Add_back_VMs_and_other_modules" }
```

## Setup

```sh
poetry install
poetry run freebox-tools vm list-vms
```

Authenticate to your freebox when asked.

## Usage

```sh
❯ poetry run freebox-tools --help
                                                                                                                                     
 Usage: freebox-tools [OPTIONS] COMMAND [ARGS]...                                                                                    
                                                                                                                                     
╭─ Options ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ *  --token-file                TEXT  The token file to use [env var: FREEBOX_TOKEN] [default: None] [required]                    │
│    --api-version               TEXT  The API version [env var: FREEBOX_API] [default: v8]                                         │
│    --freebox-host              TEXT  The Freebox host [env var: FREEBOX_HOST] [default: mafreebox.freebox.fr]                     │
│    --freebox-port              TEXT  The Feeebox port [env var: FREEBOX_PORT] [default: 443]                                      │
│    --install-completion              Install completion for the current shell.                                                    │
│    --show-completion                 Show completion for the current shell, to copy it or customize the installation.             │
│    --help                            Show this message and exit.                                                                  │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ contact   Manage Contacts                                                                                                         │
│ dhcp      Manage DHCP                                                                                                             │
│ fw        Manage ports forwarding                                                                                                 │
│ profile   Manage Profiles                                                                                                         │
│ storage   Manage Storage                                                                                                          │
│ vm        Manage VMs                                                                                                              │
│ vpn       Manage VPNs                                                                                                             │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

## VMs

```sh
❯ poetry run freebox-tools vm get 4
{
  "mac": "9a:3e:52:1b:db:6e",
  "cloudinit_userdata": "#cloud-config\nssh_authorized_keys:\n  - ssh-rsa ...\nsystem_info:\n  default_user:\n    name: myuser\npackages_update: true\npackages:\n  - cifs-utils\n  - kitty-terminfo\n  - mlocate\nmounts:\n  - [ '//mafreebox.freebox.fr/vms-datas-1', '/mnt/vms-datas-1', cifs, 'guest,uid=1000,gid=1000', '0', '0' ]\n  - [ '//mafreebox.freebox.fr/vms-datas-2', '/mnt/vms-datas-2', cifs, 'guest,uid=1000,gid=1000', '0', '0' ]\nruncmd:\n  - mount -a\n",
  "cd_path": "..",
  "id": 4,
  "os": "unknown",
  "enable_cloudinit": true,
  "disk_path": "...",
  "vcpus": 2,
  "memory": 5120,
  "name": "nixos-test",
  "cloudinit_hostname": "nixos-test",
  "status": "stopped",
  "bind_usb_ports": "",
  "enable_screen": false,
  "disk_type": "raw"
}
```
