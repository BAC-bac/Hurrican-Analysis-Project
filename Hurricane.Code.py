# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
def updated_damages(damages):
    updated_damages_list = []
    for num in damages:
        if num == "Damages not recorded":
            updated_damages_list.append(num)
        elif num.find("M") > -1:
            num = num.replace("M", "")
            num = float(num)*100000
            updated_damages_list.append(num)
        else:
            num = num.replace("B", "")
            num = float(num)*100000000
            updated_damages_list.append(num)
    return updated_damages_list

# test function by updating damages
updated_damages_list = updated_damages(damages)

print(updated_damages(damages))

# 2 
# Create a Table
def hur_dict_names(names, months, years, max_sustained_winds, areas_affected, updated_damages_list, deaths):
  hurricanes = {}
  num_hurricanes = len(names)
  for num in range(num_hurricanes):
    hurricanes[names[num]] = {"Name": names[num],
                            "Month": months[num],
                            "Year": years[num],
                            "Max Sustained Wind": max_sustained_winds[num],
                            "Areas Affected": areas_affected[num],
                            "Damage": updated_damages_list[num],
                            "Deaths": deaths[num]}
  return hurricanes

# Create and view the hurricanes dictionary
hurricanes = hur_dict_names(names, months, years, max_sustained_winds, areas_affected, updated_damages_list, deaths)

print(hur_dict_names(names, months, years, max_sustained_winds, areas_affected, updated_damages_list, deaths))

# 3
# Organizing by Year
def hur_dict_years(hurricanes):
  hur_by_year = {}
  for num in hurricanes:
    year = hurricanes[num]["Year"]
    name = hurricanes[num]
    if year not in hur_by_year:
      hur_by_year[year] = [name]
    else:
      hur_by_year[year].append(name)
  return hur_by_year

# create a new dictionary of hurricanes with year and key
hur_by_year = hur_dict_years(hurricanes)
print(hur_by_year[1932])

# 4
# Counting Damaged Areas
def count_affected_areas(hurricanes):
  count_affected = {}
  for value in hurricanes.values():
    for num in value["Areas Affected"]:
      if num not in count_affected:
        count_affected[num] = 1
      else:
        count_affected[num] += 1
  return count_affected

# create dictionary of areas to store the number of hurricanes involved in

count_affected = count_affected_areas(hurricanes)
print(count_affected_areas(hurricanes))

# 5 
# Calculating Maximum Hurricane Count
def most_affected_areas(count_affected):
  most_affected = {}
  count = 0
  for key, value in count_affected.items():
    if value > count:
      most_affected[key] = value
      count = value
  return most_affected

# find most frequently affected area and the number of hurricanes involved in
most_affected = most_affected_areas(count_affected)
print(most_affected_areas(count_affected))

# 6
# Calculating the Deadliest Hurricane
def greatest_death(hurricanes):
  max_death = ""
  count = 0
  for num in hurricanes:
    if hurricanes[num]["Deaths"] > count:
      max_death = num
      count = hurricanes[num]["Deaths"]
  return max_death, count

# find highest mortality hurricane and the number of deaths
max_death, count = greatest_death(hurricanes)
print(greatest_death(hurricanes))

# 7
# Rating Hurricanes by Mortality
def mortality_scale(hurricanes):
  m_scale = {}
  zero_list = []
  one_list = []
  two_list = []
  three_list = []
  four_list = []
  for key, value in hurricanes.items():
    if hurricanes[key]["Deaths"] == 0:
     zero_list.append(value)
     m_scale[0] = zero_list
    elif hurricanes[key]["Deaths"] <= 100:
     one_list.append(value)
     m_scale[1] = one_list
    elif hurricanes[key]["Deaths"] <= 500:
     two_list.append(value)
     m_scale[2] = two_list
    elif hurricanes[key]["Deaths"] <= 1000:
     three_list.append(value)
     m_scale[3] = three_list
    elif hurricanes[key]["Deaths"] <= 10000:
     four_list.append(value)
     m_scale[4] = four_list
  return m_scale

# categorize hurricanes in new dictionary with mortality severity as key
m_scale = mortality_scale(hurricanes)
for key in sorted(m_scale):
    print("\n{} -- {}".format(key, m_scale[key]))

# 8 Calculating Hurricane Maximum Damage
def greatest_damage(hurricanes):
  damage = 0
  name = ""
  for num in hurricanes:
    if hurricanes[num]["Damage"] == "Damages not recorded":
      pass   
    elif hurricanes[num]["Damage"] > damage:
      damage = hurricanes[num]["Damage"]
      name = num
  return name, damage

# find highest damage inducing hurricane and its total cost
print(greatest_damage(hurricanes))

# 9
# Rating Hurricanes by Damage
def damage_scale(hurricanes):
  damage_scale = {0: 0,
                  1: 100000000,
                  2: 1000000000,
                  3: 10000000000,
                  4: 50000000000}
  hurricanes_by_damage = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
  for num in hurricanes:
    total_damage = hurricanes[num]["Damage"]
    if total_damage == "Damages not recorded":
      hurricanes_by_damage[0].append(hurricanes[num])
    elif total_damage == damage_scale[0]:
      hurricanes_by_damage[0].append(hurricanes[num])
    elif total_damage > damage_scale[0] and total_damage < damage_scale[1]:
      hurricanes_by_damage[1].append(hurricanes[num])
    elif total_damage > damage_scale[1] and total_damage < damage_scale[2]:
      hurricanes_by_damage[2].append(hurricanes[num])
    elif total_damage > damage_scale[2] and total_damage < damage_scale[3]:
      hurricanes_by_damage[3].append(hurricanes[num])
    elif total_damage > damage_scale[3] and total_damage < damage_scale[4]:
      hurricanes_by_damage[4].append(hurricanes[num])
    elif total_damage > damage_scale[4]:
      hurricanes_by_damage[5].append(hurricanes[num])
  return hurricanes_by_damage
  
# categorize hurricanes in new dictionary with damage severity as key
dam_scale = damage_scale(hurricanes)

for num in sorted(dam_scale):
  print("\n{} ---> {}".format(num, dam_scale[num]))
