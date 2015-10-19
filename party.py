# -*- coding: utf-8 -*-
'''
    trytonlls_party_access_control.py

    :copyright: The file COPYRIGHT at the top level of this
    :repository contains the full copyright notices.
    :license: , see LICENSE for more details.

'''
from trytond.pool import PoolMeta
from trytond.model import ModelView, ModelSQL, fields

__all__ = ['Party', 'Badge']

__metaclass__ = PoolMeta


class Party:
    __name__ = 'party.party'

    badges = fields.One2Many('access.control.badge', 'party', 'Badge')

class Badge(ModelSQL, ModelView):
    "Badge"
    __name__ = 'access.control.badge'
    _rec_name = 'code'

    code = fields.Char('Code', select=True, required=True )
    disabled = fields.Boolean('Disabled', )
    description = fields.Char('Description' )
    party = fields.Many2One(
        'party.party', 'Party', ondelete='CASCADE', select=True, required=True
    )
    
    @classmethod
    def __setup__(cls):
        super(Badge, cls).__setup__()
        cls._sql_constraints = [
            ('code_uniq', 'UNIQUE(code)',
             'A badge must be unique for the instance.')
        ]
        cls._order.insert(0, ('code', 'ASC'))

    @classmethod
    def default_disabled(cls):
        return False

