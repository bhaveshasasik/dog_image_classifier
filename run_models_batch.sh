#!/bin/sh
# */AIPND-revision/intropyproject-classify-pet-images/run_models_batch.sh
#                                                                             
# PROGRAMMER: Bhavesha Sasikumar
# DATE CREATED: 7/2/2024
# REVISED DATE: 
# PURPOSE: Runs all three models to test which provides 'best' solution.
#          Please note output from each run has been piped into a text file.
#
# Usage: sh run_models_batch.sh -- will run program from commandline within Project Workspace
#

# Enable verbose mode
set -x


python check_images.py --dir pet_images/ --arch resnet --dogfile dognames.txt > resnet_pet-images.txt
cat resnet_pet-images.txt

python check_images.py --dir pet_images/ --arch alexnet --dogfile dognames.txt > alexnet_pet-images.txt
cat alexnet_pet-images.txt

python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt > vgg_pet-images.txt
cat vgg_pet-images.txt

# Disable verbose mode
set +x

