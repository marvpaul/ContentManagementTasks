import pickle
import gzip
import numpy

with open('english_ace_multiclass.pickle', 'rb') as f:
    u = pickle._Unpickler(f)
    u.encoding = 'latin1'
    p = u.load()
    print(p)