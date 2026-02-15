@"
# 🛡️ AI-Powered Scam Detection System

## 📋 Overview
An intelligent scam detection system that uses Machine Learning to identify fraudulent messages, SMS, and WhatsApp texts. Includes an awareness website with quizzes and educational content.

## 🎯 Features

### 🤖 AI Dashboard (Port 5000)
- Real-time scam detection using ML
- 15+ scam pattern recognition
- Risk scoring (0-100%)
- Severity levels (Critical/High/Medium/Low)
- Detailed explanations for each detection
- Actionable recommendations

### 🌐 Awareness Website (Port 5500)
- Interactive quiz about scams
- Educational videos
- Anonymous story sharing
- Safety tips and resources

## 🏗️ Architecture

\`\`\`
scam-detection-system/
├── ai-dashboard/          # ML-powered detection interface
│   ├── app.py            # Flask backend
│   ├── detect_scam.py    # Detection logic
│   ├── templates/        # HTML templates
│   └── scam_detector_model.joblib  # Trained model
├── website/              # Awareness website
│   ├── index.html        # Homepage
│   ├── quiz.html         # Interactive quiz
│   ├── learn.html        # Video tutorials
│   └── story.html        # Community stories
└── bot/                  # Archived WhatsApp bot
\`\`\`

## 🛠️ Tech Stack

- **Machine Learning**: scikit-learn (Naive Bayes + TF-IDF)
- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Data**: 30 curated scam/safe examples

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip package manager

### Installation

1. **Clone the repository**
\`\`\`bash
git clone https://github.com/Anshu-1506/scam-detection-system.git
cd scam-detection-system
\`\`\`

2. **Set up AI Dashboard**
\`\`\`bash
cd ai-dashboard
pip install -r requirements.txt
python app.py
\`\`\`

3. **Start Website**
\`\`\`bash
cd ../website
python -m http.server 5500
\`\`\`

4. **Access the applications**
- Dashboard: http://localhost:5000
- Website: http://localhost:5500

## 📊 How It Works

1. **Message Input**: User enters suspicious message
2. **ML Analysis**: Model predicts scam probability
3. **Pattern Matching**: 15+ scam patterns checked
4. **Risk Calculation**: Weighted scoring system
5. **Recommendations**: Actionable safety tips

## 🧪 Sample Test Messages

### Scam Messages:
\`\`\`
"Congratulations! You won a lottery of ₹10,00,000. Click here to claim"
"URGENT: Your bank account will be suspended. Update KYC immediately"
"Work from home job! Earn ₹50,000 monthly. No experience needed"
\`\`\`

### Safe Messages:
\`\`\`
"Hi, are we meeting for lunch tomorrow at 3 PM?"
"Thanks for the payment, I received it successfully"
"Meeting at 3 PM in conference room"
\`\`\`

## 📁 Project Structure

\`\`\`
scam-detection-system/
├── 📂 ai-dashboard/
│   ├── 📄 app.py                 # Flask server
│   ├── 📄 detect_scam.py         # Detection engine
│   ├── 📄 requirements.txt       # Dependencies
│   ├── 📄 scam_detector_model.joblib # ML model
│   └── 📂 templates/
│       └── 📄 dashboard.html      # UI
├── 📂 website/
│   ├── 📄 index.html              # Homepage
│   ├── 📄 quiz.html               # Quiz
│   ├── 📄 learn.html              # Videos
│   ├── 📄 story.html              # Stories
│   └── 📄 style.css               # Styling
└── 📂 bot/                        # Archived
    ├── 📄 train_model.py           # Training script
    └── 📄 scam_data.csv             # Training data
\`\`\`

## 👨‍💻 Author

**Anshu** 

## 📝 License

This project is licensed under the MIT License.

## 📞 Contact

- Project Link: [https://github.com/Anshu-1506/scam-detection-system](https://github.com/Anshu-1506/scam-detection-system)
"@ | Out-File -FilePath README.md -Encoding utf8