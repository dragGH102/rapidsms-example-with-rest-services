# root file of the our app (named app.py by convention)

from rapidsms.apps.base import AppBase

class PingPong(AppBase):

    def handle(self, msg):
        if msg.text == 'ping': # when received msg's text = 'ping' ==> send an answer to the sending number...
            msg.respond('pong') # .. with text 'pong'
            return True
        return False