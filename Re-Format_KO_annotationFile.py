#This script formats the 2-column annotation file output from kofamscan

import os as os
import pandas as pd
import glob as glob

## Import kofamscan annotation files as dictionary of DATAFRAMES
## Drop rows that do not have a KO ID

filenames = glob.glob('/Users/brittanysuttner/Desktop/KOs_MAGs_ttest_clustermap/Assembly_KO_annotation_tables/*txt')
fns = [os.path.splitext(os.path.basename(x))[0] for x in filenames]
d2 = {}
for i in range(len(fns)):
    d2[fns[i]] = pd.read_csv(filenames[i], sep='\t', names=["ORF","KO"]).dropna()
    
##Create new dfs that removes the UN-annotated ORFs
Sample_IDs = list(d2.keys())
for i in range(len(Sample_IDs)):
    d2[Sample_IDs[i]].to_csv(str(Sample_IDs[i]) + "_reformat.txt", index=False, sep='\t', header=None)
