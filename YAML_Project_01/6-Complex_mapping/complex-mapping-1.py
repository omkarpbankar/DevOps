import yaml

with open('complex-mapping-02.yaml', 'r') as stream:
    try:
        data = yaml.safe_load(stream)
        print(data)
        for key, value in data.items():
            print(f'{key} : {value}')
            for k, v in value.items():
                print(f'{k} : {v}')
                print(type(v))

    except yaml.YAMLError as exc:
        print(exc)