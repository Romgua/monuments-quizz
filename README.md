
# Monuments Quizz

## Summary

 1. [How it works ?](#how-it-works)
	 1. [Features](#features)
	 2. [Future improvements](#future-improvements)
 2. [How to install solution for Windows ?](#how-to-install-solution-for-windows)
	 1. [Clone the repository](#0---clone-the-repository)
	 2. [Installing Python 3](#1---installing-python-3)
	 3. [Installing with Pip](#2---installing-with-pip)
	 4. [Installing Virtualenv](#3---installing-virtualenv)
	 5. [Installing requirements](#4---installing-requirements)
	 6. [Running the server](#5---running-the-server)


## How it works ?

The Monuments Quiz application is a website which aims to *test the user's knowledge of world monuments* and their cities.

The game system is based on a point system which **rewards risk taking**. On a series of **10 questions**, the user will be asked to choose, for each question, a response mode in order to identify the city of the monument displayed on the screen.

The different choice modes and the number of points rewarded are described below:

| Modes of choice | Number of points | Number of proposed responses |
| - | - | - |
| Duo | +1 point | 2 suggested responses |
| Carré| +3 points | 4 suggested responses |
| Cash | +5 points | No response proposal |

### Features

The user can **play for free** and without creating an account.
However, it is strongly advised to create an account that will allow him to store his statistics and compare them with his friends. 

### Future improvements

In future versions, accounts may allow you to check game history, use wild cards shared on the game.
A difficulty system based on the displayed monument will also be implemented.


## How to install solution for Windows?

### 0 - Clone the repository

First of all, you need to clone this repository by running this command line:

    git clone git@github.com:thomasberard/monuments-quizz.git

OR

    git clone https://github.com/thomasberard/monuments-quizz.git


### 1 - Installing [Python 3](https://www.python.org/downloads/)

First, you need to Download the latest version by following this link: [Latest version of Python](https://www.python.org/downloads/)


### 2 - Installing with [Pip](https://pip.pypa.io/en/stable/installing/#installing-with-get-pip-py "Permalink to this headline")

To install pip for python 3, securely download  `get-pip.py`  by following this link:  [get-pip.py](https://bootstrap.pypa.io/get-pip.py).
Alternatively, use  `curl`:

    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

Then run the following command in the folder where you have downloaded  `get-pip.py`:

    python get-pip.py


### 3 - Installing [Virtualenv](https://virtualenv.pypa.io/en/latest/installation.html#via-pip)

To install virtualenv via pip, run the following command:

    python -m pip install --user virtualenv

Then run the follow command to create a python virtual environment:

    python -m virtualenv venv

Finally, run your environment by running this command:

     .\venv\Scripts\activate.bat


### 4 - Installing requirements

Then, you need to install all requirements in your new environment by running this command:

    pip install -r %PATH_OF_YOUR_CLONE_REPOSITORY%\monument-quizz\MonumentQuizz\requirements.txt

`%PATH_OF_YOUR_CLONE_REPOSITORY%` is where you clone the repository `monument-quizz`.

### 5 - Running the server

To run the server, go to the directory:

    monuments-quizz\MonumentQuizz

Then run the following commands:

    python manage.py migrate
    python manage.py runserver

FInally, on your browser, go to this URL:

    http://127.0.0.1:8000/
