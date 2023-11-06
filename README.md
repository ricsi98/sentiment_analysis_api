# Sentiment Analysis API
## Overview

The Sentiment Analysis API is a web service that provides sentiment analysis using the VADER model. It offers endpoints to predict sentiment, check the API's health, and retrieve model metadata.

## Features

- Sentiment analysis of text using VADER model.
- Health check endpoint for monitoring the API's status.
- Model metadata endpoint to retrieve information about the deployed model.

## Installation

1. Clone the repository:

```bash
git clone git@github.com:ricsi98/sentiment_analysis_api.git
cd  sentiment_analysis_api
```

2. (OPTIONAL) run tests:
```bash
pip install -r requirements.txt
pytest src
```

3. Build docker image:
```bash
docker build -t sentiment-api .
```

4. Run the container:
```bash
docker run -p 8000:8000 sentiment-api
```
5. Now the service should be alive, you can access (and try) the API at [http://0.0.0.0:8000/docs](http://0.0.0.0:8000/docs)


## Application Components

### File structure

The project is organized into the following directories and files:

- **src**: This is the main source directory containing the application code and configuration.
  - `app.py`: The main FastAPI application, which defines the API endpoints.
  - `logconfig.py`: A module that sets up the logging configuration for the application.
  - `vader.py`: The file containing the VADER sentiment analysis model, responsible for sentiment analysis.

- **src/models**: This directory contains Pydantic models used by the application.
- **src/tests**: This directory contains unit tests for the application.
  - `test_app.py`: Unit tests for the FastAPI application endpoints defined in `app.py`.
  - `test_vader.py`: Unit tests for the VADER sentiment analysis model in `vader.py`.


### Singleton VADER Wrapper

The application utilizes a Singleton design pattern for the VADER sentiment analysis model. The Singleton VADER wrapper ensures that only one instance of the VADER model is created and reused throughout the application's lifecycle.


The Singleton VADER wrapper serves two main purposes:

1. **Efficiency**: By creating a single instance of the VADER model, the application avoids the overhead of model initialization on every request. This leads to improved performance and resource management.

2. **Consistency**: The Singleton design pattern ensures that all parts of the application interact with the same VADER model instance, promoting data consistency.


### Additional Validation
I've added an extra validation rule for input data in the `POST /predict` endpoint. Specifically, the input text provided should have a minimum length of 3 characters. This ensures that text inputs are of a sufficient length to perform sentiment analysis accurately.

### Model Metadata

The application includes a model metadata endpoint (`/metadata`) that provides information about the deployed model. The metadata includes the following details:

- **Model Version**: The version of the deployed model, which can be customized using the `MODEL_VERSION` environment variable. If not specified, it defaults to "1.0.0."

- **Model Type**: The type of the model, which is set to "VADER Sentiment Analysis" by default and can be customized using the `MODEL_TYPE` environment variable.

- **Model Training Date**: The date when the model was trained, which can be customized using the `MODEL_TRAINING_DATE` environment variable. If not specified, it defaults to "2023-09-01"

It's important to note that these metadata details, particularly the model version and training date, may not be applicable to the VADER sentiment analysis model. VADER is a lexicon-based sentiment analysis tool and does not have version-specific updates or a conventional training date like machine learning models. As a result, the default values or customizations of these fields may not provide meaningful information in the context of VADER.


## Limitations

While the Sentiment Analysis API is designed to be a reliable and efficient tool for sentiment analysis, it comes with some inherent limitations:

1. **English Language Support**: The VADER sentiment analysis model used in this application is primarily designed for the English language. It may not provide accurate results for texts in other languages.

2. **Sensitivity to Text Length**: VADER is sensitive to the length of input text. Extremely short texts or single-word inputs may produce less accurate sentiment scores.

3. **No Customization**: The application does not currently support customizing the sentiment analysis model. Users cannot fine-tune the model for specific industries or domains.


4. **Security Considerations**: Security features, such as input validation and security headers, may need to be enhanced depending on the deployment environment and use cases.