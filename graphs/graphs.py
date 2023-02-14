import pandas as pd
import plotly_express as px

graphs_df=pd.read_csv("resultados.csv", header=None, sep="\t")
graphs_df.columns=['fichero', 'n', 'sol', 'time', 'alpha']


