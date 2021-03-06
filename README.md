# Udacity Project - Image Classification for a City Dog Show

My project submission for the Udacity AI Programming with Python Nanodegree, Python Module, Classifying Images Project

### Installation

- Requires Anaconda, Python 3.6, PyTorch
- `conda create -n py36 python=3.6` - Create environment with python 3.6
- `conda activate py36` - Activate environment
- `conda install pytorch torchvision python-resize-image cudatoolkit=10.2 -c pytorch` - [Install PyTorch](https://pytorch.org/get-started/locally/)


### Scripts

Go to `src/` (`cd src`) directory to run scripts

- `python check_images.py` - Classify images with default arguments
- `python check_images.py --dir uploaded_images/ --arch vgg  --dogfile dognames.txt`  - Classify `uploaded_images/` using `vgg` classifier and `dognames.txt` dogbreeds list.
- `python resize_images.py` - Resizes `uploaded_images` to max 960p x 960p
- `./run_models_batch.bat` - Run classifier on `pet_images` for every classifier and save results
- `./run_models_batch_uploaded.bat` - Run classifier on `uploaded_images` for every classifier and save results


## Udacity Specifications

### Principal Objectives

1. Correctly identify which pet images are of dogs (even if breed is misclassified) and which pet images aren't of dogs.
2. Correctly classify the breed of dog, for the images that are of dogs.
3. Determine which CNN model architecture (ResNet, AlexNet, or VGG), "best" achieve the objectives 1 and 2.
4. Consider the time resources required to best achieve objectives 1 and 2, and determine if an alternative solution would have given a "good enough" result, given the amount of time each of the algorithms take to run.

### TODO:

**Edit program `check_images.py`**

The **check_images.py** is the program file that you will be editing to achieve the four objectives above. This file contains a main() function that outlines how to complete this program through using functions that have not yet been defined. You will be creating these undefined functions in **check_images.py** to achieve the objectives above.

All of the TODOs are listed in **check_images.py**. You will find further elaborations and explanations for each, in the following concepts of this project.

**If you feel that you need more guidance, please refer to the files ending with_hints.py. In the workspace you will find a hint file for each of the tasks.**

### Important notes:

- Before beginning the project please review the [Frequently Asked Questions](https://github.com/udacity/AIPND-revision/blob/master/notes/project_intro-to-python.md), FAQ, about the project.
- This project and other lessons within the Nanodegree will be using a [GitHub repository](https://github.com/udacity/AIPND-revision) to store program files and other resources for this Nanodegree. To learn more about GitHub, please see the GitHub Lesson that's located within the Extracurricular (optional) section of this Nanodegree.
- The Project Workspace is set up with the programs and files (like pet_images folder) you will need to complete the project.
- The Python comments that begin with `# TODO:` in the **check_images.py** program indicates where you will need to change the code of the program. The comments in **check_images.py** will help you make the changes needed.
- Function docstrings contain input parameters and return values, which were left to provide guidance. You are welcome to program these functions differently.
- In 6. Timing Code to 19. Printing Results we will provide additional guidance for programming the undefined functions and completing the **check_images.py** program. This information has been provided to help you through the process.

  The information provides:

  - Which Lessons to review regarding programming the undefined functions.
  - Details about the assignment's files (e.g. image files in pet_images folder, dognames.txt).
  - Details regarding using the classifier function in classifier.py.
  - Links to relevant python documentation.
  - Relevant example code.

- You can use the functions within the program [print_functions_for_lab_checks.py](https://github.com/udacity/AIPND-revision/blob/master/intropyproject-classify-pet-images/print_functions_for_lab_checks.py) to check your code for sections 8. Command Line Arguments through 17. Calculating Results. You will find this program within the Project Workspace and within the [GitHub repository](https://github.com/udacity/AIPND-revision).

### Program Outline
 - Time your program
   - Use Time Module to compute program runtime
 - Get program Inputs from the user
   - Use command line arguments to get user inputs
 - Create Pet Images Labels
   - Use the pet images filenames to create labels
   - Store the pet image labels in a data structure (e.g. dictionary)
 - Create Classifier Labels and Compare Labels
   - Use the Classifier function to classify the images and create the classifier labels
   - Compare Classifier Labels to Pet Image Labels
   - Store Pet Labels, Classifier Labels, and their comparison in a complex data structure (e.g. dictionary of lists)
 - Classifying Labels as "Dogs" or "Not Dogs"
   - Classify all Labels as "Dogs" or "Not Dogs" using dognames.txt file
   - Store new classifications in the complex data structure (e.g. dictionary of lists)
 - Calculate the Results
   - Use Labels and their classifications to determine how well the algorithm worked on classifying images
 - Print the Results

 You will need to repeat these tasks for each of the three image classification algorithms that are provided to you.

 - [Frequently Asked Questions for Classifying Images Project](https://github.com/udacity/AIPND-revision/blob/master/notes/project_intro-to-python.md)
 - [Lab Worksace How-To](https://www.youtube.com/watch?v=EQTttywUnXQ&feature=emb_logo)