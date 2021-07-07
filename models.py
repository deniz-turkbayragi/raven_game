from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Huanren Zhang'

doc = """
Raven's progressive matrices test measuring cognitive ability (Turkish)
"""


class Constants(BaseConstants):
    name_in_url = 'raven'
    players_per_group = None
    minutes_given = 8
    payment_per_question = 1
    payment_in_points = 3
    num_rounds = 23
    answer_keys = [4, 1, 6, 1, 5, 2, 1, 5, 4, 8, 3, 7, 7, 1, 3, 8, 5, 1, 7, 8, 1, 1, 3]
    instructions_template = 'raven/Instructions.html'


class Subsession(BaseSubsession):
    def creating_session(self):
        # this is run before the start of every round
        if self.round_number == 1:
            for p in self.get_players():
                p.participant.vars['payoff_ravens'] = 0


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    answer = models.IntegerField(choices=[1,2,3,4,5,6,7,8], widget=widgets.RadioSelect)

    ans_correct = models.BooleanField()
    raven_total_correct = models.IntegerField(
        initial=0,
    )

    def set_payoffs(self):

        self.raven_total_correct = sum([self.ans_correct for self in self.in_all_rounds()])
        print("RAVEN: Total number of correct answers:", self.raven_total_correct)



