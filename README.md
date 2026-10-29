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

Verify that every OCT scan has a valid disease label and can be opened correctly. REmove the corrupted files and duplicates. Record the number of images in each disease category. Use the same disease categories for both neural networks (ViT and Resnet18) throughout the experiment.
Separate the images into training, validation, and testing groups. Use 70% of the data for training (clean images), 15% for validation, and 15% for testing in the Kaggle 2026 October OCT Scan dataset.
 
Prepare all scans prior to training and testing. Resize the OCT scans to 224 by 224 pixels and normalize pixel intensities. Apply this image preparation to both neural nets, do not add speckle noise to the training data.

Configure the two neural network architectures. Use python 3, pytorch, and torchvision to initialize the two models. Resnet18 contains 18 learned layers and uses convolutional operations to extract the image features. ViT-B/16 divides each 224x224 pixel scan into 196 patches measuring 16x16 pixels and processes the patches using transformer self attention. Replace each model's final classification layer with a new output layer containing our output for each retinal disease category. For example a dataset containing four categories will require four output neurons, use the same class to number mapping for both models.

Establish the training configuration. Use a batch size of 32 images, a maximum of 50 training epochs, and the AdamW optimizer for both models. Set the initial learning rate to 0.0001 for Resnet18 and for ViT-B/16 set its learning rate to 0.00001. Both models should have a weight decay of 0.01. Use cross entropy loss to measure the difference between predicted disease probabilities and truth disease labels. Apply a cosine learning rate schedule that gradually reduces the learning rate during training. Use random seed 42 for model instantiation and data loading. If a batch size of 32 is too much, use gradient accumulation to maintain an effective batch size of 32 and record the microbatch size. Don’t change these settings after examining test set results.

Use only the OCT2026 kaggle dataset for the retinal OCT images organized into training, validation, and testing groups (this is done already). Retain that datasets four classification categories including choroidal neovascularization (CNV), diabetic macular edema (DME), drusen, and normal retinal scans. Don’t combine these datasets with other pretrained datasets. Use the same image preprocessing method from step 4 , convert images to grayscale if necessary and scale pixel intensities to values between 0 and 1. Duplicate the grayscale channel three times to create 3 channel input then apply the normalization associated with the model weights after these transformations. Don’t add synthetic speckle noise to either the training nor validation scans in this step.

Tune the Resnet18 with the weights=None setting. This will ensure that every trainable parameter begins with randomly initialized values rather than weights learned from another dataset. Resnet18 will learn all of its retinal image classification features exclusively from the OCT2026 training dataset. Adjust the final connected classification layer to contain four output neurons corresponding to the OCT2026 categories of CNV, DME, DRUSEN, and normal retinal scans. The mapping used will be CNV=0, DME=1, DRUSEN=2, and NORMAL = 3. The optimizer should use AdamW, the initial learning rate of 0.0003, weight decay at 0.01, loss function must use cross entropy loss, effective batch size must be 32 scans, maximum training duration 100 epochs, early stopping duration set at 15 epochs, learning rate schedule should use 5 epoch warmup followed by cosine decay, random initialization seed at 42, and model input size 224x224 pixels as you had done in step 4.

Configure the ViT B/16, initialize the network with the weights=None setting as you have done with the Resnet18, this ensures that no pretrained model weights from external datasets are used (reiterating from before). The ViT should process presized 224x224 pixel sized images by dividing 196 non overlapping patches measuring 16x16 pixels. The patches are converted into numbers and processed using 12 transformer encoder layers, each containing 12 self attention heads. The model learns relationships between the different regions of the OCT scans to distinguish different retinal diseases. Configure the classification head with 4 output neurons corresponding to the same disease categories used for REsnet18 CNV=0, DME = 1, DRUSEN = 2, and Normal = 3. Use the AdamW optimizer with an initial learning rate of 0.00001, weight decay of 0.01, cross entropy loss, effective batch size of 32 scans, and a max training duration of 50 epochs. Apply a cosine learning rate scheduler with linear 5 epoch warmup period. Set the early stopping patience to 15 epochs and use random seed 42 for initialization and training data mixing. Record all settings so that the experiment can be done again.

Load the OCT2026 training data and retain its original 4 disease categories, don't include images from the validation partition or the testing partition. Initialize Resnet18 with random seed 42 and the configuration established in step 6. At the beginning of each epoch, randomly shuffle the OCT2026 training images and divide them into batches with an effective size of 32. For each batch, do a forward pass through Resnet18 to generate 4 disease classification “scores”. Calculate cross entropy loss by comparing these scores with the corresponding correct disease labels. Use backpropagation to calculate the gradients and update the network parameters using AdamW (the optimizer from earlier).

Train VIT: Load the OCT2026 training and validation partitions used for Resnet18, use the same four disease labels and the same preprocessing method for consistency including your grayscale conversion, resizing, three channel conversion, and fixed normalization of the scans. Initialize ViT using randomly generated weights and random seed 42, don't load pretrained imagenet weights from other datasets, all data must come from the OCT2026 Kaggle dataset. Randomly shuffle the OCT2026 training images at the beginning of each epoch and arrange them into batches of 32 images. For each batch, pass the images through the ViT, the model should divide each image into patches, process them through the transformer encoder (consisting of the encoder blocks from earlier), and generate four classification scores. Calculate cross entropy loss by using the actual disease labels, use backpropagation and update the parameters from step 9 again utilizing the AdamW optimizer. Make checkpoints whenever validation MacroF1 scores improve, continue training for a max of 50 epochs or after 15 consecutive epochs without improvement in MacroF1 scores. Retain the checkpoint after getting the highest MacroF1 score. Record all parameters used and don’t add speckle noise until after both models have been trained.

After training, load the Resnet18 and ViT checkpoints selected using their highest validated MacroF1 scores. Evaluate both models using the clean validation images, confirm that each model produces four output scores, one for each disease category, then convert the scores into probabilities using the softmax function and verify the probabilities sum to about 1 for every image. Study the loss curves to determine whether either model is underfitting or overfitting. Look at the disease classification f1 scores and confusion matrices to identify whether either architecture consistently predicts only one disease category or fails to distinguish multiple categories.

Establish the control from OCT2026: Load the original images from the OCT2026 testing folder, evaluate every image using the finalized Resnet18 model without adding artificial speckle noise. Repeat this process for the ViT model. This represents the control condition with a speckle noise standard deviation of 0.00. For each OCT scan, record its UII (unique image identifier), actual disease category, predicted disease category, and predicted probabilities for CNV, DME, DRUSEN, Diabetic Retinopathy (Dr), Macular hole, and NORMAL. Calculate the models classification accuracy, Macro f1, and multiclass Macro AUROC using python and scikit learn. 

Implement the multiplicative speckle noise generation algorithm: create a python function using numpy to introduce synthetic multiplicative speckle noise into OCT2026 test images. First, load each original grayscale OCT test image and resize it to 224x224 pixels. Convert its pixel values into doubles between 0 and 1. Generate an array of random values with the same height and width as the image. Each value will be sampled from a normal distribution with a mean of 0 and a standard deviation equal to the selected noise level.use numPYs clipping to restrict all pixel intensities from 0 to 1. Apply noise to the grayscale image before creating the three identical input channels. Then apply the same normalization transformation used during training. The generated noisy images must be identical for Resnet18 and ViT within each experimental condition.
 Establish the four experimental speckle noise levels with
Control: σ = 0.00
Experimental Level 1: σ = 0.10
Experimental Level 2: σ = 0.20
Experimental Level 3: σ = 0.30
Experimental Level 4: σ = 0.40

Each nonzero noise level should generate a corrupted image in the testing folder. Always generate the corrupted images rather than applying new noise to images that were already “speckled”. Ensure the following are the same, image counts, class labels, dimensions, and test set labels across all 5 IV’s.
Generate five noise trials at each experimental level. Conduct five trials for every nonzero speckle noise level using random seeds like 101, 102, 103, 104, and 105. Each trial will generate one complete noisy version of the OCT2026 testing folder. Every image will be given its own noise array. Generate the random arrays in a fixed order based on the sorted image identifiers so that the same trial can be created once more. Use the same seed at every noise level. Because the noise arrays are scaled based on standard deviation which allows for real comparisons between the different noise severities using corresponding patterns. Generate the corrupted images from the saved noise parameters and seeds and verify that both architectures are evaluated on teh same pixel values for each image, noise level, and trial. The experimental design will thus produce 20 noisy evaluation conditions: four noise levels multiplied by the 5 trials we do.

Evaluate Resnet18 on all noisy OCT2026 testing images. Load the finalized Resnet18 checkpoint and keep the model evaluating, begin with standard dev of 0.10 and a random seed 101. Pass teh entire corresponding noisy testing folder through Resnet18 in batch sizes indicated before. For each image, obtain the four raw output scores and convert them to class probabilities using the softmax function. Identify the predicted disease category as the category with the highest probability. Record the image identifier, actual disease, predicted disease, four class probabilities, noise standard deviation, and trial seed. Repeat the evaluation for seeds 102, 103, 104, and 105. Do the same five trial procedures at standard deviation 0.20, 0.30, and 0.40. Don’t change model weights, disease label mapping, or input preprocessing at all. Export all predictions to a CSV file with one row per image evaluation.
Evaluate ViT on the identical noisy testing images: Load the finalized ViT checkpoint and keep the model in test mode. Evaluate ViT on the exact same noisy OCT2026 testing images generated for ResNet18 preserving the same noise arrays, image identifiers, real labels, noise trials, and trial seeds. Record the same information collected for Resnet18 in step 16. Repeat the evaluation for all five trials at all levels of standard deviation. Export the results to a separate CSV file and check that each recorded ViT prediction has a matching Resnet18 prediction with the same image identifier, noise level, and trial seed. The pairing allows differences between the models to be studied without going too far into depth.
Calculate Accuracy, Disease specific F1, Macro F1, and Macro AUROC.  Using python and scikit learn, compare the predicted disease categories with the original OCT2026 truth labels. Calculate the accuracy using Accuracy% = (# of correct predictions / total # of images) *100. For each disease category, calculate the true positives, false positives, and false negatives. The precision can be found using Precision = TP / (TP+FP). Get the recall from Recall = TP / (TP + FN) Calculate the disease specific F1 score using F1 = 2 * (Precision * Recall) / (Precision + Recall). Get the dependent variable from averaging the F1 scores for the four OCT2026 categories with MacroF1 = (F1CV + F1DME + F1Drusen + F1Normal) / 4. Get the Macro AUROC using the one v rest method, for each disease category, use the model's predicted probabilities to evaluate its ability to distinguish a disease from the remaining three categories, average the four disease AUROC values equally.  Calculate these metrics separately for each model, noise level, and trial. MacroF1 and AUROC are calculated across tons of images, not for one individual image.

Calculate average performance, standard deviation, and performance degradation. For each network and experimental noise level, find the arithmetic mean of the five MacroF1 scores. Calculate the standard deviation of the five trial measurements to quantify the performance variation caused by different random speckle noise patterns. Repeat the math for classification accuracy and Macro AUROC. For each network, subtract the mean MacroF1 and each experimental noise level from its corresponding clean control MacroF1. A positive result indicates the model's classification performance decreased from its control. Determine the difference between Resnet18 and ViT macroF1 scores on each trial. Compare their losses to their controls. 

Analyze disease specific classification errors/losses. Generate confusion matrices for Resnet18 and ViT using OCT2026 test images at every noise level. For the noisy conditions, calculate the matrices for each individual trial and summarize said results across all five trials. Find the frequency of misclassification between CNV, DME< DRUSEN, and NORMAL and determine whether certain disease categories experience larger decreases in recall or F1 as speckle noise increases. Find the paired difference in Macro F1 between Resnet18 and ViT in every noise trial. 

Create the graphs. Create a line graph displaying speckle noise standard deviation on the horizontal x axis and average Macro F1 on the y axis. Create more graphs comparing classification accuracy, Macro AUROC, and MacroF1 loss across noise levels. Make tables with the disease specific F1 scores, confusion matrices, individual trial values, averages, standard deviations, and differences between the two networks. Please keep in mind both neural networks have been trained from scratch on the 2026OCT dataset.



## 4) DATA COLLECTION: Detailed description of how the data will be collected.  You should include how your DV is going to be measured, what equipment you will be using, and what units you will be using.  Also include how you will present the data.  You need to include a draft of your data tables used to record data, including titles, units at top of rows/columns, and what type of qualitative observations will be recorded.

We will have a separate group of OCT scans that weren’t used to train either architecture that will be used for testing them. Both Resnet18 and ViT will be tested on original clear images (control). Then we will add speckle noise to each of those same images at 4 different levels (Levels of IV). At each noise level, both models will attempt to identify the retinal disease shown in those images. Then we repeat this 5 times at each noise level with different random patterns of speckle noise. For each image, the actual disease in the image, the disease predicted by its respective model, and the accuracy of the prediction will be recorded. Then we calculate the DV (percent accuracy of each model) and find how their performance changes with increasing amounts of speckle noise.

## 5) DATA ANALYSIS:  Detailed description of how the raw data will be analyzed.  What calculations or formulas will you use?  What types of graphs will you use, and why?  How will you evaluate the validity of your data?  

The classification results from Resnet18 and ViT will be compared at each level of IV (speckle noise stdvs). The five trials at each noise level will be averaged to determine the performance of each model and how consistently each model does as noise increases. The results will be compared with each model's performance on the control. 

## What types of graphs will you use and why?
We will use a line graph with the amount of speckle noise on the x axis and average classification accuracy on the y axis. Resnet18 and ViT will differ in the color of the lines. 

## How will you evaluate the validity of your data? Statistical analysis
The five trials at each noise level will be used to find the mean and standard deviation of each model's classification accuracy. Standard deviation will show the consistency of the results. Statistical testing will be used to determine if the performance differences in the models are real or caused by inconsistencies.


