# ATELIER 2 
## This repository contains code for two distinct parts:

### Part 1: Text Processing and Bill Generation
In this part, a Python script is provided to generate a bill from a given text input provided by the user. The script utilizes regular expressions (Regex) to extract relevant information such as product names, quantities, and prices from the text. It then formats this information into a structured bill table. Here's a summary of the key functionalities:

Clean Text Function: Removes stop words and extra whitespaces from input text.
Generate Bill Function: Extracts item names, quantities, and prices from the cleaned text and generates a bill table with product details and total prices.


### Part 2: Word Embedding
This part focuses on applying various word embedding techniques to a dataset collected during a lab session.

1. **One Hot Encoding, Bag of Words, TF-IDF:**
   - One hot encoding, bag of words, and TF-IDF techniques are applied to the dataset to represent text documents as numerical vectors.

2. **Word2Vec Approach:**
   - Both Skip Gram and Continuous Bag of Words (CBOW) models are implemented using Word2Vec to learn word embeddings from the dataset.

3. **GloVe and FastText Approaches:**
   - GloVe (Global Vectors for Word Representation) and FastText models are employed to generate word embeddings based on the dataset.

4. **Visualization and Evaluation:**
   - All encoded/vectorized vectors are plotted using the t-SNE algorithm for visualization in 3D space. This visualization aids in evaluating the effectiveness of each approach and drawing general conclusions.

Each part is elaborated with detailed code snippets and explanations to facilitate understanding and implementation.

