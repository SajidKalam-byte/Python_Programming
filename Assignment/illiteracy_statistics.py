# Given data
total_population = 80000
percentage_men = 52 / 100
percentage_literacy = 48 / 100
percentage_literate_men = 35 / 100

# Calculate number of men and women
num_men = total_population * percentage_men
num_women = total_population * (1 - percentage_men)

# Calculate number of literate men and women
literate_men = total_population * percentage_literate_men
total_literate = total_population * percentage_literacy
literate_women = total_literate - literate_men

# Calculate illiterate men and women
illiterate_men = num_men - literate_men
illiterate_women = num_women - literate_women

# Output results
print("Total number of illiterate men:", int(illiterate_men))
print("Total number of illiterate women:", int(illiterate_women))
