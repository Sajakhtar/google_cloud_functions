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
This is a package to test Google Cloud Functions locally. It installs Flask as a dependancy.


To add new packages to `venv`, execute:
```
pip install -r requirements.txt
```
May need to also install:
```
pip install wheel
```

## Test Cloud Function locally
To test a Google Cloud Function locally, from your application folder, run:
```
functions-framework --target my_function
```
or allow for server to update automatically if changes are made tto my_function
```
functions-framework --target my_function --debug
```

Then navigate to `http://localhost:8080/` or `http://127.0.0.1:8080/`, not `http://0.0.0.0:8080/`, for Windows at least.

See [docs](https://github.com/GoogleCloudPlatform/functions-framework-python) and [troubleshooting](https://stackoverflow.com/questions/53693987/test-python-google-cloud-functions-locally)

Test the function endpoing using `GET` requests in Postman with the endpoint URL or `POST` requests with raw json

You can test functions that have parameters by using query parameters on the end point `http://127.0.0.1:8080/?name=jon&lastname=snow` or using JSON `{"name":"iron","lastname":"man"}`

## Deploying Google Cloud Function

Install the [Google Cloud SDK](https://cloud.google.com/sdk/docs/downloads-versioned-archives). For Windows [isntallaltion](https://cloud.google.com/sdk/docs/downloads-interactive) and [quick start](https://cloud.google.com/sdk/docs/quickstart-windows)


Google Cloud SDK commands in the Google Cloud SDK Shell or Cloud Tools for Powershell :
* initialize project: `gcloud init`
* List projects: `gcloud projects list`
* Set/change project: `gcloud config set project prject_name` (First, set set project ID to which you want to deploy the functions)
* Deploy Cloud Function: `gcloud functions deploy function_name --runtime python37 --trigger-http` (Google Cloud only supports Python 3.7, and python file must be `main.py`)


## Security

We need to add security to our Cloud Function, else anyone can access the endpoint and send millions of requests, leading toa costly GCP bill
