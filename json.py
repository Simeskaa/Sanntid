import jsonlib as json


test = json.write({'sensor 1' : 25,
                   'sensor 2' : 13,
                   'sensor 3' : "feil melding :("},sort_keys=True, indent=' ').decode ('utf8')

read = json.read(test)

test_value = read['sensor 1']

print(read['sensor 1'])
print(read['sensor 2'])
print(read['sensor 3'])
print(test_value)


