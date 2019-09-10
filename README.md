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

This is basically the initial release.
I'm not perfectly satisfied with the colors yet, but it's a start.
Also, I'm definitely open for suggestions.
If you think that a certain color combination looks awful or that something could be slightly improved, let me know.
