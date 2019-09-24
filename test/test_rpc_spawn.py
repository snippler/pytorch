#!/usr/bin/env python3
from __future__ import absolute_import, division, print_function, unicode_literals

from rpc_test import RpcTest
from common_distributed import MultiProcessTestCase
from common_utils import TEST_WITH_ASAN

import unittest

@unittest.skipIf(TEST_WITH_ASAN, "Skip ASAN as torch + multiprocessing spawn have known issues")
class RpcTestWithSpawn(MultiProcessTestCase, RpcTest):

    def setUp(self):
        super(RpcTestWithSpawn, self).setUp()
        self._spawn_processes()

if __name__ == '__main__':
    run_tests()
