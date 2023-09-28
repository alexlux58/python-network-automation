# Python Network Automation

## Overview

This repository contains Python scripts that automate various network tasks using the Paramiko library. The scripts are designed to work with both Cisco and Linux devices.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
  - [Single Device Backup](#single-device-backup)
  - [Multiple Devices Backup](#multiple-devices-backup)
  - [OSPF Configuration](#ospf-configuration)
- [Contributing](#contributing)
- [License](#license)

## Installation

To get started, clone this repository and install the required Python packages.

```bash
git clone https://github.com/alexlux58/python-network-automation.git
cd python-network-automation
pip install -r requirements.txt
```

## Usage

### Single Device Backup

Use the script [myparamiko_backup_single_device.py](https://github.com/alexlux58/python-network-automation/blob/main/Paramiko/myparamiko_backup_single_device.py) to backup the configuration of a single device.

```bash
python Paramiko/myparamiko_backup_single_device.py
```

### Multiple Devices Backup

For backing up multiple devices, you can use [myparamiko_backup_multiple_devices.py](https://github.com/alexlux58/python-network-automation/blob/main/Paramiko/myparamiko_backup_multiple_devices.py).

```bash
python Paramiko/myparamiko_backup_multiple_devices.py
```

### OSPF Configuration

To configure OSPF on multiple routers, use [paramiko_multiple_routers_ospf.py](https://github.com/alexlux58/python-network-automation/blob/main/Paramiko/paramiko_multiple_routers_ospf.py).

```bash
python Paramiko/paramiko_multiple_routers_ospf.py
```

## Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
