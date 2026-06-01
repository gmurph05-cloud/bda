### Session 3 | Part 3
# +==========+==========+==========+==========+==========+
# In Part 3, you will run the most basic version of RAG over *Les Misérables*.
'''
In this tutorial, we will:

1. read *Les Misérables* line by line,
2. retrieve a few lines that look relevant,
3. place those lines inside the prompt,
4. ask Gemini to answer using that context.

This is not a full search engine It is the smallest useful version of the idea.
'''

#### 3. Connect to iterators
# +==========+==========+==========+==========+==========+
# Before Gemini, remember that a file object is already an iterator.
TEXT_FILE = "data/les_miserables.txt"
with open(TEXT_FILE, "r", encoding="utf-8") as file:
    # This reads only the first two lines. It does not load the whole book into memory.
    first_line = next(file)
    second_line = next(file)

print(first_line)
print(second_line)


#### 4. Connect to `yield`
# +==========+==========+==========+==========+==========+
# `yield` lets us create our own iterator.
print('''\n
#### 4. Connect to `yield`
# +==========+==========+==========+==========+==========+
# `yield` lets us create our own iterator.
''')
def non_empty_lines(path):
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line != "":
                yield line


for line in non_empty_lines(TEXT_FILE):
    print(line)
    break
'''
This generator is useful because it hides the file-reading details. The rest of the program can simply ask for the next useful line.

For RAG, this matters because we often do not want the whole document. We want a small useful chunk.
'''


#### 5. Tiny RAG demo
# +==========+==========+==========+==========+==========+

import os

from google import genai


TEXT_FILE = "data/les_miserables.txt"
QUESTION = "Who is Bishop Myriel?"
KEYWORDS = ["bishop", "myriel", "digne"]
MAX_LINES = 8

# QUESTION = "Who is Fantine?"
# KEYWORDS = ["fantine"]

def useful_lines(path):
    """Yield non-empty lines from a text file."""
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line != "":
                yield line

def retrieve_context(path, keywords, max_lines):
    """Find a small chunk of text that matches the question."""
    matches = []
    extra_lines = 0

    for line in useful_lines(path):
        line_lower = line.lower()

        if any(keyword in line_lower for keyword in keywords):
            matches.append(line)
            # Keep two lines after a match so Gemini has a little context.
            extra_lines = 2
        elif extra_lines > 0:
            matches.append(line)
            extra_lines -= 1

        if len(matches) >= max_lines:
            break

    return "\n".join(matches)

context = retrieve_context(TEXT_FILE, KEYWORDS, MAX_LINES)

# Send only the retrieved context to Gemini.
prompt = f"""Use only this context to answer the question.

Question:
{QUESTION}

Context:
{context}
"""

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt,
)

print(response.text)

#### 6. What is happening?
# +==========+==========+==========+==========+==========+
""" This is RAG in its simplest form:

1. `useful_lines()` streams the book and yields one non-empty line at a time.
2. `retrieve_context()` keeps lines that mention `bishop`, `myriel`, or `digne`.
3. It also keeps a couple of lines after each match for context.
4. The retrieved text becomes the context in the prompt.
5. Gemini answers using that context.

The generator keeps the reading logic small and reusable. It also means the program can stop once it has enough context. """

#### 7. Why not load the whole book?
# +==========+==========+==========+==========+==========+
""" with open("les_miserables.txt", "r", encoding="utf-8") as file:
    text = file.read() """

# That loads the whole file into memory. Sometimes that is fine, but it is not the habit we want for large files.
# For this task, streaming is enough:
# This can stop as soon as it finds useful text.
""" for line in useful_lines("les_miserables.txt"):
    if "myriel" in line.lower():
        print(line)
        break """

#### 8. Exercise
# +==========+==========+==========+==========+==========+

# 1. Which lines were retrieved?
# QUESTION = "Who is Bishop Myriel?"
# KEYWORDS = ["bishop", "myriel", "digne"]
'''
Les Misérables
M. Charles-François-Bienvenu Myriel was the Bishop of Digne in 1815. He was an old man of about seventy-five years of age and had occupied the see of Digne since 1806. He was formerly the Curé of Brignolles in 1804 and before that, returned from Italy as a priest. He was the son of a councillor of the Parliament of Aix.
'''

# QUESTION = "Who is Fantine?"
# KEYWORDS = ["fantine"]
""" 
Les Misérables
Fantine is one of four "ravishing young women," who is the mistress of Félix Tholomyès. She is called "the Blonde" because of her beautiful, sunny hair. She is described as being "still in her first illusions" and is characterized as a "good girl," in contrast to her companions Favorite, Dahlia, and Zéphine, who are more experienced and "philosophical." She is also depicted as being "still a little like working-women" and retaining "something of the serenity of toil" and "that flower of honesty."
"""

# 2. Did Gemini have enough context?
# Yes


# 3. What would improve this tiny RAG system?

#### 9. Small improvement exercise
# +==========+==========+==========+==========+==========+
# 1. In your own words, what is RAG?
'''
RAG (Retrieval-Augmented Generation) system looks through an external database or file system to find facts relevant to a user's question, attaches those facts to the prompt, and hands them to the AI to write a grounded, accurate answer. It does not only rely on the training data within the Large Language Model
'''

#2. What is the context window? Why can we not always send a whole book, website, or dataset to an LLM?
'''
The context window is the maximum amount of text (measured in tokens) that an LLM can read and process in a single interaction. Different LLMs have different maximums which may or may not be able to handle a full novel like War and Peace. 

Cost and Speed are factors too. We are fast moving to a token economy where we py for every token sent. It is costly to process words that are not needed. Larger prompts also mean slower response times.
'''

#3. How do iterators and `yield` help us build the context gradually instead of loading everything at once?
'''
When a student wants to search through 50 lecture transcripts for "What did we say about dynamic programming?", loading all 50 massive files into computer memory at once could easily freeze or crash the program.
yield reads the transcripts one line at a time, checking it for keywords, handing it off if it matches, and immediately throwing it out of memory before moving to the next line. This keeps memory usage incredibly low and allows the system to build a compact context chunk-by-chunk.
'''

# 4. What is one trade-off between sending more context and sending less context to Gemini?
'''
Less context:
cheap and fast, but you risk missing useful evidence—like the actual definition or code example explained in the next three sentences—resulting in a low-quality, incomplete answer.

More context:
Using all transcript text could introduce massive noise, make the prompt highly expensive in terms of token costs, and risk the model losing focus on the specific concept the student actually asked about.
'''