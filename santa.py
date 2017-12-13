""""Santa Object can do everything santa does!"""
from pycountry import countries
from faker import Faker
import random


class Santa(object):
    """Building an Santa."""

    def __init__(self, kids_name=[], delivery_country=[c.name for c in countries]):
        """Init method."""
        self.faker = Faker()
        self.kids_list = {}
        if kids_name == []:
            for _ in range(100):
                self.kids_list[self.faker.first_name()] = bool(random.getrandbits(1))
        else:
            for kid in range(len(kids_name)):
                self.kids_list[kid] = bool(random.getrandbits(1))

        self.places = delivery_country  # didn't have time to use it

    def prepare_to_land(self, name=None):
        """Decide what gift to give to the kid."""
        if not name:
            name = random.choice(self.kids_list.keys())
        self.curr_kid = name
        getting_gift = self.kids_list[name]
        if getting_gift:
            verb = 'is'
        else:
            verb = 'is not'
        print('Santa is going to ' + name + '\s house, and he/she ' + verb + ' getting a gift')

    def approach_house(self, situation=None):
        """Delivery gift, change mind from yes to no if hostile no to yes if friendly."""
        things = ['dog', 'police', 'milk', 'cookies']
        if not situation:
            if self.kids_list[self.curr_kid]:
                print(self.curr_kid + ' got his gift!')
            else:
                print(self.curr_kid + ' didnt get this gift!')
        if situation == 'dog' or situation == 'police':
            self.kids_list[self.curr_kid] = False
            print(self.curr_kid + ' didn\'t get his gift because of ' + situation)
        elif situation == 'milk' or situation == 'cookies':
            self.kids_list[self.curr_kid] = True
            print(self.curr_kid + ' got his gift since he provided ' + situation)
        else:
            print('must input situation from ' + things)



