from odoo import models, fields, api


class TaskStatus(models.Model):
    _name = 'lj_med_delivery.task_status'
    _description = 'Medical Delivery Task Status'
    _order = 'sequence, name'

    name = fields.Char(string='Status Name', required=True, translate=True)
    sequence = fields.Integer(string='Sequence', default=10)
    description = fields.Text(string='Description')
    # odoo color field
    color = fields.Integer(string='Color Index')
