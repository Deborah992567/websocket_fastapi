from fastapi import WebSocket

# connects different users 
class ConnectManager:
    def __init__(self):
        self.active_connection :dict[str ,WebSocket] = []
        
        async def Connect(self ,username , websocket:WebSocket):
            await websocket.accept()
            self.active_connection[username] =websocket
            
        async def disconnect(self , username ,websocket:WebSocket):
            self.active_connection.pop(username ,None)
            
        async def  personal_info(self , message:str , username:str ):
            websocket = self.active_connection.get(username)
            if websocket:
                await websocket.send_text(message)
            
        async def broadcast(self , message:str):
            for connection in self.active_connection:
                await connection.send_text(message)