"""
PRISMA Sandbox V.1 - FIWARE Client

Python client for interacting with FIWARE Context Broker.
This replicates MCP functionality for use in Python applications.
"""

import requests
from typing import Dict, List, Optional, Any
from datetime import datetime, timedelta
import logging
import urllib3

from config import config

# Disable SSL warnings for Telefónica platform
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

logger = logging.getLogger(__name__)


class FIWAREClient:
    """Client for FIWARE Context Broker operations."""
    
    def __init__(self, subservice: Optional[str] = None):
        """
        Initialize FIWARE client.
        
        Args:
            subservice: FIWARE-ServicePath (defaults to dev subservice)
        """
        self.cb_url = config.FIWARE_CB_URL
        self.service = config.SERVICE
        self.subservice = subservice or config.SUBSERVICE_PRISMA
        self._token = config.AUTH_TOKEN
        self._token_expires = None
    
    def _get_headers(self) -> Dict[str, str]:
        """Get request headers with authentication."""
        return {
            'Fiware-Service': self.service,
            'Fiware-ServicePath': self.subservice,
            'X-Auth-Token': self._token
        }
    
    def refresh_token(self) -> str:
        """
        Refresh token using Telefónica's Keystone auth.
        
        Returns:
            New access token
        """
        url = f"{config.FIWARE_AUTH_URL}/v3/auth/tokens"
        
        payload = {
            "auth": {
                "identity": {
                    "methods": ["password"],
                    "password": {
                        "user": {
                            "domain": {"name": config.SERVICE},
                            "name": config.USERNAME,
                            "password": config.PASSWORD
                        }
                    }
                },
                "scope": {
                    "project": {
                        "domain": {"name": config.SERVICE},
                        "name": self.subservice
                    }
                }
            }
        }
        
        headers = {"Content-Type": "application/json"}
        
        response = requests.post(url, json=payload, headers=headers, verify=False)
        response.raise_for_status()
        
        # Token is in the X-Subject-Token header
        self._token = response.headers.get("X-Subject-Token")
        
        # Set expiration (usually 24 hours)
        self._token_expires = datetime.now() + timedelta(hours=24)
        
        logger.info(f"Token refreshed, expires at {self._token_expires}")
        
        return self._token
    
    def _ensure_token(self):
        """Ensure we have a valid token."""
        if not self._token or (self._token_expires and datetime.now() >= self._token_expires):
            self.refresh_token()
    
    def get_version(self) -> Dict[str, Any]:
        """Get Context Broker version."""
        self._ensure_token()
        url = f"{self.cb_url}/version"
        # Version endpoint doesn't need Fiware-Service headers
        headers = {'X-Auth-Token': self._token} if self._token else {}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    
    def query_entities(
        self,
        entity_type: Optional[str] = None,
        limit: int = 100,
        offset: int = 0,
        query: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Query entities from Context Broker.
        
        Args:
            entity_type: Filter by entity type
            limit: Maximum number of results
            offset: Pagination offset
            query: Query filter (e.g., "temperature>25")
        
        Returns:
            List of entities
        """
        self._ensure_token()
        url = f"{self.cb_url}/v2/entities"
        
        params = {
            'limit': limit,
            'offset': offset
        }
        
        if entity_type:
            params['type'] = entity_type
        
        if query:
            params['q'] = query
        
        response = requests.get(url, headers=self._get_headers(), params=params)
        response.raise_for_status()
        
        return response.json()
    
    def get_entity(self, entity_id: str, entity_type: Optional[str] = None) -> Dict[str, Any]:
        """
        Get specific entity by ID.
        
        Args:
            entity_id: Entity ID
            entity_type: Entity type (optional)
        
        Returns:
            Entity data
        """
        self._ensure_token()
        url = f"{self.cb_url}/v2/entities/{entity_id}"
        
        params = {}
        if entity_type:
            params['type'] = entity_type
        
        response = requests.get(url, headers=self._get_headers(), params=params)
        response.raise_for_status()
        
        return response.json()
    
    def create_entity(self, entity_data: Dict[str, Any]) -> bool:
        """
        Create new entity.
        
        Args:
            entity_data: Entity data (must include 'id' and 'type')
        
        Returns:
            True if successful
        """
        self._ensure_token()
        url = f"{self.cb_url}/v2/entities"
        
        response = requests.post(url, headers=self._get_headers(), json=entity_data, verify=False)
        response.raise_for_status()
        
        return True
    
    def update_entity(self, entity_id: str, attributes: Dict[str, Any]) -> bool:
        """
        Update entity attributes.
        
        Args:
            entity_id: Entity ID
            attributes: Attributes to update
        
        Returns:
            True if successful
        """
        self._ensure_token()
        url = f"{self.cb_url}/v2/entities/{entity_id}/attrs"
        
        response = requests.patch(url, headers=self._get_headers(), json=attributes, verify=False)
        response.raise_for_status()
        
        return True
    
    def delete_entity(self, entity_id: str, entity_type: Optional[str] = None) -> bool:
        """
        Delete entity.
        
        Args:
            entity_id: Entity ID
            entity_type: Entity type (optional)
        
        Returns:
            True if successful
        """
        self._ensure_token()
        url = f"{self.cb_url}/v2/entities/{entity_id}"
        
        params = {}
        if entity_type:
            params['type'] = entity_type
        
        response = requests.delete(url, headers=self._get_headers(), params=params, verify=False)
        response.raise_for_status()
        
        return True

    # =========================================================================
    # SUBSCRIPTIONS
    # =========================================================================
    
    def list_subscriptions(self) -> List[Dict[str, Any]]:
        """List all subscriptions in current subservice."""
        self._ensure_token()
        url = f"{self.cb_url}/v2/subscriptions"
        
        response = requests.get(url, headers=self._get_headers(), verify=False)
        response.raise_for_status()
        
        return response.json()
    
    def get_subscription(self, subscription_id: str) -> Dict[str, Any]:
        """Get a specific subscription by ID."""
        self._ensure_token()
        url = f"{self.cb_url}/v2/subscriptions/{subscription_id}"
        
        response = requests.get(url, headers=self._get_headers(), verify=False)
        response.raise_for_status()
        
        return response.json()
    
    def create_subscription(self, subscription_data: Dict[str, Any]) -> str:
        """
        Create a new subscription.
        
        Args:
            subscription_data: Subscription definition
        
        Returns:
            Subscription ID (from Location header)
        """
        self._ensure_token()
        url = f"{self.cb_url}/v2/subscriptions"
        
        headers = self._get_headers()
        headers['Content-Type'] = 'application/json'
        
        response = requests.post(url, headers=headers, json=subscription_data, verify=False)
        response.raise_for_status()
        
        # ID is in Location header: /v2/subscriptions/{id}
        location = response.headers.get('Location', '')
        subscription_id = location.split('/')[-1] if location else None
        
        return subscription_id
    
    def delete_subscription(self, subscription_id: str) -> bool:
        """Delete a subscription."""
        self._ensure_token()
        url = f"{self.cb_url}/v2/subscriptions/{subscription_id}"
        
        response = requests.delete(url, headers=self._get_headers(), verify=False)
        response.raise_for_status()
        
        return True


# Example usage
if __name__ == '__main__':
    # Configure logging
    logging.basicConfig(level=logging.INFO)
    
    # Create client for development subservice
    client = FIWAREClient(subservice=config.FIWARE_SUBSERVICE_DEV)
    
    # Get version
    print("Context Broker Version:")
    print(client.get_version())
    
    # Query entities
    print("\nQuerying entities...")
    entities = client.query_entities(limit=5)
    print(f"Found {len(entities)} entities")
    
    for entity in entities:
        print(f"  - {entity['id']} ({entity['type']})")

