# -*- coding: utf8 -*-
import os, sys

def find_all_py_files(slicer_root_dir, relative_path=True):
	pyFiles = []
	slicer_root_dir = os.path.realpath(slicer_root_dir)
	
	for root, folders, files in os.walk(slicer_root_dir):
		pyFiles += [os.path.join(root, file) for file in files if file.endswith('.py')]
	files = [uiFile.replace(slicer_root_dir, '')[1:] for uiFile in pyFiles] if relative_path else pyFiles;
	return files;
	

if __name__ == '__main__':
	if len(sys.argv) == 2 :
		if os.path.isdir(sys.argv[1]):
			root_dir = sys.argv[1]
			pyFiles = find_all_py_files(root_dir)
			print('\n'.join(pyFiles))
			print(f"\n\n{len(pyFiles)} files found")
		else:
			print("Sorry, the specified parameter is not a folder")
	else:
		print("You should specify the slicer root folder as an argument !")