#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py
#                                                                             
# PROGRAMMER: Alex Tkatchev
# DATE CREATED: 9/4/19                                
# REVISED DATE: 9/4/19 
# PURPOSE: Create a function classify_images that uses the classifier function 
#          to create the classifier labels and then compares the classifier 
#          labels to the pet image labels. This function inputs:
#            -The Image Folder as image_dir within classify_images and function 
#             and as in_arg.dir for function call within main. 
#            -The results dictionary as results_dic within classify_images 
#             function and results for the functin call within main.
#            -The CNN model architecture as model wihtin classify_images function
#             and in_arg.arch for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           classifier label as the item at index 1 of the list and the comparison 
#           of the pet and classifier labels as the item at index 2 of the list.
#
##
# Imports classifier function for using CNN to classify images 
from classifier import classifier 

def classify_images(images_dir, results_dic, model):
    """
    Creates classifier labels with classifier function, compares pet labels to 
    the classifier labels, and adds the classifier label and the comparison of 
    the labels to the results dictionary using the extend function. Be sure to
    format the classifier labels so that they will match your pet image labels.
    The format will include putting the classifier labels in all lower case 
    letters and strip the leading and trailing whitespace characters from them.
    For example, the Classifier function returns = 'Maltese dog, Maltese terrier, Maltese' 
    so the classifier label = 'maltese dog, maltese terrier, maltese'.
    Recall that dog names from the classifier function can be a string of dog 
    names separated by commas when a particular breed of dog has multiple dog 
    names associated with that breed. For example, you will find pet images of
    a 'dalmatian'(pet label) and it will match to the classifier label 
    'dalmatian, coach dog, carriage dog' if the classifier function correctly 
    classified the pet images of dalmatians.
     PLEASE NOTE: This function uses the classifier() function defined in 
     classifier.py within this function. The proper use of this function is
     in test_classifier.py Please refer to this program prior to using the 
     classifier() function to classify images within this function 
     Parameters: 
      images_dir - The (full) path to the folder of images that are to be
                   classified by the classifier function (string)
      results_dic - Results Dictionary with 'key' as image filename and 'value'
                    as a List. Where the list will contain the following items: 
                  index 0 = pet image label (string)
                --- where index 1 & index 2 are added by this function ---
                  NEW - index 1 = classifier label (string)
                  NEW - index 2 = 1/0 (int)  where 1 = match between pet image
                    and classifer labels and 0 = no match between labels
      model - Indicates which CNN model architecture will be used by the 
              classifier function to classify the pet images,
              values must be either: resnet alexnet vgg (string)
     Returns:
           None - results_dic is mutable data type so no return needed.         
    """
    for key in results_dic:
        #call classifier function to classify the images 
        #filename(key) and model   
        #pet_images/Basenji_00974.jpg, vgg
        #returns model_label as classifier label as type string       
        model_label = classifier(images_dir+key, model)
        
        #Process the results so they can be compared with pet_image label
        #set labels to lowercase and strip whitespace
        model_label = model_label.lower()
        model_label = model_label.strip()
        
        #result_dic gets appended using the append() method with the return of the classifier() method 
        results_dic[key].append(model_label)
        #define truth as pet image label
        truth = results_dic[key][0]
        
        #If the pet image label is found within the classifier label list of terms
        #as an exact match to one of the terms in the list - then they are added to
        #results_dic as an exact match(1) using extend list function
        #result_dic gets a 1 or 0 appended using the append() method 
        #if the image label is found in the classifier label.
        if truth in model_label:
            results_dic[key].append(1)
        #if not found then add to results dictionary as NOT a mathch
        else:
            results_dic[key].append(0)
    
    #DEBUG
    #print("\n classify_images.py: results_dic:\n", results_dic)
    #for key in results_dic:
    #    print("\nFilename=", key,
    #            "\nlabel=", results_dic[key][0],
    #            "\nimage=", results_dic[key][1])
                #"\nthird", results_dic[key][2])        
            
    #       This function doesn't return anything because the 
    #       results_dic dictionary that is passed into the function is a mutable 
    #       data type so no return is needed.
    None 