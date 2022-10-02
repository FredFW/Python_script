# --------------------------------------------------------------------- #
# insert_text_file.py                                                   #
# Desc: Add text to the top of file, and then append text to each line  #
# Usage: python insert_text_file.py [file_name] [input_text]            #
# By: fredfw                                                            #
# --------------------------------------------------------------------- #

import os
import sys

user_input_file_name = sys.argv[1]
user_input_text = sys.argv[2]

def insert_text(file_name, text):
    new_file = 'inserted_' + file_name                                          # define name of new file
    with open(file_name, 'r') as read_obj, open(new_file, 'w') as write_obj:    # open original file in read mode and new file in write mode
        write_obj.write(text + '\n')                                            # write text to the top of the new file
        print(text)
        for line in read_obj:                                                   # read lines from original file one by one, append each line with the inserted text (at the separate line) to the new file
            write_obj.write(line)
            print(line.strip('\n'))
            write_obj.write(text + '\n')
            print(text)
    
    print('\n Done! \n')
    
    # Uncomment below lines if need to replace the original file with new file
    # os.remove(file_name)
    # os.rename(dummy_file, file_name)

insert_text(user_input_file_name, user_input_text)
