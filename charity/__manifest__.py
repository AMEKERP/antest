# -*- coding: utf-8 -*-
{
    'name': "charity",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Initume Solution",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','website','mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        # 'security/security_rules.xml',
        'report/case.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/web_form.xml',
       # 'views/web_asset_backend_template.xml',
    ],
    'application': True,
    'installable': True,
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
