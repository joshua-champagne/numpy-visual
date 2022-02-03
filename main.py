# Joshua Champagne
# SIE507 Project #2
# 12/15/20
# This program will calculate and display data and statistics on sunspots from 1700-1999
import numpy as np
import matplotlib.pyplot as plt

# Imports Data
sun_spots = np.genfromtxt("sunspots_1700_1999.csv", delimiter=",", skip_header=1, dtype='float')

# Calculate Overall Data Statistics
data_min = sun_spots.min(axis=0)
data_max = sun_spots.max(axis=0)
data_mean = sun_spots.mean(axis=0)
data_std = sun_spots.std(axis=0)
data_median = np.median(sun_spots, axis=0)

# Calculate 1700s Data Statistics
data_min_1700 = sun_spots[0:99].min(axis=0)
data_max_1700 = sun_spots[0:99].max(axis=0)
data_mean_1700 = sun_spots[0:99].mean(axis=0)
data_std_1700 = sun_spots[0:99].std(axis=0)
data_median_1700 = np.median(sun_spots[0:99], axis=0)

# Calculate 1800s Data Statistics
data_min_1800 = sun_spots[100:200].min(axis=0)
data_max_1800 = sun_spots[100:200].max(axis=0)
data_mean_1800 = sun_spots[100:200].mean(axis=0)
data_std_1800 = sun_spots[100:200].std(axis=0)
data_median_1800 = np.median(sun_spots[100:200], axis=0)

# Calculate 1900s Data Statistics
data_min_1900 = sun_spots[201:300].min(axis=0)
data_max_1900 = sun_spots[201:300].max(axis=0)
data_mean_1900 = sun_spots[201:300].mean(axis=0)
data_std_1900 = sun_spots[201:300].std(axis=0)
data_median_1900 = np.median(sun_spots[201:300], axis=0)


# Classifies & Reshapes Data Yearly, Decennially, Centennially
spots_year_trans = sun_spots.transpose()     # 2D Array 2x300

spots_dec = sun_spots.reshape(30, 10, 2)
spots_dec_sum = spots_dec.sum(axis=1)
spots_dec_trans = spots_dec_sum.transpose()  # 2D Array of Decade Sums

spots_cent = sun_spots.reshape(3, 100, 2)
spots_cent_sum = spots_cent.sum(axis=1)
spots_cent_trans = spots_cent_sum.transpose()  # 2D Array of Century Sums


# Displays Statistics in Std Output
print("*** Sunspot Data and Statistics 1700-1999 ***")
print('{:<10}{:<10}{:<10}{:<10}{:<10}'.format('', '1700\'s', '1800\'s', '1900\'s', 'Overall'))
print('{:<10}{:<10.1f}{:<10.1f}{:<10.1f}{:<10.1f}'.format('Min:', data_min_1700[1], data_min_1800[1], data_min_1900[1], data_min[1]))
print('{:<10}{:<10.1f}{:<10.1f}{:<10.1f}{:<10.1f}'.format('Max:', data_max_1700[1], data_max_1800[1], data_max_1900[1], data_max[1]))
print('{:<10}{:<10.1f}{:<10.1f}{:<10.1f}{:<10.1f}'.format('Mean:', data_mean_1700[1], data_max_1800[1], data_mean_1900[1], data_mean[1]))
print('{:<10}{:<10.1f}{:<10.1f}{:<10.1f}{:<10.1f}'.format('Std Dev:', data_std_1700[1], data_std_1800[1], data_std_1900[1], data_std[1]))
print('{:<10}{:<10.1f}{:<10.1f}{:<10.1f}{:<10.1f}'.format('Median:', data_median_1700[1], data_median_1800[1], data_median_1900[1], data_median[1]))


# Display Sunspot Data in Two Graph & Data Forms
years = spots_year_trans[0]
years_dec = years[::10]
years_cent = years[::100]

fig, axs = plt.subplots(3, 1, figsize=(20, 10))
fig.suptitle('Number of Sunspots Per Year 1700-1999')

axs[0].set(title='Yearly', ylabel='# of Sunspots')
axs[0].bar(spots_year_trans[0], spots_year_trans[1])

axs[1].set(title='Decennially', ylabel='# of Sunspots')
axs[1].plot(years_dec, spots_dec_trans[1], 'o--', color='g')

axs[2].set(title='Centennially', ylabel='# of Sunspots')
axs[2].bar(years_cent, spots_cent_trans[1], color='r', width=10)
axs[2].set_xticks(years_cent)
#axs[2].set_xticklabels(years_cent)

plt.show()
