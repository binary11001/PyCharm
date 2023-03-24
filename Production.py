
from main import *


class production:
    def __init__(self):
        '''

        :param yest_prod: consider this parameter as 70 MT
        :param tody_prod: consider this parameter as 60 MT
        :param yest_req: consider this parameter as 80 MT
        :param tody_req: consider this parameter as 70 MT
        '''

        self.yest_prod = int(input("Yesterday's Production: "))  # yesterday production filled
        self.tody_prod = int(input("Today's Production: "))  # today production filled
        self.yest_req = int(input("Requirement Yesterday: "))     # requirement yesterday
        self.tody_req = int(input("Requirement Today: "))     # requirement today
        self.avg30_prod = None

    def lossInProduction(self):
        self.loss  = (self.yest_req - self.yest_prod) + (self.tody_req - self.tody_prod)
        print("There is about "+ str(self.loss) + "MT"+" amount of requirement pending !")



obj = production()
obj.lossInProduction()