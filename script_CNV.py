# Import pyNBS modules
from pyNBS import data_import_tools as dit
from pyNBS import network_propagation as prop
from pyNBS import pyNBS_core as core
from pyNBS import pyNBS_single
from pyNBS import consensus_clustering as cc
from pyNBS import pyNBS_plotting as plot

# Import other needed packages
import os
import time
import pandas as pd
import numpy as np
from IPython.display import Image
import sys
import datetime
print("\n")
print("start_time : ", datetime.datetime.now())
print("\n")
sys.stdout.flush()

# here name_prefix is the prefix for the file name
# if sm_mat already exist put maf_path = None


def do_nbs(maf_path, sm_path, network_filepath, clinical_path, surv_data, output_filepath, name_prefix, clusters, niter, alpha):

    # print("Doing NBS on ", sm_path, " Using network ", network_filepath,
    # " with clusters and iterations ", clusters , " ", niter)

    # loading somatic mutation matrix
    if maf_path != None:
        dit.process_TCGA_MAF(maf_path, sm_path, verbose=True)

    sm_mat = pd.read_csv(sm_path, index_col=0).astype(int)

    def changeones(x):
        if x != 0:
            x = 1
        return x
    sm_mat = sm_mat.apply(np.vectorize(changeones))
    sys.stdout.flush()
    # loading network file
    network = dit.load_network_file(network_filepath)
    sys.stdout.flush()
    # constructing kknglap and kernel
    knnGlap = core.network_inf_KNN_glap(network)
    sys.stdout.flush()
    if alpha == None:
        alpha = 0.7

    network_nodes = network.nodes()
    network_I = pd.DataFrame(np.identity(
        len(network_nodes)), index=network_nodes, columns=network_nodes)

    kernel = prop.network_propagation(
        network, network_I, alpha=alpha, symmetric_norm=False)
    sys.stdout.flush()
    # performing nbs iterations
    # Optional: Setting the output directory for files to be saved in
    outdir = output_filepath+'c' + \
        str(clusters)+'_i'+str(niter)+'_alpha_'+str(alpha)+'/'

    # Optional: Creating above output directory if it doesn't already exist
    if not os.path.exists(outdir):
        os.makedirs(outdir)

    # Optional: Setting a filename prefix for all files saved to outdir
    job_name = name_prefix+str(clusters)+'_i'+str(niter)+'_alpha_'+str(alpha)

    # Constructs dictionary to be passed as "save_args" to functions if output to be saved
    save_args = {'outdir': outdir, 'job_name': job_name}

    # Run pyNBS 'niter' number of times
    Hlist = []
    for i in range(niter):
        netNMF_time = time.time()
        # Run pyNBS core steps and save resulting H matrix to Hlist
        Hlist.append(pyNBS_single.NBS_single(sm_mat, knnGlap,
                     propNet=network, propNet_kernel=kernel, k=clusters))

        ##########################################################################################################
        # Optional: If the user is saving intermediate outputs (propagation results or H matrices),
        # a different 'iteration_label' should be used for each call of pyNBS_single().
        # Otherwise, the user will overwrite each H matrix at each call of pyNBS_single()
        # Uncomment and run the two lines below to save intermediate steps instead of the previous line
        # save_args['iteration_label']=str(i+1)
        # Hlist.append(pyNBS_single.NBS_single(sm_mat, propNet=network, propNet_kernel=kernel, regNet_glap=knnGlap,
        #                                      k=clusters, **save_args))
        ##########################################################################################################

        # Report run time of each pyNBS iteration
        t = time.time()-netNMF_time
        print('NBS iteration:', i+1, 'complete:', t, 'seconds')
        sys.stdout.flush()

    NBS_cc_table, NBS_cc_linkage, NBS_cluster_assign = cc.consensus_hclust_hard(
        Hlist, k=clusters, **save_args)
    # Assign colors to clusters from pyNBS
    sys.stdout.flush()
    pyNBS_KIR_clust_cmap = plot.cluster_color_assign(
        NBS_cluster_assign, name=outdir)
    sys.stdout.flush()
    # Plot and save co-cluster map figure
    plot.plot_cc_map(NBS_cc_table, NBS_cc_linkage,
                     col_color_map=pyNBS_KIR_clust_cmap, **save_args)
    Image(filename=save_args['outdir']+save_args['job_name'] +
          '_cc_map.png', width=600, height=600)
    sys.stdout.flush()

    clinical = pd.read_csv(clinical_path, index_col=0)

    clinical = clinical[['submitter_id', 'vital_status',
                         'days_to_death', 'days_to_last_follow_up']]

    clinical = clinical.replace(
        {'Dead': 1, 'Alive': 0, 'Not Reported': 0}).fillna(0)

    clinical['overall_survival'] = [max(i, j) for i, j in zip(
        clinical['days_to_death'], clinical['days_to_last_follow_up'])]

    # survival Data

    clinical.to_csv(surv_data, index=False)

    # Plot KM Plot for patient clusters
    plot.cluster_KMplot(NBS_cluster_assign, surv_data,
                        delimiter=',', **save_args)
    Image(filename=save_args['outdir']+save_args['job_name'] +
          '_KM_plot.png', width=600, height=600)
    sys.stdout.flush()
    print("\n")
    print("end_time : ", datetime.datetime.now())
    print("\n")
    sys.stdout.flush()

# def run_in_loop():
#     do_nbs(maf_path, sm_path, network_filepath, clinical_path, surv_data, output_filepath, name_prefix, clusters, niter = 1000, alpha = None)


if __name__ == "__main__":
    maf_path = sys.argv[1]
    sm_path = sys.argv[2]
    network_filepath = sys.argv[3]
    clinical_path = sys.argv[4]
    surv_data = sys.argv[5]
    output_filepath = sys.argv[6]
    name_prefix = sys.argv[7]
    clusters = int(sys.argv[8])
    niter = int(sys.argv[9])
    alpha = float(0.7)
    no_inp = 0
    if len(sys.argv) > 9:
        alpha = sys.argv[10]
    if len(sys.argv) > 10:
        no_inp = int(sys.argv[11])

    print("arguments : ", len(sys.argv))
    print("maf_path : ", maf_path)
    print("sm_path : ", sm_path)
    print("network_filepath : ", network_filepath)
    print("clinical_filepath : ", clinical_path)
    print("surv_data : ", surv_data)
    print("output_file path : ", output_filepath)
    print("file name_prefix : ", name_prefix)
    print("cluster no : ", clusters)
    print("iteration no : ", niter)
    print("alpha : ", alpha)
    print("no input : ", no_inp)
    print("\n")
    val = 'y'
    sys.stdout.flush()

    if no_inp == 1:
        pass
    else:
        val = input("Continue y/n (no capitals allowed) : ")
    if val == 'y':
        if (os.path.exists(maf_path)):
            pass
        else:
            maf_path = None

        do_nbs(maf_path, sm_path, network_filepath, clinical_path,
               surv_data, output_filepath, name_prefix, clusters, niter, alpha)
