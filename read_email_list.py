import pandas as pd

# Load email addresses from the csv file
df = pd.read_csv("email_list.csv", delimiter=";")
# add not contacted emails to a list (Contacted column is empty)
email_list = df[df['Contacted'].isnull()]['Email Address'].tolist()
print(email_list)