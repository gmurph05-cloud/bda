import json
import os
from urllib.error import HTTPError
from urllib.request import Request, urlopen


def ask_gemini(prompt, model_name="gemini-2.5-flash"):
    # Read your API key from the environment.
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is not set")

    # Build the remote Gemini endpoint URL.
    url = (
        "https://generativelanguage.googleapis.com/v1beta/models/"
        f"{model_name}:generateContent"
    )

    # Prepare the request body with your prompt.
    payload = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }

    # Create an HTTP POST request with JSON payload and API key.
    request = Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "x-goog-api-key": api_key,
        },
        method="POST",
    )

    # Send request, parse JSON response, and return only model text.
    # If quota/rate limit is reached, show a student-friendly message.
    try:
        with urlopen(request, timeout=60) as response:
            data = json.loads(response.read().decode("utf-8"))
    except HTTPError as err:
        if err.code == 429:
            raise RuntimeError(
                "Gemini rate/limit reached. Please wait a minute and try again."
            ) from err
        raise

    return data["candidates"][0]["content"]["parts"][0]["text"].strip()


answer = ask_gemini("Return only the 4-digit release year for the Studio Ghibli movie 'Ponyo'.\n Output format: only 4 digits, no extra text.")
print(answer)

"""
// https://github.com/warestack/bda/blob/main/session2/session-02-homework.md
8. Homework task
In session2/solutions/exercise-02-homework.py:

1. Load studio_ghibli_movies.csv using csv.DictReader.
2. Find rows with missing year.
3. For each missing year, call ask_gemini(...) and fill value.
4. Find rows with missing music_by.
5. For each missing music_by, call ask_gemini(...) and fill value.
6. Save output file as studio_ghibli_movies_ai_clean.csv.
7. Print:
    - how many values were filled by AI
    - any rows still missing values
Keep it simple. You are using Gemini as a helper function, not building a full framework.

9. Submission
Include:
session2/solutions/exercise-02-homework.py
optional: studio_ghibli_movies_ai_clean.csv
"""

