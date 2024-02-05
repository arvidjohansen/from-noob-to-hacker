import json

def summarize(obj, level=0):
    indent = '  ' * level
    if isinstance(obj, list):
        if all(isinstance(i, str) for i in obj):
            return f"A list of strings with max len {max(len(i) for i in obj)}"
        elif all(isinstance(i, dict) for i in obj):
            keys = set().union(*(d.keys() for d in obj))
            return f"A list of dictionaries with the following keys: {', '.join(keys)}"
        else:
            return '\n'.join(f"{indent}* {summarize(i, level+1)}" for i in obj)
    elif isinstance(obj, dict):
        return '\n'.join(f"{indent}* {k}: {summarize(v, level+1)}" for k, v in obj.items())
    elif isinstance(obj, str):
        try:
            json_obj = json.loads(obj)
            return summarize(json_obj, level)
        except json.JSONDecodeError:
            return "A string"
    else:
        return f"An object of type {type(obj).__name__}"

# Test the function
print(summarize(["hello", "world"]))
print(summarize([{"name": "John", "age": 30}, {"name": "Jane", "age": 25}]))
print(summarize({"name": "John", "age": 30}))
print(summarize('{"name": "John", "age": 30}'))
print(summarize([{"name": "John", "age": 30, "friends": [{"name": "Jane", "age": 25}]}]))
obj = [{"name": "John", "age": 30, "friends": [{"name": "Jane", "age": 25}]}]
print(summarize(obj))
# list of pets with names and ages
pets = [
    {"name": "John", "age": 30},
    {"name": "Jane", "age": 25},
    {"name": "Jack", "age": 5},
    {"name": "Jill", "age": 4},]
print(summarize(pets))

data = json.load(open('example_data.json'))

print(summarize(data))

