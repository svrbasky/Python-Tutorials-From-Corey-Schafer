from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")


minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# player1 = [1, 2, 3, 3, 4, 4, 4, 4, 5]
# player2 = [1, 1, 1, 1, 2, 2, 2, 3, 4]
# player3 = [1, 1, 1, 2, 2, 2, 3, 3, 3]

developer1 = [8, 6, 5, 5, 4, 2, 1, 1, 0] # developer 1 who is doing knowledge transfer to 2 new developers.
developer2 = [0, 1, 2, 2, 2, 4, 4, 4, 4] # new developer 1
developer3 = [0, 1, 1, 1, 2, 2, 3, 3, 4] # new developer 2


# labels
# labels = ['player1', 'player2', 'player3']
labels = ['developer1', 'developer2', 'developer3']

# Colors
colors = ['#6d904f','#fc4f30','#008fd5']

# pie plot
# plt.pie([1, 1, 1], labels = ["Player 1", "Player 2", "Player 3"])

# stack plot
plt.stackplot(minutes, developer1, developer2, developer3, labels = labels, colors = colors)

# plt.legend() # To show labels/legend
# plt.legend(loc = 'lower left') # To show labels/legend, hardcoded location (verbal)
plt.legend(loc = (0.07, 0.05)) # To show labels/legend, hardcoded location with coordinates

plt.title("My Awesome Stack Plot")
plt.tight_layout()
plt.show()

# Colors:
# Blue = #008fd5
# Red = #fc4f30
# Yellow = #e5ae37
# Green = #6d904f
