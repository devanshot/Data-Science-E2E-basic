# Data-Science-E23-basic
This project is an Industry project based on Data Science and Machine Learning models to predict the legitimacy of False Alarm Condition in Chemical Industry.


False Alarm Prediction Model for Leakage Detection of H2S Gas
Problem Statement-This project is  developed for a chemical industry which has  sensors installed in various parts of the factory to detect Hydrogen Sulfide(H2S) gas.The consumption of H2S gas above the permissible limit is hazardous to health. Every time one or multiple sensors detects the H2S leak, an emergency alarm rings to alert the workers. For every alarm, the industry calls a sanitation team which sanitizes the place and checks for the leak. This results in the shutdown of the industry and also makes huge loss.
Most of the sensors including modern sensors like Enhanced Laser Diode Spectroscopic sensors (ELDS ) also fails to trigger  the alarm exactly at the calibrated gas leakage value in the service environment. This causes many occurences of False Alarm triggering .A few of the alarms that ring are not even hazardous. The industry thus relies more on the data centric approach to check the legitimacy of the alarm and to take further steps.



The data is first pre-processed and analysed with  libraries like Numpy and Pandas to make it ready to be utilized by a machine learning algorithm/model.
Problems like standard scaling, categorical data and missing values are handled with appropriate techniques.
Here Naïve Bayes mode is used to make a classifier with first six column as independent columns and dangerous column/spuriosity column  as dependent/target column.
Now whenever, there is a leakage and the alarm rings, the data is fed to the model and prediction is made by the model if the alarm is benign or not. The industry is shutdown and sanitation team is called only if the model prediction is labelled dangerous.This saves lot of the production money and time.

