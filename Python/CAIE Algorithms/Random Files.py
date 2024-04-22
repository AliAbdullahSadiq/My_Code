import pickle

# Example objects to serialize
data_to_serialize = {
    'name': 'John',
    'age': 30,
    'is_student': False
}

# Serialization: Writing data to a file
with open('data.pickle', 'wb') as f:
    pickle.dump(data_to_serialize, f)

# Deserialization: Reading data from a file
with open('data.pickle', 'rb') as f:
    deserialized_data = pickle.load(f)

# Print the deserialized data
print(deserialized_data)
