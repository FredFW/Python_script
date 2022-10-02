# --------------------------------------------------------------------- #
# generte_text_file.py                                                  #
# Desc: Repeat user-input several times and write them to file          #
# Usage: python generate_text_file.py [input_text] [repeat_times]       #
# By: fredfw                                                            #
# --------------------------------------------------------------------- #

import os
import sys

user_input_text = sys.argv[1]
user_input_repeat_times = sys.argv[2]

def repeat_text(text, repeat_times):
    new_file = text[0] + ' x ' + str(repeat_times)   # define name of new file
    with open(new_file, 'w') as write_obj:           # open new file in write mode
        for x in range(int(repeat_times)):           # write text to the new file several times
            write_obj.write(text + '\n')        
            print(text.strip('\n'))

    print('\n Done! \n')

repeat_text(user_input_text, user_input_repeat_times)
