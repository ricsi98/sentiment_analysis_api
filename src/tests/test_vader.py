import pytest
import nltk
import os
from vader import VaderSingleton


def test_vader_download_fallback():
    ptr = nltk.data.find("sentiment/vader_lexicon.zip")
    os.unlink(str(ptr))
    try:
        nltk.data.find("sentiment/vader_lexicon.zip")
        raise Exception("Could not remove vader package")
    except LookupError:
        pass
    VaderSingleton().analyze_sentiment("I ate two apples")
    

def test_vader():
    sentiment, _ = VaderSingleton().analyze_sentiment("I am very happy")
    assert sentiment == "positive"