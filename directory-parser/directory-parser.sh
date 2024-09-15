#!/bin/bash



# This file is part of [osint-tools]. 
# # [osint-tools] is free software: you can redistribute it and/or 
# # modify it under the terms of the GNU General Public License as published by 
# the Free Software Foundation, either version 3 of the License, or (at your option) 
# any later version. 
# # [osint-tools] is distributed in the hope that it will be useful, 
# but WITHOUT ANY WARRANTY; without even the implied warranty of 
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the 
# GNU General Public License for more details. 
# # You should have received a copy of the GNU General Public License 
# # along with [osint-tools]. If not, see <http://www.gnu.org/licenses/>.



VENV_DIR="venv"

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if ! command -v python3 &> /dev/null
then
    echo "ERROR: Python3 is not installed. Please install Python3 before the script launch."
    exit 1
fi

if [ ! -d "$DIR/$VENV_DIR" ]; then
  echo "Creating virtual environment..."
  if ! python3 -m venv "$DIR/$VENV_DIR"; then
    echo "ERROR: Failed to create virtual environment. Please delete ./venv folder and try again."
    exit 1
  fi
fi

echo "Activating virtual environment..."
source "$DIR/$VENV_DIR/bin/activate"

if [ -f "$DIR/requirements.txt" ]; then
  echo "Installing dependencies..."
  if ! pip install -r "$DIR/requirements.txt"; then
    echo "ERROR: Failed to install dependencies."
    deactivate
    exit 1
  fi
else
  echo "There is no requirements.txt ... , skipping dependencies installation."
fi

echo "Launching directory-parser.py..."
if ! "$DIR/$VENV_DIR/bin/python" "$DIR/directory-parser.py" "$@"; then
  echo "ERROR: Failed to launch directory-parser.py."
  deactivate
  exit 1
fi

echo "Deactivating virtual environment."
deactivate

echo "The script has finished its work. You can close the window now." 
echo "Your result is in ./links.txt"

