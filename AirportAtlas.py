import itertools 
import math
import csv
from Airport import Airport
from Currency import Currency
from CountryCurrency import Countrycurrency
import numpy as np
import time


class AirportAtlas:
    __airportDict = {}
    __myAirports=[]
    airport_objs=[]
    airport_object={}

    def __init__(self, csvFile):
        self.readCsv('airportcsv.csv')
        
    def readCsv(self, csvFile):
        try:
            with open('airportcsv.csv') as file:
                reader=csv.reader(file)
                next(reader,None)#skip header
                for row in reader:
                      
                    self.__airportDict[row[4]] = {'Code':row[4], 'AirportID':row[0],
                    'AirportName':row[1],'Cityname':row[2], 'Country':row[3], 'lat':row[6],'long':row[7]}
                       
        except FileNotFoundError:
            print('file not found')



    

    def calculate_distance (self,lat1,long1,lat2,long2):
       rad = math.pi/180
       earthrad = 6371
    


       distance_1 = (90-float(lat1))*rad
       distance_2 = (90-float(lat1))*rad

       distance_3 = float(long1)*rad
       distance_4 = float(long2)*rad

       formula = math.acos(math.sin(distance_1)*math.sin(distance_2)*math.cos(distance_3-distance_4) +math.cos(distance_1)*math.cos(distance_2))
       answer= formula*earthrad

       return answer 


    def getAirportDistance(self,code1,code2):

            
            airport_1 = Airport
            airport_2 = Airport

            airport_1=Airport.createInstance(airport_1,code1)
            airport_2=Airport.createInstance(airport_2,code2)

      


        #my airport data is in tuple (code,lat,long,ID,Country,city,name) so i acess the values by index
            lat1  = airport_1[1]
            long1 = airport_1[2]
            lat2  = airport_2[1]
            long2 = airport_2[2]
            
            #print("information on airport:",code1,airport_1,"\ninformation on airport:",code2,airport_2)
      
            return  (self.calculate_distance(lat1, long1, lat2, long2))


    def calculate_trip(self,code1,code2,code3,code4):

        
        depart_home = Airport
        airport_2 = Airport
        airport_3 = Airport
        airport_4 = Airport
        return_home = Airport

        depart_home=depart_home.createInstance(depart_home,code1)
        airport_2=Airport.createInstance(airport_2,code2)
        airport_3=Airport.createInstance(airport_3,code3)
        airport_4=Airport.createInstance(airport_4,code4)
        return_home=Airport.createInstance(return_home,code1)
        
        print("information on airport 1:",code1,depart_home,"\ninformation on airport 2:",code2,airport_2,"\ninformation on airport 3:",code3,airport_3,"\ninformation on airport 4:",code4,return_home)

        lat1  = depart_home[1]
        long1 = depart_home[2]
        lat2  = airport_2[1]
        long2 = airport_2[2]
        #first_trip=(self.calculate_distance(lat1, long1, lat2, long2))
        #print( first_trip)
        

        lat2  = airport_2[1]
        long2 = airport_2[2]
        lat3 = airport_3[1]
        long3 = airport_3[2]

        #second_trip=(self.calculate_distance(lat2, long2, lat3, long3))
        #return second_trip
        
        
        lat3  = airport_3[1]
        long3 = airport_3[2]
        lat4 = airport_4[1]
        long4 = airport_4[2]

        #third_trip=(self.calculate_distance(lat3, long3, lat4, long4))
        #print ("third trip distance:",third_trip)

       

        lat4 = airport_4[1]
        long4 = airport_4[2]
        lat5 = return_home[1]
        long5= return_home[2]

        #fourth_trip=(self.calculate_distance(lat4, long4, lat5, long5))
        #print ("fourth trip distance:",fourth_trip)

        #final_distance = third_trip + second_trip +first_trip+fourth_trip
        #print("the final distance between airports is:",final_distance)

    def possibleTrips(self,home, airport_2,airport_3,airport_4,airport_5):
        start_time=time.time()

         #creates a list of tuples with all possible permutations:
        trips_possible_1 = list(itertools.permutations([home,airport_2,airport_3,airport_4,airport_5], 5))
        print(trips_possible_1)
        print(len(trips_possible_1))

    

        total_trip_costs = []

        for tuple_values in trips_possible_1:
            tuple_values = list(tuple_values)
            #make it so we always leave from home
            # list(tuple_values).insert(0,home)
            #make it so we always return to home
            # tuple_values.insert(5,home)
            #actually can just append the first value ->wont have to del a value later
            tuple_values.append(tuple_values[0])
           
            
            print("Possible permutation:", tuple_values)

            #creating lists to store my trips later
            total_distance_list=[]   
            trips=[]
            total_cost = 0

            convert=Currency
           
            pound = Currency
            dollar = Currency
            calculate = AirportAtlas("airport.csv")
            pound = Currency.FindConversion(Currency,'GBP')
            dollar = Currency.FindConversion(Currency,'USD')

           
            trip_1=calculate.getAirportDistance(tuple_values[0],tuple_values[1])
            #print(trip_1)

            trip_1=float(trip_1)
            cost1=trip_1
           
            total_cost += cost1 
            #cost is in euro as it fuels in Dublin
            #print(trip_1)
      
            trip_2=calculate.getAirportDistance(tuple_values[1],tuple_values[2])

            trip_2=float(trip_2)
            cost2=trip_2*pound
            
            total_cost += cost2
            #cost is in pounds as it fuels in London


            trip_3=calculate.getAirportDistance(tuple_values[2],tuple_values[3])
            trip_3=float(trip_3)
          
            cost3=trip_3*dollar
            
            total_cost += cost3
            #cost is in Dollars as it fuels in New york

            trip_4=calculate.getAirportDistance(tuple_values[3],tuple_values[4])
            trip_4=float(trip_4)
           
            cost4=trip_4*pound
            
            total_cost += cost4
            #cost is in pounds as it fuels again back in london
    
            trip_5=calculate.getAirportDistance(tuple_values[4],tuple_values[0])
            
         
            cost5=float(trip_5)
            total_cost += cost5
            #back in dublin so EURO

            #print(total_cost)

         
            
            #print (total_cost, tuple_values)
            
                
            total_trip_costs.append([total_cost, tuple_values])

            #print(total_trip_costs)
            
            np.total_trip_costs=total_trip_costs
            total_trip_costs = sorted(total_trip_costs, key=lambda total_trip_costs_entry: total_trip_costs_entry[0])
        #alot of the first values are returning 0 so I will try to remove all elements in array total_trip_costs where total_cost = 0

        #print(total_trip_costs)  
           
            
        #print("The the most optimum (cheapest) itenerary in the list for a 5 flight simulation is:", total_trip_costs[0])
        #print ()
        #print ("The least optimum (most expensive) itenerary for a 5 flight simulation is:", total_trip_costs[-1])
             #alot of the first values are returning total cost is 0 or 47 so I write the conditional in 267
             #found the error in an earlir line

            


            


            # print("the minimum cost journey is:", minimumCost)

            # print("the maximum cost journey is:", maximumCost)

            

        #calculating with a 6th trip
        trip_6 = calculate.getAirportDistance(tuple_values[4],tuple_values[2])
        total_cost+=trip_6

        total_trip_costs.append([total_cost, tuple_values])

        #print(total_trip_costs)
            
        np.total_trip_costs=total_trip_costs
        total_trip_costs = sorted(total_trip_costs, key=lambda total_trip_costs_entry: total_trip_costs_entry[0])
        

        print ("----------------------------------------------------")
           
            
        print("The most optimum  (cheapest) itenerary  for a 6 flight simulation is:", total_trip_costs[0])
        print()
        print ("The most least optimum (most expensive) itenerary for a 6 flights simulation is:", total_trip_costs[-1])











   



  
             


