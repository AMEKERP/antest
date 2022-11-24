# -*- coding: utf-8 -*-

from odoo import models, fields, api


class cases(models.Model):
    _name = 'charity.cases'
    _description = 'charity.cases'

    name = fields.Char(string='Case Type')
    description = fields.Text(string='Descriptions')


class charity(models.Model):
    _name = 'charity.charity'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = 'charity.charity'

    # Date = fields.Date()
    name = fields.Char(string='Name')
    case_id = fields.Char(string='الرقم المدنى')
    social_state = fields.Selection(
        [('married', 'Married'), ('single', 'Single'), ('widowed', 'Widowed'), ('student', 'Student')],
        string="الحالة الاجتماعية")
    mobile = fields.Char(string="رقم المحمول")
    job_title = fields.Char(string="الوظيفة")
    case_type = fields.Many2one('charity.cases', ondelete='cascade', store=True, string='نوع الحالة')
    religion = fields.Selection([('muslim', 'Muslim'), ('christian', 'Christian'), ('others', 'Others')],string='الديانة')
    currency_id = fields.Many2one('res.currency', string='Currency')
    main_income = fields.Float(string="Main Income", currency_field='currency_id')
    additional_income = fields.Float(string="Additional Income")
    total_income = fields.Float(compute='_total_income', string='Total Income')
    basic_expenses = fields.Float(string='Basic Expenses')
    debts_fines = fields.Float(string='Debts And Fines')
    details = fields.Text(string='Details')
    details_of_last_aid = fields.Text(string='تفاصيل أخر مساعدة')
    last_update = fields.Text(string='أخر المستجدات')
    recommendation = fields.Text(string='اقتراحات الباحث للحالة')
    decision = fields.Selection([('agreed', 'Agreed'),
                                 ('rejected', 'Rejected'),
                                 ('postponed', 'Postponed'),
                                 ('cut help', 'Cut Help'),
                                 ('ongoing help', 'Ongoing Help')], string='قرار اللجنة')
    last_help_date = fields.Date(string="تاريخ اخر مساعده من الجمعية")
    cut_help_amount = fields.Monetary(string="Cut Help Amount")
    ongoing_help_amount = fields.Monetary(string="Ongoing Help Amount")
    bank_statement6m = fields.Binary(string="كشف حساب من البنك أخر 6 شهور")
    salary_statement = fields.Binary(string="شهادة راتب حديثة التاريخ")
    rent_copy = fields.Binary(string="صورة عقد الإيجار")
    rent_copy_last = fields.Binary(string="صوره اخر عقد ايجار")
    marriage_copy = fields.Binary(string="صوره عقد الزواج")
    id_copy = fields.Binary(string="صورة بطاقات الأسرة من الجهتين")
    dept_copy = fields.Binary(string="صور مديونيات أو رسوم دراسية بتاريخ حديث")
    widowed_copy = fields.Binary(string="شهادة وفاة للأرامل وخلو زوجية")
    help_book = fields.Binary(string="كتاب جمعية صندوق إعانة المرضي")
    case_seq = fields.Char(string='رقم الطلب', readonly=True, copy=False, default='New')
    nationality = fields.Many2one('res.country', String='الجنسية')
    comments = fields.Text(string="تعليقات خاصه بالطلب")

    @api.onchange('main_income')
    def _total_income(self):
        self.total_income = self.main_income + self.additional_income

    @api.onchange('additional_income')
    def _total_income(self):
        self.total_income = self.main_income + self.additional_income

    @api.model
    def create(self, vals):
        if vals.get('case_seq', 'New') == 'New':
            vals['case_seq'] = self.env['ir.sequence'].next_by_code('case.seq') or 'New'
            result = super(charity, self).create(vals)
            return result
