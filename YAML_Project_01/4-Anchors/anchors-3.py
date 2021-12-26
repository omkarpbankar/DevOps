import yaml
import sys

server=sys.argv[1]

with open("anchors-3.yaml",'r',encoding="utf8") as stream:
    try:
        data = yaml.safe_load(stream)
        for key, value in data.items():
            if key == server:
                for k,v in value.items():
                    print(f'{k}:{v}')
    except yaml.YAMLError as e:
        print(e)