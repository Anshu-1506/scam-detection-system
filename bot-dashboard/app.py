# app.py - Using enhanced ScamDetector
from flask import Flask, render_template, request, jsonify
from detect_scam import ScamDetector
from datetime import datetime

app = Flask(__name__)

# Initialize the scam detector
detector = ScamDetector()

@app.route('/')
def dashboard():
    """Render the main dashboard"""
    return render_template('dashboard.html')

@app.route('/api/analyze', methods=['POST'])
def analyze():
    """API endpoint for message analysis"""
    data = request.json
    message = data.get('message', '')
    
    if not message:
        return jsonify({'error': 'No message provided'}), 400
    
    # Use the detector to analyze
    results = detector.analyze(message)
    return jsonify(results)

@app.route('/api/health')
def health():
    """Health check endpoint"""
    stats = detector.get_statistics()
    return jsonify({
        'status': 'healthy',
        'model_loaded': detector.model is not None,
        'timestamp': datetime.now().isoformat(),
        'stats': stats
    })

@app.route('/api/stats')
def stats():
    """Get detector statistics"""
    return jsonify(detector.get_statistics())

if __name__ == '__main__':
    print("\n" + "="*60)
    print("🚀 SCAM DETECTION DASHBOARD")
    print("="*60)
    print("\n📊 Detector Status:")
    print(f"   Model Loaded: {'✅' if detector.model else '❌'}")
    print(f"   Patterns: {len(detector.scam_patterns)}")
    print(f"   Categories: {', '.join(set(p['category'] for p in detector.scam_patterns.values()))}")
    print("\n🌐 Dashboard URL: http://localhost:5000")
    print("🔗 API Endpoint: http://localhost:5000/api/analyze")
    print("\n💡 To use:")
    print("   1. Open http://localhost:5000 in your browser")
    print("   2. Enter any suspicious message")
    print("   3. Get instant AI analysis with detailed indicators")
    print("\n" + "="*60)
    print("✅ Dashboard running! Press Ctrl+C to stop")
    print("="*60 + "\n")
    
    app.run(host='0.0.0.0', port=5000, debug=True)