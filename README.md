# ZeroDayZooKeepers_Starterkit

## Introduction

The ZeroDayZooKeepers is a schoolproject aimed to be a toolbox for etichal hackers and others in the cybersecurity buisness. It aims to automate certain tasks made regulary all runnable with one and the same script. !Disclaimer: This is a school project and may or may not be finished!

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [Configuration](#configuration)
   - [Editing the Configurations](#editing-the-configuration)
   - [Configuration Parameters](#configuration-parameters)
6. [Usage](#usage)
   - [Running the Program with `run.py`](#running-the-program-with-runpy)
   - [Help Command](#help-command)
   - [How `run.py` Works](#how-runpy-works)
   - [Enumeration Commands](#enumeration-commands)
   - [Cryptography Commands](#cryptography-commands)
   - [Nmap Scanner Commands](#nmap-scanner-commands)
   - [SSH Commands](#ssh-commands)
7. [Logging](#logging)
   - [Purpose of logging](#purpose-of-logging)
   - [Logging levels](#logging-levels)
   - [Configuration of Logging](#configuration-of-logging)
8. [Contributing](#contributing)


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
    "scanner_path_default": true,

    "default_cipher_key_file": "generated_key.key",
    "cipher_path_default": true,
    "cipher_path_default_key": true,
    
    "logging_level": "INFO",

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

2. **scanner_path_default**
   - **Type**: Boolean
   - **Description**: While set to `true`, the program will assume all files to be written or read will be saved in the Program/Scanner/Scanner_files folder. Set to `false` if you wanna input the path from current working directory to the file location instead or save an output file in a specific folder.

3. **default_nmap_flags**: 
   - **Type**: String or null
   - **Description**: Default flags for Nmap scans. If you wish to customize the scan behavior (e.g., using specific scan techniques), specify the appropriate Nmap flags here.

4. **default_cipher_key_file**: 
   - **Type**: String
   - **Description**: The name of the file where the cipher key will be stored. This is used for encrypting and decrypting sensitive information.

5. **cipher_path_default**:
   - **Type**: Boolean
   - **Description**: While set to `true`, the program will assume all files used for encrypting or decrypting will be saved in the Program/Cipher/Cipher_files folder. Set to `false` if you wanna input the path from current working directory to the file location instead or if you want to save output files in a specific place.

6. **cipher_path_default_key**:
   - **Type**: Boolean
   - **Description**: While set to `true`, the program assumes all keys will exist in the Program/Cipher/Cipher_files folder. Set to `false` if you want to input the path from current working directory to the file location instead. Generated keys always get stored in default path Program/Cipher/Cipher_files.

7. **logging_level**
   - **Type**: String or null:
   - **Description**: Set the desired default logging level, choose between: `INFO`, `DEBUG`, `WARNING`, `ERROR`. Default logging level will be set to `INFO` if this option is set to null in the `config.json` file.

8. **enumeration_thread_option**: 
   - **Type**: Integer
   - **Description**: Number of threads to use for concurrent subdomain enumeration. Increasing this number can speed up the enumeration process but may also increase the load on the network.

9. **enumeration_port_option**: 
   - **Type**: String or null
   - **Description**: Optional parameter to specify ports for enumeration. If set to null, default ports will be used.

10. **enumeration_silent_option**:
   - **Type**: Boolean
   - **Description**: When set to `true`, suppresses output during enumeration. Use this option for cleaner logs when running in automated environments.

11. **enumeration_verbose_option**: 
   - **Type**: Boolean
   - **Description**: When set to `true`, provides verbose output during enumeration, which can be helpful for debugging and monitoring the enumeration process.

12. **enumeration_bruteforce_option**: 
   - **Type**: Boolean
   - **Description**: Enables or disables brute force enumeration of subdomains. This can be useful for discovering hidden or unlinked subdomains.

13. **enumeration_engine_option**: 
   - **Type**: Array or null
   - **Description**: Specifies which search engines to use for subdomain enumeration. If set to null, the default engines will be used.

14. **ssh_default_script**: 
    - **Type**: String
    - **Description**: Default path to the SSH script file that will be executed when establishing an SSH connection. Users can change this path to point to their own scripts.

15. **ssh_default_local_path**: 
    - **Type**: String or null
    - **Description**: The default local path where files will be saved when downloaded via SSH. Set to null if you want to specify the path at runtime.

16. **ssh_default_remote_path**: 
    - **Type**: String or null
    - **Description**: The default remote path from which files will be downloaded via SSH. Set to null if you want to specify the path at runtime.
   
## Usage

### Running the Program with `run.py`

The `run.py` file serves as the main entry point for executing the various functionalities of the ZeroDayZooKeepers_Starterkit. It orchestrates the execution of other scripts in the program, allowing users to perform tasks such as subdomain enumeration, port scanning, SSH file transfers, and more—all from the terminal.

Important to be located in the following project path: /ZeroZooKeepers_StarterKit/Program before running the run.py command!

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

### Enumeration Commands

The enumeration script is initiated by typing 'enumerate' after the ` python run.py ` command

#### Command Format enumerate

```bash
python run.py enumerate example.com [-o result.txt] [-t 20]
```
1. Required Arguments
   - Domain: 
     The target domain for subdomain enumeration.
     
2. Optional Arguments
   - '-o' '--output_file': 
     Name of the output file for results. Defaults to the value in the config file.

   - '-t' '--thread': 
     Number of threads for concurrent enumeration. Defaults to 20, default changeable in config.json
   

### Cryptography Commands

The Cryptography script is initiated by typing 'cipher' or 'keygen' after the ` python run.py ` command depending on which of the 2 you wanna run.
The cipher module assumes by default that the file to be decryted or encrypted aswell as key files lies in the folder with path: Program/Cipher/Cipher_files, this can be altered with configurations given in chapter 5: [Configuration](#configuration).
All files stored in Cipher_files are gitignored by default to make sure you dont push them by accident.

#### Command Format cipher

```bash
python run.py cipher encrypt file test.txt [-o secret_message.enc] [-k generated_key.key]
```
1. **Required Arguments**
   - Action:
     Specify whether to Encrypt or Decrypt data. either enter 'Encrypt' or 'Decrypt'
   - Data_type:
     Indicate the source of data, either 'File' (input from a file) or 'Terminal_input' (input directly from the terminal).
   - Input:
     The path to the input file or the text you want to encrypt/decrypt. If file, make it a .txt
2. **Optional Arguments**
   - '-o' '--output_file':
     Specify the name of the output file where the encrypted or decrypted data will be saved. Defaults to the value set in the configuration file if not provided.
   - '-k' '--key'
     Provide the path to the file containing the cryptographic key. If not specified, it defaults to generated.key as defined in the configuration file.

#### Command Format keygen

```bash
python run.py keygen [-k my_secret_key.key]
```
1. **Optional Arguments**
   - '-k' '--key_file'
     Name of the file you wish to store the key in, if not in use, default name will be given from option in config.json file.

### Nmap Scanner Commands

The nmap scanning script is initiated by typing 'scanner' after the ` python run.py ` command
The scanner module assumes by default that the files to be read or the output files gets saved and stored in the folder with path: Program/Scanner/Scanner_files, this can be altered with configurations given in chapter 5: [Configuration](#configuration).
All files stored in Scanner_files are gitignored by default to make sure you dont push them by accident.

#### Command Format scanner

```bash
python run.py scanner file <input> [-o result.txt] [-f "-sS -p 21"]
```
1. **Required Arguments**
   - Action:
     Specify the method of scanning, choose either 'file' or 'terminal_input'
   - Input:
     The file name containing host addresses (if file action) or the IP address/range (if terminal_input action).
2. **Optional Arguments**
   - '-o' '--output_file':
     Specify the name of the output file where the scan results will be saved. If not provided, a default name will be given as defined in the configuration file.
   - '-f' '--flags'
     Add optional Nmap flags for advanced scanning options (e.g., -sS for SYN scan). Default flags can be set in configuration file. Input as quoted string.

### SSH Commands

#### Command Format ssh

The ssh script is initiated by typing 'ssh' after the ` python run.py ` command

```bash
python run.py ssh script 127.0.0.1 debian test123 [-s my_script.txt] [-l <local_path>] [-r <remote_path>]
```
1. **Required Arguments**
   - Action:
     Choose between executing a 'script', 'upload' to upload a file or 'download' to download a file
   - Ip:
     The IP address of the SSH server you want to connect to.
   - Username:
     The username to log into the SSH server.
   - Password:
     Password for specified username.
2. **Otional Arguments**
   - '-s' '--script_file':
     The path or name of the file containing the script to be executed (required if action is 'script', default script can be set in config.json).
   - '-l' '--local_path':
     The path on the local machine where the file will be saved or retrieved from.(Requierd if action is 'upload' or 'download', a default local_path can be set in config.json).
   - '-r' '--remote_path':
     The path on the SSH server where the file will be uploaded or downloaded from.(Requierd if action is 'upload' or 'download', a default remote_path can be set in config.json).

### SSH Scripts
The program contains a folder where you can store your own scripts made specifically for the ssh portion for quick access. However make sure the scripts you make follow the rough guidelines given in the example script that is part of this project, located in the `SSH_Scripts`folder in the `SSH`folder.

## Logging

The application uses the `logging` module to provide comprehensive logging capabilities, which helps in monitoring and debugging. 

### Purpose of Logging

Logging is an essential feature that allows you to track the application's behavior during execution. It captures important events, errors, and status messages, making it easier to diagnose issues and understand the flow of the application.

### Logging Levels

The following logging levels are used throughout the application:

- **DEBUG**: Detailed information, typically of interest only when diagnosing problems. This level is used for low-level events.
- **INFO**: Confirmation that things are working as expected. This level indicates the general operational status of the application.
- **WARNING**: An indication that something unexpected happened, or indicative of some problem in the near future (e.g., ‘disk space low’). The application is still functioning as expected.
- **ERROR**: Due to a more serious problem, the software has not been able to perform a specific operation.
- **CRITICAL**: A very serious error, indicating that the program itself may be unable to continue running.

### Configuring logging

The default logging level can easily be set in the `config.json` file, see chapter 5: [Configuration](#configuration) for more on this.

## Contributing
- ** Guide yet to be implemented **



