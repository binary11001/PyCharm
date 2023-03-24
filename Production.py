
class Production:
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

    def lossInProduction(self , prod=None):
        self.loss  = (self.yest_req - self.yest_prod) + (self.tody_req - self.tody_prod)
        self.lossToday =(self.tody_req - self.tody_prod)
        self.lossYest = (self.yest_req - self.yest_prod)
        print("There is about "+ str(self.loss) + "MT"+" amount of requirement pending !")
        if (self.yest_prod != self.yest_req) and (self.tody_prod != self.tody_req):
            print("You Have a Pending Production Loss of "+ str(self.loss)+ "MT for yesterday & Today !")
        elif (self.yest_prod == self.yest_req) and (self.tody_prod != self.tody_req):
            print("You Have Pending Production Loss For today of "+ str(self.lossToday)+"MT")
        elif (self.yest_prod != self.yest_req) and (self.tody_prod == self.tody_req):
            print("You Have Pending Production Loss For yesterday of " + str(self.lossYest)+"MT")




prod = Production()
prod.lossInProduction()