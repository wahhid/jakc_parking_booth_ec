from openerp.osv import fields, osv
from datetime import datetime
import logging

_logger = logging.getLogger(__name__)


AVAILABLE_STATES = [
    ('draft','Draft'),
    ('open','Open'),
    ('done','Close'),
]

AVAILABLE_BOOTH_TYPES = [
    ('in','Booth In'),
    ('out','Booth Out'),
    ('inout','Booth In and Out'),
]

class park_booth(osv.osv):
    _name = "park.booth"
    _description = "Parking Booth"
    _columns = {
        'name': fields.char('Name', size=100, required=True),
        'booth_type_id': fields.selection(AVAILABLE_BOOTH_TYPES,'Booth Type', size=16, required=True),
        'is_manless': fields.boolean('Manless'),
        'booth_detail_ids': fields.one2many('park.booth.detail','booth_id','Detail'),
        'booth_image_type_ids': fields.one2many('park.booth.image','booth_id','Image'),
        'state': fields.selection(AVAILABLE_STATES,'Status', size=16, readonly=True, required=True),        
    }
    _defaults = {
        'state': lambda *a: 'open',
    }
park_booth()

class park_booth_detail(osv.osv):
    _name = "park.booth.detail"
    _description  = "Parking Booth Detail"
    _columns  = {
        'booth_id': fields.many2one('park.booth','Booth', required=True, readonly=True),
        'pricing_id': fields.many2one('park.pricing','Pricing', required=True),
        'is_default': fields.boolean('Default'),        
    }    
    _defaults = {
        'booth_id': lambda self, cr, uid, context: context.get('booth_id', False),
        'is_default': lambda *a: False,        
        
    }
park_booth_detail()

class park_booth_image(osv.osv):
    _name = 'park.booth.image'
    _description = "Parking Booth Image"
    _columns = {
        'booth_id': fields.many2one('park.booth', 'Booth', required=True),
        'image_type_id': fields.many2one('park.image.type', 'Image Type', required=True),
        'camera_device': fields.char('Camera Device', size=100),
    }
    
    _defaults = {
        'booth_id': lambda self, cr, uid, context: context.get('booth_id', False),
    }

park_booth_image()