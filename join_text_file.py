# ---------------------------------------------------------------------------------- #
# join_text_file.py                                                                  #
# Desc: Join each line of both files with delimiter                                  #
# Usage: python join_text_file.py [file_name_1] [input_delimiter_text] [file_name_2] #
# By: fredfw                                                                         #
# ---------------------------------------------------------------------------------- #

import os
import sys

user_input_file_name_1 = sys.argv[1]
user_input_text = sys.argv[2]
user_input_file_name_2 = sys.argv[3]

def join_text(file_name_1, text, file_name_2):
    new_file = 'joined_' + file_name                                                                                      # define name of new file
    with open(file_name_1, 'r') as read_obj_1, open(new_file, 'w') as write_obj, open(file_name_2, 'r') as read_obj_2:    # open original files in read mode and new file in write mode
        for line_1 in read_obj_1:                                                                                         # read lines from original files one by one, join each line with the delimiter
            for line_2 in read_obj_2:
                write_obj.write(line_1 + text + line_2)
                
join_text(user_input_file_name_1, user_input_text, user_input_file_name_2)
