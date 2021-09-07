class Character:

    damage = 0.0
    hp = 0.0
    luck = 0.0
    accuracy = 0.0
    attack_speed = 0.0
    crit_power = 0.0
    fear = 0.0
    armor = 0.0

    def __init__(self, d, h, l, a, a_s, cp, f, arm):
        self.damage = d
        self.hp = h
        self.luck = l
        self.accuracy = a
        self.attack_speed = a_s
        self.crit_power = cp
        self.fear = f
        self.armor = arm

    def Dps(self):
        return self.damage * self.attack_speed * self.accuracy + \
               self.damage * self.crit_power * self.accuracy * self.attack_speed * self.luck


def main():
    Char1 = Character(9, 83, 0.4, 0.8, 2, 1.4, 14, 34)
    Char2 = Character(4, 98, 0.6, 1, 4, 1.1, 20, 15)

    print(Char1.Dps())
    print(Char2.Dps())


main()