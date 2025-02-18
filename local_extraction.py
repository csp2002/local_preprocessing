import os
import pydicom
import numpy as np
from DicomRTTool.ReaderWriter import DicomReaderWriter, ROIAssociationClass


#read RTSS file
patient_folder = 'local_data/anon_SMet1/SMET1'
rtss_path = os.path.join(patient_folder, 'anon_RTSS.dcm')
ds = pydicom.dcmread(rtss_path)

#extract ROI names and types
struct_names = {item.ROINumber: item.ROIName for item in ds.StructureSetROISequence}
struct_types = {item.ReferencedROINumber: item.RTROIInterpretedType for item in ds.RTROIObservationsSequence}
print(struct_names)    # a dictionary with ROINumber as key and ROIName as value
print(struct_types)   # a dictionary with ReferencedROINumber as key and RTROIInterpretedType as value

Dicom_reader = DicomReaderWriter(description='Examples', arg_max=True)
Dicom_reader.walk_through_folders(patient_folder)   #walk through all dcm files in the patient folder
all_rois = Dicom_reader.return_rois(print_rois=False)

Contour_Names = ['l parietal'] #set ROI name
Dicom_reader.set_contour_names_and_associations(contour_names=Contour_Names)
indexes = Dicom_reader.which_indexes_have_all_rois() 
pt_indx = indexes[-1]

#read corresponding image and mask
Dicom_reader.set_index(pt_indx)
Dicom_reader.get_images_and_mask()
image = Dicom_reader.ArrayDicom
mask = Dicom_reader.mask

#print shape, max, min value of image, mask
print(image.shape)
print(mask.shape)
print(np.max(image))
print(np.min(image))
print(np.max(mask))
print(np.min(mask))