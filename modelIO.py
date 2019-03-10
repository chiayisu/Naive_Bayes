import numpy as np
import pandas as pd

class modelIO:
    def __init__(self, condi_file, prior_file, num_of_cat_file):
        self.condi_file = condi_file
        self.prior_file = prior_file
        self.num_of_cat_file = num_of_cat_file
        
    def SaveModel(self, condi_prob, prior_prob):
        if(self.condi_file != "" and  self.prior_file != "" and self.num_of_cat_file != ""):
            np.savetxt(self.condi_file, condi_prob, delimiter=',')
            np.savetxt(self.prior_file, prior_prob, delimiter=',')
            cat_num = np.array([prior_prob.shape[0]])
            np.savetxt(self.num_of_cat_file, cat_num, delimiter=',')
        else:
            print("one of files are is not exist")
    def loadModel(self):
        if(self.condi_file != "" and  self.prior_file != "" and self.num_of_cat_file != ""):
            dataframe = pd.read_csv(self.condi_file, sep=",", header = None)
            conditional_prob = np.array(dataframe)
            prior_prob = np.loadtxt(self.prior_file)
            num_of_cat = np.loadtxt(self.num_of_cat_file)
        else:
            print("one of files are is not exist")
        return conditional_prob, prior_prob, num_of_cat
            
        
        
