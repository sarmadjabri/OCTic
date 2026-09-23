# OCTic
## What is the benefit? Why does this topic interest you
The benefit of this project is that it will allow us to determine how speckle noise and image denoising affects the ability of Resnet18  and ViT models to classify retinal diseases from OCT images that will be important for disease classification. By comparing both network architectures, we can determine whether denoising improves performance and whether one architecture is less susceptible to image degradation. This project could help identify more effective combinations of image preprocessing and the corresponding neural net architecture for retinal disease identification.

## What question are you trying to answer by completing this project?  Why is this project scientifically relevant 
We care about this project because noisy OCT scans are a major issue, OCT scans have a lot of speckle noise due to patients moving and also the coherent light that scans tissues scatters light around causing a grainy pattern. Using a CNN architecture like ResNet-18 and a self-attention model like a ViT in pair with denoising can help us decide which combination is the best to use to automatically diagnose retinal diseases and this helps doctors because noise can make it very hard to diagnose certain diseases and our combination of denoising and the right network architecture can really help.


## What will you be changing in this project?
Our IV is the image denoising process which is measured in Contrast to Noise Ratio (CNR), which measures how clearly a retinal abnormality stands out from the surrounding tissue compared to the background noise and our denoising process aims to increase the decibels (unit for CNR). Higher decibels means lower noise level meaning less interference.

## What different levels of the IV will you be testing?  
Our different level of IV would be no denoising + ResNet-18, no denoising + ViT, denoising + ResNet-18 , denoising + ViT. This can accurately tell us if denoising and using a network architecture is useful in diagnosing retinal diseases.

## How could you measure or describe the response of the subject to the change? What type of quantitative data will you be collecting?
We will be analyzing the Macro-F1 score which measures overall model accuracy and is calculated with the precision and recall for each disease class and averages them ensuring diseases that are not classified accurately most of the time are not ignored.

## What tools will you be using to make these measurements?
Major Python packages, torch, opencv-python, scikit-learn, matplotlib.

## What materials are readily available for conducting the experiment? 
There are many open source databases that have OCT Scans categorized into normal and different retinal diseases available for training data. 
These are some datasets available
https://borealisdata.ca/dataverse/OCTID 
https://data.mendeley.com/datasets/sncdhf53xc/1 



## Datasets
https://www.kaggle.com/datasets/kawtarnaim/octid-dataset?select=OCTID
https://www.kaggle.com/datasets/orvile/octdl-optical-coherence-tomography-dataset/data

Another study:
https://pmc.ncbi.nlm.nih.gov/articles/PMC6829984/


## Speckle Noise
Studying speckle noise levels: 
Measuring and Quantifying Levels
Equivalent Number of Looks (ENL): Higher ENL values indicate lower speckle noise levels. Uniform areas in an image help calculate ENL by dividing the square of the mean intensity by the variance (ENL = μ² / σ²).
Amplitude Statistics: Speckle intensity often follows a negative exponential distribution, while its amplitude follows a Rayleigh or Gamma distribution.
Application-Specific Levels: Laser vibrometry measures dynamic speckle levels as a small percentage of target velocity (e.g., roughly 0.1% for in-plane motions). [1, 2]


## Miscellaneous
Possible Sources
Bi Z, Li J, Liu Q and Fang Z (2025) Deep learning-based optical coherence tomography and retinal images for detection of diabetic retinopathy: a systematic and meta analysis. Front. Endocrinol. 16:1485311. doi: 10.3389/fendo.2025.1485311 

