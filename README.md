
# Local Dataset Preprocessing for Medical Image Segmentation

This repository provides code for extracting medical images from DICOM (`.dcm`) files to deal with segmentation tasks.

## **Dataset Structure**
The local dataset follows the structure below:
local_data/ │── anon_SMet1/ │ ├── SMET1/ │ ├── SMET2/ │ ├── ... │── anon_SMet2/ │ ├── SMET141/ │ ├── SMET142/ │ ├── ...


## **Installation**
First, create a virtual environment using Conda:

conda create -n medimg_env python=3.9 -y
conda activate medimg_env

Then, install the required dependencies:
pip install -r requirements.txt

Usage
To extract images, run:


python extraction.py
The detailed instructions are provided in the code comments.