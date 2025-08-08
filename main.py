from fastapi import FastAPI , HTTPException , WebSocket
from fastapi.responses import HTMLResponse

app  = FastAPI()

html = """
<html>
    <body>
        <h1>WebSocket Chat</h1>
        <textarea id="chat" cols="30" rows="10"></textarea><br/>
        <input id="msg" type="text"/>
        <button onclick="sendMsg()">Send</button>

        <script>
            const ws = new WebSocket("ws://localhost:8000/ws");

            ws.onmessage = function(event) {
                document.getElementById('chat').value += '\\n' + event.data;
            };

            function sendMsg() {
                let msg = document.getElementById("msg").value;
                ws.send(msg);
                document.getElementById("msg").value = "";
            }
        </script>
    </body>
</html>
"""


@app.get("/")
def get_html():
    return HTMLResponse(html)

@app.websocket("/web-socket")
async def webSocket_create(webscoket:WebSocket):
    await webscoket.accept()
    while True:
        data = await webscoket.receive()
        await webscoket.send_text(f"server says {data}")
    