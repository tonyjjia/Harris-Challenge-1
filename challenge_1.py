# CHALLENGE PROBLEMS
# YOU MAY NOT USE ANY ADDITIONAL LIBRARIES OR PACKAGES TO COMPLETE THIS CHALLENGE

#Weixuan Tony Jia 12244896
# Divvy is Chicago's bike share system, which consists of almost 600 stations scattered
# around the city with blue bikes available for anyone to rent. Users begin a ride by removing
# a bike from a dock, and then they can end their ride by returning the bike to a dock at any Divvy 
# station in the city. You are going to use real data from Divvy collected at 1:30pm on 4/7/2020 
# to analyze supply and demand for bikes in the system. 

# NOTE ** if you aren't able to run this, type "pip install json" into your command line
import json
# do not delete; this is the data you'll be working with
divvy_stations = json.loads(open('divvy_stations.txt').read())

# PROBLEM 1
# find average number of empty docks (num_docks_available) and 
# available bikes (num_bikes_available) at all stations in the system


num_docks_count=[x['num_docks_available'] for x in divvy_stations]
total_empty_docks=sum(num_docks_count)
num_total_stations=len(divvy_stations)
average_empty_docks=total_empty_docks/num_total_stations
print(average_empty_docks) #9.532773109243697

num_bikes_count=[x['num_bikes_available'] for x in divvy_stations]
total_available_bikes=sum(num_bikes_count)
average_available_bikes=total_available_bikes/num_total_stations
print(average_available_bikes) #7.7596638655462185

# PROBLEM 2
# find ratio of bikes that are currently rented to total bikes in the system (ignore ebikes)

#Assume that the total number of docks equal to the total number of bikes:
total_disabled_bikes=sum([x['num_bikes_disabled'] for x in divvy_stations])
ratio_bikes_rented=total_empty_docks/(total_disabled_bikes+total_available_bikes+total_empty_docks)
print(ratio_bikes_rented) #0.5502522312766783

# PROBLEM 3 
# Add a new variable for each divvy station's entry, "percent_bikes_remaining", that shows 
# the percentage of bikes available at each individual station (again ignore ebikes). 
# This variable should be formatted as a percentage rounded to 2 decimal places, e.g. 66.67%


percent_bikes_remaining=[num_bikes_count[i]/(num_bikes_count[i]+num_docks_count[i]) for i in range(len(divvy_stations))]
percent_func=lambda x: format(x,'.2%')
percent_bikes_remaining=[percent_func(x) for x in percent_bikes_remaining]
for i,x in zip(divvy_stations,percent_bikes_remaining):
        i['percent_bikes_remaining']=x
print(divvy_stations)

