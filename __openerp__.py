# -*- coding: utf-8 -*-
{
    'name': "fortuna",

    'summary': """
       Adaptaciones del odoo a La Fortuna""",

    'description': """
         Adaptaciones del odoo a La Fortuna
    """,

    'author': "Nayeli Valencia Diaz",
    'website': "http://www.xmarts.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','purchase','stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/report_fortuna_sale.xml',
        'templates.xml',
        'views/report_reordenamiento.xml',
        'views/report_purchaseorderfortuna.xml',
        'fortuna_report.xml',
        'views/report_inventoryqty.xml',
        'views/pos_order.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}