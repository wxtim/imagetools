"""
Look through a folder and put all .jpg files into subfolders based on date
originally taken in EXIF DATA
"""
from glob import glob
import os
from shutil import copyfile

from PIL import Image
from PIL.ExifTags import TAGS


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
    output = {}
    i = Image.open(file_name)
    info = i._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        output[decoded] = value
    return output


def main():
    """Search through current directory and
    subfolders looking for jpeg files, reading
    exif data and sorting files by creation date
    """
    files = glob("*.jpg")
    for file_name in files:
        date = get_exif(file_name)['DateTime']
        date = date[:10].replace(':', '')
        try:
            os.stat(date)
        except:
            os.mkdir(date)
        copyfile(file_name, os.path.join(date, file_name))

if __name__ == "__main__":
    main()
