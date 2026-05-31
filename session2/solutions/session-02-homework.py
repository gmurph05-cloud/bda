import json
import os
from urllib.error import HTTPError
from urllib.request import Request, urlopen
import csv
from google import genai

# in Windows CMD terminal
# # set GEMINI_API_KEY={key without quotes for Windows CMD}

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
    # If quota/rate limit is reached, show a beginner friendly message.
    try:
        with urlopen(request, timeout=60) as response:
            data = json.loads(response.read().decode("utf-8"))
    except HTTPError as err:
        if err.code == 429:
            raise RuntimeError(

    # 6. Save output file as studio_ghibli_movies_ai_clean.csv.


    # 7. Print:
    #     - how many values were filled by AI
    #     - any rows still missing values             "Gemini rate/limit reached. Please wait a minute and try again."
            ) from err
        raise

    return data["candidates"][0]["content"]["parts"][0]["text"].strip()


# answer = ask_gemini("Return only the 4-digit release year for the Studio Ghibli movie 'Ponyo'.\n Output format: only 4 digits, no extra text.")
# answer = ask_gemini(f'''Return only the composer full name for the Studio Ghibli movie "Howl's Moving Castle".\nOutput format: name only, no extra text.''')
# print(answer)

"""
// https://github.com/warestack/bda/blob/main/session2/session-02-homework.md
8. Homework task
In session2/solutions/exercise-02-homework.py:

# 1. Load studio_ghibli_movies.csv using csv.DictReader.
# 2. Find rows with missing year.
# 3. For each missing year, call ask_gemini(...) and fill value.
# 4. Find rows with missing music_by.
# 5. For each missing music_by, call ask_gemini(...) and fill value.
# 6. Save output file as studio_ghibli_movies_ai_clean.csv.
# 7. Print:
#     - how many values were filled by AI
#     - any rows still missing values
# Keep it simple. You are using Gemini as a helper function, not building a full framework.

9. Submission
Include:
session2/solutions/exercise-02-homework.py
optional: studio_ghibli_movies_ai_clean.csv
"""

import csv
import os
import google.genai as genai

GEMINI_MODEL = "gemini-2.5-flash-lite"

def correct_all_text(texts):
    """
    Sends a batch list of items to Gemini to process all at once.
    """
    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    
    # Creates a numbered list: "1. Spirited Away", "2. My Neighbor Totoro", etc.
    numbered = "\n".join(f"{i+1}. {t}" for i, t in enumerate(texts))
    
    # Prompt tailored for Movie Years
    prompt = (
        "For each numbered Studio Ghibli movie below, provide ONLY its 4-digit release year. "
        "Return the output as a matching numbered list with no extra text or explanations.\n"
        f"{numbered}"
    )
    
    response = client.models.generate_content(model=GEMINI_MODEL, contents=prompt)
    return response.text.strip()


# --- Main Execution Flow ---

FILE_PATH = "data/studio_ghibli_movies.csv"
OUTPUT_PATH = "data/studio_ghibli_movies_ai_clean.csv"

# Step 1: Read all rows and isolate the ones that need fixing
all_rows = []
missing_year_titles = []
missing_year_row_indices = []

with open(FILE_PATH, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    fieldnames = reader.fieldnames # Save headers for later writing
    
    for idx, row in enumerate(reader):
        all_rows.append(row) # Keep a master copy of the row
        
        # Check if the year column is blank
        if row.get("year", "").strip() == "":
            title = row.get("title", "Unknown")
            missing_year_titles.append(title)
            # Track the index in all_rows so we know exactly where to put the answer back
            missing_year_row_indices.append(idx)

# Variable to track how many rows we successfully modify
ai_filled_count = 0

# Step 2: Make ONE batch call to Gemini if any missing values exist
if missing_year_titles:
    print(f"Found {len(missing_year_titles)} missing years. Batching request to Gemini...\n")
    
    raw_response = correct_all_text(missing_year_titles)
    
    # Parse the response lines (e.g., "1. 2001", "2. 1988") into just the years
    ai_years = []
    for line in raw_response.splitlines():
        if "." in line:
            year_clean = line.split(".", 1)[1].strip()
            ai_years.append(year_clean)

    # Step 3: Map the answers back to the tracked rows
    if len(ai_years) == len(missing_year_row_indices):
        for i, row_idx in enumerate(missing_year_row_indices):
            original_row = all_rows[row_idx]
            original_row["year"] = ai_years[i]
            ai_filled_count += 1
            print(f"Successfully fixed '{original_row['title']}' -> {ai_years[i]}")
    else:
        print("⚠️ Warning: Gemini's list count didn't match our missing rows count.")
        print(f"Sent: {len(missing_year_titles)} | Received: {len(ai_years)}")
else:
    print("No missing years found initially!")


# --- # 6. Save output file as studio_ghibli_movies_ai_clean.csv ---
with open(OUTPUT_PATH, "w", newline="", encoding="utf-8") as out_file:
    writer = csv.DictWriter(out_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(all_rows)

print(f"\n📁 File saved successfully to: {OUTPUT_PATH}")


# --- # 7. Summary Report ---
print("\n" + "="*40)
print("             FINAL SUMMARY            ")
print("="*40)
print(f"Total values filled by AI: {ai_filled_count}")
print("-" * 40)

# Scan through final data to see if any missing fields remain
still_missing_rows = []
for idx, row in enumerate(all_rows, start=2): # CSV standard starts content at row 2
    # Check if ANY column in the row is still an empty string
    empty_cols = [col for col, val in row.items() if val.strip() == ""]
    if empty_cols:
        still_missing_rows.append((idx, row.get("title", "Unknown"), empty_cols))

if still_missing_rows:
    print("⚠️ Rows still missing values:")
    for row_idx, title, cols in still_missing_rows:
        print(f"  • Row {row_idx} | Movie: '{title}' | Missing column(s): {', '.join(cols)}")
else:
    print("✅ Complete! No rows are missing values in the final file.")
print("="*40)