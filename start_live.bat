@echo off
echo Starting CineMatch Movie Recommendation Server...
start "" ".\venv\Scripts\uvicorn.exe" backend.main:app --host 127.0.0.1 --port 8000
timeout /t 3 >nul
echo Starting Cloudflare Live Tunnel...
start "" ".\cloudflared.exe" tunnel --url http://127.0.0.1:8000
echo Both the server and live tunnel are running!
echo Check the Cloudflare terminal window for your live public HTTPS link.
