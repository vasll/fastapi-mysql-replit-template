#!/bin/bash
#  DATABASE CONFIG  #
# Check if secrets are set
are_secrets_unset=false
if [ -z ${db_name+x} ]; then 
	echo "[startup.sh] Secret 'db_name' is not set";
 	are_secrets_unset=true
fi
if [ -z ${db_user+x} ]; then 
	echo "[startup.sh] Secret 'db_user' is not set";
 	are_secrets_unset=true
fi
if [ -z ${db_pass+x} ]; then 
	echo "[startup.sh] Secret 'db_pass' is not set";
 	are_secrets_unset=true
fi
if [ "$are_secrets_unset" = true ]; then	# If at least one of the secrets is missing show a message and exit
	echo "[startup.sh] ERROR: Required secrets are NOT set, read the README.md first"
 	echo "For more information on replit secrets, visit [https://docs.replit.com/programming-ide/workspace-features/storing-sensitive-information-environment-variables]"
    exit
fi

# shutdown of existing database
mariadb-admin shutdown 2> /dev/null

# Check if install is new
fresh_install=false
if [ ! -d "$MYSQL_HOME" ]; then
	echo "[startup.sh] Fresh MySQL install detected"
    fresh_install=true
    mkdir "$MYSQL_HOME"
else
	echo "[startup.sh] MySQL found"
    fresh_install=false
fi

# $MYSQL_HOME/my.cnf file. This is the mysql config startup file
echo "[server]
datadir = $MYSQL_HOME
user = runner
bind-address = 127.0.0.1
pid-file = mysqld.pid
log-error = error.log
general_log_file = general.log
general_log = 1
disable-log-bin = 1
innodb-log-file-size = 4194304
# I prefer case-insensitive table names
lower_case_table_names = 1
default-storage-engine = InnoDB" > $MYSQL_HOME/my.cnf

# If install is new, install the db and create auth/database data based on replit secrets
if [ "$fresh_install" = true ]; then
	echo "[startup.sh] Running mysql_install_db"
    mysql_install_db --skip-test-db --ldata="$MYSQL_HOME" &> /dev/null
	
	echo "[startup.sh] Running mysqld_safe"
    mysqld_safe &> /dev/null &
	
	echo -n "[startup.sh] Testing connection"
    while ! mysqladmin ping &> /dev/null; do
        sleep 0.5
		echo -n "."
    done
	echo " Successful"
	
	echo "[startup.sh] Creating database based on secrets"
	echo "CREATE DATABASE IF NOT EXISTS $db_name;
	CREATE USER IF NOT EXISTS '$db_user'@'localhost' IDENTIFIED BY '$db_pass';
	GRANT ALL PRIVILEGES ON $db_name.* TO '$db_user'@'localhost';
	FLUSH PRIVILEGES;
	QUIT" | mysql

    mariadb-admin shutdown &> /dev/null
fi


#  PYTHON CONFIG  #
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

# Start the mysql server as a background task with the parameters in $MYSQL_HOME/my.cnf, then the python main.py file

echo "[startup.sh] Starting MySQL server & main.py"
mysqld_safe & python "$HOME/$REPL_SLUG/$APP_DIR_NAME/main.py" && fg