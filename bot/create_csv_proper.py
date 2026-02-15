# create_csv_proper.py
import pandas as pd
import csv

print("=" * 50)
print("📝 Creating Properly Formatted CSV")
print("=" * 50)

# Create the data as a list of dictionaries (easier to manage)
data = [
    # SCAM EXAMPLES (15 examples)
    {"text": "Congratulations! You have won a lottery of ₹10,00,000. Click here to claim now", "label": "scam"},
    {"text": "Your bank account will be suspended. Update KYC immediately: http://bit.ly/kyc-update", "label": "scam"},
    {"text": "URGENT: Your parcel contains illegal items. Call immediately to avoid arrest", "label": "scam"},
    {"text": "Get a personal loan in 5 minutes with 0% interest. No paperwork!", "label": "scam"},
    {"text": "You have been selected for a work-from-home job with ₹50,000 monthly salary", "label": "scam"},
    {"text": "Your Aadhaar will be deactivated in 24 hours. Click to verify now", "label": "scam"},
    {"text": "Free iPhone 15! You are our lucky winner. Just pay ₹500 shipping", "label": "scam"},
    {"text": "Your UPI transaction of ₹5000 is pending. Click to complete payment", "label": "scam"},
    {"text": "Fake KYC update required for your SBI bank account. Share details", "label": "scam"},
    {"text": "Dear customer, your account has been compromised. Share OTP to secure", "label": "scam"},
    {"text": "WINNER! You've been selected for a FREE trip to Goa. Call now to claim!", "label": "scam"},
    {"text": "Your Netflix account is suspended. Update payment: http://netflix-verify.com", "label": "scam"},
    {"text": "Amazon: Your package delivery failed. Reschedule here: http://amzn-delivery.info", "label": "scam"},
    {"text": "SBI Alert: Your debit card has been blocked. Click to unblock now", "label": "scam"},
    {"text": "COVID-19 Compensation: You are eligible for ₹25,000. Apply here", "label": "scam"},
    
    # NOT SCAM EXAMPLES (15 examples)
    {"text": "Hi, are we still meeting for lunch tomorrow at 3 PM?", "label": "not_scam"},
    {"text": "Thanks for the payment. I received it successfully.", "label": "not_scam"},
    {"text": "Can you send me the project files when you get a chance?", "label": "not_scam"},
    {"text": "Meeting at 3 PM in conference room. Please be on time.", "label": "not_scam"},
    {"text": "Please review the attached document and share your feedback.", "label": "not_scam"},
    {"text": "Your OTP for transaction is 123456. Do not share this with anyone.", "label": "not_scam"},
    {"text": "Your bill payment of ₹1500 is successful. Thank you for using our service.", "label": "not_scam"},
    {"text": "Thank you for your order. It will be delivered tomorrow between 10 AM - 6 PM.", "label": "not_scam"},
    {"text": "Your salary for this month has been credited to your account.", "label": "not_scam"},
    {"text": "Please find the report attached. Let me know if you have any questions.", "label": "not_scam"},
    {"text": "Can you pick up some groceries on your way home? We need milk and bread.", "label": "not_scam"},
    {"text": "The meeting has been rescheduled to 4 PM. Let me know if that works for you.", "label": "not_scam"},
    {"text": "Happy Birthday! Hope you have a great day!", "label": "not_scam"},
    {"text": "Your Amazon order #12345 has been shipped. Track here: amazon.in/track", "label": "not_scam"},
    {"text": "Please call me when you get this. It's important but not urgent.", "label": "not_scam"}
]

# Convert to DataFrame
df = pd.DataFrame(data)

print(f"✅ Created DataFrame with {len(df)} examples")
print(f"   Scam examples: {len(df[df['label'] == 'scam'])}")
print(f"   Safe examples: {len(df[df['label'] == 'not_scam'])}")

# Save to CSV properly
df.to_csv('scam_data.csv', index=False, encoding='utf-8')
print("✅ Saved to scam_data.csv")

# Verify the file was saved correctly
print("\n🔍 Verifying CSV file:")
df_check = pd.read_csv('scam_data.csv')
print(f"   Shape: {df_check.shape}")
print(f"   Columns: {list(df_check.columns)}")
print(f"   First 3 rows:")
print(df_check.head(3))
print(f"\n   Label distribution:")
print(df_check['label'].value_counts())