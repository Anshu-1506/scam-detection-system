# train_final.py
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib
import os

print("=" * 60)
print("🚀 FINAL VERSION - Scam Detection Model Training")
print("=" * 60)

# Step 1: Check if file exists
if not os.path.exists('scam_data.csv'):
    print("❌ ERROR: scam_data.csv not found!")
    exit()

# Step 2: Read the CSV file
print("\n📂 Reading CSV file...")
try:
    df = pd.read_csv('scam_data.csv', encoding='utf-8')
    print(f"✅ Successfully read {len(df)} rows")
    print(f"📊 Columns: {list(df.columns)}")
except Exception as e:
    print(f"❌ Error reading CSV: {e}")
    exit()

# Step 3: Display data info
print("\n📊 Data Overview:")
print(f"   First 5 rows:")
print(df.head())
print(f"\n   Data types:")
print(df.dtypes)
print(f"\n   Label distribution:")
print(df['label'].value_counts())

# Step 4: Prepare features and labels
X = df['text'].values  # Features (the messages)
y = df['label'].values  # Labels (scam/not_scam)

print(f"\n📊 Training set size: {len(X)} examples")

# Step 5: Create and train model
print("\n🛠️ Creating TF-IDF Vectorizer and Naive Bayes model...")

# Create a pipeline
model = Pipeline([
    ('tfidf', TfidfVectorizer(
        max_features=5000,
        lowercase=True,
        stop_words='english'
    )),
    ('classifier', MultinomialNB())
])

# Train the model
print("🎓 Training model...")
model.fit(X, y)
print("✅ Model training complete!")

# Step 6: Test the model
print("\n🧪 Testing model on examples:")
test_messages = [
    "You won a lottery! Click here to claim your prize",
    "Meeting scheduled for tomorrow at 3 PM",
    "URGENT: Your KYC needs update, click link now",
    "Thanks for sending the project files",
    "Free iPhone giveaway! Just pay shipping",
    "Can we reschedule our lunch meeting?"
]

for msg in test_messages:
    pred = model.predict([msg])[0]
    proba = model.predict_proba([msg])[0]
    confidence = max(proba) * 100
    
    if pred == 'scam':
        print(f"   ⚠️  '{msg[:30]}...' -> SCAM (confidence: {confidence:.1f}%)")
    else:
        print(f"   ✅ '{msg[:30]}...' -> SAFE (confidence: {confidence:.1f}%)")

# Step 7: Save the model
print("\n💾 Saving model...")
joblib.dump(model, 'scam_detector_model.joblib')
print("✅ Model saved as 'scam_detector_model.joblib'")

# Step 8: Also save the vectorizer separately (optional)
vectorizer = model.named_steps['tfidf']
joblib.dump(vectorizer, 'vectorizer.joblib')
print("✅ Vectorizer saved as 'vectorizer.joblib'")

print("\n" + "=" * 60)
print("🎉 SUCCESS! Model is ready to use!")
print("=" * 60)

# Step 9: Quick test with your own message
print("\n📝 Quick Test:")
test_msg = input("Enter a message to test (or press Enter to skip): ")
if test_msg:
    pred = model.predict([test_msg])[0]
    proba = model.predict_proba([test_msg])[0]
    confidence = max(proba) * 100
    print(f"\nResult: {pred.upper()} (confidence: {confidence:.1f}%)")