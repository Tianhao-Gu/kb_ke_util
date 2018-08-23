# -*- coding: utf-8 -*-
import unittest
import os  # noqa: F401
import json  # noqa: F401
import time
import requests  # noqa: F401
import inspect


from os import environ
try:
    from ConfigParser import ConfigParser  # py2
except:
    from configparser import ConfigParser  # py3

from pprint import pprint  # noqa: F401

from biokbase.workspace.client import Workspace as workspaceService
from kb_ke_util.kb_ke_utilImpl import kb_ke_util
from kb_ke_util.kb_ke_utilServer import MethodContext
from kb_ke_util.authclient import KBaseAuth as _KBaseAuth
from DataFileUtil.DataFileUtilClient import DataFileUtil
from kb_ke_util.Utils.KnowledgeEngineUtil import KnowledgeEngineUtil


class kb_ke_utilTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.token = environ.get('KB_AUTH_TOKEN', None)
        config_file = environ.get('KB_DEPLOYMENT_CONFIG', None)
        cls.cfg = {}
        config = ConfigParser()
        config.read(config_file)
        for nameval in config.items('kb_ke_util'):
            cls.cfg[nameval[0]] = nameval[1]
        # Getting username from Auth profile for token
        authServiceUrl = cls.cfg['auth-service-url']
        auth_client = _KBaseAuth(authServiceUrl)
        user_id = auth_client.get_user(cls.token)
        # WARNING: don't call any logging methods on the context object,
        # it'll result in a NoneType error
        cls.ctx = MethodContext(None)
        cls.ctx.update({'token': cls.token,
                        'user_id': user_id,
                        'provenance': [
                            {'service': 'kb_ke_util',
                             'method': 'please_never_use_it_in_production',
                             'method_params': []
                             }],
                        'authenticated': 1})
        cls.shockURL = cls.cfg['shock-url']
        cls.wsURL = cls.cfg['workspace-url']
        cls.wsClient = workspaceService(cls.wsURL)
        cls.serviceImpl = kb_ke_util(cls.cfg)
        cls.scratch = cls.cfg['scratch']
        cls.callback_url = os.environ['SDK_CALLBACK_URL']

        cls.dfu = DataFileUtil(cls.callback_url)
        cls.cfg['KB_AUTH_TOKEN'] = cls.token
        cls.ke_util = KnowledgeEngineUtil(cls.cfg)

        suffix = int(time.time() * 1000)
        cls.wsName = "test_kb_ke_apps_" + str(suffix)
        cls.wsClient.create_workspace({'workspace': cls.wsName})

        cls.nodes_to_delete = []
        cls.prepare_data()

    @classmethod
    def tearDownClass(cls):
        if hasattr(cls, 'wsName'):
            cls.wsClient.delete_workspace({'workspace': cls.wsName})
            print('Test workspace was deleted')
        if hasattr(cls, 'nodes_to_delete'):
            for node in cls.nodes_to_delete:
                cls.delete_shock_node(node)

    @classmethod
    def delete_shock_node(cls, node_id):
        header = {'Authorization': 'Oauth {0}'.format(cls.token)}
        requests.delete(cls.shockURL + '/node/' + node_id, headers=header,
                        allow_redirects=True)
        print('Deleted shock node ' + node_id)

    @classmethod
    def prepare_data(cls):
        # upload ndarray object
        workspace_id = cls.dfu.ws_name_to_id(cls.wsName)
        object_type = 'KBaseGenerics.NDArray'
        ndarray_object_name = 'test_ndarray'
        ndarray_data = {'dim_context': [{'typed_values': [{'values': {'scalar_type': 'string',
                                                                      'string_values': ['gene_id_1',
                                                                                        'gene_id_2',
                                                                                        'gene_id_3']},
                                                           'value_type': {'term_name': 'gene ids'}}],
                                         'size': 3,
                                         'data_type': {'term_name': 'gene ids'}},
                                        {'typed_values': [{'values': {'scalar_type': 'string',
                                                                      'string_values': ['condition_1',
                                                                                        'condition_2',
                                                                                        'condition_3',
                                                                                        'condition_4']},
                                                           'value_type': {'term_name': 'conditions'}}],
                                         'size': 4,
                                         'data_type': {'term_name': 'conditions'}}],
                        'typed_values': {'values': {'scalar_type': 'float',
                                                    'float_values': [0.1, 0.2, 0.3, 0.4,
                                                                     0.3, 0.4, 0.5, 0.6,
                                                                     0.5, 0.6, 0.7, 0.8]},
                                         'value_type': {'term_name': 'data values'}},
                        'name': 'test_name',
                        'description': 'test_ndarray',
                        'data_type': {'term_name': 'test ndarray'},
                        'n_dimensions': 2}
        save_object_params = {
            'id': workspace_id,
            'objects': [{'type': object_type,
                         'data': ndarray_data,
                         'name': ndarray_object_name}]
        }

        dfu_oi = cls.dfu.save_objects(save_object_params)[0]
        cls.ndarray_ref = str(dfu_oi[6]) + '/' + str(dfu_oi[0]) + '/' + str(dfu_oi[4])

        # ci env object
        # cls.ndarray_ref = '25895/6/1'
        # cls.ndarray_ref = '25895/5/1'

    def getWsClient(self):
        return self.__class__.wsClient

    def getWsName(self):
        return self.__class__.wsName

    def getImpl(self):
        return self.__class__.serviceImpl

    def getContext(self):
        return self.__class__.ctx

    def start_test(self):
        testname = inspect.stack()[1][3]
        print('\n*** starting test: ' + testname + ' **')

    def fail_run_kmeans2(self, params, error, exception=ValueError, contains=False):
        with self.assertRaises(exception) as context:
            self.getImpl().run_kmeans2(self.ctx, params)
        if contains:
            self.assertIn(error, str(context.exception.message))
        else:
            self.assertEqual(error, str(context.exception.message))

    def fail_run_pdist(self, params, error, exception=ValueError, contains=False):
        with self.assertRaises(exception) as context:
            self.getImpl().run_pdist(self.ctx, params)
        if contains:
            self.assertIn(error, str(context.exception.message))
        else:
            self.assertEqual(error, str(context.exception.message))

    def fail_run_linkage(self, params, error, exception=ValueError, contains=False):
        with self.assertRaises(exception) as context:
            self.getImpl().run_linkage(self.ctx, params)
        if contains:
            self.assertIn(error, str(context.exception.message))
        else:
            self.assertEqual(error, str(context.exception.message))

    def fail_run_fcluster(self, params, error, exception=ValueError, contains=False):
        with self.assertRaises(exception) as context:
            self.getImpl().run_fcluster(self.ctx, params)
        if contains:
            self.assertIn(error, str(context.exception.message))
        else:
            self.assertEqual(error, str(context.exception.message))

    def fail_run_dendrogram(self, params, error, exception=ValueError, contains=False):
        with self.assertRaises(exception) as context:
            self.getImpl().run_fcluster(self.ctx, params)
        if contains:
            self.assertIn(error, str(context.exception.message))
        else:
            self.assertEqual(error, str(context.exception.message))

    def fail_build_biclusters(self, params, error, exception=ValueError, contains=False):
        with self.assertRaises(exception) as context:
            self.getImpl().build_biclusters(self.ctx, params)
        if contains:
            self.assertIn(error, str(context.exception.message))
        else:
            self.assertEqual(error, str(context.exception.message))

    def fail_enrich_onthology(self, params, error, exception=ValueError, contains=False):
        with self.assertRaises(exception) as context:
            self.getImpl().enrich_onthology(self.ctx, params)
        if contains:
            self.assertIn(error, str(context.exception.message))
        else:
            self.assertEqual(error, str(context.exception.message))

    def fail_calc_onthology_dist(self, params, error, exception=ValueError, contains=False):
        with self.assertRaises(exception) as context:
            self.getImpl().calc_onthology_dist(self.ctx, params)
        if contains:
            self.assertIn(error, str(context.exception.message))
        else:
            self.assertEqual(error, str(context.exception.message))

    def check_run_pdist_output(self, ret):
        self.assertTrue('dist_matrix' in ret)
        self.assertTrue('labels' in ret)

    def check_run_kmeans2_output(self, ret):
        self.assertTrue('centroid' in ret)
        self.assertTrue('idx' in ret)

    def check_run_linkage_output(self, ret):
        self.assertTrue('linkage_matrix' in ret)

    def check_run_fcluster_output(self, ret):
        self.assertTrue('flat_cluster' in ret)

    def check_run_dendrogram_output(self, ret):
        self.assertTrue('result_plots' in ret)

    def check_build_biclusters_output(self, ret, expect_gene_ids):
        self.assertTrue('biclusters' in ret)

        gene_ids = list()
        biclusters = ret['biclusters']
        for bicluster in biclusters:
            gene_ids += bicluster

        self.assertItemsEqual(gene_ids, expect_gene_ids)

    def check_enrich_onthology_output(self, ret, expect_go_ids):
        self.assertTrue('enrichment_profile' in ret)

        enrichment_profile = ret['enrichment_profile']
        self.assertItemsEqual(enrichment_profile.keys(), expect_go_ids)

    def check_calc_onthology_dist_output(self, ret, expect_steps):
        self.assertTrue('onthology_dist_set' in ret)

        onthology_dist_set = ret['onthology_dist_set']
        self.assertItemsEqual(onthology_dist_set, expect_steps)

    def test_bad_run_kmeans2_params(self):
        self.start_test()
        invalidate_params = {'missing_dist_matrix': 'dist_matrix',
                             'k_num': 'k_num'}
        error_msg = '"dist_matrix" parameter is required, but missing'
        self.fail_run_kmeans2(invalidate_params, error_msg)

        invalidate_params = {'dist_matrix': 'dist_matrix',
                             'missing_k_num': 'k_num'}
        error_msg = '"k_num" parameter is required, but missing'
        self.fail_run_kmeans2(invalidate_params, error_msg)

    def test_run_kmeans2(self):
        self.start_test()

        dist_matrix = [10.0, 1.0, 1.0, 1.0, 1.0, 1.0]
        k_num = 2

        params = {'dist_matrix': dist_matrix,
                  'k_num': k_num}
        ret = self.getImpl().run_kmeans2(self.ctx, params)[0]
        self.check_run_kmeans2_output(ret)
        idx = ret.get('idx')
        self.assertEqual(len(idx), 4)
        self.assertIn(idx.count(0), [1, 3])
        self.assertIn(idx.count(1), [1, 3])

    def test_bad_run_pdist_params(self):
        self.start_test()
        invalidate_params = {'missing_data_matrix': 'data_matrix'}
        error_msg = '"data_matrix" parameter is required, but missing'
        self.fail_run_pdist(invalidate_params, error_msg)

        invalidate_params = {'data_matrix': {'row_ids': 'row_ids',
                                             'col_ids': 'col_ids',
                                             'values': 'values'},
                             'metric': 'invalidate_metric'}
        error_msg = 'INPUT ERROR:\nInput metric function [invalidate_metric] is not valid.\n'
        self.fail_run_pdist(invalidate_params, error_msg, contains=True)

    def test_bad_data_matrix(self):

        data_matrix = """
            {"condition_1":{"gene_1":"a","gene_2":0.3,"gene_3":null},
             "condition_2":{"gene_1":0.2,"gene_2":0.4,"gene_3":null},
             "condition_3":{"gene_1":0.3,"gene_2":0.5,"gene_3":null},
             "condition_4":{"gene_1":0.4,"gene_2":0.6,"gene_3":null}}
        """

        params = {'data_matrix': data_matrix}
        error_msg = "INVALID data_matrix:\ncannot convert all element to number:"
        self.fail_run_pdist(params, error_msg, contains=True)

    def test_run_pdist(self):
        self.start_test()

        data_matrix = """
            {"condition_1":{"gene_1":0.1,"gene_2":0.3,"gene_3":null},
             "condition_2":{"gene_1":0.2,"gene_2":0.4,"gene_3":null},
             "condition_3":{"gene_1":0.3,"gene_2":0.5,"gene_3":null},
             "condition_4":{"gene_1":0.4,"gene_2":0.6,"gene_3":null}}
        """
        # data_matrix = json.loads(json_str)
        params = {'data_matrix': data_matrix}
        ret = self.getImpl().run_pdist(self.ctx, params)[0]
        self.check_run_pdist_output(ret)

    def test_bad_run_linkage_params(self):
        self.start_test()
        invalidate_params = {'missing_dist_matrix': 'dist_matrix'}
        error_msg = '"dist_matrix" parameter is required, but missing'
        self.fail_run_linkage(invalidate_params, error_msg)

        invalidate_params = {'dist_matrix': 'dist_matrix',
                             'method': 'invalidate_method'}
        error_msg = "INPUT ERROR:\nInput linkage algorithm [invalidate_method] is not valid.\n"
        self.fail_run_linkage(invalidate_params, error_msg, contains=True)

    def test_run_linkage(self):
        self.start_test()

        dist_matrix = [0, 0.34641016, 0.69282032]
        params = {'dist_matrix': dist_matrix}
        ret = self.getImpl().run_linkage(self.ctx, params)[0]
        self.check_run_linkage_output(ret)

    def test_bad_run_fcluster_params(self):
        self.start_test()
        invalidate_params = {'missing_linkage_matrix': 'linkage_matrix',
                             'dist_threshold': 'dist_threshold'}
        error_msg = '"linkage_matrix" parameter is required, but missing'
        self.fail_run_fcluster(invalidate_params, error_msg)

        invalidate_params = {'linkage_matrix': 'linkage_matrix',
                             'missing_dist_threshold': 'dist_threshold'}
        error_msg = '"dist_threshold" parameter is required, but missing'
        self.fail_run_fcluster(invalidate_params, error_msg)

        invalidate_params = {'linkage_matrix': 'linkage_matrix',
                             'dist_threshold': 'dist_threshold',
                             'criterion': 'invalidate_criterion'}
        error_msg = "INPUT ERROR:\nInput criterion [invalidate_criterion] is not valid.\n"
        self.fail_run_fcluster(invalidate_params, error_msg, contains=True)

    def test_run_fcluster(self):
        self.start_test()
        linkage_matrix = [[1.0, 2.0, 0.6, 2.0],
                          [0.0, 3.0, 0.87177978, 3.0]]
        params = {'linkage_matrix': linkage_matrix,
                  'dist_threshold': 0.7,
                  'labels': ['gene_1', 'gene_2', 'gene_3']}
        ret = self.getImpl().run_fcluster(self.ctx, params)[0]
        self.check_run_fcluster_output(ret)

    def test_bad_run_dendrogram_params(self):
        self.start_test()
        invalidate_params = {'missing_linkage_matrix': 'linkage_matrix'}
        error_msg = '"linkage_matrix" parameter is required, but missing'
        self.fail_run_dendrogram(invalidate_params, error_msg)

    def test_run_dendrogram(self):
        self.start_test()
        linkage_matrix = [[1.0, 2.0, 0.6, 2.0],
                          [0.0, 3.0, 0.87177978, 3.0]]
        params = {'linkage_matrix': linkage_matrix,
                  'dist_threshold': 0.7,
                  'labels': ['gene_1', 'gene_2', 'gene_3'],
                  'last_merges': 2}
        ret = self.getImpl().run_dendrogram(self.ctx, params)[0]
        self.check_run_dendrogram_output(ret)

    def test_bad_build_biclusters_params(self):
        self.start_test()
        invalidate_params = {'missing_ndarray_ref': 'ndarray_ref',
                             'dist_threshold': 'dist_threshold'}
        error_msg = '"ndarray_ref" parameter is required, but missing'
        self.fail_build_biclusters(invalidate_params, error_msg)

        invalidate_params = {'ndarray_ref': 'ndarray_ref',
                             'missing_dist_threshold': 'dist_threshold'}
        error_msg = '"dist_threshold" parameter is required, but missing'
        self.fail_build_biclusters(invalidate_params, error_msg)

        invalidate_params = {'ndarray_ref': 'ndarray_ref',
                             'dist_threshold': 'dist_threshold',
                             'dist_metric': 'invalidate_metric'}
        error_msg = 'INPUT ERROR:\nInput metric function [invalidate_metric] is not valid.\n'
        self.fail_build_biclusters(invalidate_params, error_msg, contains=True)

        invalidate_params = {'ndarray_ref': 'ndarray_ref',
                             'dist_threshold': 'dist_threshold',
                             'linkage_method': 'invalidate_method'}
        error_msg = "INPUT ERROR:\nInput linkage algorithm [invalidate_method] is not valid.\n"
        self.fail_build_biclusters(invalidate_params, error_msg, contains=True)

        invalidate_params = {'ndarray_ref': 'ndarray_ref',
                             'dist_threshold': 'dist_threshold',
                             'fcluster_criterion': 'invalidate_criterion'}
        error_msg = "INPUT ERROR:\nInput criterion [invalidate_criterion] is not valid.\n"
        self.fail_build_biclusters(invalidate_params, error_msg, contains=True)

    @unittest.skip("build_biclusters skipping")
    def test_build_biclusters(self):
        self.start_test()
        params = {'ndarray_ref': self.ndarray_ref,
                  'dist_threshold': 1}
        ret = self.getImpl().build_biclusters(self.ctx, params)[0]
        self.check_build_biclusters_output(ret, ['gene_id_1', 'gene_id_2', 'gene_id_3'])

        params = {'ndarray_ref': self.ndarray_ref,
                  'dist_threshold': 1,
                  'dist_metric': 'cityblock',
                  'linkage_method': 'ward',
                  'fcluster_criterion': 'distance'}
        ret = self.getImpl().build_biclusters(self.ctx, params)[0]
        self.check_build_biclusters_output(ret, ['gene_id_1', 'gene_id_2', 'gene_id_3'])

    def test_bad_enrich_onthology_params(self):
        self.start_test()
        invalidate_params = {'missing_sample_set': 'sample_set',
                             'entity_term_set': 'entity_term_set'}
        error_msg = '"sample_set" parameter is required, but missing'
        self.fail_enrich_onthology(invalidate_params, error_msg)

        invalidate_params = {'sample_set': 'sample_set',
                             'missing_entity_term_set': 'entity_term_set'}
        error_msg = '"entity_term_set" parameter is required, but missing'
        self.fail_enrich_onthology(invalidate_params, error_msg)

    def test_enrich_onthology(self):
        self.start_test()

        sample_set = ['gene_id_1', 'gene_id_1', 'gene_id_2', 'gene_id_2']
        # sample_set = ['gene_id_1', 'gene_id_2']
        # relationship: GO:0006355 -> GO:2001141 -> GO:0050789 -> GO:0065007 -> GO:0008150
        entity_term_set = {'gene_id_1': ['GO:0008150'],
                           'gene_id_2': ['GO:0065007', 'GO:0050789'],
                           'gene_id_3': ['GO:2001141'],
                           'gene_id_4': ['GO:0006355']}

        params = {'sample_set': sample_set,
                  'entity_term_set': entity_term_set,
                  'propagation': 1}
        ret = self.getImpl().enrich_onthology(self.ctx, params)[0]
        expect_go_ids = ['GO:0050789', 'GO:0065007', 'GO:0008150']
        self.check_enrich_onthology_output(ret, expect_go_ids)

        enrichment_profile = ret['enrichment_profile']
        print enrichment_profile

    def test_bad_calc_onthology_dist_params(self):
        self.start_test()
        invalidate_params = {'missing_onthology_set': 'onthology_set'}
        error_msg = '"onthology_set" parameter is required, but missing'
        self.fail_calc_onthology_dist(invalidate_params, error_msg)

        invalidate_params = {'onthology_set': {'gene_id_1':
                                               ['go_term_1', 'go_term_2', 'go_term_3']}}
        error_msg = 'Input Error: one or more gene is associated with more than 2 GO terms'
        self.fail_calc_onthology_dist(invalidate_params, error_msg)

    def test_calc_onthology_dist(self):
        self.start_test()
        # graph structure:
        # GO:0008150 <-- GO:0065007 <-- GO:0050789 <-- GO:0050794 <-- GO:0031323
        #                                          <-- GO:0019222 <-- GO:0031323
        params = {'onthology_set': {'gene_id_1':
                                    ['GO:0050794', 'GO:0019222'],
                                    'gene_id_2':
                                    ['GO:0031323', 'GO:0050794'],
                                    'gene_id_3':
                                    ['GO:0031323', 'GO:0019222'],
                                    'gene_id_4':
                                    ['GO:0065007', 'GO:0031323'],
                                    'gene_id_5':
                                    ['GO:0031323', 'GO:not_existing'],
                                    'gene_id_6':
                                    ['GO:0031323', 'GO:0031323']}}
        ret = self.getImpl().calc_onthology_dist(self.ctx, params)[0]
        expect_steps = {'gene_id_1': 2,
                        'gene_id_2': 1,
                        'gene_id_3': 1,
                        'gene_id_4': 3,
                        'gene_id_5': float('inf'),
                        'gene_id_6': 0}
        self.check_calc_onthology_dist_output(ret, expect_steps)

    def test_compute_weighted_edges(self):
        # root: [u'GO:0003674', u'GO:0008150', u'GO:0005575']
        # leave: GO:0000432
        roots = ['GO:0003674', 'GO:0008150', 'GO:0005575']
        leave = 'GO:0000432'
        weighted_edges = self.ke_util._compute_weighted_edges()

        self.assertTrue(leave not in weighted_edges)

        for root in roots:
            weights = list(set(weighted_edges[root].values()))
            self.assertEqual(len(weights), 1)
            self.assertEqual(weights[0], 0.5)

        first_children = weighted_edges[roots[1]].keys()

        for first_child in first_children:
            weights = list(set(weighted_edges[first_child].values()))
            self.assertEqual(len(weights), 1)
            self.assertEqual(weights[0], 0.25)

    def test_calc_weighted_onthology_dist(self):
        self.start_test()
        # graph structure:
        # GO:0008150 <-0.5- GO:0065007 <-0.25- GO:0050789 <-0.125- GO:0006792
        #            <-0.5- GO:0099531 <-0.25- GO:0007269
        params = {'onthology_set': {'gene_id_1': ['GO:0065007', 'GO:0099531'],
                                    'gene_id_2': ['GO:0050789', 'GO:0008150'],
                                    'gene_id_3': ['GO:0006792', 'GO:0007269'],
                                    'gene_id_4': ['GO:0050789', 'GO:0050789']}}

        ret = self.getImpl().calc_weighted_onthology_dist(self.ctx, params)[0]

        expected_dist = {'gene_id_1': 0.5,
                         'gene_id_2': 0.375,
                         'gene_id_3': 0.8125,
                         'gene_id_4': 0}

        onthology_dist_set = ret['onthology_dist_set']
        self.assertItemsEqual(onthology_dist_set, expected_dist)
