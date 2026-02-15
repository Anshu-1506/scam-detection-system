# train_model.py
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os
import sys

def check_data_file():
    """Check if data file exists and has content"""
    if not os.path.exists('scam_data.csv'):
        print("❌ ERROR: scam_data.csv not found!")
        print("Please create the file first.")
        return False
    
    # Check if file is empty
    if os.path.getsize('scam_data.csv') == 0:
        print("❌ ERROR: scam_data.csv is empty!")
        return False
    
    return True

def load_and_clean_data():
    """Load and clean the training data"""
    try:
        # Load data with explicit encoding
        df = pd.read_csv('scam_data.csv', encoding='utf-8')
        
        # Remove any rows with NaN values
        initial_rows = len(df)
        df = df.dropna()
        
        if len(df) < initial_rows:
            print(f"⚠️  Removed {initial_rows - len(df)} rows with missing values")
        
        # Remove any empty strings
        df = df[df['text'].str.strip() != '']
        
        # Convert labels to strings and strip whitespace
        df['label'] = df['label'].str.strip().str.lower()
        
        # Verify we have both classes
        unique_labels = df['label'].unique()
        print(f"📊 Classes found: {unique_labels}")
        
        if 'scam' not in unique_labels or 'not_scam' not in unique_labels:
            print("❌ ERROR: Need both 'scam' and 'not_scam' classes in data!")
            return None
        
        return df
        
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        return None

def train_model():
    """Main training function"""
    print("=" * 50)
    print("🚀 Scam Detection Model Training")
    print("=" * 50)
    
    # Check if data file exists
    if not check_data_file():
        return False
    
    # Load and clean data
    print("\n📂 Loading training data...")
    df = load_and_clean_data()
    
    if df is None:
        return False
    
    print(f"✅ Loaded {len(df)} training examples")
    print(f"   Scam messages: {len(df[df['label']=='scam'])}")
    print(f"   Safe messages: {len(df[df['label']=='not_scam'])}")
    
    # Show sample of data
    print("\n📝 Sample data:")
    print(df.head(3))
    
    # Prepare features and labels
    X = df['text'].values
    y = df['label'].values
    
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    print(f"\n📊 Training set size: {len(X_train)} examples")
    print(f"📊 Testing set size: {len(X_test)} examples")
    
    # Create pipeline
    print("\n🛠️ Building AI model pipeline...")
    model_pipeline = Pipeline([
        ('vectorizer', TfidfVectorizer(
            max_features=5000,
            lowercase=True,
            stop_words='english',
            ngram_range=(1, 2)  # Consider pairs of words too
        )),
        ('classifier', MultinomialNB(alpha=1.0))  # Add smoothing parameter
    ])
    
    # Train model
    print("🎓 Training model...")
    model_pipeline.fit(X_train, y_train)
    print("✅ Model training complete!")
    
    # Evaluate model
    print("\n📈 Evaluating model performance...")
    y_pred = model_pipeline.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"🎯 Accuracy: {accuracy:.2%}")
    
    print("\n📋 Detailed Classification Report:")
    print(classification_report(y_test, y_pred))
    
    # Test with examples
    print("\n🧪 Testing model on sample messages:")
    test_messages = [
        "You won a lottery! Click here to claim ₹10 lakhs",
        "Meeting at 3 PM tomorrow in conference room",
        "URGENT: Your KYC needs update, click link now",
        "Thanks for sending the project files"
    ]
    
    for msg in test_messages:
        prediction = model_pipeline.predict([msg])[0]
        proba = model_pipeline.predict_proba([msg])[0]
        confidence = max(proba) * 100
        
        if prediction == 'scam':
            print(f"   ⚠️  '{msg[:30]}...' -> SCAM (confidence: {confidence:.1f}%)")
        else:
            print(f"   ✅ '{msg[:30]}...' -> SAFE (confidence: {confidence:.1f}%)")
    
    # Save model
    print("\n💾 Saving model to disk...")
    joblib.dump(model_pipeline, 'scam_detector_model.joblib')
    print("✅ Model saved as 'scam_detector_model.joblib'")
    
    # Save vectorizer separately for reference
    vectorizer = model_pipeline.named_steps['vectorizer']
    joblib.dump(vectorizer, 'vectorizer.joblib')
    print("✅ Vectorizer saved as 'vectorizer.joblib'")
    
    print("\n" + "=" * 50)
    print("🎉 Training complete! Your AI model is ready.")
    print("=" * 50)
    
    return True

if __name__ == "__main__":
    success = train_model()
    if not success:
        print("\n❌ Training failed. Please fix the issues and try again.")
        sys.exit(1)