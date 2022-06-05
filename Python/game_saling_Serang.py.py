import sys


class Hero:
    jumlah = 0

    def __init__(self, name, health, attack, armor):
        self.name = name
        self.health = health
        self.attack = attack
        self.armor = armor
        Hero.jumlah += 1

    def serang(self, lawan):
        print(self.name + ' menyerang ' + lawan.name)
        lawan.diserang(self, self.attack)

    def diserang(self, lawan, attack_lawan):
        print(self.name + ' diserang ' + lawan.name)
        attack_diterima = attack_lawan/self.armor
        print('Serangan terasa ' + str(attack_diterima))
        self.health -= attack_diterima
        print('darah ' + self.name + ' tersisa ' + str(self.health))


ucup = Hero('Ucup', 100, 10, 5)
bambang = Hero('Bambang', 100, 5, 10)

ucup.serang(bambang)
bambang.serang(ucup)
input("Klik Enter To Quit....")
sys.exit()
