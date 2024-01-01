# Make a program that displays the cities in the Japan.
# Display all cities starting with the letter N
cities = ["Tokyo",
"Osaka",
"Kyoto",
"Sapporo",
"Nagoya",
"Hiroshima",
"Kobe",
"Sendai",
"Nara",
"Nagasaki"]
print(cities)
for cities in cities:
    if cities.startswith("N"):
        print(cities)
