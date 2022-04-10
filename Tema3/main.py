import csv
import random
import json

# Exercitiul 1
cars_from_file = []
with open('input.csv') as csv_file:
    reader = csv.reader(csv_file)

    for index, row in enumerate(reader):
        if index == 0:
            keys = row
        else:
            cars_from_file.append(dict(zip(keys, row)))


list_of_id = list(range(1000))


def get_id_cars(car):
    new_car = car.copy()
    id_unique = random.choice(list_of_id)
    list_of_id.pop(id_unique)
    new_car['id'] = id_unique
    return new_car


cars = list(map(get_id_cars, cars_from_file))
print(cars)

# Exercitiul 2
slow_cars = list(filter(lambda item: int(item['hp']) < 120, cars))
fast_cars = list(filter(lambda item: int(item['hp']) in range(120, 180), cars))
sport_cars = list(filter(lambda item: int(item['hp']) >= 180, cars))
cheap_cars = list(filter(lambda item: int(item['price']) < 1000, cars))
medium_cars = list(filter(lambda item: int(item['price']) in range(1000, 5000), cars))
expensive_cars = list(filter(lambda item: int(item['price']) >= 5000, cars))
dacia = list(filter(lambda item: item['brand'] == 'dacia', cars))
bmw = list(filter(lambda item: item['brand'] == 'bmw', cars))
ford = list(filter(lambda item: item['brand'] == 'ford', cars))
renault = list(filter(lambda item: item['brand'] == 'renault', cars))
volkswagen = list(filter(lambda item: item['brand'] == 'volkswagen', cars))
audi = list(filter(lambda item: item['brand'] == 'audi', cars))

with open('output_data/slow_cars.json', 'w') as json_file:
    json.dump(slow_cars, json_file, indent=2)

with open('output_data/fast_cars.json', 'w') as json_file:
    json.dump(fast_cars, json_file, indent=2)

with open('output_data/sport_cars.json', 'w') as json_file:
    json.dump(sport_cars, json_file, indent=2)

with open('output_data/cheap_cars.json', 'w') as json_file:
    json.dump(cheap_cars, json_file, indent=2)

with open('output_data/medium_cars.json', 'w') as json_file:
    json.dump(medium_cars, json_file, indent=2)

with open('output_data/expensive_cars.json', 'w') as json_file:
    json.dump(expensive_cars, json_file, indent=2)

with open('output_data/dacia.json', 'w') as json_file:
    json.dump(dacia, json_file, indent=2)

with open('output_data/bmw.json', 'w') as json_file:
    json.dump(bmw, json_file, indent=2)

with open('output_data/renault.json', 'w') as json_file:
    json.dump(renault, json_file, indent=2)

with open('output_data/ford.json', 'w') as json_file:
    json.dump(ford, json_file, indent=2)

with open('output_data/volkswagen.json', 'w') as json_file:
    json.dump(volkswagen, json_file, indent=2)

with open('output_data/audi.json', 'w') as json_file:
    json.dump(audi, json_file, indent=2)
