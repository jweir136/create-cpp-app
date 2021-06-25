import os
import sys

import colorama

"""
    VALID COMMANDS:
        create = creates a new project.
"""

def create_empty_directories(project_name: str):
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
        except Exception as err:
            print(colorama.Back.RED + "[-] Error: Script failed to create project directory. {}".format(str(err).split(":")[0]))
            sys.exit(-1)
    else:
        print(colorama.Back.RED + "[-] Error: Command '{}' is not valid. Try --help to get a full list of commands".format(command))
        sys.exit(-1)