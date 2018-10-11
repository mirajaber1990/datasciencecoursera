import json
from pprint import pprint

# open file
with open('C:\Users\imj\Desktop\Ford_alles\New_scrits\write_data_08552c21ba9b5d83827d248733728058_1505920921.json') as infile:
    # decode json
    json_data = json.load(infile)

print ('Original File:\n')
pprint(json_data)

# Changing a value in the json
json_data["blocks"][0]["messages"][0]["0x420"]["signals"]["FUEL_FLOW"]["value"] = 0.9999999999
print ('\n\nChanged File: \n')
pprint (json_data)
file = open("copy.txt", "w") 
file.write("Your text goes here") 
file.close() 
testfile1 = open('testfile1.txt', 'w')
# outputting json to file


with open('jfile.json', 'w') as outfile:
    # indent, separators and sort_keys is only important for pretty printing. otherwise the file would only have one very long line
    json.dump(json_data, outfile, indent=4, separators=(',', ': '), sort_keys=True)