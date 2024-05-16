import json

input_file = 'email-template.txt'
output_file = 'companies.json'

companies = []

try: 
    with open(input_file, 'r') as file:
        lines = file.readlines()
        for i in range(0, len(lines), 2):
            company = {
                'name': lines[i].strip(),
                'email': lines[i+1].strip()
            }
            companies.append(company)
except:
    print("invalid input file")


with open(output_file, 'w') as file:
    json.dump(companies, file, indent=4)
