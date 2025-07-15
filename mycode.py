import pandas as pd
import os


data={
    'NAME':['A','B','C','D'],
    'AGE':[21,34,22,19],
    'CLASS':['XII','XI','X','XI']
}


df=pd.DataFrame(data)


datadir='data'

os.makedirs(datadir,exist_ok=True)


file_path=os.path.join(datadir,'my_data.csv')


df.to_csv(file_path,index=False)

print(f"File is saved on the path {file_path}")

