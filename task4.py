import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=',', new_line='\n'):
    with open(filename) as f:
        table = []
        for index, line in enumerate(f):
            fields = line.strip(new_line).replace('"','').split(delimiter)
            if index == 0:
                header = fields
                continue
            table.append({})

            for i, _ in enumerate(header):
                table[-1][header[i]] = fields[i]
    return table


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
