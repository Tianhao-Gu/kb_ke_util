# -*- coding: utf-8 -*-
#BEGIN_HEADER
import os

from kb_ke_util.Utils.KnowledgeEngineUtil import KnowledgeEngineUtil
#END_HEADER


class kb_ke_util:
    '''
    Module Name:
    kb_ke_util

    Module Description:
    A KBase module: kb_ke_util
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "1.0.0"
    GIT_URL = "https://github.com/Tianhao-Gu/kb_ke_util.git"
    GIT_COMMIT_HASH = "674ae5e9e7eb31d7c4894a3efff154c448ff42e4"

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.config = config
        self.config['SDK_CALLBACK_URL'] = os.environ['SDK_CALLBACK_URL']
        self.config['KB_AUTH_TOKEN'] = os.environ['KB_AUTH_TOKEN']
        #END_CONSTRUCTOR
        pass


    def run_pdist(self, ctx, params):
        """
        run_pdist: a wrapper method for scipy.spatial.distance.pdist
        reference: 
        https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.pdist.html
        :param params: instance of type "PdistParams" (Input of the run_pdist
           function data_matrix - raw data matrix with row_ids, col_ids and
           values e.g.{'row_ids': ['gene_1', 'gene_2'], 'col_ids':
           ['condition_1', 'condition_2'], 'values': [[0.1, 0.2], [0.3, 0.4],
           [0.5, 0.6]]} Optional arguments: metric - The distance metric to
           use. Default set to 'euclidean'. The distance function can be
           ["braycurtis", "canberra", "chebyshev", "cityblock",
           "correlation", "cosine", "dice", "euclidean", "hamming",
           "jaccard", "kulsinski", "matching", "rogerstanimoto",
           "russellrao", "sokalmichener", "sokalsneath", "sqeuclidean",
           "yule"] Details refer to:
           https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.
           distance.pdist.html Note: Advanced metric functions 'minkowski',
           'seuclidean' and 'mahalanobis' included in
           scipy.spatial.distance.pdist library are not implemented) ->
           structure: parameter "data_matrix" of mapping from String to
           String, parameter "metric" of String
        :returns: instance of type "PdistOutput" (Ouput of the run_pdist
           function square_dist_matrix - square form of distance matrix where
           the data is mirrored across the diagonal labels - item name
           corresponding to each square_dist_matrix element) -> structure:
           parameter "square_dist_matrix" of list of list of String,
           parameter "labels" of list of String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN run_pdist

        for key, value in params.iteritems():
            if isinstance(value, basestring):
                params[key] = value.strip()

        ke_util = KnowledgeEngineUtil(self.config)
        returnVal = ke_util.run_pdist(params)
        #END run_pdist

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method run_pdist return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def run_linkage(self, ctx, params):
        """
        run_linkage: a wrapper method for scipy.cluster.hierarchy.linkage
        reference: 
        https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html
        :param params: instance of type "LinkageParams" (Input of the
           run_linkage function square_dist_matrix - square form of distance
           matrix (refer to run_pdist return) Optional arguments: method -
           The linkage algorithm to use. Default set to 'ward'. The method
           can be ["single", "complete", "average", "weighted", "centroid",
           "median", "ward"] Details refer to:
           https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.
           hierarchy.linkage.html) -> structure: parameter
           "square_dist_matrix" of list of list of String, parameter "method"
           of String
        :returns: instance of type "LinkageOutput" (Ouput of the run_linkage
           function linkage_matrix - The hierarchical clustering encoded as a
           linkage matrix) -> structure: parameter "linkage_matrix" of list
           of list of String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN run_linkage
        for key, value in params.iteritems():
            if isinstance(value, basestring):
                params[key] = value.strip()

        ke_util = KnowledgeEngineUtil(self.config)
        returnVal = ke_util.run_linkage(params)
        #END run_linkage

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method run_linkage return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def run_fcluster(self, ctx, params):
        """
        run_fcluster: a wrapper method for scipy.cluster.hierarchy.fcluster
        reference: 
        https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.fcluster.html
        :param params: instance of type "FclusterParams" (Input of the
           run_fcluster function linkage_matrix - hierarchical clustering
           linkage matrix (refer to run_linkage return) dist_threshold - the
           threshold to apply when forming flat clusters Optional arguments:
           labels - items corresponding to each linkage_matrix element (If
           labels are given, result flat_cluster will be mapped to element in
           labels.) criterion - The criterion to use in forming flat
           clusters. Default set to 'distance'. The criterion can be
           ["inconsistent", "distance", "maxclust"] Note: Advanced criterion
           'monocrit', 'maxclust_monocrit' in
           scipy.cluster.hierarchy.fcluster library are not implemented
           Details refer to:
           https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.
           hierarchy.fcluster.html) -> structure: parameter "linkage_matrix"
           of list of list of String, parameter "dist_threshold" of Double,
           parameter "labels" of list of String, parameter "criterion" of
           String
        :returns: instance of type "FclusterOutput" (Ouput of the
           run_fcluster function flat_cluster - A dictionary of flat
           clusters. Each element of flat_cluster representing a cluster
           contains a label array. (If labels is none, element position array
           is returned to each cluster group)) -> structure: parameter
           "flat_cluster" of mapping from String to list of String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN run_fcluster
        for key, value in params.iteritems():
            if isinstance(value, basestring):
                params[key] = value.strip()

        ke_util = KnowledgeEngineUtil(self.config)
        returnVal = ke_util.run_fcluster(params)
        #END run_fcluster

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method run_fcluster return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def run_dendrogram(self, ctx, params):
        """
        run_dendrogram: a wrapper method for scipy.cluster.hierarchy.dendrogram
        reference: 
        https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.dendrogram.html
        :param params: instance of type "DendrogramParams" (Input of the
           run_dendrogram function linkage_matrix - hierarchical clustering
           linkage matrix (refer to run_linkage return) Optional arguments:
           dist_threshold - the threshold to apply when forming flat clusters
           (draw a horizontal line to dendrogram) labels - items
           corresponding to each linkage_matrix element (If labels are given,
           result dendrogram x-axis will be mapped to element in labels.)
           last_merges - show only last given value merged clusters) ->
           structure: parameter "linkage_matrix" of list of list of String,
           parameter "dist_threshold" of Double, parameter "labels" of list
           of String, parameter "last_merges" of Long
        :returns: instance of type "DendrogramOutput" (Ouput of the
           run_dendrogram function result_plots - List of result plot
           path(s)) -> structure: parameter "result_plots" of list of String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN run_dendrogram
        for key, value in params.iteritems():
            if isinstance(value, basestring):
                params[key] = value.strip()

        ke_util = KnowledgeEngineUtil(self.config)
        returnVal = ke_util.run_dendrogram(params)
        #END run_dendrogram

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method run_dendrogram return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
