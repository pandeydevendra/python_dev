import pandas as pd
from matplotlib import pyplot as plt
"""
# Read CSV into pandas
data = pd.read_csv(r"cars.csv")
data.head()
df = pd.DataFrame(data)

name = df['car'].head(12)
price = df['price'].head(12)"""

# creating the dataset; in dict:
brand_sales = {
    'BETAMOM': 3565,
    'OMEFORTE-D': 620,
    'MOMACE-SP': 2300,
    'LEVOMOM': 880,
    'MOMNIX-TH': 2980,
    'IVERMOM-12': 0,
    'SEFDICTH': 475,
    'AMOXOBIC-CV/LB': 4730,
    'PPGUT': 1440,
    'ARKLE-AX': 0,
    'KARKOF-LS': 2620,
    'GASBYE': 1520,
    'VITLOARK': 3612,
    'COLDNIX': 0,
    'COLDNIXDS': 2105,
    'SEFLOMS': 4273,
    'MAGNAFORTE-XT': 0,
    'CALKOFIT-C': 0,
    'CEPODANX-O': 0,
    'LEFMOM -OZ': 0
}

brands = list(brand_sales.keys())
revenue = list(brand_sales.values())
"""
fig = plt.figure(figsize=(25, 10))
# creating the bar plot
plt.bar(brands, revenue, color='green', width=0.4)

plt.xlabel("Brands------>>")
plt.ylabel("Revenue----->>")
plt.title("Revenue of different brands")
plt.show()
, color = 'red', color = 'yellow'
"""
# Figure Size
fig, ax = plt.subplots(figsize =(20, 10))
# creating the bar plot::
# Horizontal Bar Plot:
ax.barh(brands, revenue)

# Remove axes splines
for s in ['top', 'bottom', 'left', 'right']:
	ax.spines[s].set_visible(False)

# Remove x, y Ticks
ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')

# Add padding between axes and labels
ax.xaxis.set_tick_params(pad = 5)
ax.yaxis.set_tick_params(pad = 10)

# Add x, y gridlines
ax.grid(b = True, color ='red',
		linestyle ='-.', linewidth = 0.5,
		alpha = 0.2)

# Show top values
ax.invert_yaxis()

# Add annotation to bars
for i in ax.patches:
	plt.text(i.get_width()+0.2, i.get_y()+0.5,
			str(round((i.get_width()), 2)),
			fontsize = 10, fontweight ='bold',
			color ='red')

# Add Plot Title
ax.set_title('Revenue of Different Brands:', color = 'blue',
			loc ='left')
ax.set_title('January-2021', color = 'blue',
			loc ='right')

# Add Text watermark
fig.text(0.9, 0.15, 'MSMother_Pharma', fontsize = 12,
		color ='green', ha ='right', va ='bottom',
		alpha = 0.7)

# Show Plot
plt.show()
