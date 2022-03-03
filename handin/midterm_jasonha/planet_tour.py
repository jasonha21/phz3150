#!/usr/bin/env python
# coding: utf-8

# In[17]:


import numpy as np
import math
#planets_and_moons=['Mercury','Venus','Earth','Moon','Ceres','Mars','Jupiter','Io','Europa','Saturn','Titan','Neptune','Pluto','Charon']
def planet_tour(tour,start_location,destination_location):
    planets_and_moons=['Mercury','Venus','Earth','Moon','Ceres','Mars','Jupiter','Io','Europa','Saturn','Titan','Neptune','Pluto','Charon']
    space_distances_date1 = np.loadtxt('solar_system_date_1.dat')
    space_distances_date2 = np.loadtxt('solar_system_date_2.dat')
    space_distances_date3 = np.loadtxt('solar_system_date_3.dat')
    start_body_i= planets_and_moons.index(start_location)#returns the index of the start location in the list
    destination_body_i= planets_and_moons.index(destination_location) #returns the index of the destination in the list
    if tour=='N' or 'No':
        d=space_distances_date1[start_body_i][destination_body_i] #returns the distance from the data file using the index of the start and end location for date 1
        date=1
        if d>space_distances_date2[start_body_i][destination_body_i]:
            d=space_distances_date2[start_body_i][destination_body_i]
        date=2
        if d>space_distances_date3[start_body_i][destination_body_i]:
            d=space_distances_date3[start_body_i][destination_body_i]
        date=3
        r=0.001 #the constant for the rate of travel
        t=d/r #time in hours because rate/speed is in au per hour
        travel_time_years=int( t/8760 ) #returns an integer value for the time in years
        travel_time_days= int((( (t/8760) - travel_time_years)*365)) #returns integer value for the time in days without counting the years
        travel_time_hours=int(( (( (t/8760) - travel_time_years)*365) - travel_time_days)*24) #returns integer value for hours without counting the years and days
        travel_time_minutes=int(((( (( (t/8760) - travel_time_years)*365) - travel_time_days)*24)-travel_time_hours)*60) #returns the value for time in minutes without counting the years, days, and hours
        num_of_stops=math.ceil((d/0.6500)-1)#minus 1 because the ship starts full of fuel
        stop_distances= 0.6500 * np.arange(1,200)#I make it stop at 130 to accomodate 200 stops, a ballpark figure I made up for how many elements I thought I'd need
        stops=stop_distances[0:num_of_stops] #splices the array to only be the values we need to write later
        f=open('message_to_stations.txt', 'w')
        f.write('My trip starts at '+ start_location +' and ends at '+ destination_location +'. I will need to encounter stations for a refueling at the distances ')
        for stop in range(len(stops)):
            f=open('message_to_stations.txt', 'a')
            f.write(str(stops[stop])+'AU, ')
        f.close()
        print('You will travel a distance of ',d,'AU on date',date,'. Your trip will take',travel_time_years, 'years',travel_time_days,'days',travel_time_hours,'hours',travel_time_minutes,'mins. We will need to make', num_of_stops,'stops to refuel.')
    elif tour=='Y' or 'Yes':
        d1=space_distances_date1[start_body_i][destination_body_i] #returns the distance from the data file using the index of the start and end location for date 1
        for tour_stop in range(len(space_distances_date1)):
            stop1n=planets_and_moons[0]
            if space_distances_date1[start_body_i][tour_stop]>space_distances_date1[start_body_i][tour_stop + 1]:#compares the distance from i element in the row to the one next to it to eventually get the smallest one
                stop1=space_distances_date1[start_body_i][tour_stop + 1]
                stop1n=planets_and_moons[tour_stop] #gets the name of the planet the current stop is at
        t1=d1 + stop1#adds the distance from the start to end with the stop to get a total distance for the tour
        d2=space_distances_date2[start_body_i][destination_body_i] #returns the distance from the data file using the index of the start and end location for date 2
        for tour_stop in range(len(space_distances_date2)):
            if space_distances_date2[start_body_i][tour_stop]>space_distances_date2[start_body_i][tour_stop + 1]:
                stop2=space_distances_date2[start_body_i][tour_stop + 1]
        t2=d2 + stop2
        d3=space_distances_date3[start_body_i][destination_body_i] #returns the distance from the data file using the index of the start and end location for date 3
        for tour_stop in range(len(space_distances_date3)):
            if space_distances_date3[start_body_i][tour_stop]>space_distances_date3[start_body_i][tour_stop + 1]:
                stop3=space_distances_date3[start_body_i][tour_stop + 1]
        t3=d3 + stop3
        print('You can make a stop at', stop1n , 'on date 1 which will add a distance of',stop1,'a stop at on date 2 which will add a distance of',stop2,'or a stop at on date 3, which will add a distance of',stop3)
    return print('Done')


# In[18]:


planet_tour('Yes','Mars','Ceres')

