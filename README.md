# pylectron
An electron.js GUI wrapper for arbitrary Python scripts

## Motivation
Python is unparalleled in certain domains and is the de facto lingua franca for many types of applications, but its GUI-building modules have always seemed suspect in their versatility/extensibility. Hence, the need for a better way to build GUIs that run Python on the backend.

## Implementation
Pylectron is a simple Electron wrapper on a series of Python scripts. It features automatic virtual environment management, in order to allow developers to focus solely on building what's important.

## Quickstart
To start, simply clone this repo and modify `main.py` and `index.html`. The former excecutes automatically on program open, but is also triggered when the button in `index.html` is clicked. The latter is naturally responsible for the overall look/layout of the GUI.