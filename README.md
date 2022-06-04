# Network diffusion-based approach for survival prediction and identification of biomarkers using multi-omics data of Papillary Renal Cell Carcinoma

This is the codebase and the datasets mentioned in the paper **_Network diffusion-based approach for survival prediction and
identification of biomarkers using multi-omics data of Papillary
Renal Cell Carcinoma_**._2022_

The repo can be divided into the following sections : 
- PyNBS
- Scripts and Runner files
- Analysis
- Gene Network Creation
- Data
- Results



## PyNBS
This python package replicates the network-based stratification algorithm used in the Nature Methods Hofree et al. 2013 paper. This Python code repository is ported from NBS Matlab 0.2.0. The companion Application Note for this repository is available online now at Oxford Bioinformatics ([PyNBS][1]). This package is further modified to support python > 3 in this project.

[1]: https://github.com/idekerlab/pyNBS/wiki/Installing-pyNBS "PyNBS"

### Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install PyNBS. 

```bash
cd NBS-KIRP-CNV
pip install .
```
## Scripts and Runner files
There are two scripts that are used:
- **script_CNV.py** : to perform NBS on the given inputs
- **script_CNV_without_network.py** : to perform NMF on the given inputs

The Runner script along with the arguments are given in **run_cnv_script.sh**


## Analysis
This section contains the results obtained after the *post-clustering* analysis, It contains results after performing ***DEG analysis*** on the cluster and ***SVD*** on the clusters.
It also contains the codes used for performing the above along with the code for finding the silhouette coefficient, the Cophenetic correlation coefficient, and PAC values.

## Gene Network Creation
This section contains the codes and files used for the creation of the Gene Network. It contains the following files : 
- KIRP_geneExp.ipynb : it contains the code for downloading the KIRP gene-expression dataset and performing DEG on the data. It creates 2 files for the upregulated and downregulated genes obtained respectively.
- GeneNet_setup.ipynb : this is the code for creating Gene Network using an already known network and list of upregulated and downregulated genes obtained form the previous step.

The data downloaded and the intermediate data produced during the above steps during our experiment are also added in the folder.
## Data
This section contains all the data used for the analyses mentioned in the paper. It includes the omics data used, the networks and respective clinical data.
It has 4 folders present in it namely:
- Clinical Files :  contains the clinical data of the tumor in the csv format.
- Network files  : contains the files containing the network information in the edgelist format.
- Sm Files : contains the preprocessed omics files used for the analysis (CNV).
- Survival files : contains the survival data processed form the clinical data in csv format.

## Results
This folder contains all the results of the NBS runs. The following naming scheme is followed : <Omic>_<Network_name> _<Cluster_number> 


## Contributions
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

