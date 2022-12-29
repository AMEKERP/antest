# -*- coding: utf-8 -*-
import base64
from datetime import datetime, timedelta
from odoo import http
from odoo.http import request
from odoo import _
from odoo.addons.portal.controllers.portal import CustomerPortal


class ShowHelpCases(http.Controller):
    @http.route('/help_cases', auth='user', website="true", type="http")
    def display_help_cases(self, sortby=None, **kw):
        searchbar_sortings = {
            'name': {'label': _('Name'), 'order': 'name asc'},
        }
        if not sortby:
            sortby = 'name'
        order = searchbar_sortings[sortby]['order']
        print('requests  is running ok...')
        help_cases = http.request.env['abwab.abwab'].search([('create_uid', '=', request.env.user.id)], order=order)
        return http.request.render('abwab.portal_my_help_cases', {
            'help_cases': help_cases,
            "page_name": "help_case",
            'searchbar_sortings': searchbar_sortings,
            'sortby': sortby
        })


class HelpCasesCustomerPortal(CustomerPortal):
    def _prepare_home_portal_values(self, counters):
        values = super(HelpCasesCustomerPortal, self)._prepare_home_portal_values(counters)
        count_help_cases = http.request.env['abwab.abwab'].search_count([('create_uid', '=', request.env.user.id)])
        values.update({
            'count_help_cases': count_help_cases,
        })
        return values


class HelpRequest(http.Controller):
    @http.route('/help_cases/<model("abwab.abwab"):help_case>/', auth='user', website=True, type="http")
    def case_status(self, help_case, **kw):
        # # case_rec = request.env['charity.charity'].sudo().search([('create_uid', '=', request.env.user.id)])
        # return http.request.render('abwab.final_help_form', {
        #     'help_case': help_case,
        #     "page_name": "help_case"
        #
        # })
        nation_record = request.env['nation.nation'].sudo().search([])
        case_record = request.env['abwab.help'].sudo().search([])
        return http.request.render('abwab.final_help_form', {
            'nation_record': nation_record,
            'case_record': case_record,
            'help_case': help_case,

        })

    @http.route('/create_final_help_request', auth='user', csrf=False, type='http', website=True, method=['POST'])
    def create_final_help_request(self, civil_id,job_status, **kw):
        six_months_period_before = (datetime.now() - timedelta(days=180))
        if request.env['abwab.final'].sudo().search(
                [('civil_id', '=', civil_id), ('create_date', '>', six_months_period_before)]):
            print('error')
            return request.render("abwab.help_error", {})
        else:
            request.env['abwab.final'].sudo().create({**kw,
                                                      'civil_id': civil_id,
                                                      'job_status': job_status,
                                                      'case_details_book': base64.b64encode(
                                                          kw.get('case_details_book').read()),
                                                      'id_copy': base64.b64encode(
                                                          kw.get('id_copy').read()),
                                                      'marriage_copy': base64.b64encode(kw.get('marriage_copy').read()),
                                                      'rent_copy_last': base64.b64encode(
                                                          kw.get('rent_copy_last').read()),
                                                      'employment_contract': base64.b64encode(
                                                          kw.get('employment_contract').read()),
                                                      'bank_statement6m': base64.b64encode(
                                                          kw.get('bank_statement6m').read()),
                                                      'dept_copy': base64.b64encode(kw.get('dept_copy').read()),
                                                      'health_reports': base64.b64encode(
                                                          kw.get('health_reports').read()),
                                                      'study_fees_report': base64.b64encode(
                                                          kw.get('study_fees_report').read()),
                                                      'kuwait_cases': base64.b64encode(
                                                          kw.get('kuwait_cases').read()),
                                                      'iban': base64.b64encode(
                                                          kw.get('iban').read()),
                                                      })
            nation_record = request.env['nation.nation'].sudo().search([])
            print("Help Created Successfully", kw)
            return request.render("abwab.final_help_thanks", {'nation_record': nation_record, })


class AbwabRequest(http.Controller):
    @http.route('/help_form', auth='user', website=True, type="http")
    def help_form(self, **kw):
        print('help form is running ok...', kw)
        nation_record = request.env['nation.nation'].sudo().search([])
        case_record = request.env['abwab.help'].sudo().search([])
        return http.request.render('abwab.help_form', {
            'nation_record': nation_record,
            'case_record': case_record,

        })

    @http.route('/create_help_request', auth='public', csrf=False, type='http', website=True, method=['POST'])
    def create_help_request(self, **kw):
        request.env['abwab.abwab'].sudo().create({**kw})
        nation_record = request.env['nation.nation'].sudo().search([])
        print("Help Created Successfully", kw)
        return request.render("abwab.help_thanks", {'nation_record': nation_record, })


# class AbwabFinalRequest(http.Controller):
#     @http.route('/final_help_form', auth='user', website=True, type="http")
#     def final_help_form(self, **kw):
#         print('final help form is running ok...', kw)
#         nation_record = request.env['nation.nation'].sudo().search([])
#         case_record = request.env['abwab.help'].sudo().search([])
#         return http.request.render('abwab.final_help_form', {
#             'nation_record': nation_record,
#             'case_record': case_record,
#
#         })
#
#     @http.route('/create_final_help_request', auth='public', csrf=False, type='http', website=True, method=['POST'])
#     def create_final_help_request(self, **kw):
#         request.env['abwab.final'].sudo().create({**kw})
#         nation_record = request.env['nation.nation'].sudo().search([])
#         print("Help Created Successfully", kw)
#         return request.render("abwab.help_thanks", {'nation_record': nation_record, })
