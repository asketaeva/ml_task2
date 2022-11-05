import pandas as pd
import seaborn as sns
import matplotlib
from Tools.scripts.dutree import display

df = pd.read_csv('full_data.csv')
matplotlib.rcParams['figure.figsize'] = (12, 8)


df.info()
info = pd.DataFrame(df.dtypes).T.rename(index={0:'column type'})
info = info.append(pd.DataFrame(df.isnull().sum()))

display(info)
df.age.min() , df.age.max()

sns.countplot(data=df, x='work_type')

sns.countplot(data=df, x='work_type', hue='stroke')

sns.histplot(data=df, x='heart_disease', kde=True)
sns.countplot(data=df, x='stroke', hue='gender')
sns.histplot(data=df, x='age', hue='heart_disease', kde=True)

sns.histplot(data=df, x='avg_glucose_level', hue='stroke', kde=True)
sns.histplot(data=df, x='age', hue='heart_disease', kde=True)
sns.histplot(data=df, x='ever_married', hue='stroke', kde=True)

sns.scatterplot(data=df, x="avg_glucose_level", y="bmi", hue="smoking_status")
sns.lineplot(data=df, x="age", y="bmi", hue="stroke")
sns.lineplot(data=df, x="age", y="avg_glucose_level", hue="stroke")