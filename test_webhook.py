import requests
import json

def test_webhook():
    """Test if webhook can receive messages"""
    
    webhook_url = "https://c3a85f73234a.ngrok-free.app/webhook"
    
    # Test data simulating WhatsApp
    test_data = {
        "object": "whatsapp_business_account",
        "entry": [{
            "id": "123456789",
            "changes": [{
                "value": {
                    "messaging_product": "whatsapp",
                    "metadata": {
                        "display_phone_number": "15551799388",
                        "phone_number_id": "950947014765895"
                    },
                    "messages": [{
                        "from": "919876543210",  # Your phone number
                        "id": "wamid.test123",
                        "timestamp": "1700000000",
                        "type": "text",
                        "text": {"body": "HELP"}
                    }]
                },
                "field": "messages"
            }]
        }]
    }
    
    print("🧪 Testing webhook...")
    
    try:
        response = requests.post(webhook_url, json=test_data)
        print(f"✅ Webhook response: {response.status_code}")
        print(f"Response: {response.json()}")
        
        # Check Flask console for logs
        print("\n📋 Check your Flask console for:")
        print("   '📥 Received webhook data'")
        print("   '📨 Message from 919876543210: HELP'")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_webhook()