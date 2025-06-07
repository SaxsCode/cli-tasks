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

### Steps

1. **Clone the repository:**

```bash
git clone https://github.com/saxscode/cli-tasks.git
cd cli-tasks
```

2. **Install dependencies:**

```bash
pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

3. **Set up Google OAuth credentials:**
- Download your `credentials.json` from the Google Cloud Console and place it in your project directory.
- Run the tool once to authenticate and generate a `token.json` file.

4. **Install the tool (optional):**

- **For global use (recommended):**  
  ```bash
  pipx install ./dist/cli_tasks-0.1-py3-none-any.whl
  ```
  *(First, build the wheel: `python -m build`)*

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
