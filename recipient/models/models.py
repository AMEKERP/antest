# -*- coding: utf-8 -*-


from odoo import models, fields


class Recipient_payment(models.Model):
    _inherit = 'account.payment'

    recipient_payment_one = fields.Many2one('receipts.notes', string='Receipt Note',
                                            domain="[('collector_name', '=?', collector),('finished','=',False)]")
    receipt_payment = fields.Many2one('receipt.receipt',
                                      domain="[('receipt_id', '=?', recipient_payment_one), ('cancelled','=',False), ('payment_id', '=', False)]",
                                      string='Receipt')
    collector = fields.Many2one('collector.collector', string='Collector Name المحصل')


# دفتر الايصالات
class Receipts_Notes(models.Model):
    _name = 'receipts.notes'

    name = fields.Integer(string='Receipt Number رقم الدفتر', required=True)
    receipts_from = fields.Integer(string='Receipts From')
    receipts_to = fields.Integer(string='Receipts To')
    collector_name = fields.Many2one('collector.collector', string='Collector المحصل')

    receipts_ids = fields.One2many('receipt.receipt', 'receipt_id', string="Receipts Notes")
    finished = fields.Boolean(string='Finished', default=False)

    def create_receipt_schedule(self):
        receipnt_obj = self.env['receipt.receipt']
        for receipnt_rec in self:
            n1 = receipnt_rec.receipts_from
            n2 = receipnt_rec.receipts_to
            if n1 > n2:
                print(n1, n2)
                print("Error")
            n_deff = (n2 - n1)
            print(n_deff)
            for n_rec in range(int(n_deff)):
                receipnt_obj.create(
                    {'receipt_id': receipnt_rec.id,
                     'name': n1,
                     'receipt_collector': receipnt_rec.collector_name
                     })
                n1 = n1 + 1


class Receipt(models.Model):
    _name = 'receipt.receipt'

    name = fields.Integer(string='Receipt Number رقم الايصال')
    receipt_collector = fields.Char(string='Collector Name المحصل', related='receipt_id.collector_name.name')
    receipt_id = fields.Many2one('receipts.notes', string='Note رقم الدفتر')
    cancelled = fields.Boolean(string='Cancelled', default=False)
    payment_id = fields.Many2one('account.payment', string='Related Payment')
    # payment = fields.Char(string='Payment', related='receipt_id.collector_name.name')


class Collector(models.Model):
    _name = 'collector.collector'

    name = fields.Char(string='Collector Name')
