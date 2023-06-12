# NonRootSetup

## Caveat

Currently, although NonRootSetup can be cleanly uninstalled by deleting the local repository, it cannot revert to the pre-install state. It means that config files like `.zshrc` has to be manually restored from the backup copy created during installation.

## Goal

Use this repo to set up a minimal development environment on any Linux or Mac. The intended use case is on a enterprise development machine where the machine already has most tools but lacks some personal touches.

NonRootSetup trades the installation speed for:
	1. platform independency, so that you are worry free
	2. exemption from root privilege, so that you are not blocked by your sys admin
	3. software installation within the repo, so that you can place everything in 
	a local storage.

To achieve above goals, all software must be compiled using homebrew
so it will take quiet some time.

## Environment Contents

- Ansible
- Anaconda3/python3 
- fzf
- htop
- nvim
- nerd fonts
- tmux using zsh as default shell
- zsh with various plugins defined in configs/zshrc

## Dependencies
 - bash
 - wget
 - gcc & g++
 - git
 - curl
 - texinfo

Need to reduce those dependencies:
automake autotools-dev libncurses-dev libncursesw5-dev libsigsegv2 m4 yodl
build-essential g++ 

