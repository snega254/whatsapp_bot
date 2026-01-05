import requests
import os
from dotenv import load_dotenv

load_dotenv()

def debug_whatsapp_api():
    """Direct test of WhatsApp API"""
    
    print("="*60)
    print("🔍 DEBUGGING WHATSAPP API")
    print("="*60)
    
    # Get credentials
    token = os.getenv('WHATSAPP_TOKEN')
    phone_id = os.getenv('WHATSAPP_PHONE_NUMBER_ID')
    
    print(f"📱 Phone ID: {phone_id}")
    print(f"🔑 Token: {'✅ Present' if token else '❌ MISSING'}")
    
    if not token:
        print("❌ ERROR: No token in .env file!")
        print("   Make sure .env has: WHATSAPP_TOKEN=EAAK...")
        return
    
    # Test 1: Check phone number info
    print("\n1️⃣ Testing API connection...")
    url = f"https://graph.facebook.com/v18.0/{phone_id}"
    headers = {'Authorization': f'Bearer {token}'}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        print(f"   Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"   ✅ Connected! Phone: {data.get('verified_name', 'Unknown')}")
            print(f"   Quality rating: {data.get('quality_rating', 'Unknown')}")
        else:
            print(f"   ❌ Failed: {response.text}")
            
    except Exception as e:
        print(f"   ❌ Connection error: {e}")
    
    # Test 2: Try sending template message (most likely to work)
    print("\n2️⃣ Sending template message...")
    
    # CHANGE THIS TO YOUR REAL WHATSAPP NUMBER!
    YOUR_NUMBER = "+91XXXXXXXXXX"  # <-- PUT YOUR NUMBER HERE!
    
    url = f"https://graph.facebook.com/v18.0/{phone_id}/messages"
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    
    # Use hello_world template (pre-approved)
    data = {
        "messaging_product": "whatsapp",
        "to": YOUR_NUMBER,
        "type": "template",
        "template": {
            "name": "hello_world",
            "language": {"code": "en_US"}
        }
    }
    
    print(f"   📤 To: {YOUR_NUMBER}")
    print(f"   📝 Template: hello_world")
    
    try:
        response = requests.post(url, headers=headers, json=data, timeout=10)
        print(f"   Status: {response.status_code}")
        
        if response.status_code == 200:
            print("   ✅ Template sent! Check your WhatsApp!")
            print(f"   Message ID: {response.json().get('messages', [{}])[0].get('id')}")
        else:
            print(f"   ❌ Failed: {response.text}")
            
    except Exception as e:
        print(f"   ❌ Send error: {e}")
    
    # Test 3: Try sending text message
    print("\n3️⃣ Sending text message...")
    
    data_text = {
        "messaging_product": "whatsapp",
        "to": YOUR_NUMBER,
        "type": "text",
        "text": {"body": "🚑 Emergency Bot Test: Reply HELP"}
    }
    
    try:
        response = requests.post(url, headers=headers, json=data_text, timeout=10)
        print(f"   Status: {response.status_code}")
        
        if response.status_code == 200:
            print("   ✅ Text sent! Check your WhatsApp!")
        else:
            print(f"   ❌ Failed: {response.text}")
            
    except Exception as e:
        print(f"   ❌ Text send error: {e}")
    
    print("\n" + "="*60)
    print("📋 DIAGNOSTIC RESULTS:")
    print("="*60)
    
    # Common issues:
    print("\n🔍 Common issues:")
    print("1. Token expired - regenerate in Meta")
    print("2. Phone number not verified - check in Meta")
    print("3. Number blocked - 'Messaging unavailable'")
    print("4. Wrong number format - use with country code")
    print("5. No message templates approved")

if __name__ == "__main__":
    # First, show current .env
    print("📄 Current .env contents:")
    print("-" * 30)
    with open('.env', 'r') as f:
        for line in f:
            if 'TOKEN' in line or 'PHONE' in line:
                print(line.strip())
    print("-" * 30)
    
    debug_whatsapp_api()