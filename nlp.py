import re
from textblob import TextBlob
import spacy

nlp = spacy.load("en_core_web_sm")
FILLER_WORDS = set(["um", "uh", "like", "so", "actually", "you know", "i mean", "right"])

def analyze_text(text: str) -> dict:
    cleaned = text.strip()
    words = re.findall(r"\w+", cleaned.lower())
    filler_count = sum(1 for w in words if w in FILLER_WORDS)

    blob = TextBlob(cleaned)
    sentiment = blob.sentiment.polarity

    doc = nlp(cleaned) if cleaned else []
    keywords = [token.lemma_ for token in doc if token.pos_ in ("NOUN","PROPN","VERB")] if cleaned else []
    keyword_count = len(keywords)

    duration_seconds = len(words) / 2.0

    score = 50
    score += max(-20, min(20, sentiment * 20))
    score += max(-10, min(10, (keyword_count - 5)))
    score -= min(15, filler_count * 2)
    final_score = max(0, min(100, score))

    return {
        "transcript": cleaned,
        "filler_count": filler_count,
        "sentiment": sentiment,
        "keyword_count": keyword_count,
        "final_score": final_score,
    }
