from die import Die
import pygal
# Create a D6 and a D10.
die_1 = Die(8)
die_2 = Die(8)
# Make some rolls, and store results in a list.
results = []
for roll_num in range(500):
    result = die_1.roll() + die_2.roll()
    results.append(result)
print(results)
frequencies = []
output = [x for x in range(2,17)]
print(output)
for value in output:
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)
"""
# Analyze the results.
--snip--
"""
# Visualize the results.
hist = pygal.Bar()
hist.title = "Results of rolling a D6 and a D10 50,000 times."
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6 + D10', frequencies)
hist.render_to_file('dice_visual_8.svg')
