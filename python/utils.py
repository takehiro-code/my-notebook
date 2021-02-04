# common function

# load libraries
import glob
import numpy as np
from tqdm import tqdm
from skimage import io
import cv2
import os
import argparse
import re
import pdb

def normalize(value, minValue, maxValue, a, b):
    return (value - minValue) / (maxValue - minValue) * (b - a) + a # normalize to [a, b] for drawing


def natural_sort(l): 
    convert = lambda text: int(text) if text.isdigit() else text.lower() 
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)] 
    return sorted(l, key=alphanum_key)


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


