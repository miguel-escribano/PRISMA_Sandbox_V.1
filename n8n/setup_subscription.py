"""
PRISMA MVP - Setup n8n Subscription
One-time script to create FIWARE subscription that sends data to n8n webhook.
"""

import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.fiware_client import FIWAREClient

# =============================================================================
# CONFIGURATION
# =============================================================================

# Para test: webhook-test (requiere n8n escuchando)
# Para producción: webhook (requiere workflow activado)
N8N_WEBHOOK_URL = "https://miguelescribano.app.n8n.cloud/webhook/fba465ee-fec7-4b21-8fca-cd3ecb2186e8"

SUBSCRIPTION_DATA = {
    "description": "PRISMA MVP - All streams to n8n",
    "subject": {
        "entities": [
            {"idPattern": ".*", "type": "WeatherObserved"},
            {"idPattern": ".*", "type": "AirQualityObserved"},
            {"idPattern": ".*", "type": "ForestFire"},
            {"idPattern": ".*", "type": "EmergencyCalls"},
            {"idPattern": ".*", "type": "HospitalStatus"},
            {"idPattern": ".*", "type": "SocialMediaAlert"},
            {"idPattern": ".*", "type": "TrafficAlert"}
        ],
        "condition": {
            "attrs": []
        }
    },
    "notification": {
        "http": {
            "url": N8N_WEBHOOK_URL
        },
        "attrs": [],
        "attrsFormat": "normalized"
    },
    "throttling": 1
}


# =============================================================================
# COMMANDS
# =============================================================================

def list_subscriptions():
    """List all current subscriptions."""
    client = FIWAREClient()
    client.refresh_token()
    
    subs = client.list_subscriptions()
    
    if not subs:
        print("No subscriptions found.")
        return
    
    print(f"\nFound {len(subs)} subscription(s):\n")
    for sub in subs:
        print(f"  ID: {sub['id']}")
        print(f"  Description: {sub.get('description', 'N/A')}")
        print(f"  Status: {sub.get('status', 'N/A')}")
        notification = sub.get('notification', {})
        print(f"  URL: {notification.get('http', {}).get('url', 'N/A')}")
        print(f"  Last notification: {notification.get('lastNotification', 'never')}")
        print(f"  Times sent: {notification.get('timesSent', 0)}")
        print()


def create_subscription():
    """Create the n8n subscription."""
    client = FIWAREClient()
    client.refresh_token()
    
    print("Creating subscription...")
    print(f"  Target: {N8N_WEBHOOK_URL}")
    
    try:
        sub_id = client.create_subscription(SUBSCRIPTION_DATA)
        print(f"\n[OK] Subscription created!")
        print(f"  ID: {sub_id}")
        return sub_id
    except Exception as e:
        print(f"\n[ERROR] Failed to create subscription: {e}")
        return None


def delete_subscription(sub_id: str):
    """Delete a subscription by ID."""
    client = FIWAREClient()
    client.refresh_token()
    
    print(f"Deleting subscription {sub_id}...")
    
    try:
        client.delete_subscription(sub_id)
        print("[OK] Subscription deleted!")
    except Exception as e:
        print(f"[ERROR] Failed to delete: {e}")


def delete_all_n8n_subscriptions():
    """Delete all subscriptions pointing to our n8n webhook."""
    client = FIWAREClient()
    client.refresh_token()
    
    subs = client.list_subscriptions()
    
    deleted = 0
    for sub in subs:
        url = sub.get('notification', {}).get('http', {}).get('url', '')
        if 'n8n' in url or 'miguelescribano' in url:
            print(f"Deleting {sub['id']}...")
            client.delete_subscription(sub['id'])
            deleted += 1
    
    print(f"\n[OK] Deleted {deleted} subscription(s)")


def test_subscription():
    """Send a test update to trigger the subscription."""
    client = FIWAREClient()
    client.refresh_token()
    
    # Update WeatherObserved entity with test value
    entity_id = "WeatherObserved:AEMET_API_Pamplona_Noain"
    test_attrs = {
        "temperature": {"value": 99.9, "type": "Number"}
    }
    
    print(f"Sending test update to {entity_id}...")
    print(f"  temperature: 99.9 (obvious test value)")
    
    try:
        client.update_entity(entity_id, test_attrs)
        print("\n[OK] Update sent!")
        print("     Check n8n webhook executions to verify notification arrived.")
        print("     URL: https://miguelescribano.app.n8n.cloud")
    except Exception as e:
        print(f"\n[ERROR] Failed to update: {e}")


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Manage PRISMA n8n subscription")
    parser.add_argument("command", choices=["list", "create", "delete", "cleanup", "test"],
                       help="list: show all subs | create: create n8n sub | delete <id>: delete specific | cleanup: delete all n8n subs | test: trigger subscription")
    parser.add_argument("sub_id", nargs="?", help="Subscription ID (for delete command)")
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("PRISMA MVP - n8n Subscription Manager")
    print("=" * 60)
    
    if args.command == "list":
        list_subscriptions()
    elif args.command == "create":
        create_subscription()
    elif args.command == "delete":
        if not args.sub_id:
            print("Error: delete requires subscription ID")
            print("Usage: python setup_n8n_subscription.py delete <subscription_id>")
        else:
            delete_subscription(args.sub_id)
    elif args.command == "cleanup":
        delete_all_n8n_subscriptions()
    elif args.command == "test":
        test_subscription()

