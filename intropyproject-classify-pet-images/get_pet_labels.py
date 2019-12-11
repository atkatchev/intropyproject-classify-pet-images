#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Alex Tkatchev
# DATE CREATED: 9/4/19                                
# REVISED DATE: 9/4/19 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    #Retrieve the filenames from the folder image_dir using listdir()
    filename_list = listdir(image_dir)
    #print(filename_list) #DEBUG
    
    #Creates an empty dictionary, that will hold Pet Image filename (keys), 
    #filenames labels (as values)
    results_dic = {}
    
    #Processes through each file in the directory, extracting only the words
    #of the file that contain the pet image label   
    for idx in range(0, len(filename_list), 1):
        #Skips files that start with "." since its not a pet image file
        if filename_list[0] != ".":
            #Sets string to lower case letters
            low_pet_label = filename_list[idx].lower()
            #Splits lower case string by _ to break into words
            word_list_pet_label = low_pet_label.split("_")
            #Creates temporary label variable to hold pet label name
            pet_label = ""
            #Loops to check if word in pet name is only alphabetic characters
            #if true append word to pet_label seperated by trailing space
            for word in word_list_pet_label:
                if word.isalpha():
                    pet_label += word + " "
            #Strip off starting/trailing whitespace characters
            pet_label = pet_label.strip()
            #If filename doesn\'t already exist in dictionary add it and it\'s
            #pet_label, otherwise print an erro message indicating duplicate files
            #(filename)
            if filename_list[idx] not in results_dic:
                results_dic[filename_list[idx]] = [pet_label]
            else:
                print("** Warning: Duplicate file exist in directory", filename_list[idx])
    #DEBUG iterating through a dictionary printing all key & their associated values
    #print("\nPrinting all key-value pairs in dictionary results_dic:")
    #for key in results_dic:
        #print("Filename=", key, " Pet Label=", results_dic[key][0])
                
    return results_dic
