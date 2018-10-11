def convert_json(json_data):
	import json
	from pprint import pprint
	print ('json data:\n')
	pprint(json_data)

	# Changing a value in the json
	json_data["blocks"][0]["messages"][0]["0x420"]["signals"]["FUEL_FLOW"]["value"] = 0.9999999999
	print ('\n\nChanged File: \n')
	pprint (json_data)

	# outputting json to file
	with open('new_file.json', 'w') as outfile:
		# indent, separators and sort_keys is only important for pretty printing. otherwise the file would only have one very long line
		json.dump(json_data, outfile, indent=4, separators=(',', ': '), sort_keys=True)
	return json_data