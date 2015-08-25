# IMPORTANT: this file goes at project-level since we lod it with myhandlers...."

from rapidsms.contrib.handlers import KeywordHandler
from rapidsms.contrib.handlers import PatternHandler

# logging
import logging
logger = logging.getLogger(__name__)
logging.basicConfig(filename="python_log.log",level=logging.INFO) # (?) if level = logging.DEBUG print ALSO debug info even when I don't explicitly use the logger
# logger usage ==> logging.info('So should this') / logging.debug('So should this')


help_text = {
    'sum': 'Write X plus Y to get the result of the addiction',
    'sub':  'Write X sub Y to get the result of the subtraction',
    'mult':  'Write X mby Y to get the result of the multiplication',
    'div':  'Write X dby Y to get the result of the division',
}


class HelpHandler(KeywordHandler):
    keyword = "help"

    def help(self):
        """Invoked if someone just sends `HELP`.  We also call this
        from `handle` if we don't recognize the arguments to HELP.
        """
        self.respond("Allowed commands are SUM, SUB, MULT, DIV. Send "
                     "HELP <command> for more help on a specific command."
                     "(only INTEGERS are supported in this version)")

    def handle(self, text):
        """Invoked if someone sends `HELP <any text>`"""
        text = text.strip().lower() # lower() = convert to lower case
        if text == 'sum':
            self.respond(help_text['sum'])
        elif text == 'sub':
            self.respond(help_text['sub'])
        elif text == 'mult':
            self.respond(help_text['mult'])
        elif text == 'div':
            self.respond(help_text['div'])
        else:
            self.help()


class CalcHandler(PatternHandler):
    pattern = r'^(\d+) (\w+) (\d+)' # \w match string, of 1+ length (+) <-- this part is delimited by parenthesis () to capture it a "word" rather than single chars
    # to use pars from pattern: %d etc.

    def handle(self, a, op, b):
        a, op, b = int(a), str(op).strip().lower(), int(b)

        if op == 'sum':
            total = a + b
        elif op == 'sub':
            total = a - b
        elif op == 'mby':
            total = a * b
        elif op == 'dby':
            if (b == 0):
                return False # TODO: when returning false, the default handler ("message not understood") is not called
            total = a / b
        else:
            return False # forward to default handler to tell the message was not understood

        self.respond(
            "Result: %d" %
            (total)) # parameters to be used in the response string
        return True