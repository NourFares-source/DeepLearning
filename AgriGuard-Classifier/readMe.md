🌿 AgriGuard: Professional Crop Disease Classifier
📌 Project Overview
AgriGuard is an end-to-end computer vision pipeline designed to identify botanical species and potential diseases from 
smartphone-captured images. This project demonstrates an industry-standard approach to Transfer Learning, handling small/noisy 
datasets, and building high-performance data pipelines.

Core Technology: TensorFlow / Keras

Architecture: MobileNetV2 (Pre-trained on ImageNet)

Key Achievement: 88%+ Validation Accuracy with robust protection against overfitting.

🛠️ The "Industry-Standard" Pipeline
This project solves three major real-world AI challenges using a modular assembly line:

1. The tf.data Performance Bridge
To prevent CPU bottlenecks, I implemented a prefetch and AUTOTUNE strategy. This allows the GPU to train on one batch
 while the CPU simultaneously prepares the next.

3. Anti-Overfitting Suite (Data Augmentation)
Real-world farm photos aren't perfect. I built a preprocessing layer that applies:

Random Flips & Rotations: To simulate different camera angles.

Random Zoom: To handle varying distances from the leaf.

Strict Split: Augmentation is applied only to the training set to prevent data leakage.

3. Transfer Learning Logic
Instead of training from scratch, I utilized MobileNetV2. I froze the "Expert" weights and attached a custom classification
 head, allowing the model to leverage complex feature detection with minimal compute resources.

📊 Results & Evaluation
The model was evaluated using a Confusion Matrix to ensure reliability across all classes.

Training Accuracy: ~88%

Validation Accuracy: ~88%

Observation: The close proximity between training and validation scores proves the effectiveness of the augmentation pipeline in generalizing to unseen data.
