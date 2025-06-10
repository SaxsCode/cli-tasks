# CLI Task Management Tool

A simple command-line tool for managing tasks and notes using the Google Tasks API.

## Features

- **Add tasks** to your default task list
- **Add notes** to your notes list
- **List tasks** and notes from their respective lists

## Installation

### Requirements

- Python 3.8 or higher
- Google account (for Google Tasks API)
- [pipx](https://pypa.github.io/pipx/) (recommended for global CLI installation)

### Steps

1. **Clone the repository:**

```bash
git clone https://github.com/saxscode/cli-tasks.git
cd cli-tasks
```

2. **Install dependencies:**

```bash
pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib build
```

3. **Set up Google OAuth credentials:**
- Go to the [Google Cloud Console](https://console.cloud.google.com/).
- Create OAuth 2.0 credentials for a desktop app.
- Download the `credentials.json` file and place it in the root of the project directory
- The application will always look for `credentials.json` and `token.json` in the project root, regardless of where you run the command.

4. **Build the package:**
```bash
python -m build
```
This will generate a `.whl` file in the `dist/` directory.

5. **Install the tool globally (recommended):**
- Ensure [pipx](https://pypa.github.io/pipx/) is installed:
  ```bash
  python -m pip install --user pipx
  python -m pipx ensurepath
  ```
- Install the CLI tool:
  ```bash
  pipx install ./dist/cli_tasks-0.1-py3-none-any.whl
  ```

**Alternatively, install locally with pip:**
```bash
pip install ./dist/cli_tasks-0.1-py3-none-any.whl
```

## Usage
```bash
task --task "Buy milk" # Add a task to the default list
task --note "Call mom" # Add a note to the notes list
task --tasks # List all tasks in the default list
task --notes # List all notes in the notes list
````

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

MIT
