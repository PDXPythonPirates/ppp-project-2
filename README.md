# ppp-project-2
Repository for the second Portland Python Pyrates project

## How to boot the app
1. run `make install` to install dependencies and jump into the virtual env
2. run `flask run` to boot the app locally

## Working with Poetry

* Install a new dep/library run `poetry add <your_dep>` or `poetry add <dep> --dev`
* Resolve poetry.lock files. Use 1. to resolve on github or 2. to resolve locally (recommended)
   1. On github **click** on resolve conflicts and follow [this guide](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/resolving-a-merge-conflict-on-github)
   2. Locally, pull the recent changes and open the file with the conflict. Resolve the conflict to make the lock file happy (see 1.). Finally, run 'poetry update poetry.lock' (this will let poetry take the wheel and update the lock file so it can be in a good state) 
* 

## Enable Virtual Environment and Install Packages

### Mac

* Note: make sure poetry is installed and first time setup is complete
* Take a look at the Makefile to see what shell commands are being executed
   ```bash
   make install
   ```
   
## Adding Python Dependencies

0. we use [poetry](https://python-poetry.org/) to track python deps
0. to install a new dep run `poetry add <your_dep>` or `poetry add <dep> --dev`
0. you can also modify the pyproject.toml directly, then run `poetry lock --no-update`

## First-Time Setup

### Mac
* Install [brew](https://brew.sh/)
* Install pyenv
   ```bash
   brew install pyenv
   echo 'eval "$(pyenv init --path)"' >> ~/.zprofile
   echo 'eval "$(pyenv init -)"' >> ~/.zshrc
   ```
* Install [zsh](https://sourabhbajaj.com/mac-setup/iTerm/zsh.html)
   ```bash
   brew install zsh
   ```
* Install Python 3.8.10
   ```bash
   pyenv install 3.8.10
   ```

### Troubleshooting

Help with various installation/setup issues:

 * [Mac](#Mac)

#### Mac

##### Edit to add

## References
1. [Flask Mega Tutorial - by Miguel Grinberg - 2018](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) 

## Other References
1. Testing Markdown - [dillinger.io](https://dillinger.io/) 
