# ppp-project-2
Repository for the second Portland Python Pyrates project


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

* Install our base tooling and spin up virtual env
   ```bash
   make install
   ```

### Troubleshooting

Help with various installation/setup issues:

 * [Mac](#Mac)

#### Mac

##### Edit to add