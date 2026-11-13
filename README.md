# my-first-app

A rock, paper, scissors game and a stocks dashboard, with automated tests and continuous integration.

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

## Configuration

The stocks dashboard requires an AlphaVantage API key. Obtain a key using the [form](https://www.alphavantage.co/support/#api-key) or get one shared by the professor.

Create a local ".env" file and store your environment variable in there:

```sh
# this is the ".env" file...

ALPHAVANTAGE_API_KEY="______________"
```

The ".env" file is listed in the ".gitignore" file, so it is never uploaded to GitHub.

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

Stocks dashboard:

```sh
python -m app.stocks
```

## Testing

Run tests:

```sh
pytest
```