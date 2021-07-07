from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        if self.subsession.round_number == 1:
            yield (pages.IntroVideo)
        yield (pages.QuestionPage, {'answer': Constants.answer_keys[self.subsession.round_number-1]})
        # if self.subsession.round_number == Constants.num_rounds:
        #     yield (pages.Results)
        if self.subsession.round_number == 23:
            yield (pages.End)
