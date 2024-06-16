from promptflow import tool
import json

# Function to calculate the total number of red cars in a JSON object
def calculate_red_cars(data):
    total_red_cars = 0
    for key, value in data.items():
        if key.lower() == "red cars":
            total_red_cars += value
    return total_red_cars

# Function to parse JSON-like data from a string
def parse_json_string(json_string):
    try:
        data = json.loads(json_string)
        return data
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return {}
        
@tool
def calculate_total_red_cars(input1: str, input2:str) -> str:
    json_string1 = input1.replace("```json\n", "").replace("```", "")
    json_string2 = input2.replace("```json\n", "").replace("```", "")
    data1 = parse_json_string(json_string1)
    data2 = parse_json_string(json_string2)
    total_red_cars = calculate_red_cars(data1) + calculate_red_cars(data2)

    return '"Total number of red cars: ' + str(total_red_cars)