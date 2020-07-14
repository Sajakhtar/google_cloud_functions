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

## Test Cloud Function Locally
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


Google Cloud SDK commands in the Command Prompt (Google Cloud SDK Shell or Cloud Tools for Powershell) :
* Initialize GCP account: `gcloud init`
* List projects: `gcloud projects list`
* Set/change project: `gcloud config set project prject_name` (First, set set project ID to which you want to deploy the functions)
* Deploy Cloud Function: `gcloud functions deploy function_name --runtime python37 --trigger-http` (Google Cloud only supports Python 3.7, and python file must be `main.py`)

The cloud function will apprear int he [GCP Console](https://console.cloud.google.com/functions/list)

A note on Security: While deploying the Cloud Functions as unauthenticated is easy, we need to add security to our Cloud Function, else anyone can access the endpoint and send millions of requests. This could lead to fraudulent requests and therefore a costly GCP bill.

## Emails Project

Using sendinblue.com as sendgrid.com account requires manual authorization, which may take some time.

[Sendinblue API docs](https://github.com/sendinblue/APIv3-python-library)

### Environment Variables for API keys

Create a .env file in the project root directory to `export API_KEY=api_string`.

In Linux we can use `source .env`, however, in windows we'll have to create a settings.py file and [`pip install -U python-dotenv`](https://github.com/theskumar/python-dotenv), and in order to "source" the .env file, run settings.py first to set all environment variables.

Environment variables can then be referenced in main.py as os.getenv("variable_name").


### Sendinblue API

Add `sib-api-v3-sdk` to requirements.txt

run `pip install -r requirements.txt` to install all the dependencies.

### Testing Emails Cloud Function

`functions-framework --target send_mail --debug`

### Adding security via Bearer token

Using the python console in the terminal, run
`>>> import secrets`
`>>> secrets.token_hex(16)`

Add the outputted bearer token as a variable in the .env file.

