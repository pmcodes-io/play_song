# YouTube Song Searcher

A lightweight, straightforward Python script that takes a song name from your terminal and instantly opens up the YouTube search results page for it in your default web browser.

## How It Works

It uses Python's built-in libraries to handle things smoothly:
* `urllib.parse` safely encodes whatever song title you type so the URL doesn't break on spaces or special characters.
* `webbrowser` launches your system's default browser directly to the generated YouTube search link.

## Requirements

You don't need to install any external packages or dependencies. This runs entirely on Python's standard library.

## Usage

1. Clone or download the repository.
2. Run the script from your terminal or command line:
   ```bash
   python play_song.py
