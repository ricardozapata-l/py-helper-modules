# ====================================================================================================
# Script intro text animation script
#
# Developed by @Zapata: rl-zapata.github.io
# ====================================================================================================
import sys
import time

# ¡--- Read the intro text file and animate its contents when printing to the console ---!
# - Requires: a valid file path to a text file where the into text is

# - Considers that the first 13 lines will be printed character by character with a delay between each one, 
# and the rest will be printed line by line with a delay between each
def intro(text_path):
    with open(text_path, 'r') as text_file:
        text_content = text_file.readlines()

    for line_cnt, line_ent in enumerate(text_content):
        if line_cnt in range(12):
            for txt_char in line_ent:
                sys.stdout.write(txt_char)
                sys.stdout.flush()

                if line_cnt == 11: # name & handle line will be the slowest
                    time.sleep(0.035)
                else: # ascii art lines
                    time.sleep(0.0025)
        else:
            print(line_ent, end='')
            time.sleep(0.12)