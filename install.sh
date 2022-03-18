#! /usr/bin/bash
if [[ ! -e install.sh ]]; then
    echo >&2 "Please cd into the repository before running this script."
    exit 1
fi

SetupHome=$PWD
PATH=$PWD/env/bin:$PATH

if [[ ! -e $SetupHome/env/bin/conda ]]; then
    wget https://repo.anaconda.com/archive/Anaconda3-2021.11-Linux-x86_64.sh
    /bin/bash Anaconda3-2021.11-Linux-x86_64.sh -p $SetupHome/env -b
    rm -rf Anaconda3-2021.11-Linux-x86_64.sh
    conda install -yc conda-forge ansible
fi

$SetupHome/env/bin/ansible-playbook $SetupHome/ansible/install_all.yml
