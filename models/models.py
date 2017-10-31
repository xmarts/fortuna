# -*- coding: utf-8 -*-
import openerp
from openerp import api, fields, models, _, tools,exceptions
from openerp.exceptions import UserError, RedirectWarning, ValidationError,except_orm
import logging
_logger = logging.getLogger(__name__)

class fortunaProducts_fields(models.Model):

    _inherit = 'product.template'
    fortuna_boxweight= fields.Float('Peso por caja')
    fortuna_unit= fields.Float('Unidades por caja')
    activo = fields.Boolean(string='Controla no. pedimento', default=True)
    @api.one
    def generate_route(self):
        _logger.info("entro al boton")
        product_obj = self.env['product.template']
        product =product_obj.search([('activo', '=', True)])
        for p in product:
            _logger.info("entro a actualizar ")
	    p.image=self.image
	    p.image_small=self.image_small
	    p.image_medium=self.image_medium
            #raise UserError(_('rutas %s')%(self.route_ids))
            #p.write({'route_ids': self.route_ids})
            #p.route_ids=self.route_ids
            #_logger.info(_('rutas %s')%(p.route_ids))


class fortunaPacking_fields(models.Model):

    _inherit = 'product.packaging'
    fortuna_boxweight= fields.Float('Peso por caja')

class FortunaPartner_fields(models.Model):

   _inherit = 'res.partner'
   fortuna_boxweight= fields.Float('Peso por caja')
   fortuna_unit= fields.Float('Unidades por caja')

class Fortunastockpack_funct(models.Model):
	_inherit = 'stock.picking'
	fortuna_dif= fields.Float('Diferencia')

@api.onchange('origin')
def onchange_qtydone(self):
	raise UserError(_('entrooo')% (self.pack_operation_product_ids.qty_done))
	if self.pack_operation_product_ids.qty_done > self.pack_operation_product_ids.product_qty:
	      raise UserError(_("Error "))
        return
class stockpickingfort(models.Model):
    _inherit = 'stock.picking'
    
    
    @api.onchange('pack_operation_product_ids')
    def _onchange_origin(self):
        #super(StockPicking, self)._onchange_origin()
        if self.pack_operation_product_ids:
            x = 0            
            for line in self.pack_operation_product_ids:
                if x: break
                if line.qty_done > line.product_qty:
                  raise UserError(_("Error: La cantidad recibida debe ser igual a la cantidad por hacer "))
                x += 1

 
    @api.one
    @api.constrains('pack_operation_product_ids')
    def condiciones(self):
        #raise exceptions.ValidationError('Debe especificar un ingreso estimado')

        if self.pack_operation_product_ids:
            x = 0            
            for line in self.pack_operation_product_ids:
                if x: break
                if line.qty_done > line.product_qty:
                  raise UserError(_('Error: La cantidad recibida debe ser igual a la cantidad por hacer '))
                x += 1

class accountinvoicefort(models.Model):
    _inherit = 'account.invoice'

    @api.one
    @api.constrains('invoice_line_ids')
    def invoicelineas(self):
        if self.invoice_line_ids:
            count = 0
            for invoice in self.invoice_line_ids:                
                count += 1

            if count >1:
                db=openerp.tools.config['db_name']
                #raise UserError(_("Error:LA BD ES :   \n%s !") % (db))
                #raise exceptions.ValidationError('Error: Solo puede agregar una orden de compra a la factura ')
class stockpickingfort(models.Model):
    _inherit = 'stock.pack.operation'
    
    
    @api.onchange('qty_done')
    def _onchange_origin(self):
        #super(StockPicking, self)._onchange_origin()
        if self.qty_done > self.product_qty:
            raise UserError(_("Error: La cantidad recibida debe ser igual a la cantidad por hacer "))
    @api.one
    @api.constrains('qty_done')
    def condicionespack(self):
        if self.qty_done > self.product_qty:
            raise UserError(_("Error: La cantidad recibida debe ser igual a la cantidad por hacer "))
