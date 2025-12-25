# chatbot.py

import difflib
from faq_data import DATASET


TOTAL_PATTERNS = sum(len(entry["patterns"]) for entry in DATASET)

def find_best_match(user_input):
    user_input = user_input.lower().strip()
    best_score = 0
    best_response = None

    for entry in DATASET:
        for pattern in entry["patterns"]:
            score = difflib.SequenceMatcher(
                None, user_input, pattern.lower()
            ).ratio()

            if score > best_score:
                best_score = score
                best_response = entry["response"]

    return best_response, best_score