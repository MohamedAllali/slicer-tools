# coding: utf8 -*-

import os, re, sys, argparse

def get_context(source_file):
    if os.path.isfile(source_file):
        parent_folder = os.path.dirname(source_file)
        init_file_path = parent_folder + os.path.sep + '__init__.py'

        if os.path.isfile(init_file_path):
            context_name = os.path.basename(parent_folder)
            context_name += '.' + os.path.basename(source_file).replace('.py', '')
            return context_name
        else:
            return os.path.basename(source_file).replace('.py', '')
    else:
        return os.path.basename(source_file)

def find_all_py_files(root_dir, relative_path=True):
    pyFiles = []
    root_dir = os.path.realpath(root_dir)
    
    for root, folders, files in os.walk(root_dir):
        pyFiles += [os.path.join(root, file) for file in files if file.endswith('.py')]
    files = [uiFile.replace(root_dir, '')[1:] for uiFile in pyFiles] if relative_path else pyFiles
    return files;

def get_source_code(source_file):
    fichier = open(source_file)
    source_code = fichier.read()
    fichier.close()

    return source_code;

def save_source_code(source_code, source_file):
    fichier = open(source_file, 'w')
    source_code = fichier.write(source_code)
    fichier.close()

def transform_translate_function(source_file, tr_function_name='translate'):
    context_name = get_context(source_file)
    source_code = get_source_code(source_file)
    
    transformed_function_text = tr_function_name + '("' + context_name + '", ' + r'\1' + ')'

    source_code = re.sub(r'_\((\s*?".+?"\s*?)\)', transformed_function_text, source_code, flags=re.DOTALL)
    source_code = re.sub(r"_\((\s*?'.+?'\s*?)\)", transformed_function_text, source_code, flags=re.DOTALL)
    source_code = re.sub(r'_\((\s*?""".+?"""\s*?)\)', transformed_function_text, source_code, flags=re.DOTALL)
    source_code = re.sub(r"_\((\s*?'''.+?'''\s*?)\)", transformed_function_text, source_code, flags=re.DOTALL)
    
    return source_code;

def main():
    parser = argparse.ArgumentParser(
        prog='lupdate_preprocess',
        description="Make translation function calls compatible to lupdate needs"
    )
    parser.add_argument("-i", "--input", type=str, help="input file/folder name")
    parser.add_argument("-o", "--output", type=str, help="output file/folder name")
    parser.add_argument("-f", "--funcname", type=str, metavar='TR_FUNCTION_NAME', help="the translation function name (e.g. tr/translate)", default='translate')

    args = parser.parse_args()
    if not args.input:
        parser.print_help()
        sys.exit(2)

    input_file = args.input
    tr_function_name = args.funcname

    if os.path.isfile(input_file):
        transformed_code = transform_translate_function(input_file, tr_function_name)
        output_file = args.output if args.output else 'processed.py'
        save_source_code(transformed_code, output_file)
        print(f"\n[+] Processed file saved in <{output_file}> file")
    elif os.path.isdir(input_file):
        output_folder = args.output if args.output else 'processed'
        if not os.path.isdir(output_folder):
            os.mkdir(output_folder)

        pyFiles = find_all_py_files(input_file)

        fileCount = 0;
        for file in pyFiles:
            output_file = output_folder + os.path.sep + file
            output_file_directory = os.path.dirname(output_file)
            file = input_file + os.path.sep + file

            try:
                if not os.path.isdir(output_file_directory):
                    os.makedirs(output_file_directory)
                transformed_code = transform_translate_function(file, tr_function_name)
                save_source_code(transformed_code, output_file)
                fileCount += 1
            except Exception as e:
                print(f"\n\t[-] Error while saving '{output_file}': \n\t\t{str(e)}")

        print(f"\n[+] {fileCount} / {len(pyFiles)} file(s) processed")
        print(f"\n[+] Processed file(s) saved in <{output_folder}> folder")

    print("\n[+] End of file processing...")

if __name__ == '__main__':
    main()