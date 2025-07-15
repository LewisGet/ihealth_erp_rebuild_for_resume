{
    'name': "lj_med_delivery",
    'version': '0.0.1',
    'demo': [],
    'depends': [
        'base',
        'hr',
        'account',
        'sale',
        'purchase'
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/task_sequence.xml',
        'data/task_status_data.xml',
        'views/task_status_views.xml',
        'views/task_views.xml',
        'views/menu.xml'
    ],
    'qweb': [],
    'installable': True,
    'application': True,
}
