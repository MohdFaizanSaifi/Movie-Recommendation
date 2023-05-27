import networkx as nx
import time
import pickle
import pandas as pd
import math
import numpy as np
import time

def recommends(movie):
    t = []
    with open(r'C:\Users\Faizan\OneDrive\Desktop\Movie\my_set.pkl', 'rb') as f:
        movie_set = pickle.load(f)
    if movie in movie_set:
        start_time = time.time()
        G = nx.read_graphml(r"C:\Users\Faizan\Downloads\my_graph.graphml")
        #movie = "Ocean's Twelve"
        commons_dict = {}
        for e in G.neighbors(movie):
            for e2 in G.neighbors(e):
                if e2==movie:
                    continue
                if G.nodes[e2]['label']=="MOVIE":
                    commons = commons_dict.get(e2)
                    if commons==None:
                        commons_dict.update({e2 : [e]})
                    else:
                        commons.append(e)
                        commons_dict.update({e2 : commons})
        movies=[]
        weight=[]
        for key, values in commons_dict.items():
            w=0.0
            for e in values:
                w=w+1/math.log(G.degree(e))
            movies.append(key) 
            weight.append(w)
    
    
        result = pd.Series(data=np.array(weight), index=movies)
        result.sort_values(inplace=True,ascending=False)  
        res = result.index.to_list()
        
        end_time = time.time()

        execution_time = end_time - start_time
        
        return res[0:5]
    
    else:
        return t
