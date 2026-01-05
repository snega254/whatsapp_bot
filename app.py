"""
🚑 EMERGENCY WHATSAPP BOT - 108 Style
REAL WhatsApp API Version - CORRECTED
"""
from flask import Flask, request, jsonify
import os
import requests
import json
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()

# Create Flask app
app = Flask(__name__)

# Store user sessions
user_sessions = {}

print("="*60)
print("🚀 REAL WHATSAPP EMERGENCY BOT STARTING...")
print("="*60)
print(f"📱 Phone Number ID: {os.getenv('WHATSAPP_PHONE_NUMBER_ID')}")
print(f"🔑 Token present: {'✅ Yes' if os.getenv('WHATSAPP_TOKEN') else '❌ No'}")
print(f"🌐 Webhook URL: https://6c9111c6d221.ngrok-free.app")
print("="*60)

# ============================================
# REAL WHATSAPP API FUNCTIONS
# ============================================

def send_whatsapp_message(phone_number, message_text):
    """Send REAL WhatsApp message via Meta API"""
    
    access_token = os.getenv('WHATSAPP_TOKEN')
    phone_id = os.getenv('WHATSAPP_PHONE_NUMBER_ID')
    
    if not access_token:
        print("❌ ERROR: No WhatsApp access token found in .env")
        print("   Make sure WHATSAPP_TOKEN= is set in .env file")
        return None
    
    if not phone_id:
        print("❌ ERROR: No Phone Number ID found in .env")
        return None
    
    # WhatsApp API URL
    url = f"https://graph.facebook.com/v18.0/{phone_id}/messages"
    
    # Headers with access token
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    
    # Message payload
    data = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": phone_number,
        "type": "text",
        "text": {"body": message_text}
    }
    
    try:
        print(f"📤 SENDING to {phone_number}: {message_text[:50]}...")
        response = requests.post(url, headers=headers, json=data, timeout=10)
        
        if response.status_code == 200:
            print(f"✅ Message sent successfully to {phone_number}")
            return response.json()
        else:
            print(f"❌ Failed to send: {response.status_code}")
            print(f"   Response: {response.text}")
            return None
            
    except Exception as e:
        print(f"❌ WhatsApp API Error: {e}")
        return None

def send_welcome_menu(phone_number):
    """Send welcome message with emergency options"""
    
    message = """🚨 *Welcome to 108 Emergency Services*

Please choose emergency type:

1. 🚑 *Medical Emergency* - Ambulance
2. 🔥 *Fire Emergency* - Fire Brigade  
3. 👮 *Police Emergency* - Police

Reply with *1*, *2*, or *3*"""
    
    return send_whatsapp_message(phone_number, message)

def ask_for_location(phone_number, emergency_type):
    """Ask user to share location"""
    
    emergency_names = {
        "medical": "Medical Emergency 🚑",
        "fire": "Fire Emergency 🔥",
        "police": "Police Emergency 👮"
    }
    
    message = f"""📍 *{emergency_names.get(emergency_type, 'Emergency')} Selected*

Please share your location:
• Tap 📎 *attachment* icon
• Select *Location*
• Send your current location

*OR* type your address manually."""

    return send_whatsapp_message(phone_number, message)

def send_confirmation(phone_number, emergency_type):
    """Send confirmation that help is coming"""
    
    messages = {
        "medical": """✅ *Ambulance Dispatched!*
        
⏱️ *ETA:* 8-12 minutes
📞 *Medical team will call you shortly*

*Please:*
• Stay with the patient
• Keep medicines handy
• Clear entrance pathway
• Keep phone accessible""",
        
        "fire": """✅ *Fire Engine Dispatched!*
        
⏱️ *ETA:* 6-10 minutes
📞 *Firefighters will contact you*

*Immediately:*
• Evacuate everyone
• Close all doors
• Don't use elevators
• Gather at safe distance""",
        
        "police": """✅ *Police Patrol Dispatched!*
        
⏱️ *ETA:* 5-9 minutes  
📞 *Officer will call for details*

*Please:*
• Stay in safe location
• Secure premises
• Keep phone ready
• Note suspect details"""
    }
    
    return send_whatsapp_message(phone_number, messages.get(emergency_type, "✅ Help is on the way!"))

# ============================================
# FLASK ROUTES
# ============================================

@app.route('/')
def home():
    """Home page"""
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>🚑 Emergency WhatsApp Bot</title>
        <style>
            body { font-family: Arial; margin: 40px; background: #f5f5f5; }
            .container { background: white; padding: 30px; border-radius: 10px; max-width: 800px; margin: auto; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
            h1 { color: #e74c3c; }
            .status { background: #2ecc71; color: white; padding: 10px; border-radius: 5px; }
            .url { background: #3498db; color: white; padding: 10px; border-radius: 5px; font-family: monospace; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚑 Emergency WhatsApp Bot</h1>
            <div class="status">✅ Server is running with REAL WhatsApp API</div>
            
            <h2>📡 Webhook URL:</h2>
            <div class="url">https://6c9111c6d221.ngrok-free.app/webhook</div>
            
            <h2>🎯 To Test:</h2>
            <ol>
                <li>Open WhatsApp on your phone</li>
                <li>Message: <strong>+1 555 179 9388</strong></li>
                <li>Send: <code>HELP</code></li>
                <li>Bot will respond with emergency menu</li>
            </ol>
            
            <h2>🔧 Status:</h2>
            <p>✅ Flask Server: Running</p>
            <p>✅ Ngrok Tunnel: Active</p>
            <p>✅ WhatsApp API: Configured</p>
            <p>✅ Webhook: Ready</p>
        </div>
    </body>
    </html>
    """

@app.route('/test')
def test():
    """Test endpoint"""
    return "✅ Emergency WhatsApp Bot is running!"

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "service": "WhatsApp Emergency Bot",
        "whatsapp_configured": bool(os.getenv('WHATSAPP_TOKEN')),
        "sessions_active": len(user_sessions),
        "webhook_url": "https://6c9111c6d221.ngrok-free.app"
    })

@app.route('/sessions')
def sessions():
    """Show active user sessions"""
    return jsonify({
        "total_sessions": len(user_sessions),
        "sessions": user_sessions
    })

# ============================================
# WHATSAPP WEBHOOK HANDLING - CORRECTED
# ============================================

@app.route('/webhook', methods=['GET'])
def verify_webhook():
    """Verify webhook with Meta"""
    mode = request.args.get('hub.mode')
    token = request.args.get('hub.verify_token')
    challenge = request.args.get('hub.challenge')
    
    print(f"🔍 Webhook verification attempt: mode={mode}, token={token}")
    
    if mode == 'subscribe' and token == os.getenv('VERIFY_TOKEN'):
        print("✅ Webhook verified successfully!")
        # RETURN THE CHALLENGE WITH THE CRITICAL HEADER
        return challenge, 200, {'ngrok-skip-browser-warning': 'any-value'}
    
    print("❌ Webhook verification failed")
    return "Verification failed", 403

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    """Handle incoming WhatsApp messages - ONLY ONE POST ROUTE!"""
    
    # LOG EVERYTHING
    print("\n" + "="*60)
    print("📥 WEBHOOK CALLED!")
    print(f"📋 Headers: {dict(request.headers)}")
    
    try:
        data = request.get_json()
        if not data:
            print("❌ No JSON data received")
            return jsonify({"error": "No data"}), 400
        
        print(f"✅ Received JSON data")
        print(f"📊 Data keys: {list(data.keys())}")
        
        # Log full data (truncated)
        data_str = json.dumps(data, indent=2)
        print(f"📄 Data preview:\n{data_str[:500]}...")
        
        # Check if this is a WhatsApp message
        if data.get('object') == 'whatsapp_business_account':
            print("🎯 WhatsApp message detected!")
            
            # Extract phone number and message
            for entry in data.get('entry', []):
                for change in entry.get('changes', []):
                    value = change.get('value', {})
                    
                    # Handle messages
                    if 'messages' in value:
                        for message in value['messages']:
                            phone = message['from']
                            msg_type = message['type']
                            
                            if msg_type == 'text':
                                text = message['text']['body']
                                print(f"📨 Message from {phone}: {text}")
                                
                                # Handle HELP command
                                if text.lower() == 'help':
                                    # Initialize session
                                    user_sessions[phone] = {
                                        'state': 'awaiting_choice',
                                        'last_active': datetime.now().isoformat()
                                    }
                                    
                                    # Send welcome menu
                                    send_welcome_menu(phone)
                                    print(f"👤 {phone}: Sent welcome menu")
                                
                                # Handle emergency choice
                                elif text in ['1', '2', '3']:
                                    if phone in user_sessions:
                                        emergency_map = {'1': 'medical', '2': 'fire', '3': 'police'}
                                        emergency_type = emergency_map.get(text)
                                        
                                        user_sessions[phone]['emergency_type'] = emergency_type
                                        user_sessions[phone]['state'] = 'awaiting_location'
                                        
                                        ask_for_location(phone, emergency_type)
                                        print(f"🚨 {phone}: Selected {emergency_type}")
                                    else:
                                        send_whatsapp_message(phone, "Please type HELP first")
                                
                                # Handle other messages
                                else:
                                    if phone in user_sessions:
                                        # If waiting for location, accept text as address
                                        if user_sessions[phone]['state'] == 'awaiting_location':
                                            user_sessions[phone]['location'] = text
                                            user_sessions[phone]['state'] = 'completed'
                                            
                                            emergency_type = user_sessions[phone].get('emergency_type', 'unknown')
                                            send_confirmation(phone, emergency_type)
                                            print(f"📍 {phone}: Provided address for {emergency_type}")
                                        
                                    else:
                                        # If no session, prompt for HELP
                                        send_whatsapp_message(phone, "Type 'HELP' to start emergency services")
                                        print(f"💬 {phone}: Prompted to type HELP")
                    
                    # Handle message status updates
                    elif 'statuses' in value:
                        for status in value['statuses']:
                            print(f"📤 Message status: {status.get('status')} for {status.get('id')}")
        
        else:
            print("⚠️ Not a WhatsApp business account message")
        
        print("="*60)
        return jsonify({"status": "ok"}), 200
        
    except Exception as e:
        print(f"❌ Error in webhook handler: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

# ============================================
# START SERVER
# ============================================

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print(f"🌐 Starting server on port {port}...")
    print(f"📱 Test URL: http://localhost:{port}")
    print(f"🌍 Ngrok URL: https://6c9111c6d221.ngrok-free.app")
    print("="*60)
    print("💡 Send 'HELP' to +1 555 179 9388 on WhatsApp!")
    print("="*60)
    
    app.run(host='0.0.0.0', port=port, debug=True, threaded=True)