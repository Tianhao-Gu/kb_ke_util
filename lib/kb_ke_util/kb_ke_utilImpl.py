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
    VERSION = "1.0.3"
    GIT_URL = "https://github.com/Tianhao-Gu/kb_ke_util.git"
    GIT_COMMIT_HASH = "8f7d69981a2daa0becdd0db336e3cb2e1a7a567b"

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.config = config
        # self.config['KB_AUTH_TOKEN'] = os.environ['KB_AUTH_TOKEN']
        #END_CONSTRUCTOR
        pass


    def linkage_2_newick(self, ctx, params):
        """
        run_PCA: perform PCA on a n-dimensional matrix
        :param params: instance of type "NewickParams" (Input of the
           linkage_2_newick function linkage_matrix - hierarchical clustering
           linkage matrix (refer to run_linkage return) labels - items
           corresponding to each linkage_matrix element (If labels are given,
           result flat_cluster will be mapped to element in labels.)) ->
           structure: parameter "linkage_matrix" of list of list of Double,
           parameter "labels" of list of String
        :returns: instance of type "NewickOutput" (Ouput of the
           linkage_2_newick function newick - newick representation of tree
           https://en.wikipedia.org/wiki/Newick_format) -> structure:
           parameter "newick" of String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN linkage_2_newick
        for key, value in params.iteritems():
            if isinstance(value, basestring):
                params[key] = value.strip()

        self.config['KB_AUTH_TOKEN'] = ctx["token"]

        ke_util = KnowledgeEngineUtil(self.config)
        returnVal = ke_util.linkage_2_newick(params)
        #END linkage_2_newick

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method linkage_2_newick return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def run_PCA(self, ctx, params):
        """
        run_PCA: perform PCA on a n-dimensional matrix
        :param params: instance of type "PCAParams" (Input of the run_PCA
           function data_matrix - raw data matrix in json format
           e.g.{u'condition_1': {u'gene_1': 0.1, u'gene_2': 0.3, u'gene_3':
           None}, u'condition_2': {u'gene_1': 0.2, u'gene_2': 0.4, u'gene_3':
           None}, u'condition_3': {u'gene_1': 0.3, u'gene_2': 0.5, u'gene_3':
           None}, u'condition_4': {u'gene_1': 0.4, u'gene_2': 0.6, u'gene_3':
           None}} n_components - number of components (default 2)) ->
           structure: parameter "data_matrix" of String, parameter
           "n_components" of Long
        :returns: instance of type "PCAOutput" (Ouput of the run_PCA function
           PCA_matrix - PCA matrix in json format with principal_component_1,
           principal_component_2 col and same index as original data matrix)
           -> structure: parameter "PCA_matrix" of String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN run_PCA
        for key, value in params.iteritems():
            if isinstance(value, basestring):
                params[key] = value.strip()

        self.config['KB_AUTH_TOKEN'] = ctx["token"]

        ke_util = KnowledgeEngineUtil(self.config)
        returnVal = ke_util.run_PCA(params)
        #END run_PCA

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method run_PCA return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def run_kmeans2(self, ctx, params):
        """
        run_kmeans2: a wrapper method for  scipy.cluster.vq.kmeans2
        reference:
        https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.vq.kmeans2.html#scipy.cluster.vq.kmeans2
        :param params: instance of type "KmeansParams" (Input of the
           run_kmeans2 function dist_matrix - a condensed distance matrix
           (refer to run_pdist return) k_num: number of clusters to form) ->
           structure: parameter "dist_matrix" of list of Double, parameter
           "k_num" of Long
        :returns: instance of type "KmeansOutput" (Ouput of the run_kmeans2
           function centroid - centroids found at the last iteration of
           k-means idx - index of the centroid) -> structure: parameter
           "centroid" of list of Double, parameter "idx" of list of Long
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN run_kmeans2
        for key, value in params.iteritems():
            if isinstance(value, basestring):
                params[key] = value.strip()

        self.config['KB_AUTH_TOKEN'] = ctx["token"]

        ke_util = KnowledgeEngineUtil(self.config)
        returnVal = ke_util.run_kmeans2(params)
        #END run_kmeans2

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method run_kmeans2 return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def run_pdist(self, ctx, params):
        """
        run_pdist: a wrapper method for scipy.spatial.distance.pdist
        reference: 
        https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.pdist.html
        :param params: instance of type "PdistParams" (Input of the run_pdist
           function data_matrix - raw data matrix in json format
           e.g.{u'condition_1': {u'gene_1': 0.1, u'gene_2': 0.3, u'gene_3':
           None}, u'condition_2': {u'gene_1': 0.2, u'gene_2': 0.4, u'gene_3':
           None}, u'condition_3': {u'gene_1': 0.3, u'gene_2': 0.5, u'gene_3':
           None}, u'condition_4': {u'gene_1': 0.4, u'gene_2': 0.6, u'gene_3':
           None}} Optional arguments: metric - The distance metric to use.
           Default set to 'euclidean'. The distance function can be
           ["braycurtis", "canberra", "chebyshev", "cityblock",
           "correlation", "cosine", "dice", "euclidean", "hamming",
           "jaccard", "kulsinski", "matching", "rogerstanimoto",
           "russellrao", "sokalmichener", "sokalsneath", "sqeuclidean",
           "yule"] Details refer to:
           https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.
           distance.pdist.html Note: Advanced metric functions 'minkowski',
           'seuclidean' and 'mahalanobis' included in
           scipy.spatial.distance.pdist library are not implemented) ->
           structure: parameter "data_matrix" of String, parameter "metric"
           of String
        :returns: instance of type "PdistOutput" (Ouput of the run_pdist
           function dist_matrix - 1D distance matrix labels - item name
           corresponding to each dist_matrix element) -> structure: parameter
           "dist_matrix" of list of Double, parameter "labels" of list of
           String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN run_pdist

        for key, value in params.iteritems():
            if isinstance(value, basestring):
                params[key] = value.strip()

        self.config['KB_AUTH_TOKEN'] = ctx["token"]

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
           run_linkage function dist_matrix - 1D distance matrix (refer to
           run_pdist return) Optional arguments: method - The linkage
           algorithm to use. Default set to 'ward'. The method can be
           ["single", "complete", "average", "weighted", "centroid",
           "median", "ward"] Details refer to:
           https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.
           hierarchy.linkage.html) -> structure: parameter "dist_matrix" of
           list of Double, parameter "method" of String
        :returns: instance of type "LinkageOutput" (Ouput of the run_linkage
           function linkage_matrix - The hierarchical clustering encoded as a
           linkage matrix) -> structure: parameter "linkage_matrix" of list
           of list of Double
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN run_linkage
        for key, value in params.iteritems():
            if isinstance(value, basestring):
                params[key] = value.strip()

        self.config['KB_AUTH_TOKEN'] = ctx["token"]

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
           of list of list of Double, parameter "dist_threshold" of Double,
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

        self.config['KB_AUTH_TOKEN'] = ctx["token"]

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

        self.config['KB_AUTH_TOKEN'] = ctx["token"]

        ke_util = KnowledgeEngineUtil(self.config)
        returnVal = ke_util.run_dendrogram(params)
        #END run_dendrogram

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method run_dendrogram return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def build_biclusters(self, ctx, params):
        """
        build_biclusters: build biclusters and store result feature sets as JSON into shock
        :param params: instance of type "BuildBiclustersParams" (Input of the
           build_biclusters function ndarray_ref: NDArray object reference
           dist_threshold: the threshold to apply when forming flat clusters
           Optional arguments: dist_metric: The distance metric to use.
           Default set to 'euclidean'. The distance function can be
           ["braycurtis", "canberra", "chebyshev", "cityblock",
           "correlation", "cosine", "dice", "euclidean", "hamming",
           "jaccard", "kulsinski", "matching", "rogerstanimoto",
           "russellrao", "sokalmichener", "sokalsneath", "sqeuclidean",
           "yule"] Details refer to:
           https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.
           distance.pdist.html linkage_method: The linkage algorithm to use.
           Default set to 'ward'. The method can be ["single", "complete",
           "average", "weighted", "centroid", "median", "ward"] Details refer
           to:
           https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.
           hierarchy.linkage.html fcluster_criterion: The criterion to use in
           forming flat clusters. Default set to 'distance'. The criterion
           can be ["inconsistent", "distance", "maxclust"] Details refer to:
           https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.
           hierarchy.fcluster.html) -> structure: parameter "ndarray_ref" of
           type "obj_ref" (An X/Y/Z style reference), parameter
           "dist_threshold" of Double, parameter "dist_metric" of String,
           parameter "linkage_method" of String, parameter
           "fcluster_criterion" of String
        :returns: instance of type "BuildBiclustersOutput" (Ouput of the
           build_biclusters function biclusters: list of biclusters e.g.
           [["gene_id_1", "gene_id_2"], ["gene_id_3"]]) -> structure:
           parameter "biclusters" of list of list of String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN build_biclusters
        for key, value in params.iteritems():
            if isinstance(value, basestring):
                params[key] = value.strip()

        self.config['KB_AUTH_TOKEN'] = ctx["token"]

        ke_util = KnowledgeEngineUtil(self.config)
        returnVal = ke_util.build_biclusters(params)
        #END build_biclusters

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method build_biclusters return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def enrich_onthology(self, ctx, params):
        """
        enrich_onthology: run GO term enrichment analysis
        :param params: instance of type "EnrichOnthologyParams" (Input of the
           enrich_onthology function sample_set: list of gene_ids in
           clustering e.g. ["gene_id_1", "gene_id_2", "gene_id_3"]
           entity_term_set: entity terms dict structure where global GO term
           and gene_ids are stored e.g. {"gene_id_1": ["go_term_1",
           "go_term_2"]} Optional arguments: propagation: includes is_a
           relationship to all go terms (default is 0)) -> structure:
           parameter "sample_set" of list of String, parameter
           "entity_term_set" of mapping from type "entity_guid" to type
           "assigned_term_guids" -> list of String, parameter "propagation"
           of type "boolean" (A boolean - 0 for false, 1 for true. @range (0,
           1))
        :returns: instance of type "EnrichOnthologyOutput" (Ouput of the
           enrich_onthology function enrichment_profile: dict structure
           stores enrichment info e.g. {"go_term_1": {"sample_count": 10,
           "total_count": 20, "p_value": 0.1, "ontology_type": "P"}}) ->
           structure: parameter "enrichment_profile" of mapping from type
           "term_guid" to type "TermEnrichment" -> structure: parameter
           "sample_count" of Long, parameter "total_count" of Long, parameter
           "expected_count" of Long, parameter "p_value" of Double
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN enrich_onthology
        for key, value in params.iteritems():
            if isinstance(value, basestring):
                params[key] = value.strip()

        self.config['KB_AUTH_TOKEN'] = ctx["token"]

        ke_util = KnowledgeEngineUtil(self.config)
        returnVal = ke_util.enrich_onthology(params)
        #END enrich_onthology

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method enrich_onthology return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def calc_onthology_dist(self, ctx, params):
        """
        calc_onthology_dist: calculate onthology distance
        (sum of steps for each node in onthology_pair travels to 
         the nearest common ancestor node)
        NOTE: return inf if no common ancestor node found
        :param params: instance of type "CalcOnthologyDistParams" (Input of
           the calc_onthology_dist function onthology_set: dict structure
           stores mapping of gene_id to paried onthology e.g. {"gene_id_1":
           ["go_term_1", "go_term_2"]}) -> structure: parameter
           "onthology_set" of mapping from type "gene_id" to type
           "onthology_pair" -> list of String
        :returns: instance of type "CalcOnthologyDistOutput" (Ouput of the
           calc_onthology_dist function onthology_dist_set: dict structure
           stores mapping of gene_id to dist e.g. {"gene_id_1": 3}) ->
           structure: parameter "onthology_dist_set" of mapping from type
           "gene_id" to Long
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN calc_onthology_dist
        for key, value in params.iteritems():
            if isinstance(value, basestring):
                params[key] = value.strip()

        self.config['KB_AUTH_TOKEN'] = ctx["token"]

        ke_util = KnowledgeEngineUtil(self.config)
        returnVal = ke_util.calc_onthology_dist(params)
        #END calc_onthology_dist

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method calc_onthology_dist return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def calc_weighted_onthology_dist(self, ctx, params):
        """
        calc_weighted_onthology_dist: calculate weighted onthology distance
        (edges are weighted from root to leaves
         root edges are weighted 1/2
         each child's edge weights half of its parent's edge)
        NOTE: return inf if no common ancestor node found
        :param params: instance of type "CalcOnthologyDistParams" (Input of
           the calc_onthology_dist function onthology_set: dict structure
           stores mapping of gene_id to paried onthology e.g. {"gene_id_1":
           ["go_term_1", "go_term_2"]}) -> structure: parameter
           "onthology_set" of mapping from type "gene_id" to type
           "onthology_pair" -> list of String
        :returns: instance of type "CalcOnthologyDistOutput" (Ouput of the
           calc_onthology_dist function onthology_dist_set: dict structure
           stores mapping of gene_id to dist e.g. {"gene_id_1": 3}) ->
           structure: parameter "onthology_dist_set" of mapping from type
           "gene_id" to Long
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN calc_weighted_onthology_dist
        for key, value in params.iteritems():
            if isinstance(value, basestring):
                params[key] = value.strip()

        self.config['KB_AUTH_TOKEN'] = ctx["token"]

        ke_util = KnowledgeEngineUtil(self.config)
        returnVal = ke_util.calc_weighted_onthology_dist(params)
        #END calc_weighted_onthology_dist

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method calc_weighted_onthology_dist return value ' +
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
