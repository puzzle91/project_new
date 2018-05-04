
#from Airport import Airport
from AirportAtlas import AirportAtlas 


def main():
         
        
        

        # Code1=input('what is the first airport?').upper()
        # Code2=input('what is the second airport?').upper()
        # Code3=input('what is the third airport?').upper()
        # Code4=input('What is the the fourth airport').upper()
        # Code5=input('What is the the fifth airport').upper()

       
    
        Tester = AirportAtlas
        # Tester=  Tester.possibleTrips(Tester, Code1, Code2, Code3, Code4,Code5)
        Tester=  Tester.possibleTrips(Tester, "DXB", "STN", "LHR","JFK","CDG")
        print("here")
        print(Tester)
        # airportTest = Airport

        # airportTest = Airport.createInstance(airportTest, Code1)
       # Tester2 = AirportAtlas

       # Tester2 = Tester2.calculate_trip(Tester2,Code1,Code2,Code3,Code4)   
      
       # (Tester2)
        #Tester3 = AirportAtlas
        #Tester3 = Tester3.possibleTrips(Tester3,Code1,Code2,Code3,Code4,Code1)

      
       


main()


