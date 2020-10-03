#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/check_images.py
#
# PROGRAMMER: Christiaan Lombard
# DATE CREATED: 2020-10-03
# REVISED DATE: 2020-10-03
# PURPOSE: Bulk resize uploaded images
#
#   Example call:
#    python resize_images.py
##

# Imports python modules
from time import time, sleep
from PIL import Image
from resizeimage import resizeimage
from os import listdir, path, remove, rename

# Main program function defined below
def main():
    # Measures total program runtime by collecting start time
    start_time = time()

    max_width = 960
    max_height = 960
    folder = 'uploaded_images'

    for filename in listdir(folder):

        filepath = "%s/%s"%(folder,filename)

        if not filename.endswith('.jpg'):
            continue

        size_slug = "contain%dx%d" % (max_width, max_height)
        new_filename = "%s.%s.%s" % (filename.split('.')[0], size_slug, filename.split('.')[-1])
        new_filepath = "%s/%s"%(folder,new_filename)
        replace_file = False

        if filename == new_filename or path.isfile(new_filepath):
            print("File %s already exists, skipping file" % (new_filename))
            continue


        with open(filepath, 'r+b') as file:
            with Image.open(file) as image:

                if image.width <= max_width and image.height <= max_height:
                    print("File %s already resized, skipping file" % (filename))
                else:
                    print('Resizing image %s => %s' % (filename, new_filename))

                    if image.width > image.height:
                        resized = resizeimage.resize_width(image, max_width)
                    else:
                        resized = resizeimage.resize_height(image, max_height)

                    resized.convert('RGB').save(new_filepath, image.format)
                    replace_file = True

        if replace_file:
            remove(filepath)
            rename(new_filepath, filepath)



    # Measure total program runtime by collecting end time
    end_time = time()

    # Computes overall runtime in seconds & prints it in hh:mm:ss format
    tot_time = end_time - start_time # calculate difference between end time and start time
    print("\n** Total Elapsed Runtime:",
          str(int((tot_time/3600)))+":"+str(int((tot_time%3600)/60))+":"
          +str(int((tot_time%3600)%60)) )


# Call to main function to run the program
if __name__ == "__main__":
    main()
