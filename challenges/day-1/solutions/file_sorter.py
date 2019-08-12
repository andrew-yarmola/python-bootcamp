import os
import random
import shutil
import requests

random_text_uri = 'http://www.randomtext.me/api/lorem/p-{}/{}-{}/'

def generate_random_text_file(file_name) :
    """ Writes random words and lines to file_name.
    Overwrites the file if it already exits. """
    num_pars = random.randint(5,10)
    min_words = random.randint(5,10)
    max_words = random.randint(20,50)

    text_request = requests.get(random_text_uri.format(num_pars,min_words,max_words))
    if not text_request.status_code == requests.codes.ok :
        raise Exception("Failed to download random text")
    
    try :
        text = text_request.json()['text_out']
        text = text.replace('<p>','')
        text = text.replace('</p>','')
        text = text.replace('\r','\n\n')
        text = text.rstrip() 
        with open(file_name, 'w') as fp :
          fp.write(text)
    except :
        raise Exception("Unexpected randomtext.me format")

def touch(file_name):
    """ Updates file access and modify times or creates file. """
    try :
        os.utime(file_name)
    except :
        open(file_name, 'a').close()

def make_files(path_to_text, files_dir = 'sorting_dir', ext = 'ext') :
    """ Makes files with file names given by words in path_to_random_text. """
    if not os.path.isdir(files_dir) :
        os.mkdir(files_dir)
    with open(path_to_text, 'r') as fp :
        for line in fp :
            basenames = line.split()
            for name in basenames :
                new_file = os.path.join(files_dir, name + '.' + ext)
                touch(new_file)                

def first_letter_sort(sorting_dir) :
    for root, dirs, files in os.walk(sorting_dir) :
        orig_cwd = os.getcwd()
        os.chdir(root)
        for path in files :
            dir_name = path[0].upper()
            # make sure our dir_name is a letter
            if not dir_name.isalpha() : continue
            if not os.path.isdir(dir_name) :
                os.mkdir(dir_name)
            shutil.move(path, dir_name)
        os.chdir(orig_cwd)
        break # only touch files in the top dir
