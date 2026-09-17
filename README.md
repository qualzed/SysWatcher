<center>

# SysWatcher
![python](https://img.shields.io/badge/python-3.14.7-brightgreen?style=for-the-badge)
![nuitka](https://img.shields.io/badge/BUILD-Nuitka_4.2.1-brightgreen?style=for-the-badge)
<hr>
<b>
A program that shows you CPU and RAM usage with dearpygui.
I use dearpygui instead of imgui because I couldn't install imgui correctly and I had some troubles with it.</b>

## Demonstration
In SysWatcher you also see the usage plot, lower you can see text information.

![img1](https://i.imgur.com/mL4DVDH.png)

## Build
```python -m nuitka --mode=onefile main.py```

## Requirements
Python 3.14.7 (You can use another one version, if it works)  
nuitka 4.2.1  
colorama 0.4.6  
dearpygui 2.3.1  
psutil 7.2.2