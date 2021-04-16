import matplotlib.pyplot as plt
import numpy as np

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

# creating lists(x and y):

brands = list(brand_sales.keys())
revenue = list(brand_sales.values())
fig = plt.figure(figsize=(25, 10))
# creating the bar plot
plt.bar(brands, revenue, color='green', width=0.4)

plt.xlabel("Brands------>>")
plt.ylabel("Revenue----->>")
plt.title("Revenue of different brands")
plt.show()
