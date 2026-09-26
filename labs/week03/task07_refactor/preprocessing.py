# Task 7 - Preprocessing Module

def clean_scores(scores):
    """Keep only scores between 0 and 100."""
    return [score for score in scores if 0 <= score <= 100]