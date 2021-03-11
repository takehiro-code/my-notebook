# common function


def normalize(value, minValue, maxValue, a, b):
    return (value - minValue) / (maxValue - minValue) * (b - a) + a # normalize to [a, b] for drawing


import re
def natural_sort(l): 
    convert = lambda text: int(text) if text.isdigit() else text.lower() 
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)] 
    return sorted(l, key=alphanum_key)



import numpy as np
#referenced: 
#https://stackoverflow.com/questions/53126305/pretty-printing-numpy-ndarrays-using-unicode-characters/53164538
# pretty print of 2d numpy array
def pprint(A):
    if A.ndim==1:
        print(A)
    else:
        w = max([len(str(s)) for s in A]) 
        print(u'\u250c'+u'\u2500'*w+u'\u2510') 
        for AA in A:
            print(' ', end='')
            print('[', end='')
            for i,AAA in enumerate(AA[:-1]):
                w1=max([len(str(s)) for s in A[:,i]])
                print(str(AAA)+' '*(w1-len(str(AAA))+1),end='')
            w1=max([len(str(s)) for s in A[:,-1]])
            print(str(AA[-1])+' '*(w1-len(str(AA[-1]))),end='')
            print(']')
        print(u'\u2514'+u'\u2500'*w+u'\u2518')




import argparse
def parse_args():
    """Parse input arguments."""
    parser = argparse.ArgumentParser(description='Running experiment')
    parser.add_argument("--class_cat", help="Select the class category", type=str)
    parser.add_argument("--seq_name", help="Select the sequence name", type=str)
    parser.add_argument("--class_id", help="Select the class ID", type=int)
    parser.add_argument("--source_path", help="source path to the images", type=str, default="/local-scratch/share_dataset/labled_hevc_sequences")
    parser.add_argument("--test", help="test for public dataset",  action='store_true')
    args = parser.parse_args()
    return args



import pandas as pd
import matplotlib.pyplot as plt
def plotdf(df, x_name, y_name, z_name):
    # x_name is name for x variable in str
    # y_name is name for y variable in str
    # z_name is name for z variable in str
    
    z_arr = pd.unique(df[z_name])
    
    for z in z_arr:
        df_chunk = df[df[z_name] == z]
        plt.plot(df_chunk[x_name], df_chunk[y_name], '.-', label=z)
        plt.legend(loc='right')
    plt.title(f"{x_name} vs {y_name} on different {z_name}")
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    plt.show()
    


import pandas as pd
import plotly.graph_objects as go
def plotlydf(df, x_name, y_name, z_name):
    # x_name is name for x variable in str
    # y_name is name for y variable in str
    # z_name is name for z variable in str
    
    fig = go.Figure()
    z_arr = pd.unique(df[z_name])
    for z in z_arr:
        df_chunk = df[df[z_name] == z]
        fig.add_trace(go.Scatter(x=df_chunk[x_name],y=df_chunk[y_name],
                            mode='lines+markers',
                            name=z))

    fig.update_layout(title=f"{x_name} vs {y_name} on different {z_name}",
                       xaxis_title=x_name,
                       yaxis_title=y_name)
    fig.show()