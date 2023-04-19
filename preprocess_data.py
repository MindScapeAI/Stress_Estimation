import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

import time
from datetime import datetime
import re
import openpyxl
import xlwt

from scipy.stats import kendalltau
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from imblearn.over_sampling import SMOTE
from collections import Counter

import warnings
warnings.filterwarnings('ignore')


# Data files and path
sleep_survey = '../Data/user_survey_2020.csv'
sleep_data = '../Data/user_sleep_2020.csv'

# Read data
survey_df = pd.read_csv(sleep_survey)
sleep_data_df = pd.read_csv(sleep_data)

#check columns
# print("Survey features: \n" + str(survey_df.columns))
# print("\nSleep data features: \n" + str(sleep_data_df.columns))

for i in range(len(sleep_data_df)):
    epoch_start = sleep_data_df['startDt'][i]
    epoch_end = sleep_data_df['endDt'][i]
    sleep_data_df['startDt'][i]=datetime.utcfromtimestamp(epoch_start).date()
    sleep_data_df['endDt'][i]=datetime.utcfromtimestamp(epoch_end).date()

# leave date only in survey data
for i in range(len(survey_df)):
    survey_df['startInput'][i]=datetime.strptime(survey_df['startInput'][i],"%Y-%m-%d %H:%M").date()
    survey_df['endInput'][i]=datetime.strptime(survey_df['endInput'][i],"%Y-%m-%d %H:%M").date()
    

# Make survey data into one row for each user

for i in range(len(survey_df)-1):
    survey_df['pmEmotion'][i] = survey_df['pmEmotion'][i+1]
    survey_df['pmStress'][i] = survey_df['pmStress'][i+1]
    survey_df['pmFatigue'][i] = survey_df['pmFatigue'][i+1]

# Remove data that won't be used
survey_df = survey_df.drop(survey_df[survey_df['amPm']=='pm'].index)
survey_df = survey_df.drop(['date','amPm','endInput','dream','caffeine', 'cAmount(ml)', 'alcohol','aAmount(ml)'],axis='columns')

sleep_data_df = sleep_data_df.drop(['userId','date','startDt','endDt','timezone','lastUpdate','wakeupduration', 'lightsleepduration', 'deepsleepduration',
       'wakeupcount', 'durationtosleep', 'remsleepduration',
       'durationtowakeup', 'hr_average', 'hr_min', 'hr_max', 'rr_average',
       'rr_min', 'rr_max', 'breathing_disturbances_intensity', 'snoring',
       'snoringepisodecount'],axis='columns')

# Reset index
survey_df = survey_df.reset_index(drop=True)
survey_df = survey_df.reset_index(drop=True)

# Merge every feature
new_df = pd.concat([survey_df,sleep_data_df],axis=1)

for i in range(len(new_df.columns)-2):
  new_df[new_df.columns[i+2]] = new_df[new_df.columns[i+2]].astype('int')

features = new_df.columns.to_list()
features = features[2:]
features.remove('pmStress')

# Convert labels  
new_df = new_df.replace({'pmStress':3},2)
new_df = new_df.replace({'pmStress':4},2)
new_df = new_df.replace({'pmStress':5},3)

## Correlation Analysis (kendall 상관계수) ##
correlated_features = [] 
coef_of_correlated = []

alpha = 0.05


# print the correlation between stress and other features
for i in range(len(features)):
    coef, p = kendalltau(new_df[features[i]].to_list(), new_df['pmStress'].to_list())
    print("%d. Average coeff between %s and stress =  %.3f" % (i+1, str(features[i]), coef))
    if p>alpha:
        print("uncorrelated\n")
    else:
        print("correlated\n")
        correlated_features.append(features[i])
        coef = round(coef,4)
        coef_of_correlated.append(coef)

print(correlated_features)
print(coef_of_correlated)

filtered_df = new_df[correlated_features]

# summarize distribution of original dataset
# counter = Counter(new_df.pmStress)
# for k,v in counter.items():
#  per = v / len(new_df.pmStress) * 100
#  print('Stress level=%d, n=%d (%.3f%%)' % (k, v, per))
# plot the distribution
# plt.bar(counter.keys(), counter.values())
# plt.show()

# 데이터 클래스 불균형 문제 해결 - SMOTE 기법
scaler=MinMaxScaler()
smote = SMOTE(random_state=0)
oversampled_X, oversampled_y = smote.fit_resample(filtered_df, new_df["pmStress"])
oversampled_X=scaler.fit_transform(oversampled_X)

# summarize distribution of oversampled dataset
# counter = Counter(oversampled_y)
# for k,v in counter.items():
#  per = v / len(oversampled_y) * 100
#  print('Stress level=%d, n=%d (%.3f%%)' % (k, v, per))
 
# plot the distribution
# plt.bar(counter.keys(), counter.values())
# plt.show()
