# Azure Monitoring CLI


## Dependencies

This CLI depends on the installation of the `az` CLI.


## Installation

```
   $ python3 setup.py --user
```

## Configuration

A default configuration file is installed to `$HOME/.azmon/resources.cfg`. Edit this file to describe your Azure resources.

Configuration headings (in `[square-brackets]`) are intended to represent environment names. These are user-defined.

Configuration keys are user-defined nicknames for long Azure resource IDs. Resource IDs may be found with the `az` CLI.


## Logging In

Before using the CLI, login to Azure from the command line using `az login`.


## Usage

```
   $ azmon -h
```
