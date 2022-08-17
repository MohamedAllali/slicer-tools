import re

def get_source_code(source_file):
	fichier = open(source_file)
	source_code = fichier.read()
	fichier.close()

	return source_code;

def save_source_code(source_code, source_file='marked.cpp'):
	fichier = open(source_file, 'w')
	source_code = fichier.write(source_code)
	fichier.close()

def get_string_list(source_file):
	source_code = get_source_code(source_file)

	source_code = re.sub('(#.*)\n', '', source_code); # se débarrasser des #include, #define, ...
	strings = re.findall('"[^"]*"', source_code);
	# strings += re.findall("'[^']*'", source_code);
	all_strings = [string[1:-1] for string in strings if string != '""'];

	return all_strings;

def find_all_strings(string, searched):
	indexes = [];
	index = string.find(searched);
	fromIndex = 0;
	while index != -1:
		indexes.append(fromIndex + index);
		string = string[index+len(searched):]
		index = string.find(searched);
		fromIndex = indexes[-1] + len(searched)
	return indexes;
			
def is_markable_string(string):
	string = string.strip();
	words_to_ignore = ['temp', 'dicomListener', 'QWidget'];
	
	if (len(string) <= 1) or string.isnumeric() or (len(string) in [2, 3] and string.startswith('%')) \
	 or string in words_to_ignore:
		return False;
	return True;


def mark_string(code, chaine):
	if not is_markable_string(chaine):
		return code;

	string = '"' + chaine + '"';

	indexes = [];
	for index in find_all_strings(code, string):
		if code[index-3:index] != 'tr(':
			indexes.append(index);

	decalage = 0; # at each replace, the index evolves
	for index in indexes:
		index += decalage;
		pattern = 'tr("' + chaine + '")';
		code = code[:index] + pattern + code[index+len(string):]
		decalage += 4;

	return code;

def mark_source_file(source_file, marked_source_file=None):
	source_code = get_source_code(source_file)
	strings = get_string_list(source_file)
	strings = list(set(strings)) # suppression des doublons

	for string in strings:
		source_code = mark_string(source_code, string)

	if not marked_source_file:
		file_extension = '.cxx';
		file_extension_index = source_file.find(file_extension)
		if file_extension_index == -1:
			file_extension = '.cpp';
			file_extension_index = source_file.find(file_extension)
		marked_source_file = source_file[:file_extension_index] + '-marked' + file_extension;
	save_source_code(source_code, marked_source_file);

if __name__ == '__main__':
	mark_source_file('test-data/qSlicerSettingsViewsPanel.cxx')
	print("Tagging process done !")
