Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv("iris.csv")
print("Dimensions of the dataset:", data.shape)
Dimensions of the dataset: (150, 5)
print("\nFirst few rows of the dataset:")
print(data.head())
SyntaxError: multiple statements found while compiling a single statement
print("\nFirst few rows of the dataset:")

First few rows of the dataset:
print(data.head())
   sepal.length  sepal.width  petal.length  petal.width variety
0           5.1          3.5           1.4          0.2  Setosa
1           4.9          3.0           1.4          0.2  Setosa
2           4.7          3.2           1.3          0.2  Setosa
3           4.6          3.1           1.5          0.2  Setosa
4           5.0          3.6           1.4          0.2  Setosa
print("\nSummary statistics:")

Summary statistics:
print(data.describe())
       sepal.length  sepal.width  petal.length  petal.width
count    150.000000   150.000000    150.000000   150.000000
mean       5.843333     3.057333      3.758000     1.199333
std        0.828066     0.435866      1.765298     0.762238
min        4.300000     2.000000      1.000000     0.100000
25%        5.100000     2.800000      1.600000     0.300000
50%        5.800000     3.000000      4.350000     1.300000
75%        6.400000     3.300000      5.100000     1.800000
max        7.900000     4.400000      6.900000     2.500000
print("\nData types of each column:")

Data types of each column:
print(data.dtypes)
sepal.length    float64
sepal.width     float64
petal.length    float64
petal.width     float64
variety          object
dtype: object
print("\nMissing values:")

Missing values:
print(data.isnull().sum())
sepal.length    0
sepal.width     0
petal.length    0
petal.width     0
variety         0
dtype: int64
sns.pairplot(data, hue='variety')
<seaborn.axisgrid.PairGrid object at 0x000001F2D19BABC0>
plt.show()
sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
<AxesSubplot:>
plt.title('Correlation Matrix')
Text(0.5, 1.0, 'Correlation Matrix')
plt.show()
sns.set(style="whitegrid")
plt.figure(figsize=(12, 6))
<Figure size 1200x600 with 0 Axes>
plt.subplot(2, 2, 1)
<AxesSubplot:>
sns.histplot(iris_df['sepal.length'], kde=True, color='blue', bins=20)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    sns.histplot(iris_df['sepal.length'], kde=True, color='blue', bins=20)
NameError: name 'iris_df' is not defined
sns.histplot(data['sepal.length'], kde=True, color='blue', bins=20)
<AxesSubplot:xlabel='sepal.length', ylabel='Count'>
plt.title('Distribution of Sepal Length')
Text(0.5, 1.0, 'Distribution of Sepal Length')
plt.subplot(2, 2, 2)
<AxesSubplot:>
sns.histplot(data['sepal.width'], kde=True, color='green', bins=20)
<AxesSubplot:xlabel='sepal.width', ylabel='Count'>
plt.title('Distribution of Sepal Width')
Text(0.5, 1.0, 'Distribution of Sepal Width')
plt.subplot(2, 2, 3)
<AxesSubplot:>
sns.histplot(data['petal.length'], kde=True, color='red', bins=20)
<AxesSubplot:xlabel='petal.length', ylabel='Count'>
plt.title('Distribution of Petal Length')
Text(0.5, 1.0, 'Distribution of Petal Length')
plt.subplot(2, 2, 4)
<AxesSubplot:>
sns.histplot(data['petal.width'], kde=True, color='orange', bins=20)4
SyntaxError: invalid syntax
sns.histplot(data['petal.width'], kde=True, color='orange', bins=20)
<AxesSubplot:xlabel='petal.width', ylabel='Count'>
plt.title('Distribution of Petal Width')
Text(0.5, 1.0, 'Distribution of Petal Width')
plt.tight_layout()
plt.show()
plt.figure(figsize=(10, 6))
<Figure size 1000x600 with 0 Axes>
sns.boxplot(data=data.drop('variety', axis=1))
<AxesSubplot:>
plt.title('Boxplots of Numerical Features')
Text(0.5, 1.0, 'Boxplots of Numerical Features')
plt.show()
plt.figure(figsize=(10, 6))
<Figure size 1000x600 with 0 Axes>
sns.violinplot(data=data.drop('variety', axis=1))
<AxesSubplot:>
plt.title('Violin Plots of Numerical Features')
Text(0.5, 1.0, 'Violin Plots of Numerical Features')
plt.show()
data['sepal_area'] = data['sepal.length'] * data['sepal.width']
data['petal_area'] = data['petal.length'] * data['petal.width']
data.head()
   sepal.length  sepal.width  petal.length  ...  variety sepal_area  petal_area
0           5.1          3.5           1.4  ...   Setosa      17.85        0.28
1           4.9          3.0           1.4  ...   Setosa      14.70        0.28
2           4.7          3.2           1.3  ...   Setosa      15.04        0.26
3           4.6          3.1           1.5  ...   Setosa      14.26        0.30
4           5.0          3.6           1.4  ...   Setosa      18.00        0.28

[5 rows x 7 columns]
data.to_csv("iris.csv",index=False)
data=pd.read_csv("iris.csv")
data.head()
   sepal.length  sepal.width  petal.length  ...  variety sepal_area  petal_area
0           5.1          3.5           1.4  ...   Setosa      17.85        0.28
1           4.9          3.0           1.4  ...   Setosa      14.70        0.28
2           4.7          3.2           1.3  ...   Setosa      15.04        0.26
3           4.6          3.1           1.5  ...   Setosa      14.26        0.30
4           5.0          3.6           1.4  ...   Setosa      18.00        0.28

[5 rows x 7 columns]
data
     sepal.length  sepal.width  petal.length  ...    variety sepal_area  petal_area
0             5.1          3.5           1.4  ...     Setosa      17.85        0.28
1             4.9          3.0           1.4  ...     Setosa      14.70        0.28
2             4.7          3.2           1.3  ...     Setosa      15.04        0.26
3             4.6          3.1           1.5  ...     Setosa      14.26        0.30
4             5.0          3.6           1.4  ...     Setosa      18.00        0.28
..            ...          ...           ...  ...        ...        ...         ...
145           6.7          3.0           5.2  ...  Virginica      20.10       11.96
146           6.3          2.5           5.0  ...  Virginica      15.75        9.50
147           6.5          3.0           5.2  ...  Virginica      19.50       10.40
148           6.2          3.4           5.4  ...  Virginica      21.08       12.42
149           5.9          3.0           5.1  ...  Virginica      17.70        9.18

[150 rows x 7 columns]
