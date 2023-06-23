from flask_socketio import SocketIO,Namespace
#websocket扩展
def websocket(app):
    global socketio 
    socketio = SocketIO(app=app,cors_allowed_origins='*')
    socketio.on_namespace(SocketEvent('/wechat'))

    return socketio

class SocketEvent(Namespace):
    def __init__(self, namespace=None):
        super().__init__(namespace)

    def on_connect(self):
        print('websocket is connect')

    def on_disconnect(self):
        print('websocket is disconnect')
    
    def on_message(self,data):
        print(f"收到客户端的消息:{data['data']}")
        socketio.emit('response',{'data':data['data']},namespace='/wechat')
    
    