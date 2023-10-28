import pytest
import nltk
import os
from vader import VaderSingleton


def test_vader_download_fallback():
    """
    The Vader implementation looks for available vader_lexicon package. If it is not found it tries downloading it.
    We expect that it is able to analyze the sentiment even if we first remove the necessary files.
    """
    ptr = nltk.data.find("sentiment/vader_lexicon.zip")
    os.unlink(str(ptr))
    try:
        nltk.data.find("sentiment/vader_lexicon.zip")
        raise Exception("Could not remove vader package")
    except LookupError:
        pass
    VaderSingleton().analyze_sentiment("I ate two apples")
    

def test_vader():
    """We expect that the sentiment analyizer labels a happy sentence positive"""
    sentiment, _ = VaderSingleton().analyze_sentiment("I am very happy")
    assert sentiment == "positive"