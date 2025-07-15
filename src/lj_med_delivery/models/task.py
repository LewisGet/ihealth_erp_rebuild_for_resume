from odoo import models, fields, api


class Task(models.Model):
    _name = 'lj_med_delivery.task'
    _description = 'Medical Delivery Task'

    name = fields.Char(string='Task Name', required=True,
                       default=lambda self: self.env['ir.sequence'].next_by_code('lj_med_delivery.task.sequence'))
    description = fields.Text(string='Description')

    status_id = fields.Many2one('lj_med_delivery.task_status', string='task status', ondelete='set null',
                                help='task status')
    sale_order_id = fields.Many2one('sale.order', string='Sale Order', ondelete='set null',
                                    help='task to sale to products')
    employee_id = fields.Many2one('hr.employee', string='Assigned Employee', required=False, ondelete='set null',
                                  help='who delivery this task')
    partner_id = fields.Many2one('res.partner', string='Customer', required=True, ondelete='restrict',
                                 help='task consumer')
