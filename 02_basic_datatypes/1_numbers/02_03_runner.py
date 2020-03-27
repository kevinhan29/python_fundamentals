'''

If a runner runs 10 miles in 30 minutes and 30 seconds,
What is his/her average speed in kilometers per hour? (Tip: 1 mile = 1.6 km)

'''
# define variables
miles = 10
time = 30.5   # in minutes

# conversions
km = miles*1.6      # miles to km
hours = time/60     # min to hr

# calculate speed in km/hr
km_per_hr = km/hours
print(km_per_hr, " km/h")