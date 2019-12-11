# Classify Pet Images

First project in Udacity's Artificial Intelligence Programming with Python Nanodegree program. Participants are supposed to submit an image of their dog. Used Convoltional Nural Network (CNN) to classify whether the image is or is not a dog. Determined which pre-trained CNN architecture model works best at classifying images of dogs and their breeds. Compared results of ResNet, AlexNet, and VGG model architectures.

## Table Of Contents

### Getting Started 

1. Clone the repository
```console
git clone https://github.com/atkatchev/ 
cd intropyproject-classify-pet-images 
./run_models_batch.sh
```

### Project Structure
- [File Descriptions](notes/project_intro-to-python.md)
- [Documenation and Project Report](documentation_and_report/documentation_and_report.md)

### Dependencies

Each directory has a `requirements.txt` describing the minimal dependencies required to run the notebooks in that directory.

### pip

To install these dependencies with pip, you can issue `pip3 install -r requirements.txt`.

### Conda Instructions
---------------------

```console
# Create a conda environment if you want or use one you already have
conda create --name intropyproject-classify-pet-images python=3
source activate intropyproject-classify-pet-images
conda install --file requirements.txt
./run_models_batch.sh
```

