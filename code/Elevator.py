# sheesh - sheesh
import time

class ElevatorSettings():    


    
    def __init__(self, numberOfFloors, currentElevatorFloor, myPosition):

        self.numberOfFloors = numberOfFloors
        self.currentElevatorFloor = currentElevatorFloor
        self.myPosition = myPosition


        self.destinationUpList = []
        self.destinationDownList = []
        
        self.downList = []
        self.upList = []

        self.floorToGo = 0
        self.countPeople = 0
        
        self.destinationToGo = 0
        self.direction = 0
        self.userCurrentFloor = 0
        self.userFloor = 0

        self.elevatorSleep = 3
    

    def settingsCheck(self):

        # floors count bllallalalala
        while True:

            try:

                if 1 <= self.numberOfFloors <= 100:
                    break
                else:
                    print('Try another number of floors.')

            except Exception as e:
                print('Failed input. ' + e.__str__())



        # elevator on current floor
        while True:
    
            try:

                if 0 < self.currentElevatorFloor <= self.numberOfFloors:
                    break
                else:
                    print('The floor entered does not exist.')

            except Exception as e:
                print('Failed input ' + e.__str__())


        # current floor
        while True:
            try:
                
                if 0 < self.myPosition <= self.numberOfFloors:
                    break
                else:
                    print('The floor entered does not exist.')

            except Exception as e:
                print('Failed input ' + e.__str__())


        ElevatorSystem.Display(self)
        print("-------------")


''' class ElevatorUser():

    def __init__(self, userName, currentUserFloor, destinationUserFloor):
        self.userName = userName
        self.currentUserFloor = currentUserFloor
        self.destinationUserFloor = destinationUserFloor

        self.currentElevatorFloor = ElevatorSettings(self.currentElevatorFloor)
        self.numberOfFloors = ElevatorSettings(self.numberOfFloors)

        self.direction = ElevatorSettings(self.direction)
        self.elevatorSleep = ElevatorSettings(self.elevatorSleep)

        self.destinationUpList = []
        self.destinationDownList = []
        self.downList = []
        self.upList = []


    def addUser(self):

        if self.currentUserFloor > self.currentElevatorFloor:
            print(self.userName, " is on the %s floor" % self.currentUserFloor)
            self.upList.append(self.currentUserFloor)

        elif self.currentUserFloor < self.currentElevatorFloor:
            print(self.userName, " is on the %s floor" % self.currentUserFloor)
            self.downList.append(self.currentUserFloor)
        
        else:
            print("You are already on this floor.")
 '''

class ElevatorSystem():

    def __init__(self):

        self.currentElevatorFloor = ElevatorSettings(self.currentElevatorFloor)
        self.numberOfFloors = ElevatorSettings(self.numberOfFloors)
        self.myPosition = ElevatorSettings(self.myPosition)

        self.direction = ElevatorSettings(self.direction)
        self.elevatorSleep = ElevatorSettings(self.elevatorSleep)

        self.userFloorToGo = 0
        self.userFloor = 0

        self.destinationUpList = []
        self.destinationDownList = []
        self.upList = []
        self.downList = []


    def takeMe(self):

        print('----- You have called the elevator. Wait. ------')
        print('Elevator is on the %s floor.' % self.currentElevatorFloor)

        if self.currentElevatorFloor != self.myPosition:
            
            if self.currentElevatorFloor <= self.myPosition:
        
                for floor in range(self.currentElevatorFloor + 1, self.myPosition + 1):
                    time.sleep(self.elevatorSleep)
                    print('Elevator is on the %s floor ↑' % floor)


            elif self.currentElevatorFloor >= self.myPosition:

                for floor in range(self.currentElevatorFloor - 1, self.myPosition - 1, -1):
                    time.sleep(self.elevatorSleep)
                    print('Elevator is on the %s floor ↓' % floor)


            self.currentElevatorFloor = self.myPosition
            print('----- Opening doors -----')
            time.sleep(self.elevatorSleep)

            time.sleep(self.elevatorSleep)
            print('----- Cloosing doors -----')
            ElevatorSystem.userToGo(self)
    

    def meToGo(self):

        self.destinationToGo = 6
        #int(input("Where do you need to go? "))
        print("-------------")

        if self.destinationToGo > self.numberOfFloors:
            print('The floor entered does not exist.')

        elif self.myPosition != self.destinationToGo:
                
            if self.myPosition <= self.destinationToGo:
        
                for floor in range(self.myPosition + 1, self.destinationToGo + 1):
                    time.sleep(self.elevatorSleep)
                    print('Elevator is on the %s floor ↑' % floor)


            elif self.myPosition >= self.destinationToGo:

                for floor in range(self.myPosition- 1, self.destinationToGo - 1, -1):
                    time.sleep(self.elevatorSleep)
                    print('Elevator is on the %s floor ↓' % floor)


            self.currentElevatorFloor = self.destinationToGo
            print('----- Opening doors -----')
            time.sleep(self.elevatorSleep)

            time.sleep(self.elevatorSleep)
            print('----- Cloosing doors -----')


    def userToGo(self):

        print("The elevator is on %s floor " % self.currentElevatorFloor)
        self.countPeople = 0
        #int(input("Is anyone enter the elevator here? "))

        if self.countPeople != 0 and self.countPeople >= 0: 

            for i in range(0, self.countPeople):

                self.userFloorToGo = 6
                #int(input("Which floor you need to go? "))

                if self.userFloorToGo > self.currentElevatorFloor:
                    self.upList.append(self.userFloorToGo)
        
                elif self.userFloorToGo < self.currentElevatorFloor:
                    self.downList.append(self.userFloorToGo)


            self.userFloorToGo = 6
            int(input("Where do you need to go? "))

            if self.userFloorToGo > self.currentElevatorFloor:
                self.upList.append(self.userFloorToGo)
    
            elif self.userFloorToGo < self.currentElevatorFloor:
                self.downList.append(self.userFloorToGo)

            else:
                return

            ElevatorSystem.sorting(self)

        else:
            print("else")
            ElevatorSystem.meToGo(self)

    
    def sorting(self):

        if len(self.upList) != 0:

            self.upList.sort()

            print("--------------")

            for floor in self.upList:

                for floors in range(self.currentElevatorFloor + 1, floor + 1):

                    time.sleep(self.elevatorSleep)
                    print('Elevator is on the %s floor ↑' % floors) 
                    
                    if floor == floors:
        
                        print('----- Opening doors -----')
                        time.sleep(self.elevatorSleep)

                        time.sleep(self.elevatorSleep)
                        print('----- Cloosing doors -----')

                        if floors == self.upList[-1]:
                            break

                self.currentElevatorFloor = floor


        elif len(self.downList) != 0:

            self.downList.sort(reverse=True)

            print("--------------")

            for floor in self.downList:
    
                for floors in range(self.currentElevatorFloor - 1, floor - 1, -1):

                    time.sleep(self.elevatorSleep)
                    print('Elevator is on the %s floor ↓' % floors) 
                    
                    if floor == floors:
        
                        print('----- Opening doors -----')
                        time.sleep(self.elevatorSleep)

                        time.sleep(self.elevatorSleep)
                        print('----- Cloosing doors -----')

                        if floors == self.downList[-1]:
                            break

                self.currentElevatorFloor = floor

        else:
            print("ee")


    def Display(self):

        if self.currentElevatorFloor > self.myPosition:

            self.direction == -1

            print("The elevator goes down.")
            print("---------------------")
            ElevatorSystem.takeMe(self)

        elif self.currentElevatorFloor < self.myPosition:

            self.direction == 1

            print("The elevator goes up.")
            print("---------------------")
            ElevatorSystem.takeMe(self)

        else:

            self.direction == 0

            print("The elevator is on this floor.")
            print("---------------------")

            ElevatorSystem.userToGo(self)


def main():

    numberOfFloors = 10
    #int(input("Enter the number of floors of the building: "))
    currentElevatorFloor = 8
    #int(input("Enter the floor where is the elevator now: "))
    myPosition = 3
    #int(input("Which floor are you on? "))
    
    print("--------------")

    elevatorSettings = ElevatorSettings(numberOfFloors, currentElevatorFloor, myPosition)
    #elevatorSystem = ElevatorSystem()

    elevatorSettings.settingsCheck()
    #elevatorSystem.Display()

'''     print("--------------")

    # (name, currentFloor, destinationFloor)
    Mary = ElevatorUser('Mary', 3, 6)
    Jack = ElevatorUser('Jack', 4, 6)

    ElevatorUser.addUser(Mary)
    ElevatorUser.addUser(Jack) '''


if __name__ == '__main__':
    main()
