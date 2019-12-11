#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py
#                                                                             
# PROGRAMMER: Alex Tkatchev
# DATE CREATED: 9/4/19                                 
# REVISED DATE: 9/4/19 
# PURPOSE: Create a function calculates_results_stats that calculates the 
#          statistics of the results of the programrun using the classifier's model 
#          architecture to classify the images. This function will use the 
#          results in the results dictionary to calculate these statistics. 
#          This function will then put the results statistics in a dictionary
#          (results_stats_dic) that's created and returned by this function.
#          This will allow the user of the program to determine the 'best' 
#          model for classifying the images. The statistics that are calculated
#          will be counts and percentages. Please see "Intro to Python - Project
#          classifying Images - xx Calculating Results" for details on the 
#          how to calculate the counts and percentages for this function.    
#         This function inputs:
#            -The results dictionary as results_dic within calculates_results_stats 
#             function and results for the function call within main.
#         This function creates and returns the Results Statistics Dictionary -
#          results_stats_dic. This dictionary contains the results statistics 
#          (either a percentage or a count) where the key is the statistic's 
#           name (starting with 'pct' for percentage or 'n' for count) and value 
#          is the statistic's value.  This dictionary should contain the 
#          following keys:
#            n_images - number of images
#            n_dogs_img - number of dog images
#            n_notdogs_img - number of NON-dog images
#            n_match - number of matches between pet & classifier labels
#            n_correct_dogs - number of correctly classified dog images
#            n_correct_notdogs - number of correctly classified NON-dog images
#            n_correct_breed - number of correctly classified dog breeds
#            pct_match - percentage of correct matches
#            pct_correct_dogs - percentage of correctly classified dogs
#            pct_correct_breed - percentage of correctly classified dog breeds
#            pct_correct_notdogs - percentage of correctly classified NON-dogs
#
##
# 
def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results of the program run using classifier's model 
    architecture to classifying pet images. Then puts the results statistics in a 
    dictionary (results_stats_dic) so that it's returned for printing as to help
    the user to determine the 'best' model for classifying images. Note that 
    the statistics calculated as the results are either percentages or counts.
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
    Returns:
     results_stats_dic - Dictionary that contains the results statistics (either
                    a percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value. See comments above
                     and the previous topic Calculating Results in the class for details
                     on how to calculate the counts and statistics.
    """        
    #Create empty dictionary for results_stats_dic
    results_stats_dic = dict()
    
    #Sets all counters to initial values of zero so that they can 
    #be incremented while processing through the images in results_dic
    results_stats_dic['n_dogs_img'] = 0
    results_stats_dic['n_match'] = 0 
    results_stats_dic['n_correct_dogs'] = 0
    results_stats_dic['n_correct_notdogs'] = 0
    results_stats_dic['n_correct_breed'] = 0
    
    #process through the results dictionary
    for key in results_dic:
        #match between pet image and classifer labels
        if results_dic[key][2] == 1:
            results_stats_dic['n_match'] +=1
            
        #Count how many pet images of dogs has breed correctly classified 
        #Happens when pet image label indicates the image is-a-dog AND
        #pet image label and the classifier label match. 
        #if dog breed is correctly classified, increment n_correct_breed
        #n_correct_breed is a key in the resut_stats_dic with its 
        #value representing the number of correctly classified dog breeds
        #Pet Image Label is-a dog AND Classifer Labels match - counts Correct Breed
        if results_dic[key][3] == 1 and results_dic[key][2] ==1:
            results_stats_dic['n_correct_breed'] += 1
        
        #Pet Image Label is a Dog - counts number of dog images
        if results_dic[key][3] == 1:
            results_stats_dic['n_dogs_img'] += 1
            
            #Classifier classifies image as-a Dog (& pet image is a dog)
            #counts number of correct dog classifications
            if results_dic[key][4] == 1:
                results_stats_dic['n_correct_dogs'] += 1
                
        #counts how many pet images that are NOT dogs that were correctly classified
        #happens when the pet image label indicates the image is-NOT-a-dog 
        #AND the classifier label indicates the images is-NOT-a-dog.
        #Determines when the classifier label indicates the image 
        #is-NOT-a-dog and increments 'n_correct_notdogs' 
        #'n_correct_notdogs' is a key in the results_stats_dic dictionary 
        #it's value represents the number of correctly classified NOT-a-dog images.
        #else below indicates that the pet image label indicates the image is-NOT-a-dog 
        else:
            #Classifier classifies image 'as-NOT-a' dog.
            if results_dic[key][4] == 0:
                results_stats_dic['n_correct_notdogs'] += 1
        #DEBUG
    #print("calculate_results_stats.py n_dogs_img:", results_stats_dic['n_dogs_img'])
    #print("calculate_results_stats.py n_match:", results_stats_dic['n_match'])
    #print("calculate_results_stats.py n_correct_dogs:", results_stats_dic['n_correct_dogs'])
    #print("calculate_results_stats.py n_correct_notdogs:", results_stats_dic['n_correct_notdogs'])
    #print("calculate_results_stats.py n_correct_breed:", results_stats_dic['n_correct_breed'])
        
    #calculates run statistics (counts & percentages) below that are 
    #using the counters from above
    #calculate number of total images
    results_stats_dic['n_images'] = len(results_dic)
    
    #calculates number of not-a-dog images using - images & dog image counts
    results_stats_dic['n_notdogs_img'] = (results_stats_dic['n_images'] - 
                                          results_stats_dic['n_dogs_img'])
    
    #calculates the % of corecctly matched images. 
    #Calcualted by number of correctly matched images (n_match) 
    #divided by number of images (n_images). Multiplied by 100
    results_stats_dic['pct_match'] = (results_stats_dic['n_match'] /
                                      results_stats_dic['n_images'])*100.0
    
    #calculates the % of correctly classified dog images.
    #calculated by the number of correctly classified dog images('n_correct_dogs') 
    #divided by the number of dog images('n_dogs_img') multiplied by 100
    results_stats_dic['pct_correct_dogs'] = (results_stats_dic['n_correct_dogs'] /
                                             results_stats_dic['n_dogs_img'])*100.0
    
    #calculates the % of correctly classified breeds of dogs
    #Calculated by the number of correctly classified breeds of dog('n_correct_breed') 
    #divided by the number of dog images('n_dogs_img'). multiplied by 100
    results_stats_dic['pct_correct_breed'] = (results_stats_dic['n_correct_breed'] /
                                              results_stats_dic['n_dogs_img'])*100.0

    #calculates % correct not-a-dog images
    #use conditional statement for when no 'not a dog' images were submitted
    if results_stats_dic['n_notdogs_img'] > 0:
        results_stats_dic['pct_correct_notdogs'] = (results_stats_dic['n_correct_notdogs'] /
                                                    results_stats_dic['n_notdogs_img'])*100.0
    else:
        results_stats_dic['pct_correct_notdogs'] = 0.0
                         
    return results_stats_dic
