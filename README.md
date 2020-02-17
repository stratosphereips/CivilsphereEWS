# CivilsphereEWS
The Early Warning System (EWS) is a tool developed by Civilsphere designed to rapidly communicate security issues, problems, service status and other important information to our users through Twitter and Telegram.

## Requirements

The following two packages are needed to communicate with Twiter and Telegram:

- Twython: a Python wrapper for the Twitter API (https://pypi.org/project/twython/)
- python-telegram-bot: a Python wrapper for the Telegram Bot API (https://pypi.org/project/python-telegram-bot/)

## Usage

The Civilsphere EWS receives one parameter, the text to share:

```
Civilsphere Early Warning System: a tool to share information on Telegram and Twitter. 
Version 0.0.2 - https://www.civilsphereproject.org

Usage:
	civilsphereEWS.py "This is the text to post to Twitter and Telegram"
```
