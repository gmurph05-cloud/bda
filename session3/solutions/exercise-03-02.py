### Session 3 | Homework
# +==========+==========+==========+==========+==========+
#   In this homework, you will use `yield` to split *Les Misérables* into small chunks and summarize those chunks with Gemini.

'''
#### 1. Goal

In Session 2, Gemini helped fill missing data. This time, you will use Gemini to summarize chunks of a large text file.

You will:

- use a generator with `yield` to stream book chunks
- avoid loading the whole book into memory
- send one small chunk at a time to Gemini
- compare generator memory use with `readlines()`
'''
import os

from google import genai


MODEL_NAME = "gemini-2.5-flash"
TEXT_FILE = "data/les_miserables.txt"
CHUNK_SIZE = 30
MAX_CHUNKS = 3


def ask_gemini(prompt):
    """Send prompt text to Gemini and return the response text."""

    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    response = client.models.generate_content(model=MODEL_NAME, contents=prompt)
    return response.text


def book_chunks(path, chunk_size=30, max_chunks=3):
    chunk = []
    chunks_sent = 0

    with open(path, "r", encoding="utf-8") as file:
        """Yield small non-empty text chunks from the book."""
        for line in file:
            line = line.strip()
            if line == "":
                continue

            chunk.append(line)

            if len(chunk) == chunk_size:
                yield "\n".join(chunk)
                chunks_sent += 1
                chunk = []

                if chunks_sent == max_chunks:
                    return

    if chunk and chunks_sent < max_chunks:
        yield "\n".join(chunk)


def build_summary_prompt(chunk_text, chunk_number):
    """Build a prompt that asks Gemini for strict JSON output."""
    return f"""You are summarizing one chunk from Les Misérables.

    Return only valid JSON with these keys:
    - chunk: the chunk number
    - characters: important character names mentioned
    - events: short event descriptions
    - summary: a 2-3 sentence summary
    - uncertainty: anything unclear

    Rules:
    - Do not include Markdown fences.
    - Do not add commentary outside the JSON.
    - If there are no clear events, use an empty list.

    Chunk number: {chunk_number}

    Excerpt:
    {chunk_text}
    """

if __name__ == "__main__":
    for chunk_number, chunk_text in enumerate(
        book_chunks(
            TEXT_FILE, 
            chunk_size=CHUNK_SIZE, 
            max_chunks=MAX_CHUNKS),
            start=1,):
        prompt = build_summary_prompt(chunk_text, chunk_number)
        summary = ask_gemini(prompt)
        print(f"Chunk {chunk_number}")
        print(summary)
        print()

#### 7. Complexity discussion
# +==========+==========+==========+==========+==========+==========+
# Loading the whole book with `readlines()` uses O(n * m) space.
# Reading and chunking the book locally is O(n * m) if all chunks are processed.
# Total local reading time is still O(n * m) if you process the whole book.
# A generator with `yield` keeps only the current chunk, so extra space is O(k * m), where `k` is chunk size.
# Extra space is O(k * m), where `k` is the chunk size. This is better than O(n * m) for loading the whole book.

#### 8. Reflection

""" Answer in your notes:

# 1. Which tasks were best solved with streaming?
# 2. Which tasks required loading all data?
# 3. Why is a generator with `yield` still an iterator?
# 4. When does `yield` save memory compared with `readlines()`?
# 5. Why is sending the whole book to Gemini in one prompt a bad idea? """

# 1. Which tasks were best solved with streaming?
'''
Reading and chunking the book (handled by the book_chunks generator) was best solved with streaming.

Instead of pulling the entire text of Les Misérables into memory all at once, the code uses a for line in file: loop. This streams the file line-by-line, processes it into small chunks of 30 lines, and sends them off sequentially. This keeps the memory footprint incredibly low.
'''


# 2. Which tasks required loading all data?
'''
Strictly speaking, none of the tasks in this specific script required loading all the data. The script is explicitly designed to avoid this. It stops entirely after processing a maximum of 3 chunks (MAX_CHUNKS = 3) >>> see lines...
# 24 >>> CHUNK_SIZE = 30
# 36 >>> def book_chunks(path, chunk_size=30, max_chunks=3):
# 49 >>> if len(chunk) == chunk_size: # part of function on line 36

Even if MAX_CHUNKS were removed, the script would still only load one chunk into memory at any given moment, rather than the whole book.
'''

# 3. Why is a generator with `yield` still an iterator?
'''
A generator function is a subclass of an iterator because it implements Python's iterator protocol under the hood.

When a function contains the yield keyword, calling it doesn't run the code immediately; instead, it returns a generator object. This object automatically has both the __iter__() and __next__() methods. Every time next() is called on it (like during the for chunk_number, chunk_text in enumerate(...) loop >>> in the __main__ function on line 84), it executes the code until it hits the yield statement, pauses and saves its execution state, and returns the value.
'''

# 4. When does `yield` save memory compared with `readlines()`?
'''
yield saves memory when dealing with large datasets or files where you only need to process one piece at a time.

# readlines() reads the entire file into a Python list in your RAM all at once. As noted in the complexity discussion, this consumes O(n x m) space (where n is lines and m is line length). If the book is massive, it can crash your program due to out-of-memory errors.

# yield only keeps the current chunk in memory. As the complexity discussion states, this reduces the space complexity to O(k x m), where k is your small chunk_size (30 lines). Once a chunk is yielded and processed, its memory can be freed up for the next one.
'''


# 5. Why is sending the whole book to Gemini in one prompt a bad 
'''
While modern LLMs like gemini-2.5-flash have massive context windows that can technically hold an entire book, doing so in a single prompt for this task is a bad idea for a few reasons:

# Granularity and Detail: 
# The goal is to get a structured JSON breakdown of specific characters, events, and summaries for individual sections. If you pass the whole book at once, the model is highly likely to drop fine-grained details, skip minor characters, or hallucinate to fit everything into a single, generic response.

# Output Limits:
# Even if an LLM can read a whole book (input context), its output limit is much smaller. It wouldn't have enough output tokens to write a detailed, chunk-by-chunk JSON breakdown for the entire novel in a single go.

# Cost and Latency: 
# Processing a massive prompt takes significantly longer to process and consumes a large number of input tokens, making it inefficient for a structured extraction task.
'''

# +==========+==========+==========+==========+==========+
# JSON produced by script
# +==========+==========+==========+==========+==========+

'''
Chunk 1
{
    "chunk": 1,
    "characters": [
        "M. Charles-François-Bienvenu Myriel",
        "Mademoiselle Baptistine",
        "Madame Magloire",
        "Napoleon",
        "M. le Cardinal Fesch"
    ],
    "events": [
        "M. Myriel's early life as a nobleman's son, marrying young and leading a worldly existence",
        "His emigration to Italy during the French Revolution, where his wife died",
        "His return to France as a priest, serving as Curé of Brignolles",
        "An encounter with Emperor Napoleon in Paris that led to his unexpected appointment as Bishop of Digne",
        "M. Myriel's arrival and installation in Digne with his sister Mademoiselle Baptistine and servant Madame Magloire",
        "The fading of initial rumors about M. Myriel's past in Digne"
    ],
    "summary": "This chunk introduces M. Charles-François-Bienvenu Myriel, the Bishop of Digne, detailing his life story up to 1815. It covers his aristocratic youth, emigration during the Revolution, the death of his wife, and his subsequent mysterious transformation into a priest, which culminated in his surprising appointment as Bishop after an encounter with Napoleon. The narrative also introduces his devoted sister, Mademoiselle Baptistine, and their bustling servant, Madame Magloire, as they settle into Digne.",
    "uncertainty": "The precise reasons for M. Myriel's transformation into a priest after his wife's death are unknown. The truth behind the many rumors circulating about his early life before the Revolution is also stated as unknown. The exact nature of the 'petty affair' that took him to Paris is not precisely known."
}

Chunk 2
{
    "chunk": 2,
    "characters": [
        "M. Myriel",
        "Director of the hospital",
        "Mademoiselle Baptistine",
        "Madame Magloire"
    ],
    "events": [
        "M. Myriel inspects the Digne hospital and his episcopal palace",
        "M. Myriel proposes a building swap to the hospital director",
        "The Bishop and 36 patients swap residences",
        "M. Myriel allocates his substantial salary to various charities, keeping only a small portion",
        "Mademoiselle Baptistine accepts the new arrangement, while Madame Magloire grumbles"
    ],
    "summary": "Upon observing the crowded Digne hospital and his spacious episcopal palace, Bishop Myriel orchestrates a swap, moving the thirty-six patients into his grand residence and relocating himself, his sister, and their servant into the small hospital building. He subsequently reallocates his fifteen thousand franc salary, reserving only one thousand francs for his household's needs and dedicating the rest to various charitable causes. This radical change is accepted with devotion by his sister, Mademoiselle Baptistine, though their servant, Madame Magloire, voices some discontent.",
    "uncertainty": null
}

Chunk 3
{
  "chunk": 3,
  "characters": [
    "M. Myriel (The Bishop/Monseigneur Bienvenu)",
    "Madame Magloire",
    "Mademoiselle Baptistine",
    "Senator of the Empire (unnamed)",
    "M. Bigot de Préameneu",
    "Madame la Comtesse de Lô",
    "M. Géborand",
    "youthful vicar"
  ],
  "events": [
    "Bishop Myriel claims an allowance for his episcopal expenses at Madame Magloire's suggestion.",
    "The General Council approves an annual sum of 3,000 francs for the Bishop.",
    "Local burgesses and a Senator express outrage over the Bishop's allowance.",
    "Bishop Myriel immediately dedicates the entire 3,000 francs to charity, disappointing Madame Magloire.",
    "He becomes a renowned treasurer of benevolence, distributing all funds received to the needy and adopting the nickname 'Monseigneur Bienvenu' from the poor.",
    "The Bishop undertakes extensive pastoral visits throughout his difficult, mountainous diocese, traveling by foot, cart, or donkey.",
    "He offers practical moral lessons and examples of generosity to various communities during his visits.",
    "Bishop Myriel consistently exhibits humility, wit, and wisdom, subtly critiquing vanity and self-interest in his interactions with others."
  ],
  "summary": "Bishop Myriel, prompted by Madame Magloire, claims an allowance for his episcopal duties, which is granted despite public outcry. He immediately designates the entire sum to charity, becoming a beloved figure among the poor who affectionately call him Monseigneur Bienvenu, as he funnels all received funds to the needy. The Bishop continues his arduous pastoral visits across his mountainous diocese, traveling humbly and offering communities practical and moral guidance, consistently demonstrating his wisdom and wit.",
  "uncertainty": []
}
'''