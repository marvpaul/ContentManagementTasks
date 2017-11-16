import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

'''This is just a playground for analyzing the given data with pandas :)'''

data = pd.read_csv("./train.csv")

#Just get an overview
print(data.columns)
print(data.describe(include = "all"))
data_table = data.describe(include = "all").to_html(float_format=lambda x: '%6.2f' % x,
                        classes="table display")
#Save as html table for better visualization
with open("out.html", 'w') as file:
    file.write(data_table)

#Plot some features
data["CabinBool"] = (data["Cabin"].notnull().astype('int'))

data["Family_size"] = (data["SibSp"].astype('int') + data["Parch"].astype('int'))
#plot = sns.barplot(x="Family_size", y="Survived", data=data)

#draw a bar plot of survival by sex
plot = sns.barplot(x="Embarked", y="Survived", data=data)
plt.show()
