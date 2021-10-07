def read_file(filename):
	#write your function here.	
	data = open(filename)
	string_list = []

	for row in data:
		string_list.append(row.strip()) 
	return string_list

def parse_csv_lines(lines):
	#write your function here. It might possibly call other functions you wrote.
	list_of_list = [[]]

	for line in lines:
		list_of_list.append(line.split(","))
	
	return list_of_list

def parse_delimited_lines(lines, delimiter):
	#write your function here. It might possibly call other functions you wrote
	line_list = []
	for line in lines:
		line_list.append(line.split(delimiter))
	return line_list

def age_difference(lines):
	#write your function here. It might possibly call other functions you wrote.
	age_diff_list = []
	
	for line in lines:
		age_diff = abs(float(line[1]) - float(line[-1]))
		age_diff_list.append([line[0],age_diff])
	return age_diff_list

def find_unisex_names(male_names, female_names):
	#write your function here. It might possibly call other functions you wrote.
	males = set(male_names)
	female = set(female_names)
	unisex = males.intersection(female)
	return unisex# This function has to return a set.

def build_name_dataset(female_names, male_names, unisex_names):
	#write your function here. It might possibly call other functions you wrote.
	# Should not return anything.
	names = set(female_names).union(set(male_names))
	filename = open("all_names.csv","w")
	for name in names: 
		if name in unisex_names:
			filename.write(name+",U\n")
		elif name in female_names:
			filename.write(name+",F\n")
		elif name in male_names:
			filename.write(name+",M\n")
	filename.close()
	return

def write_sorted_names(names):
	#write your function here. It might possibly call other functions you wrote.
	first_letter = set()
	for name in names: 
		first_letter.add(name[0][0])

	for letter in sorted(first_letter):
		filename = open(letter+".csv","w")
		for name in names:
			if letter == name[0][0]:
				filename.write(name[0]+","+name[1]+"\n")
			filename.close()
	print("Done")
	return None


def main():
	# Here you will need to call some or all of the above functions to test that your code is working. Some functions will generate an output that is used as input in another function.

	filename = "/Users/computer/Documents/GitHub/python_examples/assignments/second_assignment/data/municipalities-2005-2019.csv"
	female_filename = "/Users/computer/Documents/GitHub/python_examples/assignments/second_assignment/data/female_names.csv"
	male_filename = "/Users/computer/Documents/GitHub/python_examples/assignments/second_assignment/data/male_names.csv"
	all_names_filename = "all_names.csv"

	print(read_file(filename))
	print(parse_csv_lines(filename))
	print(parse_csv_lines(filename),";")
	print(age_difference(parse_delimited_lines(read_file(filename),";")))
	print(find_unisex_names(read_file(male_filename),read_file(female_filename)))
	build_name_dataset(read_file(male_filename), read_file(female_filename), find_unisex_names(read_file(male_filename),read_file(female_filename)))
	write_sorted_names(parse_delimited_lines(read_file(all_names_filename),","))

if __name__ == "__main__":
	# Executes only if run as a script
	main()
