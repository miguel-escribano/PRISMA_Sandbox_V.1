"""Start PRISMA MVP - MCP Server + Streamlit."""
import subprocess
import sys
import socket
import os

# =============================================================================
# CONFIG
# =============================================================================

MCP_SERVER_PATH = r"C:\Users\migue\FIWARE-MCP-Server-Auth-Miguel"
MCP_PORT = 5002
STREAMLIT_PORT = 8501
STREAMLIT_APP = "streamlit/app.py"

# =============================================================================
# HELPERS
# =============================================================================

def is_port_open(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('127.0.0.1', port)) == 0
    sock.close()
    return result

# =============================================================================
# START MCP SERVER (opcional)
# =============================================================================

if is_port_open(MCP_PORT):
    print(f"[OK] MCP Server already running on http://127.0.0.1:{MCP_PORT}/mcp")
elif os.path.exists(MCP_SERVER_PATH):
    print(f"Starting MCP Server on port {MCP_PORT}...")
    subprocess.Popen(
        [sys.executable, 'server.py', '--http', '--port', str(MCP_PORT)],
        cwd=MCP_SERVER_PATH,
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )
    print(f"[OK] MCP Server starting at http://127.0.0.1:{MCP_PORT}/mcp")
else:
    print(f"[!] MCP Server path not found, skipping: {MCP_SERVER_PATH}")

# =============================================================================
# START STREAMLIT
# =============================================================================

if is_port_open(STREAMLIT_PORT):
    print(f"[OK] Streamlit already running on http://localhost:{STREAMLIT_PORT}")
else:
    if os.path.exists(STREAMLIT_APP):
        print(f"Starting Streamlit on port {STREAMLIT_PORT}...")
        subprocess.Popen(
            [sys.executable, '-m', 'streamlit', 'run', STREAMLIT_APP, 
             '--server.port', str(STREAMLIT_PORT),
             '--server.headless', 'true'],
            creationflags=subprocess.CREATE_NEW_CONSOLE
        )
        print(f"[OK] Streamlit starting at http://localhost:{STREAMLIT_PORT}")
    else:
        print(f"[!] Streamlit app not found: {STREAMLIT_APP}")

print("\nPRISMA MVP ready")
