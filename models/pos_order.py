# -*- coding: utf-8 -*-
import openerp
from openerp import api, fields, models, _, tools,exceptions
from openerp.exceptions import UserError, RedirectWarning, ValidationError,except_orm
import logging
_logger = logging.getLogger(__name__)

class POSOrder(models.Model):
    _inherit = 'pos.order'

    @api.one
    def _compute_pay(self):
        list =[]
        for x in self.statement_ids:
            if x.journal_id.name not in list:
                list.append(x.journal_id.name)
        self.pay_method = ''.join(list)

    pay_method = fields.Char(string="Método de Pago", compute="_compute_pay", store=True,
                             help="Campo para agrupacion de metodo de pago")

