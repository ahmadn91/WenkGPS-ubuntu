#-*- coding: utf-8 -*-

from odoo import models, fields, api



class Wenk(models.Model):

    _inherit="crm.lead"
    RISK_CHOICES = [
        ("competitor","Competitor"),
        ("edgy high management","Edgy Higher Management"),
        ("gerographical distance","Geographical Distance")
    ]
    ''' This field belongs to main form
    added by AhmedNaseem @INTEGRATEDPATH - 11/07/2020 
    '''

    risk=fields.Selection(RISK_CHOICES,string="Risk")

    ''' Fields below belongs to to competitor notepad page
    added by AhmedNaseem @INTEGRATEDPATH - 11/07/2020
    '''
    competitor_field_1 = fields.Char(string="Competitor Field 1")
    competitor_field_2 = fields.Char(string="Competitor Field 2")
    competitor_field_3 = fields.Char(string="Competitor Field 3")
    competitor_field_4 = fields.Char(string="Competitor Field 4")
    competitor_field_5 = fields.Char(string="Competitor Field 5")
    competitor_field_6 = fields.Char(string="Competitor Field 6")


    ''' Fields below belongs to Technical and financial proposal
    segment of the form added by AhmedNaseem @INTEGRATEDPATH - 11/07/202
    '''

    financial_proposal = fields.Binary("Financil Proposal ",required=True)
    technical_proposal = fields.Binary("Technical Proposal ",required=True)


