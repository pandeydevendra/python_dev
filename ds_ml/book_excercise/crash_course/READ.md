1. colormap
You can see all the colormaps available in pyplot at;
http://matplotlib.org/
go to Examples, scroll down to Color Examples, and click colormaps_reference.

2. Saving Your Plots Automatically
to automatically save the plot to a file, 
replace the call to plt.show() with a call to plt.savefig():
plt.savefig('squares_plot.png', bbox_inches='tight')