<p align="center">
	<a href="https://discord.gg/3uRnMJTFnU"><img src="icon.ico" alt="Versatools" height="90" /></a>
</p>

<h4 align="center">VERSATOOLS - FREE MULTITOOL | BOT FOLLOWERS/GROUP JOINS & MORE</h4>
<p align="center">
	Best FREE opensource Roblox botting tools written in Python.
</p>

<p align="center">
	<a href="#installation">Installation</a> •
	<a href="#file-templates">File templates</a> •
  <a href="https://garry.lol/versatools">Website</a> •
	<a href="https://discord.gg/3uRnMJTFnU">Discord server</a>
</p>
<br/>

> <h4>Our Discord server was banned. Here's the new one: <a href="https://garry.lol/versatools/discord">https://discord.com/invite/JFeuwfz8gx</a></h4>

## Screenshot

![Screenshot](./screenshot.png)

## Installation

This installation is designed for advanced users. To install Versatools, you can either download the latest release or run the program from source (Must have git and python installed).

Download the latest Windows release from [here](https://github.com/GarryyBD/versatools/releases/tag/v3.0.0).

## Running from source

First clone this repository:

```bash
git clone
```

Then install the requirements:

```bash
pip install -r requirements.txt
```

Finally, run the program:

```bash
python src/main.py
```

To convert the program to an executable, run:

```bash
pyinstaller --onefile --add-data '.venv/Lib/site-packages/tls_client/dependencies/tls-client-64.dll;tls_client/dependencies' --icon=icon.ico --name=Versatools src/main.py
```

To run unit tests:

```bash
python -m unittest discover src
```

## Capbypass

Versatools uses Capbypass to solve captchas. You can add your Capbypass API key in the `config.json` file.

Register for a Capbypass API key [here](https://capbypass.com/).

## RAMPAGE

RAMPAGE is the premium version of Versatools. It has more features and is more stable. You can purchase RAMPAGE from [here](https://rampageteam.mysellix.io).

## File templates

### files/config.json

All attributes are mandatory. Removing them will break the program.

### files/cookies.txt

Add your cookies in this file. You can generate them using our Cookie Generator tool.
Versatools understands both UPC and C format for cookies.

### files/proxies.txt

You can use this template to add your proxies. We currently only support HTTP proxies.
Here are some examples of valid proxies lines:

```
8.8.8.8:5001
http:8.8.8.8:5001
8.8.8.8:5003:username:password
```

## Star History

<a href="https://star-history.com/#garryybd/versatools&Timeline">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=garryybd/versatools&type=Timeline&theme=dark" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=garryybd/versatools&type=Timeline" />
    <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=garryybd/versatools&type=Timeline" />
  </picture>
</a>
