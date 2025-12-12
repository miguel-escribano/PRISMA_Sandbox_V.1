"""
PRISMA Sandbox V.1 - Configuration Management

Loads environment variables and provides configuration for the application.
"""

import os
from pathlib import Path
from typing import Optional
from dotenv import load_dotenv

# Load environment variables from .env file
env_path = Path(__file__).parent / '.env'
load_dotenv(dotenv_path=env_path)


class Config:
    """Application configuration from environment variables."""
    
    # =============================================================================
    # FIWARE Configuration - Telefónica IoT Platform
    # =============================================================================
    
    # Credentials (FIWARE_ prefix to avoid Windows USERNAME env var conflict)
    USERNAME: str = os.getenv('FIWARE_USERNAME', '')
    PASSWORD: str = os.getenv('FIWARE_PASSWORD', '')
    SERVICE: str = os.getenv('SERVICE', 'sc_pamplona_sandbox')
    
    # Subservices
    SUBSERVICE_PRISMA: str = os.getenv('SUBSERVICE_PRISMA', '/02_Escribano')
    SUBSERVICE_SDMENVIRONMENT: str = os.getenv('SUBSERVICE_SDMENVIRONMENT', '/sdmenvironment')
    
    # Auth endpoint
    AUTH_HOST: str = os.getenv('AUTH_HOST', 'auth.iotplatform.telefonica.com')
    AUTH_PORT: str = os.getenv('AUTH_PORT', '15001')
    FIWARE_AUTH_URL: str = f"https://{AUTH_HOST}:{AUTH_PORT}"
    
    # Context Broker endpoint
    CB_HOST: str = os.getenv('CB_HOST', 'cb.iotplatform.telefonica.com')
    CB_PORT: str = os.getenv('CB_PORT', '10027')
    FIWARE_CB_URL: str = f"https://{CB_HOST}:{CB_PORT}"
    
    # STH (Short Term Historic) endpoint
    STH_HOST: str = os.getenv('STH_HOST', 'sth.iotplatform.telefonica.com')
    STH_PORT: str = os.getenv('STH_PORT', '18666')
    FIWARE_STH_URL: str = f"https://{STH_HOST}:{STH_PORT}"
    
    # CEP (Perseo) endpoint
    CEP_HOST: str = os.getenv('CEP_HOST', 'cep.iotplatform.telefonica.com')
    CEP_PORT: str = os.getenv('CEP_PORT', '18090')
    FIWARE_CEP_URL: str = f"https://{CEP_HOST}:{CEP_PORT}"
    
    # IoT Agent Ultralight endpoint
    IOTA_UL_HOST: str = os.getenv('IOTA_UL_HOST', 'iota-ul.iotplatform.telefonica.com')
    IOTA_UL_PORT: str = os.getenv('IOTA_UL_PORT', '8085')
    FIWARE_IOTA_UL_URL: str = f"https://{IOTA_UL_HOST}:{IOTA_UL_PORT}"
    UL_APIKEY: str = os.getenv('UL_APIKEY', '')
    
    # IoT Agent JSON endpoint
    IOTA_JSON_HOST: str = os.getenv('IOTA_JSON_HOST', 'iota-json.iotplatform.telefonica.com')
    IOTA_JSON_PORT: str = os.getenv('IOTA_JSON_PORT', '8185')
    FIWARE_IOTA_JSON_URL: str = f"https://{IOTA_JSON_HOST}:{IOTA_JSON_PORT}"
    
    # IoT Agent Manager endpoint
    IOTA_MANAGER_HOST: str = os.getenv('IOTA_MANAGER_HOST', 'iota.iotplatform.telefonica.com')
    IOTA_MANAGER_PORT: str = os.getenv('IOTA_MANAGER_PORT', '8088')
    FIWARE_IOTA_MANAGER_URL: str = f"https://{IOTA_MANAGER_HOST}:{IOTA_MANAGER_PORT}"
    
    # Token
    AUTH_TOKEN: Optional[str] = os.getenv('AUTH_TOKEN')
    
    # Example entity values (for testing)
    ENTITY_ID: str = os.getenv('ENTITY_ID', 'FIWARE:room1:ent')
    ENTITY_TYPE: str = os.getenv('ENTITY_TYPE', 'Room')
    DEVICE_ID: str = os.getenv('DEVICE_ID', 'FIWARE:room1:dev')
    
    # For backwards compatibility
    FIWARE_SERVICE: str = SERVICE
    FIWARE_SUBSERVICE_DEV: str = SUBSERVICE_PRISMA
    FIWARE_SUBSERVICE_PROD: str = SUBSERVICE_SDMENVIRONMENT
    FIWARE_OAUTH_TOKEN: Optional[str] = AUTH_TOKEN
    
    # =============================================================================
    # Application Settings
    # =============================================================================
    
    APP_ENV: str = os.getenv('APP_ENV', 'development')
    DEBUG: bool = os.getenv('DEBUG', 'True').lower() == 'true'
    
    LOG_LEVEL: str = os.getenv('LOG_LEVEL', 'INFO')
    LOG_FILE: str = os.getenv('LOG_FILE', 'logs/prisma.log')
    
    # =============================================================================
    # External APIs
    # =============================================================================
    
    AEMET_API_KEY: Optional[str] = os.getenv('AEMET_API_KEY')
    REE_API_KEY: Optional[str] = os.getenv('REE_API_KEY')
    IDENA_API_URL: str = os.getenv('IDENA_API_URL', 'https://idena.navarra.es/ogc/wfs')
    
    # =============================================================================
    # AI/ML Services
    # =============================================================================
    
    OPENAI_API_KEY: Optional[str] = os.getenv('OPENAI_API_KEY')
    MISTRAL_API_KEY: Optional[str] = os.getenv('MISTRAL_API_KEY')
    LANGCHAIN_API_KEY: Optional[str] = os.getenv('LANGCHAIN_API_KEY')
    LANGCHAIN_TRACING_V2: bool = os.getenv('LANGCHAIN_TRACING_V2', 'false').lower() == 'true'
    
    # =============================================================================
    # Database
    # =============================================================================
    
    DATABASE_URL: Optional[str] = os.getenv('DATABASE_URL')
    REDIS_URL: str = os.getenv('REDIS_URL', 'redis://localhost:6379/0')
    
    # =============================================================================
    # n8n
    # =============================================================================
    
    N8N_WEBHOOK_URL: str = os.getenv('N8N_WEBHOOK_URL', 'http://localhost:5678/webhook')
    N8N_API_KEY: Optional[str] = os.getenv('N8N_API_KEY')
    
    # =============================================================================
    # Web Application
    # =============================================================================
    
    STREAMLIT_SERVER_PORT: int = int(os.getenv('STREAMLIT_SERVER_PORT', '8501'))
    STREAMLIT_SERVER_ADDRESS: str = os.getenv('STREAMLIT_SERVER_ADDRESS', 'localhost')
    
    API_HOST: str = os.getenv('API_HOST', '0.0.0.0')
    API_PORT: int = int(os.getenv('API_PORT', '8000'))
    
    # =============================================================================
    # Security
    # =============================================================================
    
    SECRET_KEY: str = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
    CORS_ORIGINS: list = os.getenv('CORS_ORIGINS', 'http://localhost:8501,http://localhost:8000').split(',')
    
    # =============================================================================
    # MCP Configuration
    # =============================================================================
    
    MCP_TRANSPORT: str = os.getenv('MCP_TRANSPORT', 'stdio')
    MCP_FIWARE_SERVER_PATH: str = os.getenv('MCP_FIWARE_SERVER_PATH', './vendor/mcp/fiware-mcp-server')
    
    @classmethod
    def validate(cls) -> bool:
        """Validate required configuration."""
        required = [
            ('USERNAME', cls.USERNAME),
            ('PASSWORD', cls.PASSWORD),
        ]
        
        missing = [name for name, value in required if not value]
        
        if missing:
            raise ValueError(f"Missing required environment variables: {', '.join(missing)}")
        
        return True
    
    @classmethod
    def get_fiware_headers(cls, subservice: Optional[str] = None) -> dict:
        """
        Get FIWARE API headers.
        
        Args:
            subservice: Subservice path (defaults to PRISMA)
        """
        headers = {
            'Fiware-Service': cls.SERVICE,
            'Content-Type': 'application/json'
        }
        
        if subservice:
            headers['Fiware-ServicePath'] = subservice
        else:
            headers['Fiware-ServicePath'] = cls.SUBSERVICE_PRISMA
        
        if cls.AUTH_TOKEN:
            headers['X-Auth-Token'] = cls.AUTH_TOKEN
        
        return headers


# Singleton instance
config = Config()


if __name__ == '__main__':
    """Test configuration loading."""
    print("PRISMA Configuration")
    print("=" * 50)
    print(f"Environment: {config.APP_ENV}")
    print(f"Debug: {config.DEBUG}")
    print(f"\nFIWARE Service: {config.SERVICE}")
    print(f"Subservice PRISMA: {config.SUBSERVICE_PRISMA}")
    print(f"Subservice SDMEnvironment: {config.SUBSERVICE_SDMENVIRONMENT}")
    print(f"Username: {config.USERNAME}")
    print(f"\nEndpoints:")
    print(f"  Auth: {config.FIWARE_AUTH_URL}")
    print(f"  Context Broker: {config.FIWARE_CB_URL}")
    print(f"  STH: {config.FIWARE_STH_URL}")
    print(f"  CEP: {config.FIWARE_CEP_URL}")
    print(f"  IoT Agent UL: {config.FIWARE_IOTA_UL_URL}")
    print(f"  IoT Agent JSON: {config.FIWARE_IOTA_JSON_URL}")
    print(f"  IoT Manager: {config.FIWARE_IOTA_MANAGER_URL}")
    print(f"\nToken configured: {'Yes' if config.AUTH_TOKEN else 'No'}")

