# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import POOL, DB_NAME, USER, CONTEXT, test_view,\
    test_depends
from trytond.transaction import Transaction


class PartyTestCase(unittest.TestCase):
    'Test Party module'

    def setUp(self):
    	trytond.tests.test_tryton.install_module('party_access_control')

    def test005views(self):
    	'Test Views'
    	test_view('party_access_control')

    def test006depends(self):
    	'Test Depends'
    	test_depends()


