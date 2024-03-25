# Environment setup

## Install pyenv and required python version
``` bash
pyenv install 3.9.6
pyenv global 3.9.6
```

## Create virtual environment using the python version installed by pyenv
``` bash
PYENV_PYTHON_PATH=$(pyenv which python)
echo $PYENV_PYTHON_PATH
virtualenv -p $PYENV_PYTHON_PATH venv
```

## Activate virtual environment and install dependencies
``` bash
. venv/bin/activate
pip install pip-tools==7.4.1
pip-sync requirements.txt
```

## Updating "requirements.in" and "requirements.txt"
The file "requirements.in" should only contain the top-level dependencies.
Run the following command to update "requirements.txt" with the latest versions of the dependencies.
```
pip-compile --annotation-style=line requirements.in --upgrade
```
