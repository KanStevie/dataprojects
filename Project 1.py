import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("C:/Users/Stevie/PycharmProjects/Python/data/sales_data.csv")

# Feature imputation - Replacing all NAS
df.Customer_Age.fillna("No Age",inplace=True)

df = pd.read_csv("C:/Users/Stevie/PycharmProjects/Python/data/sales_data.csv")



# Labelling categorical variables
labels = {}
for c in ["Customer_Gender"]:
    labels[c] = LabelEncoder()
    df[c] = labels[c].fit_transform(df[c])


# Exporting Processed Data
sales_data_process = "data/sales_data_processed.csv"
df.to_csv(sales_data_process)

