# Multiple inheritence

class Predator:
    def hunt(self):
        print('Time to hunt.')


class Prey:
    def run(self):
        print('Time to escape')


class Lion(Predator):
    pass


class Deer(Prey):
    pass


class Cheetah(Predator, Prey):
    pass


lion = Lion()
deer = Deer()
cheetah = Cheetah()

lion.hunt()
deer.run()
cheetah.run()
cheetah.hunt()
