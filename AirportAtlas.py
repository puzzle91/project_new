import itertools 
import math
import csv
from typing import Mapping,Iterable
import random
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

      

#        airport_1 = airport_1(Mapping[str,str],[str,int],[str,str],[str,str],[str,str],[str,float],[str,float])
#        airport_2 = airport_2(Mapping[str,str],[str,int],[str,str],[str,str],[str,str],[str,float],[str,float])
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

        # trips_possible_1 = [list(i) for i in trips_possible_1]
        # #second trip
        # trips_possible_2 = list(itertools.permutations([home,airport_2,airport_3,airport_4,airport_5], 5))

        # trips_possible_2 = [list(i) for i in trips_possible_2]

        # #third trip
        # trips_possible_3 = list(itertools.permutations([home,airport_2,airport_3,airport_4,airport_5], 5))

        # trips_possible_3 = [list(i) for i in trips_possible_3]

        #  #fourth trip
        # trips_possible_4 = list(itertools.permutations([home,airport_2,airport_3,airport_4,airport_5], 5))

        # trips_possible_4 = [list(i) for i in trips_possible_4]

        #  #fifth trip
        # trips_possible_5 = list(itertools.permutations([home,airport_2,airport_3,airport_4,airport_5], 5))

        # trips_possible_5 = [list(i) for i in trips_possible_5]

        #potential legs based on trips
        # first_leg=list(trips_possible_1)

        # second_leg = list(trips_possible_2)

        # third_leg = list(trips_possible_3)

        # fourth_leg = list(trips_possible_4)

        # fifth_leg= list(trips_possible_5)

        #make trips_possible into a full list:
        #max_possible_permuations = list(trips_possible_1 + trips_possible_2+ trips_possible_3,trips_possible_4+trips_possible_5)
        #I assume that the airport has one main flight leg between two airports at close proximity and travels between them#
        # main_leg = list(itertools.permutations([first_leg,second_leg,third_leg,fourth_leg,fifth_leg], 2))
        # return("potential main leg:", main_leg)

        # max_possible_permuations = list(fifth_leg + fourth_leg + third_leg +second_leg+first_leg)
        #return (max_possible_permuation)    
        #Change it from being a list of tuples into a list of lists where the ith element
        #  is the list inside the list(so we can calcuate leg journeys)

        total_trip_costs = []

        for tuple_values in trips_possible_1:
            tuple_values = list(tuple_values)
            #make it so we always leave from home
            # list(tuple_values).insert(0,home)
            #make it so we always return to home
            # tuple_values.insert(5,home)
            #actually can just append the first value ->wont have to del a value later
            tuple_values.append(tuple_values[0])
           
            
            print(tuple_values)

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
            trips.append(trip_1)
            cost1=trip_1
           
            total_cost += trip_1 
            #cost is in euro as it fuels in Dublin
            #print(trip_1)
      
            trip_2=calculate.getAirportDistance(tuple_values[1],tuple_values[2])

            trip_2=float(trip_2)
            trips.append(trip_2)
            cost2=trip_2*pound
            
            total_cost += trip_2
            #cost is in pounds as it fuels in London


            trip_3=calculate.getAirportDistance(tuple_values[2],tuple_values[3])
            trip_3=float(trip_3)
            trips.append(trip_3)
            cost3=trip_3*dollar
            
            total_cost += trip_3
            #cost is in Dollars as it fuels in New york

            trip_4=calculate.getAirportDistance(tuple_values[3],tuple_values[4])
            trip_4=float(trip_4)
            trips.append(trip_4)
            cost4=trip_4*pound
            
            total_cost += trip_4
            #cost is in pounds as it fuels again back in london
    
            trip_5=calculate.getAirportDistance(tuple_values[4],tuple_values[0])
            # trip_5=float(trip_5)
            # trips.append(trip_5)
            # cost5=int(trip_5)
            total_cost += trip_5
            #back in dublin

            print(total_cost)

            all_triplist = trips[:]

            minimum_distance=min(trips) #Min distance route is the optimum route for the 5 plane problem for is little currency
            # fluctuation between the airports/countries I am using (JFK, LHR, DUB, CDG) as Dublin also always occurs at least twice. 
            maximum_distance=max(trips)
            #print("The minimum distance covered in this journey is:",minimum_distance,"the maximum distance covered in this journey is:", maximum_distance)

            
            #print (total_cost, tuple_values)
            
                
            total_trip_costs.append([total_cost, tuple_values])

            print(total_trip_costs)
            
            np.total_trip_costs=total_trip_costs
            total_trip_costs = sorted(total_trip_costs, key=lambda total_trip_costs_entry: total_trip_costs_entry[0])
        #alot of the first values are returning 0 so I will try to remove all elements in array total_trip_costs where total_cost = 0

        #print(total_trip_costs)  
           
            
            print("The cheapest itenerary in the list is:", total_trip_costs[0])
            print ("The most expensive itenerary is:", total_trip_costs[-1])
             #alot of the first values are returning total cost is 0 or 47 so I write the conditional in 267
             #found the error in an earlir line

            


            


            # print("the minimum cost journey is:", minimumCost)

            # print("the maximum cost journey is:", maximumCost)

            
            
            # print("minimum distance travelled for in between all trips:", minimum_distance)
            # print ("minimum cost paid for travelling between all trips:", minimumCost)
            # print("maximum distance travelled in between  all trips:", maximum_distance)
            # print("maximum cost paid for travelling between all trips:", maximumCost)
            # trip_6 = calculate.getAirportDistance(tuple_values[4],tuple_values[2])
            # trips.append(trip_6)

            # newlist_with_6th = trips[:]
            # newlist_with_6th.append(trip_6)
            # cost6=trip_6 
            # total_cost.update({'trip_6':cost6})
            # #we assume it is still in Europe
            # total_distance=(trip_1+trip_2+trip_3+trip_4+trip_5+trip_6)
            # #note total_distance==min(Airport.__fuel_required)
            # print(total_distance)

            # #print("total_distance travelled for trips:")
            # total_distance_list=[trip_3 + trip_2 +trip_1+trip_5+trip_4+trip_6]
            # #print("total_dist_list:",total_distance_list)
            # total_dist_list = newlist_with_6th[:]
            # print(total_dist_list)
            # one=min(total_dist_list)
            # print("min cost of 6th trip", one)
            


            # #creating a dictionary with final distance as key with all final tuples as my values because
            # #it would be more efficient for value lookup 
            # total_distance_dict = {}
            
            # total_distance_dict[total_distance] = tuple_values

           
            # #print(total_distance_dict)
           
            # total_dist_list = list(total_distance)[:]
            # shortest_final_journey = min(list(total_dist_list))
            # longest_final_journey = max(list(total_dist_list))

            # print(shortest_final_journey,"longes_final_trip in km is:", longest_final_journey)

           


            # #completes in 214.secs
            # print (total_distance_dict)

            # Cost_dict={}

            # trip = Airport

            # #total_cost=trip*Currency.FindConversion(currencyRate,trip.getName(trip))
            

            # print(Cost_dict)


            #print(trips)
   

            
    #print("--- %s seconds ---" % (time.time() - start_time))
    try:
            currencyRate = Currency
            currencyRate.createInstance(currencyRate,'EU')
            #usd=currencyRate.FindConversion(currencyRate,tuple_values[1])
            #gbp=currencyRate.FindConversion(currencyRate,tuple_values[2])
            #euro=currencyRate.FindConversion(currencyRate,tuple_values[0])
            costs=np.array
            leg_dist=np.array
        

    except TypeError:
        pass

  
             


