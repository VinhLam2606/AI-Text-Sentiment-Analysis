# 🎭 AI Emotion Detector

An intelligent web application that analyzes the sentiment of English sentences and identifies the underlying emotion (e.g., Joy, Sadness, Anger, Fear) with a confidence score.

## 📋 Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## 📖 Introduction
The **AI Emotion Detector** utilizes Natural Language Processing (NLP) to classify text input into specific emotional categories. It provides users with immediate visual feedback, including an emoji representation and a confidence percentage, making it easy to understand the tone of any given text.

## ✨ Features
* **Real-time Analysis:** Instant processing of English text inputs.
* **Visual Feedback:** Dynamic UI changes (colors and emojis) based on the detected emotion.
* **Confidence Score:** Displays how certain the AI is about its prediction (e.g., 99.2%).
* **Bilingual Display:** Shows the emotion label in both Vietnamese and English (e.g., VUI VẺ - JOY).
* **Clean UI/UX:** A minimalist and user-friendly interface.

## 🛠 Tech Stack
* **Frontend:** HTML5, CSS3, JavaScript (Vanilla or Framework)
* **Backend:** Python (Flask/FastAPI) *[OR Node.js/Express]*
* **AI Model:** TensorFlow / PyTorch / Hugging Face Transformers
* **Data Format:** JSON for API communication
## 🧠 Model Training
You have two options: use the pre-trained model provided or train your own using the dataset.

Option 1: Download Pre-trained Model (Recommended)
If you want to run the app immediately without training: 👉 Download Pre-trained Model https://drive.google.com/drive/folders/1luRlKYdXynH6oJEhKIbPerOoU9kJ7EgR

Important: Download all files from this link and place them inside a folder named six_emotion_model in the project root.

Option 2: Train Your Own Model
If you wish to retrain the model or see how the dataset was processed:

Download Dataset: Link to Dataset on Google Drive https://drive.google.com/drive/folders/132yBWyXlyF81StfICkg-5r2nAmBp352j

Train on Google Colab: Open Training Notebook https://colab.research.google.com/drive/1ruboCaEOEef8M63P9BxUM3cxFGmbOEn3#scrollTo=h4tpiW2kxgAh
## 🚀 Installation
📊 Model PerformanceThe model was trained over 5 epochs. 
| Epoch | Training Loss | Validation Loss | Accuracy | F1 Score | Precision | Recall |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | 0.254200 | 0.196778 | 92.44% | 0.9252 | 0.9267 | 0.9244 |
| 2 | 0.143900 | 0.159733 | 93.31% | 0.9341 | 0.9398 | 0.9331 |
| 3 | 0.099800 | 0.152716 | 93.56% | 0.9360 | 0.9379 | 0.9356 |
| 4 | 0.075300 | 0.146098 | 93.81% | 0.9381 | 0.9386 | 0.9381 |
| 5 | 0.049200 | 0.147719 | 93.88% | 0.9391 | 0.9398 | 0.9388 |

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/ai-emotion-detector.git](https://github.com/your-username/ai-emotion-detector.git)
    cd ai-emotion-detector
    ```

2.  **Install Backend Dependencies:**
    ```bash
    # Example for Python
    pip install -r requirements.txt
    ```

3.  **Run the Application:**
    ```bash
    # Example for Flask
    python app.py
    ```

4.  **Access the App:**
    Open your browser and navigate to `http://127.0.0.1:5000` (or your specific port).

## 💡 Usage
1.  Enter an English sentence into the text area (e.g., *"Today I feel so good"*).
2.  Click the **"Analyze Now"** button.
3.  View the result card which displays the detected emotion, a matching emoji, and the confidence score.

## 📂 Project Structure

```text
ai-emotion-detector/
├── templates/              # HTML templates
│   └── index.html
├── app.py                  # Main backend application file
├── model/                  # AI/ML Model files
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
