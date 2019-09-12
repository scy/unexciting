# An Unexciting Color Scheme

This project defines the **Unexciting** 16-color scheme.
It has three goals:

1. **Represent the usual ANSI colors.**
   There are some people who get really creative with color schemes that basically contain only three colors in different variations.
   This can look beautiful, but once you have a diff where the added lines are yellow and the removed lines are a slightly lighter yellow, it gets annoying.
2. **Be readable.**
   A lot of color schemes look really nice, but their “dark blue” color cannot be read on black.
   Or their grey (aka “dark white” aka default color) is unreadable once it has a background color (e.g. in a status bar or when highlighted).
3. **Be available on many terminals and platforms.**
   The **Unexciting** theme is defined in a Python script that generates configuration files for multiple terminals automatically.

## Supported Terminals

Currently, we generate configuration files for:

* Termux
* Windows Console (`cmd.exe`)
* xterm (`.Xresources` file)

Planned:

* Linux text console
* Visual Studio Code
* Windows Terminal

## Status

This project is abandoned and superseded by [_One Dark Pro_ Everywhere](https://github.com/scy/one-dark-pro-everywhere), because I was too lazy to create a VS Code theme on my own.
