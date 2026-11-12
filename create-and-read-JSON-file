import json

# 1. Create and write JSON data
data = {
    "name": "Rahul",
    "age": 22,
    "skills": ["Python", "Data Analysis", "Machine Learning"],
    "is_student": True
}

with open("student.json", "w") as file:
    json.dump(data, file, indent=4)

print("JSON file created successfully!")

# 2. Read the JSON file
with open("student.json", "r") as file:
    loaded_data = json.load(file)

print("\nData read from JSON file:")
print(loaded_data)
print("\nName:", loaded_data["name"])
print("Skills:", loaded_data["skills"])
