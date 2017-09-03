import time
import json
import numpy
import scipy.spatial.distance as dist
import scipy.cluster.hierarchy as hier

# import matplotlib
# matplotlib.use('Agg')

def log(message, prefix_newline=False):
    print(('\n' if prefix_newline else '') + str(time.time()) + ': ' + message)

class KnowledgeEngineUtil:

    METRIC = ["braycurtis", "canberra", "chebyshev", "cityblock", "correlation", "cosine", 
              "dice", "euclidean", "hamming", "jaccard", "kulsinski", "matching", 
              "rogerstanimoto", "russellrao", "sokalmichener", "sokalsneath", "sqeuclidean", 
              "yule"]

    METHOD = ["single", "complete", "average", "weighted", "centroid", "median", "ward"]

    CRITERION = ["inconsistent", "distance", "maxclust"]

    def _validate_run_pdist_params(self, params):
        """
        _validate_run_pdist_params:
                validates params passed to run_pdist method
        """

        log('start validating run_pdist params')

        # check for required parameters
        for p in ['data_matrix']:
            if p not in params:
                raise ValueError('"{}" parameter is required, but missing'.format(p))

        # check data_matrix validation
        data_matrix = params['data_matrix']
        if not isinstance(data_matrix, dict):
            error_msg = 'INPUT ERROR:\nRequiring dictionary data_matrix.\n'
            error_msg += 'Got: {}'.format(type(data_matrix))
            raise ValueError(error_msg)

        required_keys = ['row_ids', 'col_ids', 'values']
        keys = data_matrix.keys()
        if not all(i in keys for i in required_keys):
            error_msg = 'INPUT ERROR:\nRequiring ["row_ids", "col_ids", "values"] keys.\n'
            error_msg += 'Got: {}'.format(keys)
            raise ValueError(error_msg)

        # check metric validation
        metric = params.get('metric')
        if metric and metric not in self.METRIC:
            error_msg = 'INPUT ERROR:\nInput metric function [{}] is not valid.\n'.format(metric)
            error_msg += 'Available metric: {}'.format(self.METRIC)
            raise ValueError(error_msg)

    def _validate_run_linkage_params(self, params):
        """
        _validate_run_linkage_params:
                validates params passed to run_linkage method
        """

        log('start validating run_linkage params')

        # check for required parameters
        for p in ['square_dist_matrix']:
            if p not in params:
                raise ValueError('"{}" parameter is required, but missing'.format(p))

        # check method validation
        method = params.get('method')
        if method and method not in self.METHOD:
            error_msg = 'INPUT ERROR:\nInput linkage algorithm [{}] is not valid.\n'.format(method)
            error_msg += 'Available metric: {}'.format(self.METHOD)
            raise ValueError(error_msg)

    def _validate_run_fcluster_params(self, params):
        """
        _validate_run_fcluster_params:
                validates params passed to run_fcluster method
        """

        log('start validating run_fcluster params')

        # check for required parameters
        for p in ['linkage_matrix', 'dist_threshold']:
            if p not in params:
                raise ValueError('"{}" parameter is required, but missing'.format(p))

        # check method validation
        criterion = params.get('criterion')
        if criterion and criterion not in self.CRITERION:
            error_msg = 'INPUT ERROR:\nInput criterion [{}] is not valid.\n'.format(criterion)
            error_msg += 'Available metric: {}'.format(self.CRITERION)
            raise ValueError(error_msg)

    def _is_number_string(self, str):
        """
        _is_number_string: check number string
        """
        try:
            float(str)
            return True
        except ValueError:
            pass
     
        return False

    def _is_number(self, num):
        """
        _is_number: check input is number
        """
        try:
            return 0 == num * 0
        except:
            return False

    def _get_data(self, data_matrix):
        """
        _get_data: get data into a 2d array
        """
        values = data_matrix.get('values')
        empty_string = ['NA', 'NULL', 'null', '']

        num_values = []
        for value_array in values:
            num_value_array = []
            for value in value_array:
                if self._is_number(value):
                    num_value_array.append(value)
                elif isinstance(value, str) and self._is_number_string(value):
                    num_value_array.append(float(value))
                elif isinstance(value, str) and value in empty_string:
                    num_value_array.append(0)
                else:
                    error_msg = 'INVALID data_matrix:\n'
                    error_msg += 'cannot convert all element to number: {}'.format(value_array)
                    raise ValueError(error_msg)
            num_values.append(num_value_array)
                    
        data = numpy.array(num_values)

        return data

    def _process_fcluster(self, fcluster, labels=None):
        """
        _process_fcluster: assign labels to corresponding cluster group
                           if labels is none, return element pos array in each cluster group
        """

        flat_cluster = {}
        for pos, element in enumerate(fcluster):
            cluster_name = str(element)
            if cluster_name not in flat_cluster:
                if labels:
                    flat_cluster.update({cluster_name: [labels[pos]]})
                else:
                    flat_cluster.update({cluster_name: [pos]})
            else:
                cluster = flat_cluster.get(cluster_name)
                if labels:
                    cluster.append(labels[pos])
                else:
                    cluster.append(pos)
                flat_cluster.update({cluster_name: cluster})

        return flat_cluster

    def __init__(self, config):
        self.ws_url = config["workspace-url"]
        self.callback_url = config['SDK_CALLBACK_URL']
        self.token = config['KB_AUTH_TOKEN']
        self.shock_url = config['shock-url']
        self.srv_wiz_url = config['srv-wiz-url']
        self.scratch = config['scratch']

    def run_pdist(self, params):
        """
        run_pdist: a wrapper method for scipy.spatial.distance.pdist
        reference:
        https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.pdist.html

        data_matrix - raw data matrix with row_ids, col_ids and values
                      e.g.{'row_ids': ['gene_1', 'gene_2'], 
                           'col_ids': ['condition_1', 'condition_2'],
                           'values': [[0.1, 0.2], [0.3, 0.4], [0.5, 0.6]]}

        Optional arguments:
        metric - The distance metric to use. Default set to 'euclidean'.
                 The distance function can be 
                 ["braycurtis", "canberra", "chebyshev", "cityblock", "correlation", "cosine", 
                  "dice", "euclidean", "hamming", "jaccard", "kulsinski", "matching", 
                  "rogerstanimoto", "russellrao", "sokalmichener", "sokalsneath", "sqeuclidean", 
                  "yule"]

        Note: Advanced metric functions 'minkowski', 'seuclidean' and 'mahalanobis' included in 
              scipy.spatial.distance.pdist library are not implemented

        return:
        square_dist_matrix - square form of distance matrix where the data is mirrored across 
                             the diagonal
        labels - item name corresponding to each square_dist_matrix element
        """

        log('--->\nrunning run_pdist\n' +
            'params:\n{}'.format(json.dumps(params, indent=1)))

        self._validate_run_pdist_params(params)

        data_matrix = params.get('data_matrix')
        metric = params.get('metric')
        if not metric:
            metric = 'euclidean'

        labels = data_matrix.get('row_ids')

        data = self._get_data(data_matrix)
        dist_matrix = dist.pdist(data, metric=metric)
        square_dist_matrix = dist.squareform(dist_matrix)

        returnVal = {'square_dist_matrix': square_dist_matrix,
                     'labels': labels}

        return returnVal

    def run_linkage(self, params):
        """
        run_linkage: a wrapper method for scipy.cluster.hierarchy.linkage
        reference:
        https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html

        square_dist_matrix - square form of distance matrix (refer to run_pdist return)

        Optional arguments:
        method - The linkage algorithm to use. Default set to 'ward'.
                 The method can be 
                 ["single", "complete", "average", "weighted", "centroid", "median", "ward"]
                 Details refer to: 
                 https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html

        return:
        linkage_matrix - The hierarchical clustering encoded as a linkage matrix
        """

        log('--->\nrunning run_linkage\n' +
            'params:\n{}'.format(json.dumps(params, indent=1)))

        self._validate_run_linkage_params(params)

        square_dist_matrix = params.get('square_dist_matrix')
        method = params.get('method')
        if not method:
            method = 'ward'

        linkage_matrix = hier.linkage(square_dist_matrix, method=method)

        returnVal = {'linkage_matrix': linkage_matrix}

        return returnVal

    def run_fcluster(self, params):
        """
        run_fcluster: a wrapper method for scipy.cluster.hierarchy.fcluster
        reference: 
        https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.fcluster.html

        linkage_matrix - hierarchical clustering linkage matrix (refer to run_linkage return)
        dist_threshold - the threshold to apply when forming flat clusters

        Optional arguments:
        labels - items corresponding to each linkage_matrix element 
                 (If labels are given, result flat_cluster will be mapped to element in labels.)
        criterion - The criterion to use in forming flat clusters. Default set to 'inconsistent'.
                    The criterion can be 
                    ["inconsistent", "distance", "maxclust"]
                    Note: Advanced criterion 'monocrit', 'maxclust_monocrit' in 
                    scipy.cluster.hierarchy.fcluster library are not implemented
                    Details refer to: 
                    https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.fcluster.html

        return:
        flat_cluster - A dictionary of flat clusters.
                       Each element of flat_cluster representing a cluster contains a label array. 
                      (If labels is none, element position array is returned to each cluster group)
        """

        log('--->\nrunning run_fcluster\n' +
            'params:\n{}'.format(json.dumps(params, indent=1)))

        self._validate_run_fcluster_params(params)

        linkage_matrix = params.get('linkage_matrix')
        dist_threshold = params.get('dist_threshold')
        criterion = params.get('criterion')
        if not criterion:
            criterion = 'inconsistent'
        labels = params.get('labels')

        fcluster = hier.fcluster(linkage_matrix, dist_threshold, criterion=criterion)

        if labels:
            flat_cluster = self._process_fcluster(fcluster, labels=labels)
        else:
            flat_cluster = self._process_fcluster(fcluster)

        returnVal = {'flat_cluster': flat_cluster}

        return returnVal
