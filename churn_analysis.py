import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

print(df.head())

print(df.info())

# Check for missing values
print("\nChecking for missing values")
print(df.isnull().sum())

# Remove any rows with missing data (if found)
print("\nRemove any rows with missing data (if found)")
df.dropna(inplace=True)

# Count of churned vs not churned
print("\nCount of churned vs not churned")
print(df['Churn'].value_counts())

# Percentage of churned customers
churn_rate = df['Churn'].value_counts(normalize=True) * 100
print("\nChurn Rate (%):\n", churn_rate)

sns.countplot(data=df, x='gender', hue='Churn')
plt.title('Churn by Gender')
plt.show()

sns.countplot(data=df, x='SeniorCitizen', hue='Churn')
plt.title('Churn by Senior Citizen Status')
plt.show()

sns.histplot(data=df, x='tenure', hue='Churn', multiple='stack', bins=30)
plt.title('Churn by Customer Tenure')
plt.show()

sns.boxplot(x='Churn', y='MonthlyCharges', data=df)
plt.title('Monthly Charges vs Churn')
plt.show()
