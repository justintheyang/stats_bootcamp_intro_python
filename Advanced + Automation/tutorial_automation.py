# This tutorial was written by Ben Prystawski in 2022 for the Stanford Psychology Department's
# statistics and programming bootcamp. It is based on Chapter 10 of Automate the Boring Stuff
# with Python, which is available for free here: https://automatetheboringstuff.com/2e/chapter10/

# shutil lets us run shell commands (like we learned about in the Bash workshop) in Python
import shutil

# os contains utilities for interacting with the operating system
import os

# pathlib contains utilities that let you manage filepaths
from pathlib import Path


# any code contained here will (only) be run when you type `python tutorial_automation.py`
if __name__ == "__main__":

    home = Path.home()
    print(home)

    # You can concatenate folders to tasks using
    # (this is because if a cheeky way pathlib redefines division)

    # TODO: change this to the folder where you downloaded the materials
    project_path = home / "Documents" / "python-bootcamp" / "advanced"

    # .glob returns a list of files that match a given description.
    # This should show the files in the current directory that start with
    # "Python module02"
    for filepath in project_path.glob("Python module02*"):
        print(filepath)

    # That's cool! Now suppose you want to create a new directory called "notebooks"
    # then move all your notebooks into it. First, you can use `os.mkdir.` Look up
    # how to do that and do it below!

    # TODO: use `os.mkdir` to create a sub-directory of `project_path` called `notebooks.`


    # Next, we want to copy all the jupyter notebooks (files ending in .ipynb) to the
    # `notebooks` directory. `shutil.move` lets you move a file into a different
    # directory. It works like this: `shutil.move(SOURCE_FILEPATH,
    # DESTINATION_DIRECTORY)`

    # TODO: move all the Jupyter notebooks into the `notebooks` folder with shutil.move
    # hint: the for loop with `glob` shown above will both be useful



    # We moved all the notebooks, but the .ipynb_checkpoints folder hasn't moved.
    # This folder contains the checkpoints for all the notebooks (i.e. which
    # cells have been run and the outputs they've produced). Let's copy that
    # into the `notebooks` folder too so the checkpoints will still be there when
    # we open the notebooks and we can also move the notebooks back out of the
    # `notebooks` directory and preserve their checkpoints.

    # We could create a new directory inside `notebooks` that's also called
    # `.ipynb_checkpoints`, then copy each file from `.ipynb_checkpoints` into
    # it, but that would be a lot of work.

    # Luckily, `shutil.copytree` lets us copy entire directories, including all
    # of the file and sub-directories they contain. You can use it just with
    # shutil.copytree(DIRECTORY_TO_COPY, DESTINATION_DIRECTORY)

    # TODO: copy .ipynb_checkpoints into the `notebooks` directory.


    # Great! We know how to move around files and copy them. Now, let's look at
    # reading and editing a text file.

    # We can open a file with open() like this:
    text_file = open("./example_text.txt", "r")

    # This gives us a file buffer.
    print(f"type of text file: {type(text_file)}")

    # If we want text, we can use the file buffer's `read` method
    print("Here's what happens when we use the `read` method:")
    print(text_file.read())

    # Now suppose we harbor an irrational hatred of Beckman Bistro.
    # Maybe we want to change the rating of Beckman Bistro to 1/5.
    # We can do that by reading the file, saving the output to a string,
    # replacing the rating in the string, then writing that string to the
    # same file. Let's do that step by step.

    # TODO: read `text_file` and save the output to a string called `ratings_str`


    # TODO: replace "Beckman Bistro: 3/5" with "Beckman Bistro: 1/5" using the
    # string `replace` method. if `s` is a string, `s.replace("asdf", "qwerty")` returns
    # a version of `s` with every instance of "asdf" replaced with "qwerty"

    # Next, we'll save the modivied string to a file. We can open a file called
    # "updated_text.txt" as follows:
    updated_file = open("./updated_text.txt", "w")
    # note "w" instead of "r" -- that means we want to write to the file rather than read from it

    # `updated_file.write(STRING)` will write the contents of STRING to the file represented by
    # `updated_file`. This will overwrite anything already stored there.

    # TODO: save the updated string to the new file



    # This tutorial just illustrated a small fraction of what Python can help
    # you with. If you ever find yourself doing something over and over again,
    # it's usually worth it to try writing a script to automate it for you.
