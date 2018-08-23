import time
import numpy as np
import os
import errno
import uuid
import json
import fisher
import scipy.spatial.distance as dist
import scipy.cluster.hierarchy as hier
import scipy.cluster.vq as vq
from matplotlib import pyplot as plt
import pandas as pd

from Workspace.WorkspaceClient import Workspace as Workspace


def log(message, prefix_newline=False):
    time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(time.time()))
    print(('\n' if prefix_newline else '') + time_str + ': ' + message)


class KnowledgeEngineUtil:

    METRIC = ["braycurtis", "canberra", "chebyshev", "cityblock", "correlation", "cosine",
              "dice", "euclidean", "hamming", "jaccard", "kulsinski", "matching",
              "rogerstanimoto", "russellrao", "sokalmichener", "sokalsneath", "sqeuclidean",
              "yule"]

    METHOD = ["single", "complete", "average", "weighted", "centroid", "median", "ward"]

    CRITERION = ["inconsistent", "distance", "maxclust"]

    ONTOLOGY_HASH = None
    WEIGHTED_EDGES = None

    @classmethod
    def update_ontology_hash(cls, ontology_hash):
        cls.ONTOLOGY_HASH = ontology_hash

    @classmethod
    def update_weighted_edges(cls, weighted_edges):
        cls.WEIGHTED_EDGES = weighted_edges

    def _mkdir_p(self, path):
        """
        _mkdir_p: make directory for given path
        """
        if not path:
            return
        try:
            os.makedirs(path)
        except OSError as exc:
            if exc.errno == errno.EEXIST and os.path.isdir(path):
                pass
            else:
                raise

    def _validate_run_kmeans2_params(self, params):
        """
        _validate_run_kmeans2_params:
                validates params passed to run_kmeans2 method
        """

        log('start validating run_kmeans2 params')

        # check for required parameters
        for p in ['dist_matrix', 'k_num']:
            if p not in params:
                raise ValueError('"{}" parameter is required, but missing'.format(p))

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
        for p in ['dist_matrix']:
            if p not in params:
                raise ValueError('"{}" parameter is required, but missing'.format(p))

        # check method validation
        method = params.get('method')
        if method and method not in self.METHOD:
            error_msg = 'INPUT ERROR:\nInput linkage algorithm [{}] is not valid.\n'.format(
                                                                                        method)
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

        # check criterion validation
        criterion = params.get('criterion')
        if criterion and criterion not in self.CRITERION:
            error_msg = 'INPUT ERROR:\nInput criterion [{}] is not valid.\n'.format(criterion)
            error_msg += 'Available metric: {}'.format(self.CRITERION)
            raise ValueError(error_msg)

    def _validate_run_dendrogram_params(self, params):
        """
        _validate_run_dendrogram_params:
                validates params passed to run_dendrogram method
        """

        log('start validating run_dendrogram params')

        # check for required parameters
        for p in ['linkage_matrix']:
            if p not in params:
                raise ValueError('"{}" parameter is required, but missing'.format(p))

    def _validate_build_biclusters_params(self, params):
        """
        _validate_build_biclusters_params:
                validates params passed to build_biclusters method
        """

        log('start validating build_biclusters params')

        # check for required parameters
        for p in ['ndarray_ref', 'dist_threshold']:
            if p not in params:
                raise ValueError('"{}" parameter is required, but missing'.format(p))

        # check metric validation
        metric = params.get('dist_metric')
        if metric and metric not in self.METRIC:
            error_msg = 'INPUT ERROR:\nInput metric function [{}] is not valid.\n'.format(metric)
            error_msg += 'Available metric: {}'.format(self.METRIC)
            raise ValueError(error_msg)

        # check method validation
        method = params.get('linkage_method')
        if method and method not in self.METHOD:
            error_msg = 'INPUT ERROR:\nInput linkage algorithm [{}] is not valid.\n'.format(
                                                                                        method)
            error_msg += 'Available metric: {}'.format(self.METHOD)
            raise ValueError(error_msg)

        # check criterion validation
        criterion = params.get('fcluster_criterion')
        if criterion and criterion not in self.CRITERION:
            error_msg = 'INPUT ERROR:\nInput criterion [{}] is not valid.\n'.format(criterion)
            error_msg += 'Available metric: {}'.format(self.CRITERION)
            raise ValueError(error_msg)

    def _validate_enrich_onthology_params(self, params):
        """
        _validate_enrich_onthology_params:
                validates params passed to enrich_onthology method
        """
        log('start validating enrich_onthology params')

        # check for required parameters
        for p in ['sample_set', 'entity_term_set']:
            if p not in params:
                raise ValueError('"{}" parameter is required, but missing'.format(p))

    def _validate_calc_onthology_dist_params(self, params):
        """
        _validate_calc_onthology_dist_params:
                validates params passed to calc_onthology_dist method
        """
        log('start validating calc_onthology_dist params')

        # check for required parameters
        for p in ['onthology_set']:
            if p not in params:
                raise ValueError('"{}" parameter is required, but missing'.format(p))

        onthology_set = params.get('onthology_set')
        len_list = map(len, onthology_set.values())

        if set(len_list) != set([2]):
            error_msg = 'Input Error: one or more gene is associated with more than 2 GO terms'
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

    def _get_data(self, values):
        """
        _get_data: get data into a 2d array
        """

        data = np.nan_to_num(np.array(values))

        try:
            data = data.astype(float)
        except:
            error_msg = 'INVALID data_matrix:\n'
            error_msg += 'cannot convert all element to number:\n{}\n'.format(data)
            raise ValueError(error_msg)

        return data

    def _process_fcluster(self, fcluster, labels=None):
        """
        _process_fcluster: assign labels to corresponding cluster group
                           if labels is none, return element pos array in each cluster group
        """

        log('start assigning labels to clusters')

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

    def _add_distance(self, ddata):
        """
        _add_distance: Add distance and cluster count to dendrogram

        credit --
        Author: Jorn Hees
        https://joernhees.de/blog/2015/08/26/scipy-hierarchical-clustering-and-dendrogram-tutorial/#Eye-Candy
        """

        log('start adding distance to dendrogram')

        annotate_above = 10  # useful in small plots so annotations don't overlap
        for i, d, c in zip(ddata['icoord'], ddata['dcoord'], ddata['color_list']):
            x = 0.5 * sum(i[1:3])
            y = d[1]
            if y > annotate_above:
                plt.plot(x, y, 'o', c=c)
                plt.annotate("%.3g" % y, (x, y), xytext=(0, -5),
                             textcoords='offset points',
                             va='top', ha='center')

    def _process_ndarray_data(self, ndarray_ref):
        """
        _process_ndarray_data: process ndarray data

        return a dict with row_ids, col_ids and values
        """
        data_matrix = dict()

        ndarray_object = self.ws.get_objects2({'objects': [{'ref': ndarray_ref}]})['data'][0]

        ndarray_data = ndarray_object['data']
        dim_context = ndarray_data['dim_context']

        row_values = dim_context[0]['typed_values'][0]['values']
        row_scalar_type = row_values['scalar_type']
        row_values_key = '{}_values'.format(row_scalar_type)
        row_ids = row_values[row_values_key]

        col_values = dim_context[1]['typed_values'][0]['values']
        col_scalar_type = col_values['scalar_type']
        col_values_key = '{}_values'.format(col_scalar_type)
        col_ids = col_values[col_values_key]

        data_values = ndarray_data['typed_values']['values']
        data_values_scalar_type = data_values['scalar_type']
        data_values_key = '{}_values'.format(data_values_scalar_type)
        one_d_values = data_values[data_values_key]
        two_d_values = list()  # each element is an array representing 1 row values

        total_values = len(row_ids) * len(col_ids)
        if len(one_d_values) != total_values:
            raise ValueError('Expecting {} values but getting {}'.format(total_values,
                                                                         len(one_d_values)))

        col_size = len(col_ids)
        empty_string = ['NA', 'NULL', 'null', '', None, 'None', 'none']

        for row_count in range(len(row_ids)):
            start_pos = row_count * col_size
            end_pos = (row_count + 1) * col_size
            row_values = one_d_values[start_pos:end_pos]
            row_values = [0 if v in empty_string else v for v in row_values]
            two_d_values.append(map(float, row_values))

        data_matrix = {'row_ids': row_ids,
                       'col_ids': col_ids,
                       'values': two_d_values}

        return data_matrix

    def _build_flat_cluster(self, data_matrix, dist_threshold,
                            dist_metric=None, linkage_method=None, fcluster_criterion=None):

        """
        _build_cluster: build flat clusters of data_matrix with distance threshold
        """

        # calculate distance matrix
        pdist_params = {'data_matrix': data_matrix,
                        'metric': dist_metric}
        pdist_ret = self.run_pdist(pdist_params)

        dist_matrix = pdist_ret['dist_matrix']
        labels = pdist_ret['labels']

        # performs hierarchical/agglomerative clustering
        linkage_params = {'dist_matrix': dist_matrix,
                          'method': linkage_method}
        linkage_ret = self.run_linkage(linkage_params)

        linkage_matrix = linkage_ret['linkage_matrix']

        # generate flat clusters
        fcluster_params = {'linkage_matrix': linkage_matrix,
                           'dist_threshold': dist_threshold,
                           'labels': labels,
                           'criterion': fcluster_criterion}
        fcluster_ret = self.run_fcluster(fcluster_params)

        flat_cluster = fcluster_ret['flat_cluster']

        return flat_cluster

    def _process_entity_term_set(self, entity_term_set, propagation):
        """
        _process_entity_term_set: process entity_term_set and get global go_id: [genes_ids] map
        """
        go_id_gene_ids_list_map = dict()

        for gene_id, go_terms in entity_term_set.iteritems():
            for go_term in go_terms:
                if go_term in go_id_gene_ids_list_map:
                    gene_ids = go_id_gene_ids_list_map.get(go_term)
                    gene_ids.append(gene_id)
                    go_id_gene_ids_list_map.update({go_term: gene_ids})
                else:
                    go_id_gene_ids_list_map.update({go_term: [gene_id]})

        return go_id_gene_ids_list_map

    def _get_immediate_parents(self, ontology_hash, go_id,
                               is_a_relationship, regulates_relationship, part_of_relationship):
        """
        _get_immediate_parents: get immediate parents go_ids for a given go_id
        """
        parent_ids = []
        antology_info = ontology_hash.get(go_id)

        if antology_info:
            if is_a_relationship:
                is_a_parents = antology_info.get('is_a')
                if is_a_parents:
                    for parent_string in is_a_parents:
                        is_a_parent_id = parent_string.split('!')[0][:-1]
                        parent_ids.append(is_a_parent_id)

            if regulates_relationship:
                relationship = antology_info.get('relationship')
                if relationship:
                    for relationship_string in relationship:
                        if relationship_string.split(' ')[0] == 'regulates':
                            parent_ids.append(relationship_string.split(' ')[1])

            if part_of_relationship:
                relationship = antology_info.get('relationship')
                if relationship:
                    for relationship_string in relationship:
                        if relationship_string.split(' ')[0] == 'part_of':
                            parent_ids.append(relationship_string.split(' ')[1])

        return parent_ids

    def _fetch_all_parents_go_ids(self, ontology_hash, go_id,
                                  is_a_relationship, regulates_relationship,
                                  part_of_relationship):
        """
        _fetch_all_parents_go_ids: recusively fetch all parent go_ids
        """

        parent_ids = self._get_immediate_parents(ontology_hash, go_id,
                                                 is_a_relationship, regulates_relationship,
                                                 part_of_relationship)
        if parent_ids:
            grand_parent_ids = parent_ids
            for parent_id in parent_ids:
                grand_parent_ids += self._fetch_all_parents_go_ids(ontology_hash,
                                                                   parent_id,
                                                                   is_a_relationship,
                                                                   regulates_relationship,
                                                                   part_of_relationship)[parent_id]
            return {go_id: list(set(grand_parent_ids))}
        else:
            return {go_id: []}

    def _generate_parent_child_map(self, ontology_hash, go_ids,
                                   is_a_relationship=True,
                                   regulates_relationship=False,
                                   part_of_relationship=False):
        """
        _generate_parent_child_map: fetch parent go_ids for given go_id
        """

        log('start fetching parent go_ids')
        start = time.time()

        go_id_parent_ids_map = {}

        for go_id in go_ids:
            fetch_result = self._fetch_all_parents_go_ids(ontology_hash, go_id,
                                                          is_a_relationship,
                                                          regulates_relationship,
                                                          part_of_relationship)

            go_id_parent_ids_map.update(fetch_result)

        end = time.time()
        log('used {:.2f} s'.format(end - start))

        return go_id_parent_ids_map

    def _get_ontology_hash(self):
        """
        _get_ontology_hash: get global ontology info hash
        """

        log('getting ontology data from workspace')

        ontology_hash = dict()
        ontologies = self.ws.get_objects([{'workspace': 'KBaseOntology',
                                           'name': 'gene_ontology'},
                                          {'workspace': 'KBaseOntology',
                                           'name': 'plant_ontology'}])
        ontology_hash.update(ontologies[0]['data']['term_hash'])
        ontology_hash.update(ontologies[1]['data']['term_hash'])

        return ontology_hash

    def _process_parent_go_terms(self, go_id_gene_ids_list_map, ontology_hash):
        """
        _process_parent_go_terms: get go term parents and include parent gene_ids to all children
        """

        go_ids = go_id_gene_ids_list_map.keys()

        go_id_parent_ids_map = self._generate_parent_child_map(ontology_hash,
                                                               go_ids,
                                                               regulates_relationship=False)

        log('including parent feature id to go_id map')
        for go_id, parent_ids in go_id_parent_ids_map.iteritems():
            mapped_features = go_id_gene_ids_list_map.get(go_id)

            for parent_id in parent_ids:
                parent_mapped_features = go_id_gene_ids_list_map.get(parent_id)

                if not parent_mapped_features:
                    parent_mapped_features = []

                if mapped_features:
                    parent_mapped_features += mapped_features

                go_id_gene_ids_list_map.update({parent_id: list(set(parent_mapped_features))})

        log('removing parent go term not in original go terms')
        for go_id in go_id_gene_ids_list_map.keys():
            if go_id not in go_ids:
                del go_id_gene_ids_list_map[go_id]

    def _append_ontology_type(self, go_enrichment, ontology_hash):
        """
        _append_go_type: append ontology type info into go_enrichment dict
        """
        for go_id, enrich_info in go_enrichment.iteritems():
            if go_id in ontology_hash:
                namespace = ontology_hash[go_id]['namespace']
                enrich_info.update({'ontology_type': namespace.split("_")[1][0].upper()})
            else:
                enrich_info.update({'ontology_type': None})

    def _calculate_go_enrichment(self, go_id_gene_ids_list_map, feature_set_ids,
                                 total_feature_ids):
        """
        _calculate_go_enrichment: calcualte go enrichment
        """
        log('start calcualting go enrichment')

        go_enrichment = dict()

        for go_id, mapped_gene_ids in go_id_gene_ids_list_map.iteritems():
            # in feature_set matches go_id
            a = len([i for i in feature_set_ids if i in mapped_gene_ids])

            if a:
                # in feature_set doesn't match go_id
                b = len(feature_set_ids) - a
                # not in feature_set matches go_id
                total_count = len(mapped_gene_ids)
                c = total_count - a
                # not in feature_set doesn't match go_id
                d = len(total_feature_ids) - len(feature_set_ids) - c

                raw_p_value = fisher.pvalue(a, b, c, d).two_tail

                expected_count = int(round(total_count * raw_p_value))

                go_enrichment.update({go_id: {'p_value': raw_p_value,
                                              'total_count': total_count,
                                              'sample_count': a,
                                              'expected_count': expected_count}})

        return go_enrichment

    def _find_comone_parent(self, pair_go_terms):
        """
        _find_comone_parent: find common parent of pair_go_terms
        """

        start_term = pair_go_terms[0]
        end_term = pair_go_terms[1]

        if start_term == end_term:
            return start_term

        if self.ONTOLOGY_HASH:
            log('using cached ontology data')
            ontology_hash = self.ONTOLOGY_HASH
        else:
            log('loading ontology data')
            ontology_hash = self._get_ontology_hash()
            self.update_ontology_hash(ontology_hash)

        step = 0
        start_parents = {start_term: step}
        end_parents = {end_term: step}

        found_common_parent = False
        common_parent = list()
        pre_step_start_parent_ids = [start_term]
        pre_step_end_parent_ids = [end_term]

        while not found_common_parent:
            step += 1
            found_start_root = False
            found_end_root = False
            current_step_start_parent_ids = list()
            for pre_step_start_parent_id in pre_step_start_parent_ids:
                step_start_parent_ids = self._get_immediate_parents(ontology_hash,
                                                                    pre_step_start_parent_id,
                                                                    is_a_relationship=True,
                                                                    regulates_relationship=False,
                                                                    part_of_relationship=False)
                map(lambda parent_id: start_parents.update({parent_id: step}),
                    step_start_parent_ids)
                current_step_start_parent_ids += step_start_parent_ids
            if current_step_start_parent_ids:
                pre_step_start_parent_ids = current_step_start_parent_ids
            else:
                found_start_root = True

            current_step_end_parent_ids = list()
            for pre_step_end_parent_id in pre_step_end_parent_ids:
                step_end_parent_ids = self._get_immediate_parents(ontology_hash,
                                                                  pre_step_end_parent_id,
                                                                  is_a_relationship=True,
                                                                  regulates_relationship=False,
                                                                  part_of_relationship=False)
                map(lambda parent_id: end_parents.update({parent_id: step}),
                    step_end_parent_ids)
                current_step_end_parent_ids += step_end_parent_ids
            if current_step_end_parent_ids:
                pre_step_end_parent_ids = current_step_end_parent_ids
            else:
                found_end_root = True

            common_parent = [val for val in start_parents.keys() if val in end_parents.keys()]

            if common_parent or (found_start_root and found_end_root):
                found_common_parent = True

        if common_parent:
            return common_parent
        else:
            return None

    def _calc_weighted_pair_term_dist(self, pair_go_terms):
        """
        _calc_weighted_pair_term_dist: calculate weighted 2 nodes distance
        """

        log('start calculating GO term distance for {}'.format(pair_go_terms))

        start_term = pair_go_terms[0]
        end_term = pair_go_terms[1]

        if start_term == end_term:
            return 0

        if self.ONTOLOGY_HASH:
            log('using cached ontology data')
            ontology_hash = self.ONTOLOGY_HASH
        else:
            log('loading ontology data')
            ontology_hash = self._get_ontology_hash()
            self.update_ontology_hash(ontology_hash)

        if self.WEIGHTED_EDGES:
            log('using cached weighted edges data')
            weighted_edges = self.WEIGHTED_EDGES
        else:
            log('loading weighted edges data')
            weighted_edges = self._compute_weighted_edges()
            self.update_weighted_edges(weighted_edges)

        step = 0
        start_parents = {start_term: step}
        end_parents = {end_term: step}

        found_common_parent = False
        common_parent = list()
        pre_step_start_parent_ids = [start_term]
        pre_step_end_parent_ids = [end_term]
        found_start_root = False
        found_end_root = False

        while not found_common_parent:
            step += 1

            current_step_start_parent_ids = list()
            current_start_step_dist = dict()
            for pre_step_start_parent_id in pre_step_start_parent_ids:
                step_start_parent_ids = self._get_immediate_parents(ontology_hash,
                                                                    pre_step_start_parent_id,
                                                                    is_a_relationship=True,
                                                                    regulates_relationship=False,
                                                                    part_of_relationship=False)
                step_start_parent_ids = list(set(step_start_parent_ids))
                for step_start_parent_id in step_start_parent_ids:
                    weighted_edge = weighted_edges[step_start_parent_id][pre_step_start_parent_id]
                    current_weight = start_parents[pre_step_start_parent_id]
                    if step_start_parent_id in current_start_step_dist:
                        current_dist = current_start_step_dist[step_start_parent_id]
                        if current_dist > current_weight + weighted_edge:
                            current_start_step_dist.update({step_start_parent_id:
                                                            current_weight + weighted_edge})
                    else:
                        current_start_step_dist.update({step_start_parent_id:
                                                        current_weight + weighted_edge})
                current_step_start_parent_ids += step_start_parent_ids

            for step_start_parent_id, distance in current_start_step_dist.iteritems():
                start_parents.update({step_start_parent_id: distance})

            # print 'step: {}, start parents: {}'.format(step, start_parents)

            current_step_start_parent_ids = list(set(current_step_start_parent_ids))
            if current_step_start_parent_ids:
                pre_step_start_parent_ids = current_step_start_parent_ids
            else:
                found_start_root = True

            current_step_end_parent_ids = list()
            current_end_step_dist = dict()
            for pre_step_end_parent_id in pre_step_end_parent_ids:
                step_end_parent_ids = self._get_immediate_parents(ontology_hash,
                                                                  pre_step_end_parent_id,
                                                                  is_a_relationship=True,
                                                                  regulates_relationship=False,
                                                                  part_of_relationship=False)
                step_end_parent_ids = list(set(step_end_parent_ids))
                for step_end_parent_id in step_end_parent_ids:
                    weighted_edge = weighted_edges[step_end_parent_id][pre_step_end_parent_id]
                    current_weight = end_parents[pre_step_end_parent_id]
                    if step_end_parent_id in current_end_step_dist:
                        current_dist = current_end_step_dist[step_end_parent_id]
                        if current_dist > current_weight + weighted_edge:
                            current_end_step_dist.update({step_end_parent_id:
                                                          current_weight + weighted_edge})
                    else:
                        current_end_step_dist.update({step_end_parent_id:
                                                      current_weight + weighted_edge})
                current_step_end_parent_ids += step_end_parent_ids

            for step_end_parent_id, distance in current_end_step_dist.iteritems():
                end_parents.update({step_end_parent_id: distance})

            current_step_end_parent_ids = list(set(current_step_end_parent_ids))
            if current_step_end_parent_ids:
                pre_step_end_parent_ids = current_step_end_parent_ids
            else:
                found_end_root = True

            common_parent = [val for val in start_parents.keys() if val in end_parents.keys()]

            if common_parent or (found_start_root and found_end_root):
                found_common_parent = True

        if common_parent:

            if len(common_parent) == 1:
                start_dist = start_parents.get(common_parent[0])
                end_dist = end_parents.get(common_parent[0])
                dist = (start_dist + end_dist) / 2.0
            else:
                dist = 0
                for common_par in common_parent:
                    start_dist = start_parents.get(common_par)
                    end_dist = end_parents.get(common_par)
                    tmp_dist = (start_dist + end_dist) / 2.0
                    if not dist or (tmp_dist < dist):
                        dist = tmp_dist
        else:
            dist = float('inf')

        return dist

    def _calc_pair_term_dist(self, pair_go_terms):
        """
        _calc_pair_term_dist: calculate 2 nodes distance
        """

        log('start calculating GO term distance for {}'.format(pair_go_terms))

        start_term = pair_go_terms[0]
        end_term = pair_go_terms[1]

        if start_term == end_term:
            return 0

        if self.ONTOLOGY_HASH:
            log('using cached ontology data')
            ontology_hash = self.ONTOLOGY_HASH
        else:
            log('loading ontology data')
            ontology_hash = self._get_ontology_hash()
            self.update_ontology_hash(ontology_hash)

        step = 0
        start_parents = {start_term: step}
        end_parents = {end_term: step}

        found_common_parent = False
        common_parent = list()
        pre_step_start_parent_ids = [start_term]
        pre_step_end_parent_ids = [end_term]

        while not found_common_parent:
            step += 1
            found_start_root = False
            found_end_root = False
            current_step_start_parent_ids = list()
            for pre_step_start_parent_id in pre_step_start_parent_ids:
                step_start_parent_ids = self._get_immediate_parents(ontology_hash,
                                                                    pre_step_start_parent_id,
                                                                    is_a_relationship=True,
                                                                    regulates_relationship=False,
                                                                    part_of_relationship=False)
                map(lambda parent_id: start_parents.update({parent_id: step}),
                    step_start_parent_ids)
                current_step_start_parent_ids += step_start_parent_ids
            if current_step_start_parent_ids:
                pre_step_start_parent_ids = current_step_start_parent_ids
            else:
                found_start_root = True

            current_step_end_parent_ids = list()
            for pre_step_end_parent_id in pre_step_end_parent_ids:
                step_end_parent_ids = self._get_immediate_parents(ontology_hash,
                                                                  pre_step_end_parent_id,
                                                                  is_a_relationship=True,
                                                                  regulates_relationship=False,
                                                                  part_of_relationship=False)
                map(lambda parent_id: end_parents.update({parent_id: step}),
                    step_end_parent_ids)
                current_step_end_parent_ids += step_end_parent_ids
            if current_step_end_parent_ids:
                pre_step_end_parent_ids = current_step_end_parent_ids
            else:
                found_end_root = True

            common_parent = [val for val in start_parents.keys() if val in end_parents.keys()]

            if common_parent or (found_start_root and found_end_root):
                found_common_parent = True

        if common_parent:
            start_dist = start_parents.get(common_parent[0])
            end_dist = end_parents.get(common_parent[0])
            dist = start_dist + end_dist
        else:
            dist = float('inf')

        return dist

    def _compute_weighted_edges(self):
        """
        _compute_top_down_tree: given nodes only knows immediate parents, computes top to down
                                tree
        """

        log('generating weighted edges')

        if self.ONTOLOGY_HASH:
            log('using cached ontology data')
            ontology_hash = self.ONTOLOGY_HASH
        else:
            log('loading ontology data')
            ontology_hash = self._get_ontology_hash()
            self.update_ontology_hash(ontology_hash)

        root_terms = list()
        weighted_edges = dict()

        for ontology_term in ontology_hash.keys():
            parent_terms = self._get_immediate_parents(ontology_hash, ontology_term,
                                                       is_a_relationship=True,
                                                       regulates_relationship=False,
                                                       part_of_relationship=False)
            if parent_terms:
                for parent_term in parent_terms:
                    if parent_term in weighted_edges:
                        temp_children = weighted_edges[parent_term]
                        temp_children.update({ontology_term: 1})
                    else:
                        weighted_edges.update({parent_term: {ontology_term: 1}})
            else:
                root_terms.append(ontology_term)

        true_root_terms = list()
        for root_term in root_terms:
            if root_term in weighted_edges:
                true_root_terms.append(root_term)

        for root_term in true_root_terms:
            self._update_weighted_edges(weighted_edges, root_term, 1.0)

        return weighted_edges

    def _update_weighted_edges(self, weighted_edges, parent_term, weight):
        """
        _update_weighted_edges: update children term weight
        """

        children = weighted_edges[parent_term].keys()

        for child in children:
            if child not in weighted_edges:
                weighted_edges[parent_term][child] = weight / 2.0
            else:
                weighted_edges[parent_term][child] = weight / 2.0
                self._update_weighted_edges(weighted_edges, child, weight / 2.0)

    def __init__(self, config):
        self.ws_url = config["workspace-url"]
        self.token = config['KB_AUTH_TOKEN']
        self.shock_url = config['shock-url']
        self.srv_wiz_url = config['srv-wiz-url']
        self.scratch = config['scratch']

        self.ws = Workspace(self.ws_url, token=self.token)

    def run_kmeans2(self, params):
        """
        run_kmeans2: a wrapper method for  scipy.cluster.vq.kmeans2
        reference:
        https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.vq.kmeans2.html#scipy.cluster.vq.kmeans2

        dist_matrix: a condensed distance matrix
        k_num: number of clusters to form

        return:
        centroid: centroids found at the last iteration of k-means
        idx - index of the centroid
        """

        log('--->\nrunning run_kmeans2\n')

        self._validate_run_kmeans2_params(params)

        dist_matrix = params.get('dist_matrix')
        k_num = params.get('k_num')

        try:
            k_num = int(k_num)
        except:
            raise ValueError('[k_num] must be a integer or integer string')

        dist_squareform = dist.squareform(dist_matrix)

        centroid, idx = vq.kmeans2(dist_squareform, k_num, minit='points')

        returnVal = {'centroid': centroid.tolist(),
                     'idx': idx.tolist()}

        return returnVal

    def run_pdist(self, params):
        """
        run_pdist: a wrapper method for scipy.spatial.distance.pdist
        reference:
        https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.pdist.html

        data_matrix - raw data matrix in json format
                      e.g.{u'condition_1': {u'gene_1': 0.1, u'gene_2': 0.3, u'gene_3': None},
                           u'condition_2': {u'gene_1': 0.2, u'gene_2': 0.4, u'gene_3': None},
                           u'condition_3': {u'gene_1': 0.3, u'gene_2': 0.5, u'gene_3': None},
                           u'condition_4': {u'gene_1': 0.4, u'gene_2': 0.6, u'gene_3': None}}

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
        dist_matrix - a condensed distance matrix
        labels - item name corresponding to each dist_matrix element
        """

        log('--->\nrunning run_pdist\n')

        self._validate_run_pdist_params(params)

        data_matrix = params.get('data_matrix')
        metric = params.get('metric')
        if not metric:
            metric = 'euclidean'

        df = pd.read_json(data_matrix)
        labels = df.index.tolist()
        values = df.values.tolist()

        data = self._get_data(values)
        log('start computing distance matrix')
        dist_matrix = dist.pdist(data, metric=metric).tolist()
        log('finished computing distance matrix')

        returnVal = {'dist_matrix': dist_matrix,
                     'labels': labels}

        return returnVal

    def run_linkage(self, params):
        """
        run_linkage: a wrapper method for scipy.cluster.hierarchy.linkage
        reference:
        https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html

        dist_matrix - 1D distance matrix (refer to run_pdist return)

        Optional arguments:
        method - The linkage algorithm to use. Default set to 'ward'.
                 The method can be
                 ["single", "complete", "average", "weighted", "centroid", "median", "ward"]
                 Details refer to:
                 https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html

        return:
        linkage_matrix - The hierarchical clustering encoded as a linkage matrix
        """

        log('--->\nrunning run_linkage\n')

        self._validate_run_linkage_params(params)

        dist_matrix = params.get('dist_matrix')
        method = params.get('method')
        if not method:
            method = 'ward'

        log('start computing linkage matrix')
        linkage_matrix = hier.linkage(dist_matrix, method=str(method)).tolist()
        log('finished computing linkage matrix')

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
        criterion - The criterion to use in forming flat clusters. Default set to 'distance'.
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

        log('--->\nrunning run_fcluster\n')

        self._validate_run_fcluster_params(params)

        linkage_matrix = params.get('linkage_matrix')
        dist_threshold = params.get('dist_threshold')
        criterion = params.get('criterion')
        if not criterion:
            criterion = 'distance'
        labels = params.get('labels')

        log('start computing flat clusters')
        fcluster = hier.fcluster(linkage_matrix, dist_threshold, criterion=criterion)

        if labels:
            flat_cluster = self._process_fcluster(fcluster, labels=labels)
        else:
            flat_cluster = self._process_fcluster(fcluster)

        log('finished computing flat clusters')

        returnVal = {'flat_cluster': flat_cluster}

        return returnVal

    def run_dendrogram(self, params):
        """
        run_dendrogram: a wrapper method for scipy.cluster.hierarchy.dendrogram
        reference:
        https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.dendrogram.html

        linkage_matrix - hierarchical clustering linkage matrix (refer to run_linkage return)

        Optional arguments:
        dist_threshold - the threshold to apply when forming flat clusters
                         (draw a horizontal line to dendrogram)
        labels - items corresponding to each linkage_matrix element
                (If labels are given, result dendrogram x-axis will be mapped to element in labels)
        last_merges - show only last given value merged clusters

        return:
        result_plots - List of result plot path(s)
        """

        log('--->\nrunning run_dendrogram\n')

        self._validate_run_dendrogram_params(params)

        plt.switch_backend('agg')

        result_plots = list()
        output_directory = os.path.join(self.scratch, str(uuid.uuid4()))
        self._mkdir_p(output_directory)
        plot_file = os.path.join(output_directory, 'dendrogram.png')

        linkage_matrix = params.get('linkage_matrix')
        dist_threshold = params.get('dist_threshold')
        labels = params.get('labels')
        last_merges = params.get('last_merges')

        plt.figure(figsize=(25, 10))
        plt.ylabel('distance')

        if last_merges:
            plt.title('Hierarchical Clustering Dendrogram (truncated)')
            plt.xlabel('cluster size')
            ddata = hier.dendrogram(linkage_matrix,
                                    leaf_rotation=90.,
                                    leaf_font_size=8.,
                                    show_leaf_counts=True,
                                    labels=labels,
                                    truncate_mode='lastp',
                                    p=last_merges,
                                    show_contracted=True)
        else:
            plt.title('Hierarchical Clustering Dendrogram')
            if labels:
                plt.xlabel('sample labels')
            else:
                plt.xlabel('sample index')
            ddata = hier.dendrogram(linkage_matrix,
                                    leaf_rotation=90.,
                                    leaf_font_size=8.,
                                    show_leaf_counts=True,
                                    labels=labels)

        self._add_distance(ddata)

        if dist_threshold:
            plt.axhline(y=dist_threshold, c='k')

        plt.savefig(plot_file)
        result_plots.append(plot_file)

        returnVal = {'result_plots': result_plots}

        return returnVal

    def build_biclusters(self, params):
        """
        build_biclusters: build biclusters and store result feature sets as JSON into shock

        ndarray_ref: NDArray object reference
        dist_threshold: the threshold to apply when forming flat clusters

        Optional arguments:
        dist_metric: The distance metric to use. Default set to 'euclidean'.
                     The distance function can be
                     ["braycurtis", "canberra", "chebyshev", "cityblock", "correlation", "cosine",
                      "dice", "euclidean", "hamming", "jaccard", "kulsinski", "matching",
                      "rogerstanimoto", "russellrao", "sokalmichener", "sokalsneath",
                      "sqeuclidean", "yule"]
                     Details refer to:
                     https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.pdist.html

        linkage_method: The linkage algorithm to use. Default set to 'ward'.
                        The method can be
                        ["single", "complete", "average", "weighted", "centroid", "median", "ward"]
                        Details refer to:
                        https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html

        fcluster_criterion: The criterion to use in forming flat clusters.
                            Default set to 'inconsistent'.
                            The criterion can be
                            ["inconsistent", "distance", "maxclust"]
                            Details refer to:
                            https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.fcluster.html

        return:
        biclusters: list of biclusters
                    e.g. [["gene_id_1", "gene_id_2"], ["gene_id_3"]]
        """

        log('--->\nrunning build_biclusters\n' +
            'params:\n{}'.format(json.dumps(params, indent=1)))

        self._validate_build_biclusters_params(params)

        ndarray_ref = params.get('ndarray_ref')
        dist_threshold = params.get('dist_threshold')

        dist_metric = params.get('dist_metric')
        linkage_method = params.get('linkage_method')
        fcluster_criterion = params.get('fcluster_criterion')

        data_matrix = self._process_ndarray_data(ndarray_ref)
        flat_cluster = self._build_flat_cluster(data_matrix, dist_threshold,
                                                dist_metric=dist_metric,
                                                linkage_method=linkage_method,
                                                fcluster_criterion=fcluster_criterion)
        biclusters = flat_cluster.values()

        returnVal = {'biclusters': biclusters}

        return returnVal

    def enrich_onthology(self, params):
        """
        enrich_onthology: run GO term enrichment analysis

        sample_set: list of gene_ids in clustering
                    e.g. ["gene_id_1", "gene_id_2", "gene_id_3"]
        entity_term_set: entity terms dict structure where global GO term and gene_ids are stored
                         e.g. {'gene_id_1': ['go_term_1', 'go_term_2']}

        Optional arguments:
        propagation: includes is_a relationship to all go terms (default is 0)

        return:
        enrichment_profile: dict structure stores enrichment info
                            e.g. {"go_term_1": {"sample_count": 10,
                                                "total_count": 20,
                                                "p_value": 0.1,
                                                "ontology_type": "P"}}
        """

        log('--->\nrunning enrich_onthology')

        self._validate_enrich_onthology_params(params)

        sample_set = params.get('sample_set')
        entity_term_set = params.get('entity_term_set')
        propagation = params.get('propagation', False)

        go_id_gene_ids_list_map = self._process_entity_term_set(entity_term_set, propagation)

        if self.ONTOLOGY_HASH:
            log('using cached ontology data')
            ontology_hash = self.ONTOLOGY_HASH
        else:
            log('loading ontology data')
            ontology_hash = self._get_ontology_hash()
            self.update_ontology_hash(ontology_hash)

        if propagation:
            self._process_parent_go_terms(go_id_gene_ids_list_map, ontology_hash)

        enrichment_profile = self._calculate_go_enrichment(go_id_gene_ids_list_map,
                                                           sample_set,
                                                           entity_term_set.keys())

        self._append_ontology_type(enrichment_profile, ontology_hash)

        returnVal = {'enrichment_profile': enrichment_profile}

        return returnVal

    def calc_onthology_dist(self, params):
        """
        enrich_onthology: calculate onthology distance
                          (sum of steps for each node in onthology_pair travels to
                           the nearest common ancestor node)
                          NOTE: return inf if no common ancestor node found

        onthology_set: dict structure stores mapping of gene_id to paried onthology
                       e.g. {"gene_id_1": ["go_term_1", "go_term_2"]}

        return:
        onthology_dist_set: dict structure stores mapping of gene_id to dist
                            e.g. {"gene_id_1": 3}
        """

        log('--->\nrunning calc_onthology_dist')

        self._validate_calc_onthology_dist_params(params)

        onthology_set = params.get('onthology_set')

        onthology_dist_set = dict()
        for gene_id, pair_go_terms in onthology_set.iteritems():
            dist = self._calc_pair_term_dist(pair_go_terms)
            onthology_dist_set.update({gene_id: dist})

        returnVal = {'onthology_dist_set': onthology_dist_set}

        return returnVal

    def calc_weighted_onthology_dist(self, params):
        """
        enrich_onthology: calculate weighted onthology distance
                          (edges are weighted from root to leaves
                           root edges are weighted 1/2
                           each child's edge weights half of its parent's edge)
                          NOTE: return inf if no common ancestor node found

        onthology_set: dict structure stores mapping of gene_id to paried onthology
                       e.g. {"gene_id_1": ["go_term_1", "go_term_2"]}

        return:
        onthology_dist_set: dict structure stores mapping of gene_id to dist
                            e.g. {"gene_id_1": 0.75}
        """

        log('--->\nrunning calc_weighted_onthology_dist')

        self._validate_calc_onthology_dist_params(params)

        onthology_set = params.get('onthology_set')

        onthology_dist_set = dict()
        for gene_id, pair_go_terms in onthology_set.iteritems():
            common_parents = self._find_comone_parent(pair_go_terms)
            if common_parents:
                dist = 0
                for common_parent in common_parents:
                    start_go_term = pair_go_terms[0]
                    end_go_term = pair_go_terms[1]
                    start_dist = self._calc_weighted_pair_term_dist([start_go_term,
                                                                     common_parent])
                    end_dist = self._calc_weighted_pair_term_dist([end_go_term, common_parent])
                    tmp_dist = start_dist + end_dist
                    if not dist or (tmp_dist < dist):
                        dist = tmp_dist
                onthology_dist_set.update({gene_id: dist})
            else:
                onthology_dist_set.update({gene_id: float('inf')})

        returnVal = {'onthology_dist_set': onthology_dist_set}

        return returnVal
