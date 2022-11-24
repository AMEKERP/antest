import base64
import binascii
import unicodedata
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from odoo import http
from odoo.http import request
from odoo import _
from odoo.addons.portal.controllers.portal import CustomerPortal


class ShowCases(http.Controller):
    @http.route('/cases', auth='public', website="true", type="http")
    def display_cases(self, sortby=None, **kw):
        searchbar_sortings = {
            'date': {'label': _('Newest'), 'order': 'create_date desc'},
            'name': {'label': _('Name'), 'order': 'name asc'},
        }
        if not sortby:
            sortby = 'date'
        order = searchbar_sortings[sortby]['order']
        print('requests  is running ok...')
        cases = http.request.env['charity.charity'].search([('create_uid', '=', request.env.user.id)], order=order)
        return http.request.render('charity.portal_my_cases', {
            'cases': cases,
            "page_name": "case",
            'searchbar_sortings': searchbar_sortings,
            'sortby': sortby
        })


class CasesCustomerPortal(CustomerPortal):
    def _prepare_home_portal_values(self, counters):
        values = super(CasesCustomerPortal, self)._prepare_home_portal_values(counters)
        count_cases = http.request.env['charity.charity'].search_count([('create_uid', '=', request.env.user.id)])
        values.update({
            'count_cases': count_cases,
        })
        return values


class Request(http.Controller):
    @http.route('/cases/<model("charity.charity"):case>/', auth='user', website=True, type="http")
    def case_status(self, case, **kw):
        # case_rec = request.env['charity.charity'].sudo().search([('create_uid', '=', request.env.user.id)])
        return http.request.render('charity.case_status', {
            'case': case,
            "page_name": "case"

        })


class AddCase(http.Controller):
    @http.route('/case_form1', auth='user', website=True, type="http")
    def case_form1(self, **kw):
        print('case form is running ok...', kw)
        currency_rec = request.env['res.currency'].sudo().search([])
        case_record = request.env['charity.cases'].sudo().search([])
        nation_rec = request.env['res.country'].sudo().search([('name', 'in',
                                                                ['الكويت', 'المغرب', 'الجزائر', 'مصر', 'تونس',
                                                                 'السودان', 'الصومال', 'السعودية', 'لبنان', 'سوريا',
                                                                 'اليمن', 'غير محدد الجنسية'])])
        return http.request.render('charity.case_form1',
                                   {'currency_rec': currency_rec, 'case_record': case_record, 'nation_rec': nation_rec})

    @http.route('/create/webcase', auth='user', website=True, type="http", csrf=False, methods=['POST'])
    def create_webcase(self, case_id=None, **kw):

        print('every thing is ok ...', kw)
        # six_months_period_before = (datetime.now() - relativedelta(months=6))
        six_months_period_before = (datetime.now() - timedelta(days=180))
        six_months_period_after = (datetime.now() + relativedelta(months=6)).date()
        print("six_months_Period_before", six_months_period_before)
        print('every thing is ok ...', kw)
        if request.env['charity.charity'].sudo().search(
                # [('case_id', '=', case_id), ('create_date', '<', six_months_period_after)]):
                [('case_id', '=', case_id), ('create_date', '>', six_months_period_before)]):
                #   [('case_id', '=', case_id), ('x_studio_case_on', '=', True)]):
            return request.render("charity.case_error", {})
        else:
            request.env['charity.charity'].sudo().create({**kw,
                                                          'case_id': case_id,
                                                          'bank_statement6m': base64.b64encode(
                                                              kw.get('bank_statement6m').read()),
                                                          'salary_statement': base64.b64encode(
                                                              kw.get('salary_statement').read()),
                                                          'rent_copy': base64.b64encode(kw.get('rent_copy').read()),
                                                          'rent_copy_last': base64.b64encode(
                                                              kw.get('rent_copy_last').read()),
                                                          'marriage_copy': base64.b64encode(
                                                              kw.get('marriage_copy').read()),
                                                          'id_copy': base64.b64encode(kw.get('id_copy').read()),
                                                          'dept_copy': base64.b64encode(kw.get('dept_copy').read()),
                                                          'widowed_copy': base64.b64encode(
                                                              kw.get('widowed_copy').read()),
                                                          'help_book': base64.b64encode(kw.get('help_book').read()),

                                                          })

            print("created successfully", kw)
            return request.render("charity.case_thanks", {})
