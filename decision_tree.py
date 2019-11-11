#Decision Tree Classifier
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('Social_Network_Ads.csv')
X = dataset.iloc[:,[2,3]]
y = dataset.iloc[:,4]
