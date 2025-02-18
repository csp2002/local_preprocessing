
# Local Dataset Preprocessing for Medical Image Segmentation

This repository provides code for extracting medical images from DICOM (`.dcm`) files to deal with segmentation tasks.

## **Dataset Preparation**
Download the dataset and put it into the folder local_data


## **Installation**
First, create a virtual environment using Conda:

```
conda create -n local python=3.9 -y
conda activate local
```

Then, install the required dependencies:
```
pip install -r requirements.txt
```

## **Usage**
To extract images, run:
```
python extraction.py
```
The detailed instructions are provided in the code comments.

By running extraction.py, you will get the 3D numpy of both the original images and the corresponding GT masks. After that, you can further preprocess the data based on different codebase (like saving the 2D image slice by slice using plt.imsave and segmenting the ROIs using 2D segmentation networks like SAM).