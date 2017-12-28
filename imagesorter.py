"""
Branch created so I can put some Comments in for DP
Look through a folder and put all .jpg files into subfolders based on date
originally taken in EXIF DATA
"""
# Any line starting with the '#' symbol is a comment
# And the program doesn't do anything with it.

# These lines are importing extra functions that
# someone else has already written

# Glob stands for global and is a search thing
from glob import glob
# OS is for interacting with the operating system
import os
# Stands for shell utilities - the shell is the command line
from shutil import copyfile

#These are some special modules to deal with images
from PIL import Image
from PIL.ExifTags import TAGS

# This line defines a function 
# tutorial on what that means at http://bit.ly/2mhdpXq
def get_exif(file_name):
    """A function wrapping PIL functionality to return
    a dictionary with exif data for the input

    takes
        fn (string)
            a file name and location
    returns
        output (dictionary)
            a dictionary of pep8 the file's exif metadata

    references
        http://bit.ly/2C1VSLH
    """
    # This creates a new data object called a dictionary
    # Tutorial at http://bit.ly/2uixoJ0
    output = {}

    # These lines do some clever stuff
    # to access the data
    i = Image.open(file_name)
    info = i._getexif()

    # goes into the data in info and 
    # for each item adds somthing to our dictionary
    # called 'output'
    # We want to do this because dictionaries are easy
    # to use and understand
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        output[decoded] = value
    return output


# It's normal to have a function called main, although you could
# just stick it straight into the file
def main():
    """Search through current directory and
    subfolders looking for jpeg files, reading
    exif data and sorting files by creation date
    """
    # search through the current folder and subfolders
    # for files with names of the form something.jpg
    # files will be a list of file names and locations
    files = glob("*.jpg")

    # this next bit is called a loop
    # for every item in the list called files we will
    # do somthing: This is powerful stuff - it doesn't matter
    # whether you want to run this for 1 file or 1 million
    # except that the million will take a bit of time
    for file_name in files:
        # use that function we defined earlier
        date = get_exif(file_name)



        # Here is an interesting place to play with what date is by
        # removing the '#' from the 'print' lines below:
        #print date
        #print type(date)

        # get the information labelled 'DateTime' from the date dictionary
        date = date['DateTime']

        # And again have a play here - all the square brackets is called
        # string indexing
        #print date
        #print type(date)
        
        #date['DateTime']
        #print date[1]
        #print date[:10]
        #print date[10:]
        #print date[:-5]
        #print date[4:8]
        # (don't forget: the first letter in a string in number 0!)

        # Chop of the date at letter 10 in the string of letters
        date = date[:10]
        # replace any ":" with nothing
        date = date.replace(':', '')



        # This is unique to Python
        # We try somthing (in this case look for a folder)
        # and if the programme fails we do somthing else
        # it's really nice
        try:
            os.stat(date)
        # if the try fails because there is no folder we create
        # the folder we want
        except:
            os.mkdir(date)

        # ...and finally we copy our file into it.
        # I've chosed to use copy because it's non destructive
        copyfile(file_name, os.path.join(date, file_name))

# This is the bit that actually runs the main() functionality
# It's called a main-guard and it checks that we are
# running this file, not using "import imagesorter" in another one
if __name__ == "__main__":
    main()
