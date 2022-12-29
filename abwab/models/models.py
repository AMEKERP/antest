# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AbwabTypes(models.Model):
    _name = 'abwab.help'
    _description = 'abwab.help'

    name = fields.Char(string='نوع المساعدة')
    description = fields.Text(string='تفاصيل')


class AbwabCases(models.Model):
    _name = 'abwab.abwab'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = 'abwab.abwab'

    name = fields.Char(string='الاسم')
    civil_id = fields.Char(string='الرقم المدني')
    nationality = fields.Many2one('nation.nation', string='الجنسية')
    case_type = fields.Many2one('abwab.help', string='نوع المساعدة')
    family_members = fields.Integer(string='عدد أفراد ألاسرة')
    state = fields.Selection(
        [('الاحمدي', 'الاحمدي'), ('مبارك الكبير', 'مبارك الكبير'), ('العاصمة', 'العاصمة'), ('حولي', 'حولي'),
         ('الفروانية', 'الفروانية'), ('الجهراء', 'الجهراء')], string='المحافظة')
    phone = fields.Integer(string='رقم الهاتف')
    case_details = fields.Text(string='شرح مختصر للحالة')
    # responsible data
    responsible_for_case = fields.Many2one('res.users', string='المسؤول عن الملف')
    Temporarily_excluded = fields.Boolean(string='مستبعد مؤقت')
    Final_excluded = fields.Boolean(string='مستبعد نهائي')
    case_relation_with_other = fields.Many2one('abwab.abwab', string='علاقة صاحب الملف مع ملف اخر')
    case_degree = fields.Selection([('شديدة', 'شديدة'), ('عالية', 'عالية'), ('متوسطة', 'متوسطة'), ('محتاج', 'محتاج')],
                                   string='درجة الحالة')
    decision = fields.Selection([('موافقة', 'موافقة'), ('رفض', 'رفض')], string='القرار المبدأي')
    status = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed'),
                               ('done', 'Done'), ('cancel', 'Cancelled')], default='draft',
                              string="Status", tracking=True)
    help_seq = fields.Char(string='رقم الطلب المبدأي', readonly=True, copy=False, default='New')

    # def action_confirm(self):
    #     self.status = 'confirm'
    #
    # def action_done(self):
    #     self.status = 'done'
    #
    # def action_draft(self):
    #     self.status = 'draft'
    #
    # def action_cancel(self):
    #     self.status = 'cancel'
    @api.model
    def create(self, vals):
        if vals.get('help_seq', 'New') == 'New':
            vals['help_seq'] = self.env['ir.sequence'].next_by_code('help.seq') or 'New'
            result = super(AbwabCases, self).create(vals)
            return result


class Nation(models.Model):
    _name = 'nation.nation'
    _description = 'nation.nation'

    name = fields.Char(string='الجنسية')


class Abwab_final(models.Model):
    _name = 'abwab.final'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = 'abwab.final'

    name = fields.Char(string='الاسم كاملاً كما هو بالبطاقة المدنية أو الأمنية')
    fhelp_seq = fields.Char(string='رقم الطلب النهائي', readonly=True, copy=False, default='New')

    id_type = fields.Selection([('بطاقة مدنية', 'بطاقة مدنية'), ('بطاقة أمنية', 'بطاقة أمنية'), ('أخري', 'أخري')],
                               string='نوع الهوية')
    civil_id = fields.Char(string='رقم الهوية')
    Identity_expiration_date = fields.Date(string='تاريخ انتهاء صلاحية الهوية')
    nationality = fields.Many2one('nation.nation', string='الجنسية')
    gender = fields.Selection([('ذكر', 'ذكر'), ('أنثي', 'أنثي')], string='الجنس')
    martial_status = fields.Selection(
        [('اعزب', 'اعزب'), ('متزوج', 'متزوج'), ('مطلق', 'مطلق'),
         ('أرمل', 'أرمل'), ('أسر سجناء', 'أسر سجناء')],
        string='الحالة الاجتماعية')
    phone = fields.Char(string='رقم الهاتف')
    family_members = fields.Integer(string='عدد أفراد الأسرة')
    male_members = fields.Integer(string='عدد الذكور')
    female_members = fields.Integer(string='عدد الإناث')
    adults_members = fields.Integer(string='عدد البالغين')
    kids_members = fields.Integer(string='عدد الأطفال')
    job_status = fields.Selection(
        [('يعمل', 'يعمل'), ('عاطل عن العمل', 'عاطل عن العمل'), ('يعمل باليومية', 'يعمل باليومية'),
         ('عاجز عن العمل', 'عاجز عن العمل')], string='الحالة الوظيفية')
    job = fields.Char(string='الوظيفة')
    salary = fields.Float(string='الراتب')
    family_members_employees = fields.Integer(string='عدد العاملين في الأسرة')
    total_salaries_for_family = fields.Float(string='مجموع رواتب العاملين في الأسرة ')
    monthly_debits = fields.Selection([('نعم', 'نعم'), ('لا', 'لا')],
                                      string='هل لديك أقساط شهرية مطلوبة للبنوك أو الشركات ؟')
    monthly_debits_value = fields.Float(string='قيمة الاقساط الشهرية')
    total_debits = fields.Float(string='قيمة الدين (مجموع الديون المستحقة للبنك أو للشركة)')
    debits_for_people = fields.Selection([('نعم', 'نعم'), ('لا', 'لا')], string='هل لديك ديون مستحقة للأفراد ؟')
    debits_prove = fields.Selection([('نعم', 'نعم'), ('لا', 'لا')], string='هل يوجد إثبات رسمي للديون ؟')
    total_debits_for_people = fields.Float(string='مجموع الديون المستحقة للأفراد')
    monthly_rent = fields.Float(string='قيمة الإيجار الشهري')
    total_debits_per_month = fields.Float(string='مجموع الإلتزامات الشهرية للأسرة')
    study_fees = fields.Float(string='الرسوم الدراسية للأبناء إن وجد')
    state = fields.Selection(
        [('الاحمدي', 'الاحمدي'), ('مبارك الكبير', 'مبارك الكبير'), ('العاصمة', 'العاصمة'), ('حولي', 'حولي'),
         ('الفروانية', 'الفروانية'), ('الجهراء', 'الجهراء')], string='المحافظة')
    zone = fields.Char(string='المنطقة')
    piece = fields.Integer(string='القطعة')
    street = fields.Integer(string='الشارع')
    elgada = fields.Integer(string='الجادة')
    home = fields.Integer(string='المنزل')
    floor = fields.Integer(string='الدور')
    flat = fields.Integer(string='الشقة')
    zakat_help = fields.Selection([('نعم', 'نعم'), ('لا', 'لا')], string='هل يساعدك بيت الزكاة ؟')
    zakat_help_value = fields.Float(string='قيمة المساعدة')
    zakat_help_type = fields.Selection(
        [('شهري', 'شهري'), ('كل شهرين', 'كل شهرين'), ('كل ثلاث شهور', 'كل ثلاث شهور'), ('كل اربع شهور', 'كل اربع شهور'),
         ('كل ست شهور', 'كل ست شهور'), ('سنوي', 'سنوي')], string='نوع المساعدة')
    other_charities_help = fields.Text(
        string='هل تساعدك لجان خيرية أخرى ؟ (يرجى كتابة أسماء اللجان وقيمة المساعدة ونوعها - مثال تساعدني (اسم اللجنة) بقيمة ١٥٠ د.ك كل سنة مرة - أو تموين أو إيجار أو رسوم دراسية .. إلخ)')
    help_details = fields.Text(string='شرح مختصر للحالة (يرجى شرح مختصر للحالة ، وأهم جوانب العجز للأسرة)')

    case_details_book = fields.Binary(string="كتاب شرح الحالة")
    id_copy = fields.Binary(string="صورة البطاقات المدنية من الجهتين")
    marriage_copy = fields.Binary(string="صوره عقد الزواج + خلو زوجية من سن 18")
    rent_copy_last = fields.Binary(string="صوره عقد ايجار + اخر وصل ايجار")
    employment_contract = fields.Binary(string=" عقد العمل او شهادة الراتب ان وجدت")
    bank_statement6m = fields.Binary(string="كشف حساب من البنك أخر 6 شهور")
    dept_copy = fields.Binary(string="اثباتات مديونيات او حكم محكمة")
    health_reports = fields.Binary(string="التقارير الطبية ان وجدت")
    study_fees_report = fields.Binary(string="الرسوم الدراسية ان وجدت")
    kuwait_cases = fields.Binary(string="شهادة لمن يهمه الامر من التأمينات للكويتي")
    iban = fields.Binary(string="شهادة ايبان")
    true_date_sure = fields.Selection([('نعم', 'نعم'), ('لا', 'لا')], string='اتعهد بصحة البيانات المقدمة في الطلب')
    associated_aid = fields.One2many('purchase.subscription', 'name', string="مساعدات مرتبطة")
    decision_ids = fields.One2many('decisions.decisions', 'decision_id', string='قرارات الاعضاء')

    @api.model
    def create(self, vals):
        if vals.get('fhelp_seq', 'New') == 'New':
            vals['fhelp_seq'] = self.env['ir.sequence'].next_by_code('fhelp.seq') or 'New'
            result = super(Abwab_final, self).create(vals)
            return result


class subscription_inherited(models.Model):
    _inherit = 'purchase.subscription'

    help_related = fields.Many2one('abwab.final', string='الحالة المرتبطة بالمساعدة')


class decisions(models.Model):
    _name = "decisions.decisions"
    _description = "decisions.decisions"

    name = fields.Char(string='نص القرار')
    member = fields.Many2one('res.users', string='عضو اللجنة')
    member_type = fields.Selection([('رئيس اللجنة', 'رئيس اللجنة'), ('مقرر اللجنة', 'مقرر اللجنة'), ('عضو', 'عضو')],
                                   string='صفة العضو')
    decision_id = fields.Many2one('abwab.final', string="رقم الطلب",readonly=True)

