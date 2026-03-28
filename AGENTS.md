# Repository Guidelines

## Project Structure & Module Organization
This repository is intentionally small. [`main.py`](/Users/reza/projects/face-tracker/main.py) is the application entrypoint and currently contains the webcam loop, OpenCV face detection, and on-screen rendering. Project metadata and dependencies live in [`pyproject.toml`](/Users/reza/projects/face-tracker/pyproject.toml), with locked versions in [`uv.lock`](/Users/reza/projects/face-tracker/uv.lock). High-level setup notes belong in [`README.md`](/Users/reza/projects/face-tracker/README.md).

When adding features, prefer extracting reusable logic into new modules rather than growing `main.py` further. Keep camera, detection, and UI concerns separated.

## Build, Test, and Development Commands
- `uv sync`: install the pinned dependencies into the local environment.
- `uv run main.py`: start the face tracker with the project-managed Python environment.
- `uv run python -m py_compile main.py`: quick syntax check before committing.

This project targets Python 3.13+, so use `uv` rather than a system interpreter when possible.

## Coding Style & Naming Conventions
Follow standard Python style: 4-space indentation, `snake_case` for functions and variables, and `UPPER_CASE` for module-level constants like `CASCADE_PATH`. Keep functions focused and side effects explicit. Prefer small helpers over dense inline blocks when logic becomes multi-step.

No formatter or linter is configured yet. Write code that is already PEP 8-friendly and keep comments brief and functional.

## Testing Guidelines
There is no automated test suite yet. For now, validate changes with:
- `uv run python -m py_compile main.py`
- `uv run main.py`

Manual testing should confirm camera startup, face box rendering, and clean exit via `q` or `Esc`. If you add tests, place them under `tests/` and name files `test_*.py`.

## Commit & Pull Request Guidelines
Git history currently uses short, imperative commit messages, for example: `Initial commit`. Continue with concise subjects such as `Add configurable camera index`.

Pull requests should include a clear summary, note any dependency changes, and describe how the change was verified. For UI-visible behavior, include screenshots or a short screen recording when practical.

## Configuration Notes
The app expects an available webcam and OpenCV-compatible runtime. Avoid hardcoding machine-specific paths or camera assumptions; keep new configuration values centralized and documented in `README.md`.
