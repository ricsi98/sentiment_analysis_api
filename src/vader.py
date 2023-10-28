import os
import threading
from typing import Dict, Tuple

import nltk
import numpy as np
from nltk.sentiment.vader import SentimentIntensityAnalyzer

from logconfig import get_logger

SENTIMENT_RESULT = Tuple[str, float]
_VADER_LEXICON = "vader_lexicon"


def _get_sentiment(pos: float, neg: float, neu: float, **kwargs) -> SENTIMENT_RESULT:
    scores = [pos, neg, neu]
    names = ["positive", "negative", "neutral"]
    argmax = np.argmax(scores)
    return (names[argmax], scores[argmax])


def get_metadata() -> Dict[str, str]:
    return {
        "model_version": os.getenv("MODEL_VERSION", "1.0.0"),
        "model_type": os.getenv("MODEL_TYPE", "VADER Sentiment Analysis"),
        "model_training_date": os.getenv("MODEL_TRAINING_DATE", "2023-09-01")
    }


class VaderSingleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance._initialize_vader_model()
        return cls._instance

    def _initialize_vader_model(self):
        self.logger = get_logger("vader")
        self.logger.info("Initializing VADER model")
        try:
            nltk.data.find(_VADER_LEXICON)
        except LookupError:
            self.logger.warn(
                f"Could not find nltk package {_VADER_LEXICON}, downloading...")
            nltk.download(_VADER_LEXICON)
        self.sid = SentimentIntensityAnalyzer()
        self.logger.info("VADER model initialized succesfully")

    def analyze_sentiment(self, text: str) -> SENTIMENT_RESULT:
        self.logger.info(f"Analyzing sentence: {text}")
        result = self.sid.polarity_scores(text)
        self.logger.info(
            f"Sentiment analysis result: {result}. Input sentence: {text}")
        return _get_sentiment(**result)
