import os
import sys
import colorama

import utility_data

"""
    VALID COMMANDS:
        create = creates a new project.
"""

def create_empty_directories(project_name):
    os.mkdir(
        os.path.join(os.getcwd(), project_name)                         # create the parent dir.
    )
    os.mkdir(
        os.path.join(os.getcwd(), project_name, project_name)           # create the src dir.
    )
    os.mkdir(
        os.path.join(os.getcwd(), project_name, "test")                 # create the tests dir.
    )
    os.mkdir(
        os.path.join(os.getcwd(), project_name, "include")              # create the deps. dir.
    )
    os.mkdir(
        os.path.join(os.getcwd(), project_name, "doc")                  # create the docs dir.
    )
    os.mkdir(
        os.path.join(os.getcwd(), project_name, "include", "catch2")    # crate the testing lib. dir.
    )

def create_gitignore(project_name):
    with open(os.path.join(os.getcwd(), project_name, ".gitignore"), "w+") as fout:
        fout.write(str(utility_data.GITIGNORE))

def create_catch_header_file(project_name):
    with open(os.path.join(os.getcwd(), project_name, "include", "catch2", "catch.hpp"), "w+") as fout:
        fout.write(str(utility_data.CATCH))

if __name__ == "__main__":
    try:
        command = str(sys.argv[1])
    except IndexError:
        print(colorama.Back.RED + "[-] Error: No Command Was Specified")
        sys.exit(-1)

    if (command.lower() == "create"):
        try:
            project_name = str(sys.argv[2])
        except IndexError:
            print(colorama.Back.RED + "[-] Error: No project name was specified")
            sys.exit(-1)

        ########################################
        #   CREATE THE BASIC EMPTY DIR STRUCT. #
        ########################################
        try:
            create_empty_directories(project_name)
            print(colorama.Back.GREEN + "[+] Successfully created the empty project directories")
        except Exception as err:
            print(colorama.Back.RED + "[-] Error: Script failed to create project directory. {}".format(str(err).split(":")[0]))
            sys.exit(-1)
        
        #########################################
        #   CREATE THE .GITIGNORE FILE AND FILL #
        #   IT UP                               #
        #########################################
        try:
            create_gitignore(project_name)
            print(colorama.Back.GREEN + "[+] Successfully created the .gitignore file")
        except Exception as err:
            print(colorama.Back.RED + "[-] Error: Failed to create the .gitignore file. {}".format(str(err).split(":")[0]))

        #########################################
        #   CREATE THE CATCH.HPP HEADER FILE    #
        #########################################
        try:
            create_catch_header_file(project_name)
            print(colorama.Back.GREEN + "[+] Successfully created the catch.hpp dependency file")
        except Exception as err:
            print(colorama.Back.RED + "[-] Error: Failed to create the catch.hpp dependency file. {}".format(str(err).split(":")[0]))
            sys.exit(-1)

        #########################################
        #   CREATE THE MAKEfile                 #
        #########################################
        """TODO"""

    else:
        print(colorama.Back.RED + "[-] Error: Command '{}' is not valid. Try --help to get a full list of commands".format(command))
        sys.exit(-1)