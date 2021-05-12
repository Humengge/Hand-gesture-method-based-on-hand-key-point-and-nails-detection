# Hand-gesture-method-based-on-hand-key-point-and-nails-detection

## Introduction
======================
Themaintaskofthisprojectistodealwithseveraltypesofdifficultsamplesduringfingertipsegmentation for touchless fingerprint recognition, such as distinguishing between innerfingers and nail caps, the degree of tightness between fingers, etc. The project simulatesthe architecture of a cascade system and designs a series of filters to filter the error sam­ples. Due to some of the limitations of publicly available databases, the database for thisproject is made up of individually collected data and publicly available data together andmerged into a new database. By constructing multiple neural networks as a frameworkfor the filters, the categories of hands in photographs are trained, classified and output.


**The database of nail detection and hand gesture should be made by yourself.**

**Before you run the project, you need to change the path value and build up several folders according the codes.**

### Nail Detection
----------------------
- If you want to make the nail detection by **yourself**. then you need to collect the hand images with nails as nail database, saving in the 'JPEGImages' folder. Then use the [labelImg](https://github.com/tzutalin/labelImg) which has already download in this project and run the commends below in Anaconda:

        conda install xml
        make qt5py3
        python labelImg.py

Then you can mark your own nail database and save the marked xml file into 'Annotations' folder. 'ImageSets' foldee saves the file names of test set, training set and validation set. Then use the SSD model to train the dataset. 

        python SSD-Tensorflow-master/train_ssd_network.py

- If you don't want to train by yourself, then you can just use the model 'model.ckpt-7246' which has already trained in 'nail_model' folder. Run the file 'ssd_nodebook.ipynb' to show the number of nails.


### Hand Keypoint Detection
----------------------
[BaiduAIapi](https://ai.baidu.com/tech/body/hand) has been used to detect hand 21 keypoints. You need to creat the Baidu AI studio accound and obtain the AK/SK code to connect the interface. Run the 'api_tes.py' to get the response from API and then run the 'api_use.py' to detect hand keypoints. The keypoints information will be saves in txt file via JSON structure.


### Classify the hand gesture for the touchless fingerprint datection
----------------------
The final dataset, connecting the number of nails, 21 kye points and label, is 'finalData.csv' which is made by 'finalInput.py'. Run the file 'training.ipynb' to train the data via four different models with cross validation. The final choosen model is the MLPC with 20 fold dross validation, named 'model_MLPC2_20Fold.m', which can be used directly to classify the hand position.

