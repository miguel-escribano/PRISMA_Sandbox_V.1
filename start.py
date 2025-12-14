"""Start PRISMA MVP - Streamlit App."""
import subprocess
import sys
import socket
import os

# =============================================================================
# CONFIG
# =============================================================================

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
