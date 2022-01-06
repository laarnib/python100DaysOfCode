#You are going to write a program that adds to a travel_log. You can see a travel_log 
#which is a List that contains 2 Dictionaries.
#Write a function that will work with the following line of code on line 21 to add the
#entry for Russia to the travel_log.
#You've visited Russia 2 times.
#You've been to Moscow and Saint Petersburg.


travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country, times_visited, cities):
    new_country = {}

    new_country["country"] = country
    new_country["visits"] = times_visited
    new_country["cities"] = cities

    travel_log.append(new_country)



#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)