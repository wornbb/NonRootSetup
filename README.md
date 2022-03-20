# NonRootSetup

## Goal

Use this repo to set up your development environment on any Linux or Mac.
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
	- mysql & nosql
	- nodejs with yarn
	- nvim
	- nerd fonts
	- tmux using zsh as default shell
	- vscode
	- WezTerm
	- zsh with various plugins defined in configs/zshrc

## Dependencies
 - bash
 - wget
 - gcc & g++
 - git
 - curl
 - texinfo

Need to reduce those dependencies:
autoconf automake autotools-dev libncurses-dev libncursesw5-dev libsigsegv2 m4 yodl

Future development may even assume no or bare minimum dependencies.

## Implementation and Explanation

Software/Package distribution strategy:
	- If appimage exists, use appimage
	- 
