# ZeroDayZooKeepers_Starterkit

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [Configuration](#configuration)
   - [Editing Configurations](#configuration-file)
   - [Json_config Class](#json_config-class)
6. [Usage](#usage)
   - [Running Scripts](#running-scripts)
   - [Enumeration Example](#enumeration-example)
   - [Port Scanning Example](#port-scanning-example)
   - [SSH Upload/Download Example](#ssh-uploaddownload-example)
7. [Logging](#logging)
8. [Contributing](#contributing)
9. [License](#license)

## Introduction

The ZeroDayZooKeepers is a schoolproject aimed to be a toolbox for etichal hackers and others in the cybersecurity buisness. It aims to automate certain tasks made regulary all runnable with one and the same script. !Disclaimer: This is a school project and may or may not be finished!

## Features

- **Subdomain Enumeration**: Identify subdomains of a target domain using multiple search engines.
- **Port Scanning**: Make your desired scans with nmap!
- **SSH Management**: Upload, download files, and execute scripts on remote servers over SSH.
- **Cryptography**: A simple Cryptography tool that lets you both decrypt and encrypt using generated cipher keys.
- **Configurable**: Easily adjustable settings through a JSON configuration file.
- **Logging**: Comprehensive logging of operations and errors for troubleshooting.

## Requirements
- **Paramiko** for SSH connections and executing commands.
- **Nmap** for flexible networkscanning.
- **Sublist3r** for Subdomain enumeration
- **Fernet Cryptography** for cipher key generation, encrypting and decrypting.
- **Standard Python libraries:** json, logging, sys, pathlib

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-directory>
```
2. Install requiered libraries:
```bash
pip install -r requirements.txt
```
3. Ensure that the config.json file i correctly setup for your needs! More about this in next chapter.

## Configuration

The project uses a json configuration file for certain default values. This is to ensure the user never have to enter the soruce code to set a new default value.

The options are as seen below:

```json

{
    "default_output_file": "result.txt",

    "default_nmap_flags": null,

    "default_cipher_key_file": "generated_key.key",

    "enumeration_thread_option": 20,
    "enumeration_port_option": null,
    "enumeration_silent_option": false,
    "enumeration_verbose_option": false,
    "enumeration_bruteforce_option": false,
    "enumeration_engine_option": null,

    "ssh_default_script": "SSH/SSH_Scripts/Example_script.txt",
    "ssh_default_local_path": null,
    "ssh_default_remote_path": null
}
```
### Editing the configuration
1. **Open the config.json file in a text editor.**
2. **Modify the parameters as needed.**
3. **Save the file.**
4. **Run the application to apply the new configuration.**



