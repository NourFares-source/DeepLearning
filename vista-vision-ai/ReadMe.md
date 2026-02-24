# Intel Scenery Classification using CNN

A Deep Learning project that classifies natural and urban landscapes into six categories: **Buildings, Forest, Glacier, Mountain, Sea, and Street.** This model was built using TensorFlow/Keras and optimized with high-performance data pipelines.

## 🚀 Performance
- **Validation Accuracy:** ~80%
- **Training Epochs:** 10
- **Model Type:** Custom Convolutional Neural Network (CNN)

## 🛠️ Key Features
* **High-Performance Pipeline:** Utilized `tf.data` with `.cache()` and `.prefetch()` to eliminate CPU/GPU bottlenecks.
* **Efficient Training:** Integrated with Google Colab's T4 GPU for accelerated training times.
* **Scalable Architecture:** Designed with a modular CNN approach suitable for multi-class image recognition.

## 📂 Project Structure
* `notebooks/`: Contains the Google Colab `.ipynb` file with the training logic.
* `models/`: The final saved model (`final_model.keras`).
* `data/`: (Instructions for downloading the Kaggle Intel Scenery dataset).

## 📊 Training Results
The model showed a strong initial learning curve, reaching over 70% accuracy in the first epoch. By epoch 10, the model achieved a solid baseline of 80% validation accuracy.



## 🔧 Future Improvements (v2.0)
- [ ] **Data Augmentation:** Implement `RandomFlip` and `RandomRotation` to reduce overfitting.
- [ ] **Transfer Learning:** Fine-tune a pre-trained `MobileNetV2` or `ResNet50` for higher precision.
- [ ] **Deployment:** Create a web interface using Streamlit or Gradio.

## 🧑‍💻 How to Run
1. Clone this repository.
2. Install dependencies: `pip install tensorflow numpy matplotlib`.
3. Load the model:
   ```python
   import tensorflow as tf
   model = tf.keras.models.load_model('models/final_model.keras')
