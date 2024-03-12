# -*- coding: utf8 -*-
import os

def find_all_cpp_files(slicer_root_dir, relative_path=True):
	cppFiles = []
	slicer_root_dir = os.path.realpath(slicer_root_dir)
	
	for root, folders, files in os.walk(slicer_root_dir):
		cppFiles += [os.path.join(root, file) for file in files if file.endswith('.cpp') or file.endswith('.cxx') or file.endswith('.h')]
	files = [uiFile.replace(slicer_root_dir, '')[1:] for uiFile in cppFiles] if relative_path else cppFiles;
	return files;
	

if __name__ == '__main__':
	root_dir = 'D:\\My world\\Medoc\\Etudes\\DIC2\\Python\\FunCoding\\3d-slicer\\Slicer'
	cppFiles = find_all_cpp_files(root_dir)
	print('\n'.join(cppFiles))
	print(f"\n\n{len(cppFiles)} fichiers trouvés")