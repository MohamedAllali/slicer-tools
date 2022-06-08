#coding:utf8

import os, sys;
import string_marker as marker;
import py_files_finder as finder;

BASE_DIR = 'slicer-marked/';

if __name__ == '__main__':
	if len(sys.argv) == 2:
		if os.path.isdir(sys.argv[1]):
			slicer_dir = sys.argv[1]
		else:
			print("Sorry, the specified parameter is not a folder")
			exit()
	else:
		print("You should specify the slicer root folder as an argument !")
		exit();

	
	pyFiles = finder.find_all_py_files(slicer_dir)

	if not os.path.isdir(BASE_DIR):
		os.mkdir(BASE_DIR);

	fileCount = 0;
	for file in pyFiles :
		if not file.endswith('__init__.py') and not file.endswith('__version__.py'):
			marked_file = BASE_DIR + file;
			file = slicer_dir + '/' + file;
			directory = os.path.dirname(marked_file);
			# directory = os.path.realpath(directory);
			print(marked_file);

			try:
				if not os.path.isdir(directory):
					os.makedirs(directory)

				marker.mark_source_file(file, marked_file)
				fileCount += 1
			except:
				print('\t[-] Error');
		else:
			print("\t[-] Skipped :", file)
	print(f"\n\n{fileCount} / {len(pyFiles)} fichiers marqués !")
