# MaterChef Project Repository

Project Manager: Josh McAdams.
Team members:
  * Luis Escamilla.
  * Ray Castaneda.
  * Emmanuel Adeyemi.
  * Eduardo Ceballos.

This is an application developed in Streamlit and designed in Figma to generate recipes according to your needs and ingredients. The functionalities of the page include:

  * API calls to Gemini to generate recipes.
  * Storing a history in BigQuery.
  * Logging in on the main page.
  * Receiving recommendations or similar recipes.
  * Implementation of AI-generated audio and images.

App link: https://mywebappservice-dgasx36rwq-wl.a.run.app/


Presentation link: https://docs.google.com/presentation/d/1Su1Y7q2DPu9edjScXMcHOz-ALiveKZ5EuelT-ZNzH4E/edit#slide=id.g26f3300d853_0_7

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
