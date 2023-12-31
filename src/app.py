from datetime import datetime

from fastapi import FastAPI, HTTPException

import models
from vader import VaderSingleton, get_metadata

app = FastAPI()


@app.get("/health", response_model=models.HealthCheckResponse)
def health():
    try:
        VaderSingleton()
    except:
        raise HTTPException(status_code=503, detail="Service Unavailable")
    return models.HealthCheckResponse(
        status="up",
        timestamp=datetime.now()
    )


@app.post("/predict", response_model=models.SentimentPrediction)
def predict(input: models.SentimentInput):
    vader = VaderSingleton()
    sentiment, score = vader.analyze_sentiment(input.text)
    return models.SentimentPrediction(
        sentiment=sentiment,
        score=score
    )


@app.get("/metadata", response_model=models.ModelMetadata)
def metadata():
    return models.ModelMetadata(
        **get_metadata()
    )
