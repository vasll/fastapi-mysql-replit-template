#!/bin/bash
VENV_PATH="$HOME/$REPL_SLUG/.venv"  # Path of python venv [https://docs.python.org/3/library/venv.html]
is_venv_new=false

# If .venv does not exist, make it
if [ ! -d $VENV_PATH ]; then  
    echo "[startup.sh] venv not found, creating at '$VENV_PATH'"
    python -m venv $VENV_PATH
	is_venv_new=true
    echo "[startup.sh] venv created"
else
	echo "[startup.sh] venv found"
fi

# Activate venv
echo "[startup.sh] activating venv at '$VENV_PATH'"
source "$VENV_PATH/bin/activate"

# If venv is new, install requirements
if [ "$is_venv_new" = true ]; then
	echo "[startup.sh] installing requirements"
	python -m pip install -r requirements.txt
fi

echo "[startup.sh] Running ./fastapi/main.py"
python "$HOME/$REPL_SLUG/fastapi-app/main.py"