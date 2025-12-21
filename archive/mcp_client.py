"""
PRISMA Sandbox V.1 - MCP Client

Uses the local FIWARE MCP Server for all FIWARE operations.
This handles all the auth complexity for us!
"""

import requests
import json
from typing import Dict, List, Any, Optional

class MCPClient:
    """Client to interact with local FIWARE MCP Server."""
    
    def __init__(self, mcp_url: str = "http://127.0.0.1:5001"):
        """
        Initialize MCP client.
        
        Args:
            mcp_url: URL of the MCP server
        """
        self.mcp_url = mcp_url
        self.tools_url = f"{mcp_url}/mcp/v1/tools"
    
    def _call_tool(self, tool_name: str, arguments: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Call an MCP tool.
        
        Args:
            tool_name: Name of the tool
            arguments: Tool arguments
        
        Returns:
            Tool result
        """
        payload = {
            "name": tool_name,
            "arguments": arguments or {}
        }
        
        response = requests.post(f"{self.tools_url}/call", json=payload)
        response.raise_for_status()
        
        result = response.json()
        
        # Parse the content (it's JSON string)
        if 'content' in result and isinstance(result['content'], list):
            for item in result['content']:
                if item.get('type') == 'text':
                    return json.loads(item['text'])
        
        return result
    
    def get_version(self) -> Dict[str, Any]:
        """Get Context Broker version."""
        return self._call_tool("CB_version")
    
    def query_entities(
        self,
        entity_type: Optional[str] = None,
        limit: int = 100,
        offset: int = 0
    ) -> List[Dict[str, Any]]:
        """
        Query entities from Context Broker.
        
        Args:
            entity_type: Filter by entity type
            limit: Maximum number of results
            offset: Pagination offset
        
        Returns:
            List of entities
        """
        query_parts = []
        
        if entity_type:
            query_parts.append(f"type={entity_type}")
        if limit:
            query_parts.append(f"limit={limit}")
        if offset:
            query_parts.append(f"offset={offset}")
        
        query = "&".join(query_parts)
        
        result = self._call_tool("query_CB", {"query": query})
        
        if result.get("success"):
            return result.get("entities", [])
        else:
            raise Exception(result.get("error", "Unknown error"))
    
    def get_entity(self, entity_id: str, entity_type: Optional[str] = None) -> Dict[str, Any]:
        """
        Get specific entity by ID.
        
        Args:
            entity_id: Entity ID
            entity_type: Entity type (optional)
        
        Returns:
            Entity data
        """
        args = {"entity_id": entity_id}
        if entity_type:
            args["entity_type"] = entity_type
        
        result = self._call_tool("get_entity", args)
        
        if result.get("success"):
            return result.get("entity", {})
        else:
            raise Exception(result.get("error", "Unknown error"))
    
    def create_entity(self, entity_data: Dict[str, Any]) -> bool:
        """
        Create new entity.
        
        Args:
            entity_data: Entity data (must include 'id' and 'type')
        
        Returns:
            True if successful
        """
        result = self._call_tool("publish_to_CB", {"entity_data": entity_data})
        
        if result.get("success"):
            return True
        else:
            raise Exception(result.get("error", "Unknown error"))
    
    def update_entity(self, entity_id: str, attributes: Dict[str, Any]) -> bool:
        """
        Update entity attributes.
        
        Args:
            entity_id: Entity ID
            attributes: Attributes to update
        
        Returns:
            True if successful
        """
        # For update, we need to include id and type
        # The MCP server handles create-or-update logic
        entity_data = {"id": entity_id, **attributes}
        
        result = self._call_tool("publish_to_CB", {"entity_data": entity_data})
        
        if result.get("success"):
            return True
        else:
            raise Exception(result.get("error", "Unknown error"))
    
    def delete_entity(self, entity_id: str, entity_type: Optional[str] = None) -> bool:
        """
        Delete entity.
        
        Args:
            entity_id: Entity ID
            entity_type: Entity type (optional)
        
        Returns:
            True if successful
        """
        args = {"entity_id": entity_id}
        if entity_type:
            args["entity_type"] = entity_type
        
        result = self._call_tool("delete_entity", args)
        
        if result.get("success"):
            return True
        else:
            raise Exception(result.get("error", "Unknown error"))


# Example usage
if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.INFO)
    
    print("Testing MCP Client...")
    print("=" * 50)
    
    # Create client
    client = MCPClient()
    
    # Test 1: Get version
    print("\n1. Getting Context Broker version...")
    try:
        version = client.get_version()
        print(f"   ✓ Success: {version}")
    except Exception as e:
        print(f"   ✗ Failed: {e}")
    
    # Test 2: Query entities
    print("\n2. Querying entities...")
    try:
        entities = client.query_entities(limit=3)
        print(f"   ✓ Found {len(entities)} entities")
        for entity in entities[:3]:
            print(f"     - {entity['id']} ({entity['type']})")
    except Exception as e:
        print(f"   ✗ Failed: {e}")
    
    print("\n" + "=" * 50)
    print("Done!")

