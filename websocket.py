from fastapi import WebSocket

# connects different users 
class ConnectManager:
    def __init__(self):
        self.active_connection = list[WebSocket] = []
        
        async def Connect(self , websocket:WebSocket):
            await websocket.accept()
            self.active_connection.append(websocket)
            
        async def disconnect(self , websocket:WebSocket):
            self.active_connection.remove(websocket)
            
        async def broadcast(self , message:str):
            for connection in self.active_connection:
                await connection.send_text(message)