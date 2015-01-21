{
    'name' : 'Parking Management System - Booth Module',
    'version' : '1.0',
    'author' : 'JakC',
    'category' : 'Generic Modules/Parking Booth Module',
    'depends' : ['base_setup','base','jakc_parking','jakc_parking_pricing'],
    'init_xml' : [],
    'data' : [			        
        'security/ir.model.access.csv',             
        'jakc_parking_booth_view.xml',
        'jakc_parking_booth_menu.xml',        
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}