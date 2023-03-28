#!/bin/bash
VENV_PATH="$HOME/$REPL_SLUG/.venv"  # Path of python venv [https://docs.python.org/3/library/venv.html]

# If .venv does not exist, make it
if [ ! -d $VENV_PATH ]; then  
    echo ".venv not found"
    python -m venv $VENV_PATH
    echo ".venv created"
fi

# Activate venv and run main.py script
source "$HOME/$REPL_SLUG/.venv/bin/activate"
python "fastapi-app/main.py"