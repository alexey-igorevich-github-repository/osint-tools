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

if [ ! -d "$DIR/$VENV_DIR" ]; then
  echo "Creating virtual environment..."
  python3 -m venv "$DIR/$VENV_DIR"
fi

echo "Activating virtual environment..."
source "$DIR/$VENV_DIR/bin/activate"

if [ -f "$DIR/requirements.txt" ]; then
  echo "Installing dependencies..."
  pip install -r "$DIR/requirements.txt"
fi

echo "Launching..."
"$DIR/$VENV_DIR/bin/python" "$DIR/main.py" "$@"

echo "The script has finished its work. You can close the window now."
echo "You can find your result in ./output.txt"

