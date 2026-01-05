import requests
import os
from dotenv import load_dotenv

load_dotenv()

def test_whatsapp_token():
    """Test if WhatsApp token works"""
    
    token = os.getenv('WHATSAPP_TOKEN')
    phone_id = os.getenv('WHATSAPP_PHONE_NUMBER_ID')
    
    if not token:
        print("❌ No token found in .env")
        return
    
    # Test URL
    url = f"https://graph.facebook.com/v18.0/{phone_id}"
    
    headers = {
        'Authorization': f'Bearer {token}'
    }
    
    print(f"🧪 Testing token for phone ID: {phone_id}")
    
    try:
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            print("✅ Token is valid!")
            print(f"Response: {response.json()}")
        else:
            print(f"❌ Token error: {response.status_code}")
            print(f"Response: {response.text}")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_whatsapp_token()