# -*- coding: utf-8 -*-
{
    'name': "examen",

    'summary': """examen""",
    
    'description': """
        StarWars module to manage jedis
    """,

    'icon': "/examen/static/img/jedi.png",


    'author': "Jaime Lopez Viartola",
    'website': "http://www.starwars.es/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Examen',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/views.xml',
    ],
}
