#-*- coding: utf-8 -*-

from odoo import models, fields, api



class Wenk(models.Model):

    _inherit="crm.lead"

    risk=fields.Char(string="Risk")
