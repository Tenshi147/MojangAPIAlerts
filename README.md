# MojangAPIAlerts

Alerts a Discord server upon detecting that Mojang has updated their API version

## Requirements

- Python3
  - requests library
- A linux VPS (Although this step is not technically required, it is recommended as you would want this program to run constantly)

## Installation

1. Replace webhook locations in `APIUpdateAlerts.py` with Discord webhooks of your choice
2. If you have a linux VPS, upload `APIUpdateAlerts.py` and [install screen](https://www.interserver.net/tips/kb/using-screen-to-attach-and-detach-console-sessions/)
3. Run `screen` and skip the information page
4. Run `python3 main.py`
5. Detach from the screen by pressing `Ctrl + A + D`

## Pictures

![Example webhook](https://github.com/Tenshi147/MojangAPIAlerts/blob/main/images/webhook.png?raw=true)
