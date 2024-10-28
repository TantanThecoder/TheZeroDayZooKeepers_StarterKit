# ZeroDayZooKeepers_Starterkit

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [Configuration](#configuration)
   - [Configuration File](#configuration-file)
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

