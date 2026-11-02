###
# A program that calculates the cost of transporting goods.
#

distance = float(input("Enter distance in km: "))
fuel_price = float(input("Enter fuel price per liter: "))
fuel_consumption = float(input("Enter fuel consumption per 100 km: "))

total_fuel_consumption = distance / 100 * fuel_consumption
total_cost = total_fuel_consumption * fuel_price

print(f"Fuel consumption: {total_fuel_consumption:.2f} liters")
print(f"Total transport cost: {total_cost:.2f} zł")