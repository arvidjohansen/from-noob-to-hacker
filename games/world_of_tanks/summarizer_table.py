import pandas as pd
import json

# Set pandas options
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', 48)


def summarize(obj):
    if isinstance(obj, list):
        if all(isinstance(i, str) for i in obj):
            return pd.DataFrame(obj, columns=['Strings'])
        elif all(isinstance(i, dict) for i in obj):
            return pd.DataFrame(obj)
    elif isinstance(obj, dict):
        return pd.DataFrame([obj])
    elif isinstance(obj, str):
        try:
            json_obj = json.loads(obj)
            return summarize(json_obj)
        except json.JSONDecodeError:
            return pd.DataFrame([obj], columns=['Strings'])
    else:
        return pd.DataFrame([str(obj)], columns=['Objects'])

# Test the function
print(summarize(["hello", "world"]))
print(summarize([{"name": "John", "age": 30}, {"name": "Jane", "age": 25}]))
print(summarize({"name": "John", "age": 30}))
print(summarize('{"name": "John", "age": 30}'))
print(summarize([{"name": "John", "age": 30, "friends": [{"name": "Jane", "age": 25}]}]))


data = json.load(open('example_data.json', 'r'))

print(summarize(data))