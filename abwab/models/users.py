# -*- coding: utf-8 -*-

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "res.users"

    help_id = fields.One2many('abwab.abwab', 'create_uid', string="طلبات المساعدة الاولية المقدمة")
    user_help_phone = fields.Integer(string='رقم الهاتف', related='help_id.phone')
    user_help_civil_id = fields.Char(string='الرقم المدني', related='help_id.civil_id')
    user_help_nation = fields.Many2one(string='الجنسية', related='help_id.nationality')
    user_help_state = fields.Selection(string='المحافظة', related='help_id.state')
    user_help_family_members = fields.Integer(string='عدد أفراد العائلة', related='help_id.family_members')
