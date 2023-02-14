import pandas as pd

def readInstance(path):
    df=pd.read_csv(path, sep=";", header=None)
    mat=[]
    for i in range(len(df.columns)):
        mat.append(df[i].tolist())
        print(type(mat[i]))
    instance={'n':500, 'p':25, 'd':mat}
    return instance

