# Final Project Repository

In order to run the *Recipes By Gemini* you'll need a Google Cloud
project. Create that project in
[the Google Cloud Console](https://console.cloud.google.com).

## APIs

Once the project is created you'll need to enable the following APIs in your
project:

  * VertexAI API
  * BigQuery API
  * Secret Manager API

## Module Installs

For local development you'll need to install some Python modules. You can
either run `pip install -r requirements.txt` or:

```
  pip install bcrypt
  pip install google-cloud-texttospeech
  pip install google-generativeai
  pip install st-pages
  pip install streamlit
  pip install vertexai
```
## Set gCloud Project

You'll also need to set the active gCloud project for development and
deployment. To do that you'll first need to log in.

```
  gcloud auth login
```

And then set the active project. In the default case that is
`raycastanedatechx24`.

```
  gcloud config set project 
```

## Run a Local Server

To run a local server you can use `streamlit` directly from the command line:

```
  streamlit run main.py --server.enableCORS=false
```