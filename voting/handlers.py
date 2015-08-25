# voting/handlers.py

from rapidsms.contrib.handlers import KeywordHandler
from django.db.models import F # used to refer to a Model field by F() in Django

from .models import Choice


class ResultsHandler(KeywordHandler):
    keyword = "results"

    def help(self):
        """help() gets invoked when we get the ``results`` message
        with no arguments"""
        # Build the response message, one part per choice
        parts = []
        for choice in Choice.objects.all(): # for each choice...
            part = "%s: %d" % (choice.name, choice.votes) # generate a string element from choice's fields in database
            parts.append(part)
        # Combine the parts into the response, with a semicolon after each
        msg = "; ".join(parts) # . = merge strings with ";" between each of them
        # Respond
        self.respond(msg)

    def handle(self, text):
        """This gets called if any arguments are given along with
        ``RESULTS``, but we don't care; just call help() as if they
        passed no arguments"""
        self.help()

class VoteHandler(KeywordHandler):
    keyword = "vote"

    def help(self):
        """Respond with the valid commands.  Example response:
        ``Valid commands: VOTE <Moe|Larry|Curly>``
        """
        choices = "|".join(Choice.objects.values_list('name', flat=True)) # values_list = return Model as dictionaries (string form) as single value (flat = True) rathen than one-tuples
        self.respond("Valid commands: VOTE <%s>" % choices)

    def handle(self, text):
        text = text.strip()
        # look for a choice that matches the attempted vote
        try:
            choice = Choice.objects.get(name__iexact=text) # __iexact = exactly equal to...
        except Choice.DoesNotExist:
            # Send help
            self.help()
        else:
            # Count the vote. Use update to do it in a single query
            # to avoid race conditions.
            Choice.objects.filter(name__iexact=text).update(votes=F('votes')+1) # filter choice ==> update corresponding fields
            self.respond("Your vote for %s has been counted" % text)