import yaml

with open('anchors-2.yaml','r', encoding= 'utf-8') as stream:
    try:
        data= yaml.safe_load(stream)
        for key, value in data.items():
            if key== "server1":
                for k,v in value.items():
                    print(f'{k}:{v}')
    except yaml.YAMLError as e:
        print(e)