from sentence_transformers import SentenceTransformer
import nltk

# Download tokenizer data (first time only)
nltk.download('punkt_tab')
from nltk.tokenize import sent_tokenize

# Load the pretrained model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Your raw text (could be a news article, interview, etc)
raw_text = """
Protesters gathered in the capital on Monday.
Police were deployed to maintain order.
Several arrests were reported by independent journalists.
"""

# Split into sentences
sentences = sent_tokenize(raw_text)

# Encode each sentence
embeddings = model.encode(sentences)

# Print embeddings (vectors)
for sentence, embedding in zip(sentences, embeddings):
    print("Sentence:", sentence)
    print("Embedding (first 5 dims):", embedding[:5])