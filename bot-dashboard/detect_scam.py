# detect_scam.py - Enhanced for Dashboard
import joblib
import re
from datetime import datetime

class ScamDetector:
    def __init__(self, model_path='scam_detector_model.joblib'):
        """Initialize the scam detector"""
        self.model_path = model_path
        self.model = None
        self.load_model()
        
        # Enhanced scam patterns with explanations
        self.scam_patterns = {
            'lottery_winning': {
                'patterns': [r'won', r'winner', r'lottery', r'prize', r'congratulation'],
                'explanation': 'Claims you won something - common lottery scam',
                'severity': 'high',
                'category': 'financial'
            },
            'kyc_update': {
                'patterns': [r'kyc', r'update.*account', r'verify.*account', r'aadhaar', r'pan'],
                'explanation': 'Asking for KYC/personal documents - bank impersonation scam',
                'severity': 'critical',
                'category': 'identity'
            },
            'account_suspension': {
                'patterns': [r'suspended', r'blocked', r'deactivated', r'closed'],
                'explanation': 'Threatening to suspend account to create panic',
                'severity': 'high',
                'category': 'threat'
            },
            'otp_request': {
                'patterns': [r'otp', r'one time password', r'share.*otp', r'verify.*otp'],
                'explanation': 'Requesting OTP - legitimate companies NEVER ask for OTP',
                'severity': 'critical',
                'category': 'security'
            },
            'suspicious_link': {
                'patterns': [r'click here', r'bit\.ly', r'tinyurl', r'http', r'www', r'\.com'],
                'explanation': 'Contains suspicious link that could be phishing',
                'severity': 'high',
                'category': 'phishing'
            },
            'urgency': {
                'patterns': [r'urgent', r'immediate', r'action required', r'warning'],
                'explanation': 'Creates false urgency to pressure you',
                'severity': 'medium',
                'category': 'tactic'
            },
            'job_offer': {
                'patterns': [r'work from home', r'earn money', r'part time', r'data entry', r'online job'],
                'explanation': 'Too-good-to-be-true job offer - common employment scam',
                'severity': 'medium',
                'category': 'employment'
            },
            'free_offer': {
                'patterns': [r'free', r'gift', r'offer', r'discount', r'limited time'],
                'explanation': 'Offers something free to lure you in',
                'severity': 'medium',
                'category': 'enticement'
            },
            'parcel_courier': {
                'patterns': [r'parcel', r'courier', r'fedex', r'dhl', r'package', r'customs'],
                'explanation': 'Fake parcel/courier scam - common in India',
                'severity': 'high',
                'category': 'delivery'
            },
            'payment_request': {
                'patterns': [r'payment pending', r'transaction failed', r'refund', r'money back', r'send money'],
                'explanation': 'Fake payment issues or money requests',
                'severity': 'high',
                'category': 'financial'
            },
            'banking_alert': {
                'patterns': [r'bank account', r'debit card', r'credit card', r'atm', r'net banking'],
                'explanation': 'Banking-related scam - impersonating bank officials',
                'severity': 'critical',
                'category': 'financial'
            },
            'govt_impersonation': {
                'patterns': [r'income tax', r'itr', r'government', r'sarkari', r'official'],
                'explanation': 'Impersonating government officials - serious scam',
                'severity': 'critical',
                'category': 'authority'
            },
            'investment': {
                'patterns': [r'investment', r'returns', r'profit', r'double.*money', r'quick money'],
                'explanation': 'Fake investment scheme promising high returns',
                'severity': 'high',
                'category': 'financial'
            },
            'lottery_overseas': {
                'patterns': [r'uk lottery', r'canada', r'usa', r'international', r'foreign'],
                'explanation': 'Claims of winning foreign lottery - common scam',
                'severity': 'high',
                'category': 'financial'
            },
            'friendship_trap': {
                'patterns': [r'dear friend', r'help me', r'need money', r'emergency', r'please help'],
                'explanation': 'Emotional manipulation to extract money',
                'severity': 'medium',
                'category': 'social'
            }
        }
    
    def load_model(self):
        """Load the trained model"""
        try:
            self.model = joblib.load(self.model_path)
            print("✅ Model loaded successfully!")
            return True
        except Exception as e:
            print(f"⚠️ Model not loaded: {e}")
            return False
    
    def analyze_patterns(self, message):
        """Analyze message against scam patterns"""
        message_lower = message.lower()
        findings = []
        
        for scam_type, info in self.scam_patterns.items():
            for pattern in info['patterns']:
                if re.search(pattern, message_lower):
                    findings.append({
                        'type': scam_type.replace('_', ' ').title(),
                        'explanation': info['explanation'],
                        'severity': info['severity'],
                        'category': info['category'],
                        'matched_pattern': pattern
                    })
                    break  # Found one pattern for this type
        
        return findings
    
    def calculate_risk_score(self, findings):
        """Calculate overall risk score based on findings"""
        severity_weights = {
            'critical': 4,
            'high': 3,
            'medium': 2,
            'low': 1
        }
        
        if not findings:
            return 0, 'low'
        
        # Calculate weighted score
        total_weight = sum(severity_weights.get(f['severity'], 1) for f in findings)
        max_possible = len(findings) * 4  # Critical weight is 4
        risk_percentage = (total_weight / max_possible) * 100 if max_possible > 0 else 0
        
        # Determine risk level
        if risk_percentage >= 75:
            risk_level = 'critical'
        elif risk_percentage >= 50:
            risk_level = 'high'
        elif risk_percentage >= 25:
            risk_level = 'medium'
        else:
            risk_level = 'low'
        
        return round(risk_percentage, 1), risk_level
    
    def get_recommendations(self, risk_level, findings):
        """Get recommendations based on risk level and findings"""
        recommendations = []
        
        # General recommendations based on risk level
        if risk_level in ['critical', 'high']:
            recommendations.extend([
                "❌ DO NOT click any links in this message",
                "❌ DO NOT share any personal information",
                "❌ DO NOT send money or OTP",
                "✅ Block and report the sender immediately",
                "📞 Report to Cyber Crime Helpline: 1930",
                "🌐 File online complaint: https://cybercrime.gov.in"
            ])
        elif risk_level == 'medium':
            recommendations.extend([
                "⚠️ Be very cautious with this message",
                "✅ Verify the sender through official channels",
                "📚 Visit our awareness website to learn more about such scams"
            ])
        else:
            recommendations.extend([
                "✅ This message appears safe, but always stay vigilant",
                "📚 Visit our website to learn about scam prevention"
            ])
        
        # Category-specific recommendations
        categories = set(f['category'] for f in findings)
        
        if 'financial' in categories:
            recommendations.append("💰 Never share bank details, OTP, or UPI PIN")
        
        if 'identity' in categories:
            recommendations.append("🆔 Never share Aadhaar, PAN, or personal documents")
        
        if 'phishing' in categories:
            recommendations.append("🔍 Check URLs carefully - look for spelling mistakes")
        
        if 'security' in categories:
            recommendations.append("🔐 Enable two-factor authentication on all accounts")
        
        return list(dict.fromkeys(recommendations))  # Remove duplicates
    
    def analyze(self, message):
        """Complete message analysis"""
        if not message or not isinstance(message, str):
            return {
                'error': 'Invalid message format',
                'original_message': message
            }
        
        # Initialize result
        result = {
            'original_message': message,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'ai_prediction': None,
            'ai_confidence': 0,
            'scam_indicators': [],
            'risk_score': 0,
            'risk_level': 'low',
            'recommendations': [],
            'message_length': len(message),
            'has_links': bool(re.search(r'http|bit\.ly|tinyurl', message.lower()))
        }
        
        # Step 1: AI Model Prediction (if available)
        if self.model:
            try:
                prediction = self.model.predict([message])[0]
                probabilities = self.model.predict_proba([message])[0]
                confidence = max(probabilities) * 100
                
                result['ai_prediction'] = prediction
                result['ai_confidence'] = round(confidence, 1)
            except Exception as e:
                print(f"Model prediction error: {e}")
        
        # Step 2: Pattern-based analysis
        findings = self.analyze_patterns(message)
        result['scam_indicators'] = findings
        
        # Step 3: Calculate risk score
        risk_score, risk_level = self.calculate_risk_score(findings)
        result['risk_score'] = risk_score
        result['risk_level'] = risk_level
        
        # Step 4: Get recommendations
        result['recommendations'] = self.get_recommendations(risk_level, findings)
        
        # Step 5: Add summary
        if risk_level in ['critical', 'high']:
            result['summary'] = "⚠️ This message shows strong scam indicators! Do not engage."
        elif risk_level == 'medium':
            result['summary'] = "⚠️ This message has some suspicious elements. Be very careful."
        else:
            result['summary'] = "✅ This message appears to be legitimate."
        
        return result
    
    def get_statistics(self):
        """Get detector statistics"""
        return {
            'total_patterns': len(self.scam_patterns),
            'model_loaded': self.model is not None,
            'categories': list(set(p['category'] for p in self.scam_patterns.values())),
            'severity_levels': ['critical', 'high', 'medium', 'low']
        }

# Quick test if run directly
if __name__ == "__main__":
    detector = ScamDetector()
    
    print("\n" + "="*60)
    print("🔍 SCAM DETECTOR TEST")
    print("="*60)
    
    test_messages = [
        "Congratulations! You won a lottery of ₹10,00,000! Click here to claim now",
        "URGENT: Your SBI bank account will be suspended. Update KYC immediately",
        "Hi, are we meeting for lunch tomorrow at 3 PM?",
        "Work from home job! Earn ₹50,000 monthly. No experience needed",
        "Your Aadhaar will be deactivated in 24 hours. Click to verify",
        "Thanks for the payment, I received it."
    ]
    
    for i, msg in enumerate(test_messages, 1):
        print(f"\n📨 Test {i}: {msg[:50]}...")
        print("-"*40)
        
        result = detector.analyze(msg)
        
        print(f"Risk Level: {result['risk_level'].upper()}")
        print(f"Risk Score: {result['risk_score']}%")
        if result['ai_prediction']:
            print(f"AI Says: {result['ai_prediction']} ({result['ai_confidence']}%)")
        
        if result['scam_indicators']:
            print(f"Found {len(result['scam_indicators'])} scam indicators")
            for idx, ind in enumerate(result['scam_indicators'][:2], 1):
                print(f"  {idx}. {ind['explanation']}")
        
        print(f"Summary: {result['summary']}")