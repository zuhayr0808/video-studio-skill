# Setup

The skill reads this file when a tool is missing. Claude does the coding, but these programs have to be installed on your own computer, because a skill is only instructions and scripts.

## What to install

| Tool | What it does | Needed for |
| --- | --- | --- |
| FFmpeg (includes ffprobe) | Cuts, joins, resizes and exports video and audio | Everything |
| Python 3 | Runs the check scripts | Everything |
| Node.js (a current version; check remotion.dev/docs for the exact minimum) | Runs Remotion | Animations, captions, titles |
| Remotion | Makes video from code | Made-from-scratch videos, animated captions |
| Whisper (faster-whisper) | Turns speech into a transcript with timestamps | Editing real footage, captions |
| earshot | Lets Claude check what audio sounds like | Choosing and checking sounds |

## Install steps

Ask Claude to run these for you, or run them yourself. Pick your system.

**Mac (with Homebrew):** `brew install ffmpeg node python`

**Windows (with winget):** `winget install Gyan.FFmpeg`, then `winget install OpenJS.NodeJS`, then `winget install Python.Python.3.12`

**Linux (Ubuntu or Debian):** `sudo apt install ffmpeg nodejs npm python3 python3-pip`

**Python packages for all systems:** `pip install faster-whisper numpy Pillow`

**Remotion:** it installs inside each video project, so nothing extra now. Claude will run `npx create-video@latest` when it needs one.

**earshot:** follow the install steps in its README at github.com/Leonxlnx/earshot, since it installs as a Python project. It runs on CPU and is free. Afterwards run `earshot doctor`, which checks the install, models and data files. Its commands include `measure` (loudness, tempo, key), `describe` (what a sound is like), `timeline` (a second-by-second listening transcript), and `critique` (a scorecard for a finished video with timestamped fixes). Each call loads its models and takes roughly 20 to 40 seconds, so for many checks use its MCP server mode (`earshot mcp`).

## The check script

The skill runs `python3 scripts/check_setup.py` before any work. That file is added to the repo separately, in a folder called scripts.

## If something fails

- Run the check script again after installing, in a new terminal window, so the computer sees the new programs.
- If FFmpeg is installed but not found, the install folder is not on your system PATH. Ask Claude to fix it.
- Rendering with Remotion needs a Chrome browser. Remotion downloads one by itself the first time.
