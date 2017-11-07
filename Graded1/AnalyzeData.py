import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("./train.csv")


print(data.columns)

print(data.describe(include = "all"))
data_table = data.describe(include = "all").to_html(float_format=lambda x: '%6.2f' % x,
                        classes="table display")

with open("out.html", 'w') as file:
    file.write(data_table)


data["CabinBool"] = (data["Cabin"].notnull().astype('int'))

data["Family_size"] = (data["SibSp"].astype('int') + data["Parch"].astype('int'))
#plot = sns.barplot(x="Family_size", y="Survived", data=data)

#draw a bar plot of survival by sex
plot = sns.barplot(x="Embarked", y="Survived", data=data)
plt.show()
