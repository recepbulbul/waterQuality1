import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

purple ='#2d023d'
tan = '#ffd4aa'

dataset = pd.read_csv("waterQuality1.csv")

print(dataset.head(5))
info = list(dataset.info())
describe = (dataset.describe())

print(dataset['is_safe'].value_counts())

print(dataset.isnull().sum())

cleaned_dataset = dataset[dataset["is_safe"] != "#NUM!"]

plotter_dataset = cleaned_dataset.drop('is_safe', axis=1)
plt.figure(figsize = (20, 20))

# Iterate through the feature list and plot a histlpot
for i in enumerate(list(cleaned_dataset.columns[:-1])):
    plt.subplot(5, 4,i[0]+1)

    # Histlot plotting the fetures in the dataset
    sns.histplot(
        data = plotter_dataset, 
        x = plotter_dataset[i[1]], 
        hue = cleaned_dataset['is_safe'], 
        palette= [tan, purple], 
        kde = True, 
        alpha=1
    )

correlation_matrix  = cleaned_dataset.corr()
plt.figure(figsize=(15, 12))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", linewidths=.10)
plt.title('Özellikler Arasındaki Korelasyon Heatmap')
plt.show()

sns.jointplot(data=cleaned_dataset, x='viruses', y='bacteria', hue='is_safe',palette=[tan,purple])
plt.show()

sns.jointplot(data=cleaned_dataset, x='perchlorate', y='chloramine',palette=[tan,purple],hue='is_safe')
plt.show()

sns.jointplot(data=cleaned_dataset, x='chromium', y='chloramine',palette=[tan,purple],hue='is_safe')
plt.show()

plt.figure(figsize=(15, 12))
sns.violinplot(x="is_safe", y="chloramine", data=cleaned_dataset,palette=[tan,purple])
plt.show()
plt.figure(figsize=(15, 12))
sns.violinplot(x="is_safe", y="viruses", data=cleaned_dataset,palette=[tan,purple])
plt.show()

plt.figure(figsize=(15, 12))
sns.lineplot(x="nitrites", y="silver", data=cleaned_dataset,color=purple)
plt.show()


























