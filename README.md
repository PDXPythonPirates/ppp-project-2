# ppp-project-2
Repository for the second Portland Python Pyrates project

## How to boot the app
  **Note**: You need an .env file with credentials to boot the mysql container locally.

  <details>
<summary>Required environment variables</summary>
<br>
   <ul>

<li> DATABASE_URL</li>
<li> MYSQL_ROOT_PASSWORD</li>
<li> MYSQL_PASSWORD</li>

   </ul>
</details>

- #### In your local environment
    1. run `make install` to install dependencies and jump into the virtual env
    2. run `flask run` to boot the app locally. Make sure you are in the top level directory that has the file "app_run.py"

- #### With docker containers + docker compose
    1. run `make up` to run the docker containers locally and open on  http://localhost:5000 (**this also boots a mysql container**)
    2. run `make stop` to stop containers and prune

## Working with Docker
* Install Docker by following the instructions on [their site](https://docs.docker.com/get-docker/)
* run `make build` to build the docker image
* run `make run` to run the docker containers locally and open on  http://localhost:5000
* run `make stop` to stop containers and prune

## Working with Poetry

* Install a new dep/library run `poetry add <your_dep>` or `poetry add <dep> --dev`
* Resolve poetry.lock files. Use 1. to resolve on github or 2. to resolve locally (recommended)
   1. On github **click** on resolve conflicts and follow [this guide](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/resolving-a-merge-conflict-on-github)
   2. Locally, pull the recent changes. Remove the lock file with the conflict `rm poetry.lock`. run `make install` to regenerate the lock file. Push changes and give yourself a high five!
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
