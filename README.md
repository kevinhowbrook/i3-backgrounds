# Unsplash Backgrounds

## Description

This is a simple script that downloads a random image from [Unsplash](https://unsplash.com/) and sets it as the desktop background. The idea is to do this for i3 with a key binding so you can change your background with a keypress.

![](images/1.jpg)

## Requirements

- Unsplash API key

## Running

1. Clone the repository into ~/shared/i3-backgrounds
1. Copy local.config.py to config.py
1. Add your Unsplash API key to config.py
1. Run with `python main.py`

You can clone it to another location but you'll have to adjust a few paths
in main.py for the download image location.

## Setup to run with an i3 binding

Add this to your i3 config file, this would configure `mod+i` to run the script. Now `mod_i` will change your background. :)

```python
bindsym $mod+i exec --no-startup-id ~/shared/i3-backgrounds/main.py
```