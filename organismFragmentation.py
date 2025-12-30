
# Prompting user for input
starting_population = int(input("Enter the starting number of organisms: "))  # Getting the initial population from the user
growth_rate = float(input("Enter the average daily population increase as a percentage: "))  # Getting the growth rate from the user
days = int(input("Enter the number of days the organism will be left to multiply: "))  # Getting the number of days from the user
daily_increase = growth_rate / 100  # Converting growth rate to decimal

population = starting_population  # Initializing the population variable with the starting population
print("Day\t\tPopulation")  # Printing column headers for the output

# Loop through each day and calculate the population
for day in range(1, days + 1):
    print(f"{day}\t \t{population:.4f}")  # Printing the day and the population for the current day with 4 decimal places
    population = population + (daily_increase * population)  # Calculating the new population for the next day
























    

