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

    def Count_Crit(self):
        return self.accuracy * self.luck * self.attack_speed



def main():
    Char1 = Character(9, 83, 0.4, 0.8, 2, 1.4, 14, 34)
    Char2 = Character(4, 98, 0.6, 1, 4, 1.1, 20, 15)

    if abs(Char1.hp / (Char2.Dps() * (1 - Char1.armor/100)) - Char2.hp / (Char1.Dps() * (1 - Char1.armor/100))) > 4:
        if Char1.hp / Char2.Dps() < Char2.hp / Char1.Dps():
            print("Char2 win ever")
        else:
            print("Char1 win ever")
    else:
        if Char1.Count_Crit() > Char2.Count_Crit():
            Char1.number += 1
        else:
            Char2.number += 1
        if (Char1.hp - Char1.fear) / Char2.Dps() > (Char2.hp - Char2.fear) / Char1.Dps():
            Char1.number += 1
        else:
            Char2.number += 1
        if Char1.hp * Char1.armor / 100 > Char2.hp * Char2.armor / 100:
            Char1.number += 1
        else:
            Char2.number += 1


main()