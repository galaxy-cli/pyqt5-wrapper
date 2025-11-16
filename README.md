# PyQt5 Minimal Web Browser

A minimal web browser application built with PyQt5 that includes a URL input bar and automatically installs PyQt5 if it's not already installed.

## Features

- Simple and clean GUI using PyQt5.
- URL bar to enter any website address dynamically.
- Automatically installs PyQt5 and required modules if missing.
- Loads a default website on startup (`http://www.google.com`).
- Updates URL bar to reflect the current page.
- Supports basic navigation by entering URLs manually.

## Requirements

- Python 3.x
- Internet connection for installing PyQt5 (if not installed).

## How to Run

1. Clone or download this repository.
2. Run the script with Python:

``python pyqt5-wrapper.py``
   
The script will check if PyQt5 packages are installed and, if not, automatically install them using pip before launching the browser.

## Code Overview

- `install_and_import(package)`: Checks for and installs missing packages.
- `PyQt5Wrapper`: Main window class with a QWebEngineView and URL input toolbar.
- URL bar allows entering and navigating to any web address.
- Automatically prepends `http://` if the scheme is missing.

## Notes

- Make sure Python and pip are properly configured on your system.
- The browser window is resizable and starts at 900x600 pixels.
- This is a minimal example and doesn't include advanced browser features.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Author & Contact

**galaxy-cli**

GitHub: [https://github.com/galaxy-cli/pyqt5-wrapper](https://github.com/galaxy-cli/pyqt5-wrapper)
