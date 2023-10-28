from pydantic import BaseModel
from datetime import datetime


class SentimentPrediction(BaseModel):
    sentiment: str
    score: float


class HealthCheckResponse(BaseModel):
    status: str
    timestamp: datetime


class ModelMetadata(BaseModel):
    model_version: str
    model_type: str
    model_training_date: str


class SentimentInput(BaseModel):
    text: str