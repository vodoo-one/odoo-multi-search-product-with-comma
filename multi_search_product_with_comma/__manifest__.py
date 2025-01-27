# Copyright © 2023 Novobi, LLC
# See LICENSE file for full copyright and licensing details.


{
    'name': 'Multi Search Product With Comma',
    'version': '16.0.0',
    'category': 'Inventory/Inventory',
    'description': '''
        Locksmith  Keyless's Customizations related to Inventory
    ''',
    'author': 'Vodoo, LLC',
    'website': 'https://www.vodoo-one.odoo.com/',
    'license': 'OPL-1',
    'depends':  ['stock'],
    'data': [
        ################## REPORTS #############################################
        ################## VIEWS #############################################
    ],
    'assets': {
        'web.assets_backend': [
            'ecs_inventory/static/src/**/*.js',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': False,
}
