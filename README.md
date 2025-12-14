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

## 🚀 Installation

Follow these steps to set up the project locally:

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
