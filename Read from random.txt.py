import matplotlib.pyplot as plt

#  read numbers
with open("random_numbers.txt", "r") as file:
    random_numbers = [float(line.strip()) for line in file]

# Create a histogram of the numbers
plt.hist(random_numbers, bins=50, density=True, facecolor='g', alpha=0.75)
plt.xlabel('x')
plt.ylabel('Probability')
plt.title('Uniform random number')
plt.grid(True)

# Show the plot
plt.show()
