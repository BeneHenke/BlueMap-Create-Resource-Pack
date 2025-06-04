import sys
import json

with open(sys.argv[1], 'r') as file:
    variants = json.load(file)["variants"]

output = {
    "multipart": []
}

def convert_condition(condition):
    new_condition = {}
    for part in condition.split(","):
        key, value = part.split("=")
        new_condition[key] = value
    return new_condition

for condition, state in variants.items():
    output["multipart"].append({
        "when": convert_condition(condition),
        "apply": state
    })

with open(sys.argv[1], "w") as file:
    json.dump(output, file, indent=2)