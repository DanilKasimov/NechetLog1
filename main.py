import random as rnd


class Character:
    damage = 0.0
    hp = 0.0
    luck = 0.0
    accuracy = 0.0
    attack_speed = 0.0
    crit_power = 0.0
    fear = 0.0
    armor = 0.0
    number = 0

    def __init__(self, d, h, l, a, a_s, cp, f, arm):
        self.damage = d
        self.hp = h
        self.luck = l
        self.accuracy = a
        self.attack_speed = a_s
        self.crit_power = cp
        self.fear = f
        self.armor = arm
        self.number = 0

    def Dps(self):
        return self.damage * self.attack_speed * self.accuracy + \
               self.damage * self.crit_power * self.accuracy * self.attack_speed * self.luck

    def CountCritic(self):
        return self.accuracy * self.luck * self.attack_speed


def Prediction(char1, char2):
    if abs(char1.hp / (char2.Dps() * (1 - char1.armor / 100)) - char2.hp / (char1.Dps() * (1 - char1.armor / 100))) > 4:
        if char1.hp / char2.Dps() < char2.hp / char1.Dps():
            return "Char2 win ever"
        else:
            return "Char1 win ever"
    else:
        if char1.CountCritic() > char2.CountCritic():
            char1.number += 1
        else:
            char2.number += 1
        if (char1.hp - char1.fear) / char2.Dps() > (char2.hp - char2.fear) / char1.Dps():
            char1.number += 1
        else:
            char2.number += 1
        if char1.hp * char1.armor / 100 > char2.hp * char2.armor / 100:
            char1.number += 1
        else:
            char2.number += 1
        if char1.luck * char1.accuracy > char2.luck * char2.accuracy:
            char1.number += 1
        else:
            char2.number += 1
        if char1.number > char2.number:
            return "Char1 will win with a {0}% chance".format(char1.number / 4 * 100)
        else:
            return "Char2 will win with a {0}% chance".format(char2.number / 4 * 100)


def StepOfFight(char1, char2):
    for i in range(char1.attack_speed):
        if char1.accuracy > rnd.random():
            if char1.luck > rnd.random():
                char2.hp -= char1.damage * char1.crit_power * (1 - char1.armor / 100)
            else:
                char2.hp -= char1.damage * (1 - char1.armor / 100)


def Fight(char1, char2):
    while True:
        StepOfFight(char1, char2)
        StepOfFight(char2, char1)


def main():
    Char1 = Character(9, 83, 0.4, 0.8, 2, 1.4, 14, 34)
    Char2 = Character(4, 98, 0.6, 1, 4, 1.1, 20, 15)
    print(Prediction(Char1, Char2))


main()
