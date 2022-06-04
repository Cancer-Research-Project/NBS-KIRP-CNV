# Network diffusion-based approach for survival prediction and identification of biomarkers using multi-omics data of Papillary Renal Cell Carcinoma

This is the codebase and the datasets mentioned in the paper **_Network diffusion-based approach for survival prediction and
identification of biomarkers using multi-omics data of Papillary
Renal Cell Carcinoma_**._2022_

The repo can be divided into the following sections :

-   PyNBS
-   Scripts and Runner files
-   Analysis
-   Gene Network Creation
-   Data
-   Results

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

-   **script_CNV.py** : to perform NBS on the given inputs
-   **script_CNV_without_network.py** : to perform NMF on the given inputs

The Runner script along with the arguments are given in **run_cnv_script.sh**

## Analysis

This section contains the results obtained after the _post-clustering_ analysis, It contains results after performing **_DEG analysis_** on the cluster and **_SVD_** on the clusters.
It also contains the codes used for performing the above along with the code for finding the silhouette coefficient, the Cophenetic correlation coefficient, and PAC values.

## Data

This section contains all the data used for the analyses mentioned in the paper. It includes the omics data used, the networks and respective clinical data.

## Results

The directories inside it contain the cluster assignments, related plots, coefficients and images for the respective runs.  
Name Format: _Data_Network_Cluster_

-   CNV_CRN_Cluster2
-   CNV_GeneNet_Cluster2
-   CNV_PCNet_Cluster2
-   CNV_NoNetwork_Cluster3
