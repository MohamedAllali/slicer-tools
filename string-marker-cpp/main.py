#coding:utf8

import os;
import string_marker_regex as marker;
import cpp_files_finder as finder;

BASE_DIR = 'slicer-marked/';

if __name__ == '__main__':
	slicer_dir = 'D:\\My world\\Medoc\\Etudes\\DIC2\\Python\\FunCoding\\3d-slicer\\Slicer'
	cppFiles = finder.find_all_cpp_files(slicer_dir)

	# Uncomment to directly put marked files on the slicer root folder
	# BASE_DIR = slicer_dir + '\\';

	if not os.path.isdir(BASE_DIR):
		os.mkdir(BASE_DIR);

	fileCount = 0;
	for file in cppFiles :
		marked_file = BASE_DIR + file;
		file = slicer_dir + '/' + file;
		directory = os.path.dirname(marked_file);
		print(marked_file);

		try:
			if not os.path.isdir(directory):
				os.makedirs(directory)

			marker.mark_source_file(file, marked_file)
			fileCount += 1
		except:
			print('\t[-] Error');
	print(f"\n\n{fileCount} / {len(cppFiles)} fichiers marqués !")
