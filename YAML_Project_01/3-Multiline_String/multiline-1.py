import yaml

my_file = "multiline-2.yaml"

with open(my_file,'r', encoding="utf8") as stream:
    try:
        data = yaml.safe_load(stream)
        for key, value in data.items():
            for k, v in value.items():
                if k == 'note1':
                    print(f'note 1 of dc: {v}')
                    print("---")
                if k == 'note2':
                    print(f'note 2 of dc: {v}')
                    print("---")

    except yaml.YAMLError as e:
        print(e)