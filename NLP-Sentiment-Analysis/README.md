Goal: Classify the emotional tone of movie reviews into Positive or Negative categories.

Architecture: Designed a custom NLP pipeline using a 10,000-word Embedding Layer and GlobalAveragePooling1D to condense sequence data into sentiment "vibes."

Performance: Achieved ~85-88% accuracy on the IMDb test set, a strong baseline for non-transformer models.

Key Learnings: Mastered the concept of "Text to Numbers" (Tokenization), handling variable review lengths (Padding), and the fundamental difference between simple pooling and complex attention-based models like BERT.

