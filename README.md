# OCTic
## What is the benefit? Why does this topic interest you
The benefit of this project is that it will allow us to determine how speckle noise affects the ability of Resnet18  and ViT models to classify retinal diseases from OCT scans that will be important for disease classification. By comparing both architectures, we can determine whether one architecture is less susceptible to image degradation. This project could help identify more effective combinations of image preprocessing and the corresponding neural net architecture for retinal disease identification.

## What question are you trying to answer by completing this project?  Why is this project scientifically relevant 
We care about this project because noisy OCT scans are a major issue, OCT scans have a lot of speckle noise due to patients moving and also the coherent light that scans tissues scatters light around causing a grainy pattern. Using a CNN architecture like ResNet-18 and a self-attention model like a ViT in pair with denoising can help us decide which combination is the best to use to automatically diagnose retinal diseases and this helps doctors because noise can make it very hard to diagnose certain diseases and our choice of neural network can really make a difference.


## What will you be changing in this project?
Our IV is the amount of speckle noise added to the OCT scans with the multiplicative noise model which is measured in Contrast to Noise Ratio (CNR). This measures how clearly a retinal abnormality stands out from the surrounding tissue compared to the background.

## What different levels of the IV will you be testing?  
The independent variable is the level of speckle noise applied to each OCT testing image. Speckle noise will be generated using the multiplicative noise model. The noise standard deviation should control the severity as we will have 4 different levels of IV including σ = 0.10, 0.20, 0.30, and 0.40. The control will have a standard deviation of 0.00. The same noised OCT images will be provided to both the Resnet and ViT models at each noise level to evaluate performance.

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

# EDD
 
## What one question are you trying to answer with your experiment? This will require you to write a paragraph of what your experimental problem is and why you are testing this topic. Who will benefit from your research (social significance)? Ask yourself WHO CARES? Who would want to know your results? Really think through the problem—this is essentially your mission statement regarding your topic. This should not be longer than one paragraph.

Retinal OCT scans are used to show structures within the retina, but OCT scans often contain speckle noise that reduces the image quality and interferes with automated disease classification systems. The experiment we conduct will hopefully yield results from how increasing levels of speckle noise affects the ability of two different neural network architectures like Resnet18 and Vanilla Vision Transformers to classify retinal diseases. Both models will be trained using clean OCT scans with no noise and will be evaluated on their ability to decipher noisy retinal scans with different controlled levels of speckle noise. The main comparison is between how convolutional neural networks differ from self attention based models when exposed to varying levels of noise. The research may be useful for future developments regarding computer vision.

## Title of the Experiment: Aim for 50 characters with spaces.  “The Effect of” is  13 characters.  Capitalize main words in the title.
The Effect of Speckle Noise Level on the Classification of Retinal Diseases on the Performance of ResNet-18 and Vision Transformer Models in Retinal OCT Scans 

## Hypothesis: A specific prediction about what you will be testing.  (Ex. If I test this (IV) then this (DV) will change how? because of?).  Your hypothesis should predict a specific level of IV.

If the level of speckle noise applied to retinal OCT scans increases, then the disease classification accuracy of both Resnet18 and ViT (Vision Transformer) will decrease because increasing speckle noise will obfuscate distinct image features used by each model to identify specific retinal diseases.

## Independent Variable:  The IV is the parameter you will change to see what will occur.  What are the different levels of your IV? You need to have different quantities tested (i.e. 0 grams, 10 g, 20 g, 30 g) - USE METRIC units for mass, volume and length measurements. 

The independent variable is the level of speckle noise applied to each OCT testing image. Speckle noise will be generated using the multiplicative noise model. The noise standard deviation should control the severity. We will have 4 different levels of IV including σ = 0.10, 0.20, 0.30, and 0.40. The control will have a standard deviation of 0.00. The same noised OCT images will be provided to both the Resnet and ViT models at each noise level. Another Independent Variable we will use is the type of NN architecture used.


<img width="842" height="591" alt="image" src="https://github.com/user-attachments/assets/89006e41-1895-453b-8757-5c80f5d80373" />


##  Procedures: Describe in detail all procedures you will use in a numbered step by step list. If part of your experiment is building, then include a procedure here as well.  Include safety procedures and disposal of waste materials.  Cite any references used. 

Find public databases with retinal OCT images pre labeled with retinal diseases
Train Resnet18 and ViT on the clean denoised scans
Test each model on the control (σ = 0.00) to establish control accuracy
Generate 5 noisy test images with multiplicative speckle noise at each of the 4 IV levels
Provide the corrupted images to both models in each of the 5 trials
Record the true disease present in the scans and the predicted disease along with its corresponding model and trial number. Then verify whether or not its prediction was correct
Determine each models accuracy, F1 score, and AUROC at each of the 4 noise levels (IV’s)


## 4) DATA COLLECTION: Detailed description of how the data will be collected.  You should include how your DV is going to be measured, what equipment you will be using, and what units you will be using.  Also include how you will present the data.  You need to include a draft of your data tables used to record data, including titles, units at top of rows/columns, and what type of qualitative observations will be recorded.

We will have a separate group of OCT scans that weren’t used to train either architecture that will be used for testing them. Both Resnet18 and ViT will be tested on original clear images (control). Then we will add speckle noise to each of those same images at 4 different levels (Levels of IV). At each noise level, both models will attempt to identify the retinal disease shown in those images. Then we repeat this 5 times at each noise level with different random patterns of speckle noise. For each image, the actual disease in the image, the disease predicted by its respective model, and the accuracy of the prediction will be recorded. Then we calculate the DV (percent accuracy of each model) and find how their performance changes with increasing amounts of speckle noise.

## 5) DATA ANALYSIS:  Detailed description of how the raw data will be analyzed.  What calculations or formulas will you use?  What types of graphs will you use, and why?  How will you evaluate the validity of your data?  

The classification results from Resnet18 and ViT will be compared at each level of IV (speckle noise stdvs). The five trials at each noise level will be averaged to determine the performance of each model and how consistently each model does as noise increases. The results will be compared with each model's performance on the control. 

## What types of graphs will you use and why?
We will use a line graph with the amount of speckle noise on the x axis and average classification accuracy on the y axis. Resnet18 and ViT will differ in the color of the lines. 

## How will you evaluate the validity of your data? Statistical analysis
The five trials at each noise level will be used to find the mean and standard deviation of each model's classification accuracy. Standard deviation will show the consistency of the results. Statistical testing will be used to determine if the performance differences in the models are real or caused by inconsistencies.


