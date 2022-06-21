#!/usr/bin/env bash
if [[ ! -e install.sh ]]; then
    echo >&2 "Please cd into the repository before running this script."
    exit 1
fi

SetupHome=$PWD
PATH=$PWD/env/bin:$PATH

if [[ "$OSTYPE" == "darwin"* ]]; then
    url=https://repo.anaconda.com/archive/Anaconda3-2022.05-MacOSX-x86_64.sh
    DL="curl"
    flag="-o"
else
    url=https://repo.anaconda.com/archive/Anaconda3-2022.05-Linux-x86_64.sh
    DL="wget"
    flag="-O"
fi

script=anaconda.sh
if [[ ! -e $SetupHome/env/bin/conda ]]; then
    $DL $url $flag $script
    /bin/bash $script -u -p $SetupHome/env -b
    rm -rf $script
    codna install -yc conda-forge/label/cf202003 ansible
    conda install -yc conda-forge/label/main ansible-lint
fi
$SetupHome/env/bin/ansible-playbook $SetupHome/ansible/install_all.yml
