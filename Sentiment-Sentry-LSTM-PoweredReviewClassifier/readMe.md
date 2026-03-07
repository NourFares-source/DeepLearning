🛡️ Sentiment-Sentry: LSTM-Powered Review Classifier
📌 Project Overview
Sentiment-Sentry is an advanced Natural Language Processing (NLP) system designed to decode the emotional context of textual
data. Unlike simple keyword-matching algorithms, this model utilizes Recurrent Neural Networks (RNNs) to understand word
order and long-term dependencies in human speech.

Core Technology: TensorFlow / Keras

Architecture: LSTM (Long Short-Term Memory) with Word Embeddings

Dataset: IMDb Movie Reviews (Binary Sentiment)

Key Achievement: Successfully reached ~85% Validation Accuracy, with a detailed analysis of model generalization and 
overfitting.

🏗️ Technical Architecture & Pipeline
This project implements a sophisticated "Sequence-to-Sentiment" pipeline:

1. The Integer Vectorization Bridge
Standard text cannot be processed by a GPU. I utilized a mapping system where each unique word is assigned a specific
 integer ID, restricted to the top 10,000 most frequent terms to reduce noise.

3. Word Embeddings (The "Vibe" Map)
Instead of treating words as isolated units, I used an Embedding Layer. This projects each word into a 128-dimensional space
where words with similar meanings (e.g., "breathtaking" and "stunning") are mathematically closer together.

4. The LSTM "Memory" Layer
The heart of the project is a 64-unit LSTM.

Sequential Awareness: It processes the review word-by-word, maintaining a "hidden state" that remembers the context of 
previous words.

Contextual Logic: This allows the model to understand that "The movie was not great" is negative, even though it contains
the word "great."

🔍 Performance Analysis (The "Engineer's Insight")
During the training phase, the model exhibited a classic Overfitting pattern after Epoch 3:

Training Accuracy: Continued to climb to 93%.

Validation Accuracy: Plateaued at ~85%.

Analysis: The divergence between training and validation loss indicates the model began "memorizing" specific training 
samples rather than learning general linguistic patterns.

🛠️ Industry-Level Solutions Implemented:
To combat this, I integrated several "Regularization" techniques used in production environments:

Dropout (50%): Randomly deactivating neurons to prevent reliance on specific word-triggers.

Recurrent Dropout: Applying dropout to the LSTM's internal memory gates to ensure robust feature extraction.
