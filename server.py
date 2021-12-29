import socket
import threading
import json
from funcs import Functions_table



class Server:
    def __init__(self, port, name) -> None:
        self.port = port
        self.disconnect_msg = "!disconnect"
        self.buffer_size = 1024
        self.name = name
        self.startup_notif()
        self.runflag = False
        self.server_thread = None
      
        
        
    def __str__(self) -> str:
        return f'[SERVER_NAME]: {self.name} [ADDRESS]: {self.addr}'

    @staticmethod
    def send_msg(cl, msg):
        cl.sendall((json.dumps(msg)).encode("utf8"))

  
    def colorized(color):
        def wrapper(func):
            style = {
                'black' : '\033[30m',
                'red' : '\033[31m',
                'green' : '\033[32m',
                'yellow' : '\033[33m',
                'blue' : '\033[34m',
                'magenta' : '\033[35m',
                'cyan' : '\033[36m',
                'white' : '\033[37m',
                'UNDERLINE' : '\033[4m',
                'RESET' : '\033[0m'
            }
            def inner_wrapper(self,*args,**kwargs):
                result = style[color] + func(self,*args,**kwargs) + style['RESET']
                print(result)    
            return inner_wrapper 
        return wrapper
        
    @colorized('green')
    def startup_notif(self):
        return (f'[SERVER INFO] Server is starting ... ')
    
    @colorized('blue')
    def listening_notif(self,addr):
        return (f'[SERVER INFO] Server is listening in on {addr} ... ')
        
    @colorized('cyan')
    def client_connected_nofif(self,addr):
        return (f"[NEW CONNECTION] {addr} connected ")
    
    @colorized('red')
    def client_disconnected_nofif(self,addr):
        return (f"[END CONNECTION] {addr} disconnected ")
        
    @colorized('white')   
    def command_notif(self,command):
        return (f"[COMMAND] {command}")


       
    def handle_client(self):
        self.serv_destin = socket.gethostbyname(socket.gethostname())
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.addr = (self.serv_destin,self.port)
        self.server.bind(self.addr)
        self.server.listen(1)
        self.listening_notif(self.addr)
        while self.runflag:
            client,cliend_addr = self.server.accept()
            self.client_connected_nofif(cliend_addr)
            Server.send_msg(client,(f'Client conncted with {self} '))
            while True:
                try:
                    msg = client.recv(self.buffer_size)
                except Exception as e:
                    res = ('[ERROR]',str(e))
                    break 
                
                try:
                    command =json.loads(msg)
                    self.command_notif(command[0])
                    if command[0] == self.disconnect_msg :
                        self.client_disconnected_nofif(cliend_addr)
                        break
                    res = Functions_table[command[0]](command)
                except Exception as e:
                    res = ('[ERROR]',str(e)) 
                
                Server.send_msg(client,res)
                
            client.close()
            
                
            
    def run(self):
        if self.server_thread: raise(Exception("[SERVER INFO] Server is already running ..."))
        self.runflag = True
        thread = threading.Thread(target=self.handle_client)
        thread.start()
           


srv = Server(5555, 'Kruksik_server') 
srv.run()   
        
            
    
    
    
    
            
    
    
    
        
        
        
        
                