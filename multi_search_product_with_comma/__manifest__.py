# Copyright © 2023 Novobi, LLC
# See LICENSE file for full copyright and licensing details.


{
    'name': 'Multi Search Product With Comma',
    'version': '16.0.0',
    'category': 'Inventory/Inventory',
    'description': '''
        Allow user to search multiple products separated by comma
    ''',
    'author': 'Vodoo, LLC',
    'website': 'https://www.vodoo-one.com/',
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
