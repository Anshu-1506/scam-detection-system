# create_balanced_data.py
import pandas as pd
import csv

print("=" * 50)
print("📝 Creating Balanced Training Data")
print("=" * 50)

# Create balanced dataset with equal scam and not_scam examples
data = [
    # SCAM EXAMPLES (10 examples)
    ["text", "label"],
    ["Congratulations! You have won a lottery of ₹10,00,000. Click here to claim now", "scam"],
    ["Your bank account will be suspended. Update KYC immediately: http://bit.ly/kyc-update", "scam"],
    ["URGENT: Your parcel contains illegal items. Call immediately to avoid arrest", "scam"],
    ["Get a personal loan in 5 minutes with 0% interest. No paperwork!", "scam"],
    ["You have been selected for a work-from-home job with ₹50,000 monthly salary", "scam"],
    ["Your Aadhaar will be deactivated in 24 hours. Click to verify now", "scam"],
    ["Free iPhone 15! You are our lucky winner. Just pay ₹500 shipping", "scam"],
    ["Your UPI transaction of ₹5000 is pending. Click to complete payment", "scam"],
    ["Fake KYC update required for your SBI bank account. Share details", "scam"],
    ["Dear customer, your account has been compromised. Share OTP to secure", "scam"],
    
    # NOT SCAM EXAMPLES (10 examples) - Regular conversations
    ["Hi, are we still meeting for lunch tomorrow at 3 PM?", "not_scam"],
    ["Thanks for the payment. I received it successfully.", "not_scam"],
    ["Can you send me the project files when you get a chance?", "not_scam"],
    ["Meeting at 3 PM in conference room. Please be on time.", "not_scam"],
    ["Please review the attached document and share your feedback.", "not_scam"],
    ["Your OTP for transaction is 123456. Do not share this with anyone.", "not_scam"],
    ["Your bill payment of ₹1500 is successful. Thank you for using our service.", "not_scam"],
    ["Thank you for your order. It will be delivered tomorrow between 10 AM - 6 PM.", "not_scam"],
    ["Your salary for this month has been credited to your account.", "not_scam"],
    ["Please find the report attached. Let me know if you have any questions.", "not_scam"],
    
    # Additional SCAM examples (5 more)
    ["WINNER! You've been selected for a FREE trip to Goa. Call now to claim!", "scam"],
    ["Your Netflix account is suspended. Update payment: http://netflix-verify.com", "scam"],
    ["Amazon: Your package delivery failed. Reschedule here: http://amzn-delivery.info", "scam"],
    ["SBI Alert: Your debit card has been blocked. Click to unblock now", "scam"],
    ["COVID-19 Compensation: You are eligible for ₹25,000. Apply here", "scam"],
    
    # Additional NOT SCAM examples (5 more)
    ["Can you pick up some groceries on your way home? We need milk and bread.", "not_scam"],
    ["The meeting has been rescheduled to 4 PM. Let me know if that works for you.", "not_scam"],
    ["Happy Birthday! Hope you have a great day!", "not_scam"],
    ["Your Amazon order #12345 has been shipped. Track here: amazon.in/track", "not_scam"],
    ["Please call me when you get this. It's important but not urgent.", "not_scam"]
]

# Write to CSV file
with open('scam_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data[1:])  # Skip the header row we used for display

print(f"✅ Created CSV file with {len(data)-1} examples")
print(f"   Total examples: {len(data)-1}")
print(f"   Scam examples: {sum(1 for row in data[1:] if row[1] == 'scam')}")
print(f"   Safe examples: {sum(1 for row in data[1:] if row[1] == 'not_scam')}")

# Verify the file
print("\n🔍 Verifying CSV file contents:")
df = pd.read_csv('scam_data.csv')
print(f"   Shape: {df.shape}")
print(f"   Columns: {list(df.columns)}")
print(f"   Scam count: {len(df[df['label']=='scam'])}")
print(f"   Safe count: {len(df[df['label']=='not_scam'])}")
print(f"   Unique labels: {df['label'].unique()}")

print("\n📝 First 5 rows:")
print(df.head())

print("\n✅ Data file created successfully!")