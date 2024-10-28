# ZeroDayZooKeepers_Starterkit

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [Configuration](#configuration)
   - [Editing the Configurations](#editing-the-configuration)
   - [Configuration Parameters](#configuration-parameters)
6. [Usage](#usage)
   - [Running the Program with `run.py`](#running-the-program-with-runpy))
   - [Help Command](#help-command)
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

!Disclamer: Most of the setable options are only sent in during runtime if optional choices are not sent in via argparse. 

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

### Configuration Parameters

1. **default_output_file**: 
   - **Type**: String
   - **Description**: The default name of the output file where results from scans and operations will be saved. Change this to specify a different file name if desired.

2. **default_nmap_flags**: 
   - **Type**: String or null
   - **Description**: Default flags for Nmap scans. If you wish to customize the scan behavior (e.g., using specific scan techniques), specify the appropriate Nmap flags here.

3. **default_cipher_key_file**: 
   - **Type**: String
   - **Description**: The name of the file where the cipher key will be stored. This is used for encrypting and decrypting sensitive information.

4. **enumeration_thread_option**: 
   - **Type**: Integer
   - **Description**: Number of threads to use for concurrent subdomain enumeration. Increasing this number can speed up the enumeration process but may also increase the load on the network.

5. **enumeration_port_option**: 
   - **Type**: String or null
   - **Description**: Optional parameter to specify ports for enumeration. If set to null, default ports will be used.

6. **enumeration_silent_option**: 
   - **Type**: Boolean
   - **Description**: When set to `true`, suppresses output during enumeration. Use this option for cleaner logs when running in automated environments.

7. **enumeration_verbose_option**: 
   - **Type**: Boolean
   - **Description**: When set to `true`, provides verbose output during enumeration, which can be helpful for debugging and monitoring the enumeration process.

8. **enumeration_bruteforce_option**: 
   - **Type**: Boolean
   - **Description**: Enables or disables brute force enumeration of subdomains. This can be useful for discovering hidden or unlinked subdomains.

9. **enumeration_engine_option**: 
   - **Type**: Array or null
   - **Description**: Specifies which search engines to use for subdomain enumeration. If set to null, the default engines will be used.

10. **ssh_default_script**: 
    - **Type**: String
    - **Description**: Default path to the SSH script file that will be executed when establishing an SSH connection. Users can change this path to point to their own scripts.

11. **ssh_default_local_path**: 
    - **Type**: String or null
    - **Description**: The default local path where files will be saved when downloaded via SSH. Set to null if you want to specify the path at runtime.

12. **ssh_default_remote_path**: 
    - **Type**: String or null
    - **Description**: The default remote path from which files will be downloaded via SSH. Set to null if you want to specify the path at runtime.
   
## Usage

### Running the Program with `run.py`

The `run.py` file serves as the main entry point for executing the various functionalities of the ZeroDayZooKeepers_Starterkit. It orchestrates the execution of other scripts in the program, allowing users to perform tasks such as subdomain enumeration, port scanning, SSH file transfers, and more—all from the terminal.

### Help Command

Run the following commands for in teminal listing of options available.

```bash
python run.py -h
```

Following is a example when accessing help towrads one of the available scripts to run. The following command can be run specified for each script using the scripts given argparse Script name.

```bash
python run.py scanner -h
```

### How `run.py` Works

1. **Initialization**:
   - When you run `run.py`, it initializes the necessary configurations by loading the `config.json` file. This file contains default settings for various operations, which can be modified according to user preferences.

2. **Command-Line Interface**:
   - The script uses Python's built-in `argparse` module to create a command-line interface. This allows users to specify actions, parameters, and options when running the script from the terminal.

3. **Action Selection**:
   - Users can choose from various actions, such as:
     - **Enumeration**: Initiating subdomain enumeration using the Sublist3r tool.
     - **Scanning**: Performing port scans using Nmap.
     - **SSH Operations**: Uploading or downloading files, or executing scripts on remote servers via SSH.

4. **Example of Running the Program**:
   - To start the program, you would typically run the following command in the terminal:
     ```bash
     python run.py --action enumeration --domain example.com --threads 20 --output result.txt
     ```
   - In this example:
     - `--action` specifies the action to perform (in this case, enumeration).
     - `--domain` specifies the target domain for enumeration.
     - `--threads` sets the number of concurrent threads to use during the operation.
     - `--output` determines the name of the output file where results will be saved.

5. **Modular Implementation**:
   - The `run.py` script imports and utilizes various classes from the program:
     - **`enumeration`**: Handles the logic for subdomain enumeration and manages the integration of Sublist3r.
     - **`scanner`**: Manages the port scanning functionalities using Nmap.
     - **`ssh`**: Responsible for establishing SSH connections, transferring files, and executing scripts remotely.
     - **`cipher`**: Insaniating the options for encrypting and decrypting aswell as generating the key.

6. **Error Handling**:
   - The script incorporates robust error handling to manage exceptions that may arise during execution, such as invalid input parameters, connection issues, or file access errors. This ensures that the user is informed of any issues and can take corrective action.

7. **Exit Strategy**:
   - If any critical error occurs or if the user opts to terminate the program (by entering "exit" when prompted), the script will gracefully exit and log the necessary information.

### Summary

The `run.py` file is a crucial component of the ZeroDayZooKeepers_Starterkit, streamlining the process of executing complex operations through a user-friendly command-line interface. By leveraging the functionalities of the various scripts within the program, it allows users to efficiently conduct security assessments, file transfers, and more—all from a single point of execution.





