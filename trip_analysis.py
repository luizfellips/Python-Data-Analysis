# default approach instead of using lib
import math

Paris = ['Paris', 200, 20, 200]
London = ['London', 250, 30, 120]
Dubai = ['Dubai', 370, 15, 80]
Mumbai = ['Mumbai', 450, 10, 70]

cities = (Paris, London, Dubai, Mumbai)


# adds total cost amount to each city
def calculateVacationCost(cities, duration_in_days):
    duration_in_weeks = duration_in_days / 7

    for city in cities:
        total_amount =  city[1] + (city[2] * duration_in_days) + (city[3] * duration_in_weeks)
        city.append(total_amount)

# returns cheapest city
def getCheapestCity(cities):
    costs = []
    for item in cities:
        costs.append(item[4])

    return cities[costs.index(min(costs))]

#  returns cities with max duration based on budget
def maximizeOnBudget(cities, budget):
    budgetCities = []
    max_duration = 0

    for city in cities:
        duration = math.ceil((budget / city[4]) * 7)

        budgetCities.append([city[0], duration])
        
        if duration > max_duration:
            max_duration = duration

    max_duration_cities = [[city[0], city[1]] for city in budgetCities if city[1] == max_duration]

    return max_duration_cities

#  returns cities with minimum duration based on budget
def minimizeOnBudget(cities, budget):
    budgetCities = []
    min_duration = float('inf')  # Initialize to a large value

    for city in cities:
        duration = math.ceil((budget / city[4]) * 7)

        budgetCities.append([city[0], duration])
        
        if duration < min_duration:
            min_duration = duration

    min_duration_cities = [[city[0], city[1]] for city in budgetCities if city[1] == min_duration]

    return min_duration_cities

duration_in_days = 7
budget = 400

## sets total cost for cities for given duration
calculateVacationCost(cities, duration_in_days)

cheapest_city = getCheapestCity(cities)
maximized_duration_cities = maximizeOnBudget(cities, budget)
minimized_duration_cities = minimizeOnBudget(cities, budget)
