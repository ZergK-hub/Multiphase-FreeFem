import matplotlib.pyplot as plt

import pandas as pd

# Specify the file path
file_path = './Data.txt'

# Read the tab-separated data into a pandas DataFrame
data = pd.read_csv(file_path, sep='\t',names=["Text","DoF","X","Y","color"])

# Annotations
annotations=data["DoF"].to_list()

x=data["X"]
y=data["Y"]

colors=data["color"].to_list()

plt.scatter(x,y,c=colors)

X=x.to_list()

Y=y.to_list()

Xstr=['{:.2e}'.format(X) for X in X]

Ystr=['{:.2e}'.format(Y) for Y in Y]

for i, txt in enumerate(annotations):
    text=str(txt)
  
    text=r"$\mathbf{"+text+"}$"
    
    annot_text="DoF "+text+"\n ["+Xstr[i]+";"+Ystr[i]+"]"
    plt.annotate(annot_text, 
                 (X[i], Y[i]), textcoords="offset points",
                 xytext=(0, 5), ha='center')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Степени свободы и координаты элемента')

plt.show()