import json
import random
import uuid
from datetime import datetime


def merge_persons_schools_hobbies(filename):
    possible_education_durations = 2 * [2] + 5 * [3] + 2 * [4] + [5, 6, 7, 8]
    possible_education_offsets = 6 * [0] + 3 * [1] + 2 * [2] + [3]
    possible_education_counts = [0] + 4 * [1] + 10 * [2] + 4 * [3] + [4]
    possible_hobbies_counts = [0] + 3 * [1] + 5 * [2] + 3 * [3] + [4]
    possible_item_counts = [0] + 3 * [1] + 5 * [2] + 3 * [3] + [4]
    possible_order_counts = [0] + 2*[1] + 2 * [2] + 5 * [3] + 2 * [4] + [i for i in range(5, 30)]

    data_orders = json.load(open("data_orders.json", "r")) * 10
    data_items = json.load(open("data_items.json", "r"))
    for order in data_orders:
        items = []
        order["order-id"] = str(uuid.uuid4().fields[-1])[:6]
        for j in range(random.choice(possible_item_counts)):
            items.append(random.choice(data_items))
        order["items"] = items

    data_persons = json.load(open("data_persons.json", "r"))
    data_schools = json.load(open("data_schools.json", "r"))
    data_hobbies = json.load(open("data_hobbies.json", "r"))

    for person in data_persons:
        birth_date = datetime.strptime(person["DateOfBirth"], "%d/%m/%Y")
        education = []
        education_end = birth_date.year + random.randint(5, 7)
        for i in range(random.choice(possible_education_counts)):
            education_duration = random.choice(possible_education_durations)
            education_start = education_end + random.choice(possible_education_offsets)
            education_end = education_start + education_duration
            education.append({
                "school": random.choice(data_schools),
                "from": education_start,
                "to": education_end
            })
        person["Education"] = education

        possible_hobbies: list = data_hobbies.copy()
        hobbies = []
        for i in range(random.choice(possible_hobbies_counts)):
            index = random.randint(0, len(possible_hobbies)-1)
            hobbies.append(possible_hobbies.pop(index))
        person["Hobbies"] = hobbies

        possible_orders: list = data_orders.copy()
        orders = []
        for i in range(random.choice(possible_order_counts)):
            index = random.randint(0, len(possible_orders)-1)
            orders.append(possible_orders.pop(index))
        person["Orders"] = orders

    json.dump(data_persons, open(filename, "w"), indent=4)


if __name__ == "__main__":
    merge_persons_schools_hobbies("data_persons_merged.json")
