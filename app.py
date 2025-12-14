from flask import Flask, render_template, request
from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification
import torch
import torch.nn.functional as F

app = Flask(__name__)

MODEL_PATH = "./six_emotion_model"

print("Đang tải model 6 cảm xúc... Vui lòng đợi.")
tokenizer = DistilBertTokenizerFast.from_pretrained(MODEL_PATH)
model = DistilBertForSequenceClassification.from_pretrained(MODEL_PATH)
print("Model đã sẵn sàng!")

EMOTION_MAP = {
    0: {"label": "BUỒN (Sadness)", "icon": "😢", "color": "#3498db"}, # Blue
    1: {"label": "VUI VẺ (Joy)", "icon": "😂", "color": "#f1c40f"},   # Yellow
    2: {"label": "YÊU THƯƠNG (Love)", "icon": "❤️", "color": "#e74c3c"}, # Red
    3: {"label": "GIẬN DỮ (Anger)", "icon": "😡", "color": "#d35400"},  # Orange
    4: {"label": "SỢ HÃI (Fear)", "icon": "😱", "color": "#8e44ad"},    # Purple
    5: {"label": "BẤT NGỜ (Surprise)", "icon": "😲", "color": "#2ecc71"} # Green
}

def predict_emotion(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=128)
    
    with torch.no_grad():
        outputs = model(**inputs)
    
    probs = F.softmax(outputs.logits, dim=-1)
    
    pred_idx = torch.argmax(probs, dim=-1).item()
    confidence = probs[0][pred_idx].item()
    
    return EMOTION_MAP[pred_idx], confidence

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    score = None
    text_input = ""
    
    if request.method == 'POST':
        text_input = request.form['text_input']
        if text_input.strip():
            emotion_info, confidence = predict_emotion(text_input)
            result = emotion_info
            score = f"{confidence*100:.1f}%"
            
    return render_template('index.html', result=result, score=score, text_input=text_input)

if __name__ == '__main__':
    app.run(debug=True, port=5000)