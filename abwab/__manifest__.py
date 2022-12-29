# -*- coding: utf-8 -*-
{
    'name': "Cases Admission",

    'summary': """
         حالات المساعدات""",

    'description': """
        استمارة تسجيل طلب مساعدة للأسر المتعففة داخل الكويت.
    """,

    'author': " AMEK CAPITAL ",
    'website': "http://amekcapital.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','website','purchase_subscription'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/web.xml',
        'report/first_help.xml',
        'report/final_help.xml',
    ],
    'application': True,
    'installable': True,
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
