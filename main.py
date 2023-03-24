# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import datetime,timedelta
from zoneinfo import ZoneInfo
from datetime import timedelta
class WorkingHours(object):
    # avg_prod , startDefault , stopDefault , totalHrs
    def __int__(self,startDefault,avg_prod,stopDefault,totalHrs):
        # self.avg_prod = avg_prod # in MT - Metric Tonnes
        # self.startDefault = startDefault
        # self.stopDefault =stopDefault
        # self.totalHrs =totalHrs
        return

    def defaults(self):
        self.totalWorkers = int(input("Total Workers: ")) # Hardcode
        self.avg_prod=int(70)  # in MT - Metric Tonnes # Hardcode
        self.startDefault="8:00" # Hardcode
        self.startDefault=datetime.datetime.strptime(self.startDefault , '%H:%M')
        self.stopDefault= "18:00" # Hardcode
        self.stopDefault=datetime.datetime.strptime(self.stopDefault , '%H:%M')
        self.totalHrs=self.stopDefault - self.startDefault
        self.allHrs = (self.stopDefault - self.startDefault)* self.totalWorkers
        print("Start Time Default: "+str(self.startDefault))
        print("Stop Time Default: "+str(self.stopDefault))
        print("Number of Hours Worked By Each Worker: ",str(self.totalHrs))


    def current(self):
        self.present = int(input("Enter the Number of Workers Present: "))
        self.date =  (input("Date in yyyy-mm-dd"))
        self.date=datetime.datetime.strptime(self.date,'%Y-%m-%d')
        print("Your Input Date is "+str(self.date))
        self.start=  datetime.datetime.strptime(input("Start Time in HH:MM:"),'%H:%M')
        self.stop=  datetime.datetime.strptime(input("Stop Time in HH:MM:"),'%H:%M')
        self.hrs =  self.stop-self.start
        print((self.hrs)) #self.hrs
        print(self.totalHrs)

    def correction(self):
        # Make sure that function "current" is run
        self.absent = int(self.totalWorkers - self.present)
        self.additional_hrs =(self.absent * self.totalHrs)  # this is for additional hrs for absent workers loss cover
        self.additional_hrs1 = (self.totalHrs - self.hrs) # for loss in work hours in current day
        self.delta = (self.additional_hrs).total_seconds()/3600
        self.delta1 = (((self.additional_hrs1).total_seconds())/3600)*self.present

        if (self.hrs < self.totalHrs) and (self.present < self.totalWorkers):
            print("Less Hours and Less Workers")
            print("Additional" + str((self.delta1/self.present) + (self.delta/self.present)) + " are required by each worker")
        elif (self.hrs < self.totalHrs) and (self.present == self.totalWorkers):
            print("Work done for less number of Hours")
            print(self.delta1)
            print("Additional "+ str(self.delta1/self.present) + " are required by each worker")
        elif (self.hrs == self.totalHrs) and (self.present < self.totalWorkers):
            print("Work done for less number of Persons for same hours")
            print("Additional "+ str(self.delta/self.present) + " are required by each worker of count "+ str(self.present))
            print(self.delta)
        elif (self.hrs>=self.totalHrs) and (self.present==self.totalWorkers):
            print("Thank You, Your Work variables are perfect!")
        else:
            raise RuntimeError

    def timeVariabe(self):
        self.absent=int(self.totalWorkers - self.present)
        self.additional_hrs=(self.absent * self.totalHrs)
        self.additional_hrs1=(self.totalHrs - self.hrs)
        print("=============================")
        print(self.absent)
        print(self.additional_hrs)
        print(self.additional_hrs1)

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




energon = WorkingHours()
energonProd = production()

energon.defaults()
energon.current()
energon.correction()
energonProd.lossInProduction()
if __name__ == '__main__':
    print('PyCharm')
    # print(energon.startDefault)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
