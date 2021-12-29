
class Functions:

    @staticmethod
    def sayhello(object):
        return ('[SERVER RESPONSE]',"Hello there, you've connect to server, you did it !")

    @staticmethod
    def saygoodbye(object):
        return ('[SERVER RESPONSE]',"Oh no, connection has been closed, see you next time")

    @staticmethod
    def saysth(object):
        return ('[SERVER RESPONSE]',"You've just say {object[1]}" , f"But you should say it fucking loud: {object[1].upper()}")
    
    @staticmethod
    def add(object):
        return ('[SERVER RESPONSE]',object[1] + object[2])
    
    @staticmethod
    def multiply(object):
        return ('[SERVER RESPONSE]',object[1] * object[2])
    
    @staticmethod
    def open_browser(object):   
        import webbrowser as wb
        wb.open_new_tab('https://github.com/kruksik-dev/MCORD_NEW_GUI')
        return ('[SERVER RESPONE]','https://github.com/kruksik-dev/MCORD_NEW_GUI')
    

Functions_table = {
    
    'say_hello' : Functions.sayhello,
    'say_goodbye' : Functions.saygoodbye,
    'say_sth' : Functions.saysth,
    'add' : Functions.add,
    'multiply' : Functions.multiply,
    'open_browser' : Functions.open_browser
}

