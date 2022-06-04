# Analysis

## SVD

Singular Value Decomposition was used to to identify CNVs that show maximum variances. It was performed on the binary CNV matrix (called Initial data) and network propagated CNV matrix (called Smoothed data) separately. The propagated CNV matrix was used to identify genes that are not directly affected by CNVs.

-   `SVD.ipynb`: Code to perform SVD on Initial and Smoothed CNV data.
-   `Smoothing.ipynb`: Code to perform smooth the Initial CNV data, by performing network propagation.
-   SVD_Genes directory
    -   Naming format: Cluster_Type_Property
    -   where: Cluster can be {c1, c2}.
        Type can be {Initial, Smooth, intersection of the two, and difference of the two}.
        Property can be {Top100, num of genes, allgenes}.

## DEG_between_clusters

Differential Gene Expression analysis performed on the two clusters and the common genes (with the network and initial data) are mentioned in the following files.

-   `downgenes_poorsurv.csv`: Down-regulated DEGs found in the cluster with poor survival, as compared against the better survival group.
-   `upgenes_poorsurv.csv`: Up-regulated DEGs found in the cluster with poor survival, as compared against the better survival group.
-   `DEG_down_surv_22_cyto.xlsx`: Intersection of down-regulated DEGs with the genes in GeneNet and CNV data.
-   `DEG_up_surv_283_cyto.xlsx`: Intersection of up-regulated DEGs with the genes in GeneNet and CNV data.

## Other files

-   `CCC_PAC.ipynb`: Code to calculate Cophenetic Correlation Coefficient and Proportion of Ambiguous Clustering (PAC).
-   `Silhouette Coeff.ipynb`: Code to calculate Silhouette Coefficient.
