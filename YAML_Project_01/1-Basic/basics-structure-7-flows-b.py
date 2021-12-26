import yaml

my_file = "basics-structure-7-flows-a.yaml"

with open(my_file,'r', encoding="utf8") as stream:
    try:
        data = yaml.safe_load(stream)
        for key, value in data.items():
            print("\n")
            print(f'key:{key}')
            print(f'value:{value}')
            data_type = type(value)
            print(f'The datatype of {value} is {data_type}')
            print("--")

    except yaml.YAMLError as e:
        print(e)