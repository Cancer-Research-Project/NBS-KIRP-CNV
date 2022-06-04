# sample script to run the NBS algorithm
maf_file='NONE'
sm_mat='./Data/Sm_files/KIRP_cna_mat_new.csv'
network_file='./Data/Network_files/CancerSubnetwork.txt'
clinical_file='./Data/Clinical_files/kirc_clinical.csv'
survival_file='./Data/Survival_files/survival_KIRC.csv'
results='./Results/CRN_KIRP/'
prefix='CRN_c_'
alpha=0.7
clusters=2
niter=100

python3 pynbs_CNV.py $maf_file $sm_mat $network_file $clinical_file $survival_file $results $prefix $clusters $niter $alpha 1 > log_file.txt
