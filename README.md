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

To run unit tests:

```bash
python -m unittest discover src
```

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
