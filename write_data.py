
import json

"""def write_data(data, name):
    with open(name, 'a+') as file:
        file.write(";".join(map(str, data)))
        file.write(f"\n")"""
def write_data(data, name):
    with open(name) as file:
        try:
            all = json.load(file)
            all.append(data)
        except:
            all = []
            all.append(data)
        #    json.dump(all, f)
    with open(name, 'w') as f:
        #try:
            
            json.dump(all, f)
        #except:
        #    all = []
        #    all.append(data)
        #    json.dump(all, f)


"""def count_data(name):
    with open(name, 'r') as file:
        data = file.read()
    return data.count('\n')"""

def count_data(name):
    with open(name) as file:
        try:
            data = json.load(file)
            file.close()
        
        except:
            file.close()
            return 1
    return len(data)+1

