# Face Tracker

This project is a small Python/OpenCV application that opens your webcam, detects faces, and draws tracking boxes in real time. Press `Space` to cycle detected faces through `normal`, `blur`, `negative`, and `grayscale` display modes.

## Requirements

- Python 3.13+
- [uv](https://github.com/astral-sh/uv) for dependency management and running the app
- A connected webcam

## Getting Started

### 1. Install `uv`

You can install `uv` using the following command:

```sh
curl -Ls https://astral.sh/uv/install.sh | sh
```

Or see the [uv installation guide](https://github.com/astral-sh/uv#installation) for more options.

### 2. Install dependencies

```sh
uv sync
```

### 3. Run the project

To start the face tracker, run:

```sh
uv run main.py
```

## Project Layout

- `main.py`: application entrypoint, webcam loop, face detection, and drawing
- `pyproject.toml`: project metadata and dependencies
- `uv.lock`: locked dependency versions

## Development Checks

Run a quick syntax check before committing:

```sh
uv run python -m py_compile main.py
```

Manual verification should confirm:

- the webcam opens successfully
- faces are outlined on screen in every mode
- pressing `Space` cycles face rendering through normal, blur, negative, and grayscale
- the app exits cleanly with `q` or `Esc`

## Notes

- Keep machine-specific paths and camera assumptions out of the code.
- If the project grows, prefer moving reusable logic out of `main.py` into dedicated modules.
- For more information about `uv`, visit the [uv GitHub page](https://github.com/astral-sh/uv).
