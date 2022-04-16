import json
import pandas as pd

if __name__ == "__main__":
    file = open('133 Examples of Hobbies - Simplicable.htm', "r")
    data = pd.read_html(file, skiprows=0)[2]
    export_data = (list(data[0]) + list(data[1]))[:-1]
    json.dump(export_data, open("./data_hobbies.json", "w"), indent=4)
