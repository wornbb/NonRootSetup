#!/usr/bin/env bash
# shellcheck source=/dev/null

if [[ ! -e install.sh ]]; then
    echo >&2 "Please cd into the repository before running this script."
    exit 1
fi

SetupHome=$PWD
PATH=$PWD/env/bin:$PATH

PYTHON_HOME="$SetupHome"/env/yienv3
/bin/python3 -m venv "$PYTHON_HOME"
source "$PYTHON_HOME"/bin/activate
pip3 install --upgrade pip
pip3 install -r requirement.txt
ansible-playbook "$SetupHome"/installers/setup_configs.yml


source ~/.zprofile
python3 ./installers/install_util.py
source ~/.zshrc
