print("hello")

import os


platform_name = "silverstone_xp"

template_p_name = "silverstone"

curr_path = os.getcwd()



def create_dir(path):
    try:
        os.mkdir(path)
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s " % path)


def collect_value(text):
    keyboard_input = input(text)
    return keyboard_input

output_path = curr_path+"/output"
create_dir(output_path)

platform_name = collect_value("Please input the platform name :")

