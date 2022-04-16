import json
import random
from datetime import datetime


def merge_persons_schools_hobbies(filename):
    possible_education_durations = 2 * [2] + 5 * [3] + 2 * [4] + [5, 6, 7, 8]
    possible_education_offsets = 6 * [0] + 3 * [1] + 2 * [2] + [3]
    possible_education_counts = [0] + 4 * [1] + 10 * [2] + 4 * [3] + [4]
    possible_hobbies_counts = [0] + 3 * [1] + 5 * [2] + 3 * [3] + [4]
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

    json.dump(data_persons, open(filename, "w"), indent=4)


if __name__ == "__main__":
    merge_persons_schools_hobbies("data_persons_merged.json")
