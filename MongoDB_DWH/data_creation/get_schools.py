import json
import pandas as pd

if __name__ == "__main__":
    file = open('School List - Anchorage School District.html', "r")
    data = pd.read_html(file, skiprows=0)[0]
    data["School"].to_json(open("./data_schools.json", "w"), indent=4, orient="records")
