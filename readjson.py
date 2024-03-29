# The “simplejson” module was renamed to “json" on newer Python versions.
import json

# To simplify, I saved the JSON example on a text file and loaded using “json” module.
file_handler = open("json_example.txt")

# This method execute the .read() and parsed the JSON to native Python.
json_structure = json.load(file_handler)

# At first level, your structure is a dictionary with strings as keys, and other dictionaries as values.
# This is using the ‘report’ key to map the columns names of the table (table header), and ‘data’ key to map each row in the table (actually the data).
table_name = json_structure["report"]["name"] # Dict uses values as keys.
table_headers = json_structure["report"]["header"]
table_rows = json_structure["report"]["data"]

# To access the first row of the table, you just need to access the first element of the table_row list.
first_row = table_rows[0] # Lists uses numbers as index.

# To access the second table header name (starting count from 0), which is “Interface Index”.
first_interface_index = first_row[2]

# To print a row with the header, you need to access both dicts at the same time.
for column_index,column_name in enumerate(table_headers):
  print("{}: {}".format(column_name, first_row[column_index])) # Python3 syntax for “print”. If yours is older, remove the outer parenthesis.