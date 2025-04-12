person = {
    "name": "John Doe",
    "age": 35,
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "state": "CA",
        "zip": "12345"
    },
    "contact": {
        "phone": "555-1234",
        "email": "john.doe@example.com"
    }
}

for key,vaule in person.items():
    print(f"{key}: {vaule}")

for key, vaule in person["address"].items():
    print(f"{key}: {vaule}")

