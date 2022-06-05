class Hero():

    def __init__(self, name, health, attack, armor):
        self.name = name
        self.health = health
        self.attack = attack
        self.armor = armor
        print('\n')

    def serang(self, lawan):
        print(self.name + ' Menyerang ' + lawan.name)
        lawan.diserang(self, self.attack)
        print('\n')

    def diserang(self, lawan, attack_lawan):
        print(self.name + ' diserang ' + lawan.name)
        attack_diterima = attack_lawan/self.armor
        print('serangan lawan terasa ' + str(attack_diterima))
        self.health -= attack_diterima
        print('darah ' + self.name + ' tersisa ' + str(self.health))


ucup = Hero('Ucup', 100, 10, 5)
sugianto = Hero('Sugianto', 100, 15, 10)

ucup.serang(sugianto)
sugianto.serang(ucup)
