# my-first-app

A rock, paper, scissors game, with automated tests and continuous integration.

## Setup

Clone the repo to download it from GitHub, for example onto the Desktop. Then navigate to the repo using the command line:

```sh
cd ~/OneDrive/Desktop/my-first-app
```

Create a virtual environment:

```sh
conda create -n rps-env python=3.11
```

Activate the virtual environment:

```sh
conda activate rps-env
```

Install package dependencies:

```sh
pip install -r requirements.txt
```

## Usage

Example script:

```sh
python app/my_script.py

# alternative "modular style" command:
python -m app.my_script
```

Game of rock, paper, scissors:

```sh
python app/rps.py

# alternative "modular style" command:
python -m app.rps
```

## Testing

Run tests:

```sh
pytest
```