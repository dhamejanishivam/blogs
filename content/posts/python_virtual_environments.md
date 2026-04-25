+++
date = '2026-04-26'
draft = false
title = 'Python Virtual Environments'
+++

A virtual environment isolates Python dependencies for a specific project, preventing version conflicts across system-wide packages.

### Creating a Virtual Environment
Use the built-in `venv` module.

```bash
python3 -m venv venv
```

### Activating the Environment
**macOS/Linux:**
```bash
source venv/bin/activate
```

**Windows:**
```cmd
venv\Scripts\activate
```

### Managing Dependencies
Install packages using `pip` and freeze them into a `requirements.txt` file.

```bash
pip install numpy pandas
pip freeze > requirements.txt
```

To install dependencies from a file:
```bash
pip install -r requirements.txt
```

### Deactivating
Return to the global Python environment.
```bash
deactivate
```
