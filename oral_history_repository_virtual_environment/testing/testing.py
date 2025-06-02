from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import nltk

# Download tokenizer data (first time only)
# nltk.download('punkt')
from nltk.tokenize import sent_tokenize

# Load the pretrained model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Raw text
raw_text = """
Protesters gathered in the capital on Monday.
Police were deployed to maintain order.
Several arrests were reported by independent journalists.
Genocide conducted in Rwanda.
"""

# Sentence splitting
sentences = sent_tokenize(raw_text)

# Encode sentences
embeddings = model.encode(sentences)

# Test query — pass directly as string, not list
test_sentence = "mass killing"
test_sentence_encoding = model.encode(test_sentence)

# Loop over corpus sentences
for corpus_sentence, corpus_embedding in zip(sentences, embeddings):
    print("original sentence:", corpus_sentence)
    similarity = cosine_similarity([corpus_embedding], [test_sentence_encoding])
    print("cosine similarity:", similarity[0][0])

