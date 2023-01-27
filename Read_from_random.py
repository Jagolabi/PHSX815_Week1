import matplotlib.pyplot as plt

#  read numbers
with open("random_numbers.txt", "r") as file:
    random_numbers = [float(line.strip()) for line in file]

# Create a histogram of the numbers
plt.hist(random_numbers, bins=50, density=True, facecolor='r', alpha=0.75)
plt.xlabel('x')
plt.ylabel('Expectancy')
plt.title('Uniform random number')
plt.grid(False)

# Show the plot
plt.show()
