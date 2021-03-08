class Player:
    def __init__(self, name, endurance, sprint, dribble, passing, shooting):
        self.shooting = shooting
        self.passing = passing
        self.dribble = dribble
        self.sprint = sprint
        self.endurance = endurance
        self.name = name

    @property
    def shooting(self):
        return self.__shooting

    @shooting.setter
    def shooting(self, value):
        self.__shooting = value

    @property
    def passing(self):
        return self.__passing

    @passing.setter
    def passing(self, value):
        self.__passing = value

    @property
    def dribble(self):
        return self.__dribble

    @dribble.setter
    def dribble(self, value):
        self.__dribble = value

    @property
    def sprint(self):
        return self.__sprint

    @sprint.setter
    def sprint(self, value):
        self.__sprint = value

    @property
    def endurance(self):
        return self.__endurance

    @endurance.setter
    def endurance(self, value):
        self.__endurance = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def __str__(self):
        return f"Player: {self.__name}\nEndurance: {self.__endurance}\n" \
               f"Sprint: {self.__sprint}\nDribble: {self.__dribble}\nPassing: " \
               f"{self.__passing}\nShooting: {self.__shooting}\n"
