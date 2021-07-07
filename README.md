<p align="center">
<img src="https://github.com/AM1CODES/HackOff---Brain-Tumor-Detection-Web-app/blob/main/Some%20Results/logo2%20(1).png" alt="drawing" width="200"/>
</p>


# Brain-Tumor-Detection-Web-app
In the recent times, the requirement for better and advanced healthcare facilities has grown to a very large extent. With this Pandemic, we not only need better healthcare facilities to handle Covid-19 but we also need advanced methods to make other healthcare facilities and diagnostics faster. With Machine learning and Artificial Intelligence taking over almost everything, we decided to tackle one such issue related to the health sector using Deep learning Techniques. 

This is our Solution for **Data Science and AI track** in **HackOff v3.0**. A web app that helps in diagnosing whether a person has Brain Tumor or not by taking the MRI scan as the input from the user.

# Tools Used
<img src="https://img.shields.io/badge/Jupyter%20-%23F37626.svg?&style=for-the-badge&logo=Jupyter&logoColor=white" /> <img src="https://img.shields.io/badge/python%20-%2314354C.svg?&style=for-the-badge&logo=python&logoColor=white"/> <img src="https://img.shields.io/badge/Keras%20-%23D00000.svg?&style=for-the-badge&logo=Keras&logoColor=white"/> <img src="https://img.shields.io/badge/TensorFlow%20-%23FF6F00.svg?&style=for-the-badge&logo=TensorFlow&logoColor=white" /> <img src="https://img.shields.io/badge/pandas%20-%23150458.svg?&style=for-the-badge&logo=pandas&logoColor=white" /> <img src="https://img.shields.io/badge/numpy%20-%23013243.svg?&style=for-the-badge&logo=numpy&logoColor=white" /> <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white" />

# About the Dataset
The data set was taken from Kaggle which contains two folders, one is for training and the other is for testing. It has 3 types of Brain Tumor - Glioma, Meningioma and pituitary along with images of patients with no tumor. <br>

<img src="https://github.com/AM1CODES/HackOff---Brain-Tumor-Detection-Web-app/blob/main/Some%20Results/Tumor.png" alt="drawing"/>

Link to the Dataset - https://www.kaggle.com/sartajbhuvaji/brain-tumor-classification-mri


# Goal and Idea
The idea was to create a full stack application that would run on web and even on cellphones and can help people in diagnosing brain tumor using MRI scans. The classifier not only classifies between Tumor and No tumor but will also return the class of the Tumor if it is present. There were three categories of Tumor in our data - Pitutary, Glioma and Meningioma and depending upon the user input the model would give the user a result. The models are usually made but are rarely deployed so one of our goals for this hackathon was to learn how to deploy these models on the web and we were successful in doing so.

# Working of the web app
Upon landing on the page, the user is asked to input the image of the MRI scan. This image is then preprocessed to make it similar to the input on which the the model was initially trained. Once the processing is done, the image is fed to the model which then gives the user a result. The model that makes the predictions is a Convolutional Neural Network which consists of 5 Convolutional layers and 5 Maxpooling layers and it was trained on a batch size of 40 and for total of 50 epochs.<br>

<img src="https://github.com/AM1CODES/HackOff---Brain-Tumor-Detection-Web-app/blob/main/Some%20Results/working.png" alt="drawing"/>

# Performance and Results
Upon testing it on the web, the model was able to give some decent results. We tried inputing various images of different types of tumors to test it. For some of the inputs, it was able to give the right result but there were instances where it failed to classify the right type of tumor. But it did classify those images correctly which had Tumor even though it wasn't accurate in telling which type of tumor it was. The model gave an accuracy of 97.5% on the training set and an accuracy of 94% on the validation set.

<img src="https://github.com/AM1CODES/HackOff---Brain-Tumor-Detection-Web-app/blob/main/Some%20Results/Result-1.PNG" alt="drawing"/> <img src="https://github.com/AM1CODES/HackOff---Brain-Tumor-Detection-Web-app/blob/main/Some%20Results/Result-2.PNG" alt="drawing"/>




