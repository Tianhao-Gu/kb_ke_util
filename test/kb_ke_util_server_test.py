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


class kb_ke_utilTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        token = environ.get('KB_AUTH_TOKEN', None)
        config_file = environ.get('KB_DEPLOYMENT_CONFIG', None)
        cls.cfg = {}
        config = ConfigParser()
        config.read(config_file)
        for nameval in config.items('kb_ke_util'):
            cls.cfg[nameval[0]] = nameval[1]
        # Getting username from Auth profile for token
        authServiceUrl = cls.cfg['auth-service-url']
        auth_client = _KBaseAuth(authServiceUrl)
        user_id = auth_client.get_user(token)
        # WARNING: don't call any logging methods on the context object,
        # it'll result in a NoneType error
        cls.ctx = MethodContext(None)
        cls.ctx.update({'token': token,
                        'user_id': user_id,
                        'provenance': [
                            {'service': 'kb_ke_util',
                             'method': 'please_never_use_it_in_production',
                             'method_params': []
                             }],
                        'authenticated': 1})
        cls.wsURL = cls.cfg['workspace-url']
        cls.wsClient = workspaceService(cls.wsURL)
        cls.serviceImpl = kb_ke_util(cls.cfg)
        cls.scratch = cls.cfg['scratch']
        cls.callback_url = os.environ['SDK_CALLBACK_URL']

    @classmethod
    def tearDownClass(cls):
        if hasattr(cls, 'wsName'):
            cls.wsClient.delete_workspace({'workspace': cls.wsName})
            print('Test workspace was deleted')

    def getWsClient(self):
        return self.__class__.wsClient

    def getWsName(self):
        if hasattr(self.__class__, 'wsName'):
            return self.__class__.wsName
        suffix = int(time.time() * 1000)
        wsName = "test_kb_ke_util_" + str(suffix)
        ret = self.getWsClient().create_workspace({'workspace': wsName})  # noqa
        self.__class__.wsName = wsName
        return wsName

    def getImpl(self):
        return self.__class__.serviceImpl

    def getContext(self):
        return self.__class__.ctx

    def start_test(self):
        testname = inspect.stack()[1][3]
        print('\n*** starting test: ' + testname + ' **')

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

    def check_run_pdist_output(self, ret):
        self.assertTrue('square_dist_matrix' in ret)
        self.assertTrue('labels' in ret)

    def check_run_linkage_output(self, ret):
        self.assertTrue('linkage_matrix' in ret)

    def check_run_fcluster_output(self, ret):
        self.assertTrue('flat_cluster' in ret)

    def test_bad_run_pdist_params(self):
        self.start_test()
        invalidate_params = {'missing_data_matrix': 'data_matrix'}
        error_msg = '"data_matrix" parameter is required, but missing'
        self.fail_run_pdist(invalidate_params, error_msg)

        invalidate_params = {'data_matrix': 'not_dict'}
        error_msg = "INPUT ERROR:\nRequiring dictionary data_matrix.\nGot: <type 'str'>"
        self.fail_run_pdist(invalidate_params, error_msg)

        invalidate_params = {'data_matrix': {'missing_keys': 'missing_keys'}}
        error_msg = 'INPUT ERROR:\nRequiring ["row_ids", "col_ids", "values"] keys.\n'
        error_msg += 'Got: [\'missing_keys\']'
        self.fail_run_pdist(invalidate_params, error_msg)

        invalidate_params = {'data_matrix': {'row_ids': 'row_ids',
                                             'col_ids': 'col_ids',
                                             'values': 'values'},
                             'metric': 'invalidate_metric'}
        error_msg = 'INPUT ERROR:\nInput metric function [invalidate_metric] is not valid.\n'
        self.fail_run_pdist(invalidate_params, error_msg, contains=True)

    def test_bad_data_matrix(self):
        params = {'data_matrix': {'row_ids': ['gene_1', 'gene_2', 'gene_3'],
                                  'col_ids': ['condition_1', 'condition_2', 'condition_3'],
                                  'values': [['a', 0.2, 0.3], [0.3, 0.4, 0.5], [0.5, 0.6, 0.7]]}}
        error_msg = "INVALID data_matrix:\ncannot convert all element to number: ['a', 0.2, 0.3]"
        self.fail_run_pdist(params, error_msg)

    def test_run_pdist(self):
        self.start_test()
        params = {'data_matrix': {'row_ids': ['gene_1', 'gene_2', 'gene_3'],
                                  'col_ids': ['condition_1', 'condition_2', 'condition_3'],
                                  'values': [[0.1, 0.2, 0.3], [0.3, 0.4, 0.5], [0.5, 0.6, 0.7]]}}
        ret = self.getImpl().run_pdist(self.ctx, params)[0]
        self.check_run_pdist_output(ret)

    def test_bad_run_linkage_params(self):
        self.start_test()
        invalidate_params = {'missing_square_dist_matrix': 'square_dist_matrix'}
        error_msg = '"square_dist_matrix" parameter is required, but missing'
        self.fail_run_linkage(invalidate_params, error_msg)

        invalidate_params = {'square_dist_matrix': 'square_dist_matrix',
                             'method': 'invalidate_method'}
        error_msg = "INPUT ERROR:\nInput linkage algorithm [invalidate_method] is not valid.\n"
        self.fail_run_linkage(invalidate_params, error_msg, contains=True)

    def test_run_linkage(self):
        self.start_test()
        square_dist_matrix = [[0, 0.34641016, 0.69282032],
                              [0.34641016, 0, 0.34641016],
                              [0.69282032, 0.34641016, 0]]
        params = {'square_dist_matrix': square_dist_matrix}
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
