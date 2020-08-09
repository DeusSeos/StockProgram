import yaml
"""Works!!!"""
testStock = [{'AMD': {"11/01/20": "1"}}]
with open("test.yml", 'a') as file:
    yaml.dump(testStock, file)