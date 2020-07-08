# Google Cloud Functions Course

## Starting a project

To start a new project in Google Cloud Platform, we can got to the [Firebase Console](https://console.firebase.google.com/) or create it from [Google Cloud Platform Console](https://console.cloud.google.com/)

## Creating a Virtual Environment

Add `venv/` to .gitignore.

Install `python3-venv` with the following command for Linux (not required for Windows):
```
sudo apt install python3-env
```

Execute the following command to create a virtual environment name `venv` for Linux:
```
python3 -m venv venv
```
and Windows:
 ```
python -m venv venv
```
Activate virtual environment `venv` for Linux:
```
source venv/bin/activate
```

Activate virtual environment `venv` for Windows:
```
venv\scripts\activate.bat
```

In order to add new packages to our virtual environment, create a file `requirements.txt` to contain all pacakages for `venv` environment

`requirements.txt` should contain:
* `functions-framework`

To add new packages to `venv`, execute:
```
pip install -r requirements.txt
```
May need to also install:
```
pip install wheel
```

