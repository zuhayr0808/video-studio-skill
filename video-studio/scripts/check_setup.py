import shutil
import subprocess
import sys

tools = {
    "ffmpeg": "ffmpeg",
    "ffprobe": "ffprobe",
    "node": "node",
    "npm": "npm",
}

missing = []
for name, command in tools.items():
    path = shutil.which(command)
    if path:
        print(f"OK       {name}: {path}")
    else:
        print(f"MISSING  {name}")
        missing.append(name)

for module in ["faster_whisper", "numpy", "PIL"]:
    try:
        __import__(module)
        print(f"OK       python package {module}")
    except ImportError:
        print(f"MISSING  python package {module}")
        missing.append(module)

if shutil.which("earshot"):  # then run: earshot doctor
    print("OK       earshot")
else:
    print("MISSING  earshot (optional but recommended)")

if missing:
    print("\nSomething required is missing. Read SETUP.md and install it.")
    sys.exit(1)

print("\nAll required tools found.")
