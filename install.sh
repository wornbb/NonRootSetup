#!/usr/bin/env bash
if [[ ! -e install.sh ]]; then
    echo >&2 "Please cd into the repository before running this script."
    exit 1
fi

SetupHome=$PWD
PATH=$PWD/env/bin:$PATH

if [[ "$OSTYPE" == "darwin"* ]]; then
    url=https://repo.anaconda.com/archive/Anaconda3-2021.11-MacOSX-x86_64.sh
else
    url=https://repo.anaconda.com/archive/Anaconda3-2021.11-Linux-x86_64.sh
fi

script=anaconda.sh
if [[ ! -e $SetupHome/env/bin/conda ]]; then
    wget $url -O $script
    /bin/bash $script -u -p $SetupHome/env -b
    rm -rf $script
    conda install -yc anaconda jinja2
    conda install -yc conda-forge/label/main ansible ansible-lint
fi
$SetupHome/env/bin/ansible-playbook $SetupHome/ansible/install_all.yml
