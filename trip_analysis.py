# default approach instead of using lib

Paris = ['Paris', 200, 20, 200]
London = ['London', 250, 30, 200]
Dubai = ['Dubai', 370, 15, 80]
Mumbai = ['Mumbai', 450, 10, 70]

cities = (Paris, London, Dubai, Mumbai)

def calculateVacationPlan(cities, duration_in_days):
    duration_in_weeks = duration_in_days / 7
    total_costs = []

    for city in cities:
        total_amount =  city[1] + (city[2] * duration_in_days) + (city[3] * duration_in_weeks)
        total_costs.append(total_amount)

    return total_costs

def getCheapestCity(cities, costs):
    return cities[costs.index(min(costs))]

costs = calculateVacationPlan(cities, 7)
cheapest_city = getCheapestCity(cities, costs)

print(cheapest_city)
