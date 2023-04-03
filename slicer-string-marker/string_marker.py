import ast

def get_source_code(source_file):
	fichier = open(source_file)
	source_code = fichier.read()
	fichier.close()

	return source_code;

def save_source_code(source_code, source_file='marked.py'):
	fichier = open(source_file, 'w')
	source_code = fichier.write(source_code)
	fichier.close()

def get_string_list(source_file):
	source_code = get_source_code(source_file)
	tree = ast.parse(source_code);
	all_strings = [node.s for node in ast.walk(tree) if isinstance(node, ast.Str)];
	# removing docstrings from translatable strings
	for node in ast.walk(tree):
		if isinstance(node, ast.FunctionDef) or isinstance(node, ast.AsyncFunctionDef) \
			or isinstance(node, ast.ClassDef) or isinstance(node, ast.Module):
			docstring = ast.get_docstring(node, False)
			if docstring != None:
				all_strings.remove(docstring)

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
	words_to_ignore = ['temp', 'dicomListener', 'dicombrowser', 'QWidget', '\n'];
	
	if (len(string) <= 1) or string.isnumeric() or (len(string) in [2, 3] and string.startswith('%')) \
	or (string.endswith('_')) or string.startswith('/') or string in words_to_ignore:
		return False;
	return True;


def mark_string(code, chaine):
	if not is_markable_string(chaine):
		return code;

	string_delimiters = ['"""', "'''", '"', "'"];

	for delimiter in string_delimiters:
		string = delimiter + chaine + delimiter;

		if len(delimiter) == 3:
			index = code.find(string)
			if index != -1 and code[index-2:index] != "_(":
				pattern = '_(' + string + ')';
				code = code.replace(string, pattern)
		else: # in case of " or ' as string delimiter
			# we just get the position of strings that are not already marked
			indexes = [index for index in find_all_strings(code, string) if code[index-4:index] not in ["_(''", '_(""']];
			indexes = [index for index in indexes if code[index-2:index] != "_("];

			decalage = 0; # at each replace, the index evolves
			for index in indexes:
				index += decalage;
				pattern = '_(' + string + ')';
				code = code[:index] + pattern + code[index+len(string):]
				decalage += 3;
	return code;

def mark_source_file(source_file, marked_source_file=None):
	source_code = get_source_code(source_file)
	strings = get_string_list(source_file)
	strings = list(set(strings)) # suppression des doublons

	for string in strings:
		source_code = mark_string(source_code, string)

	if not marked_source_file:
		file_extension_index = source_file.find('.py')
		marked_source_file = source_file[:file_extension_index] + '-marked.py'
	save_source_code(source_code, marked_source_file);

if __name__ == '__main__':
	mark_source_file('data/dicom.py');
	print("Tagging process done !")