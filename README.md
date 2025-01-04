# Freebox tools

This is a **work in progress** python client tool for the Freebox API. Tests are done on a Freebox Delta. It rely on a PR sent from my fork of `freebox-api`, which extends another older fork that i don't recall yet.

## Setup

```sh
poetry install
poetry run freebox-tools vm list-vms
```

Authenticate to your freebox when asked.

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
