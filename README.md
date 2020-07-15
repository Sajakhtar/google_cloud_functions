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

### Locally test Function

In the emails directory, run `functions-framework --target send_mail --debug`

## Scheduling Google Cloud Functions

### Create Firebase project and Firestore Database

Create [Firebase project](https://console.firebase.google.com/) using the underlying GCP projects used for the previous functions.

Enable the Firestore Database.

Navigate to Project Settings > Service Accounts > Generate key>>

Download the JSON file, store in the project root directory and add the file to .gitignore.


### Firebase SDK Python

In Firebase, navigate to Firestore database.

* Start a collection named `expenses`.
* Add fields
    * createdAt = timestamp, select today's date
    * expense = number, value = 100

We'll create a cloud function that when invoked, it will create a document with a random ID with the date and expense fields

Add `firebase-admin` to the requirementst.txt file in the project root and the `expense` directory. Then run `pip install -r requirements.txt` at the project root level.

Add `python-dotenv` to the `requirements.txt` in the `expenses` directory as well.


### Locally test Function and Deploy

In the expenses directory, run `functions-framework --target set_expense --debug`

Deploy as before.


### Scheduling

In the project root directory, run
* `gcloud components install beta`
* `gcloud components update`
* Then we will create a topic to Pub/Sub: `gcloud pubsub topics create cloud-function-test`
* Subscribe to the topic: `gcloud pubsub subscriptions create cron-sub --topic cloud-function-test`

In the GCP console go to [Cloud Scheduler](https://console.cloud.google.com/cloudscheduler)

Create Job >>
* Name: set-expense
* Descrition: cloud function to create documents with random data
* Frequency: */2 * * * *
    * Takes the chrontab format
    * [chrontab field](https://man7.org/linux/man-pages/man5/crontab.5.html)
    * 5 fields: min, hour, day of month, month, day of week
    * Use [Chrontab Guru](https://crontab.guru/) to workout the syntax
    * syntax for [every 2 mins](https://crontab.guru/every-2-minutes)
* Timezone
* Target: HTTP
    * URL: paste the `set_expense` Cloud Function endpoint
    * HTTP Method: GET

The Cloud Function will now run at the frequency specified


## Adding CORS to a Cloud Function

In the GCP Console, navigate to the [Cloud Functions](https://console.cloud.google.com/functions).

Select a Cloud Function and navigate to the `Trigger` tab and copy the endpoint URL.

In a new browser tab, use the developer tools Console to fetch the endpoint using JavsScript, using the fetch method:

```
fetch(`Cloud Functions endpoint`, {method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({'name':'Jon','lastname':'Snow'})}).then(response => response.text()).then(result => console.log(result))
```

Notes
* Content-Type specifies the format of the data we're sending
* fetch() is a promise, so we call the .then() method for the response we expect to receive
* When we run this JavaScript in the console, we will get a CORS error
    * Access to fetch at '*Clound Function endpoint*' from origin 'chrome-search://local-ntp' has been blocked by CORS policy: Response to preflight request doesn't pass access control check: No 'Access-Control-Allow-Origin' header is present on the requested resource
* The browser is sending a request to the Cloud Function endpoint with a method called *OPTIONS*, the server has to return some headers and in the headers there has to be 'Access-Control-Allow-Origin' present

The solution is to modify the Cloud Function main.py file with the following pre-flight request code that occurs before the main request (purpose of the function)
```
# Pre-flight request for CORS
if request.method == 'OPTIONS':
    headers = {
        'Access-Control-Allow-Origin': '*', # access from specific domains or * for all domains
        'Access-Control-Allow-Methods': 'POST', # access via any method '*'
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600' # remember headers for 1hr (3600 secs) for future requests
    }
    return '', 204, headers
    # 204 status means No Content

# Set headers for CORS
headers = {
    'Access-Control-Allow-Origin': '*'
}
```

Redeploy the Cloud Function `gcloud functions deploy function_name --runtime python37 --trigger-http`

Then retest the JavaScript code in the Console of a new browser tab and this time there will be no CORS error and we'll get the expected response from the Cloud Function.
```
fetch(`Cloud Functions endpoint`, {method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({'name':'Jon','lastname':'Snow'})}).then(response => response.text()).then(result => console.log(result))
```

## Deleting Cloud Functions

In the project root directory, run
```
gcloud functions delete function_name
```


