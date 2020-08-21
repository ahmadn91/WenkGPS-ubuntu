#-*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime


class Wenk(models.Model):

    _inherit = "crm.lead"
    
    

    RISK_CHOICES = [
        ("competitor","Competitor"),
        ("edgy high management","Edgy Higher Management"),
        ("gerographical distance","Geographical Distance")
    ]
    ''' This field belongs to main form
    added by AhmedNaseem @INTEGRATEDPATH - 11/07/2020 
    '''

    risk = fields.Selection(RISK_CHOICES,string="Risk")

    ''' Fields below belongs to to competitor notepad page
    added by AhmedNaseem @INTEGRATEDPATH - 11/07/2020
    '''
    competitor_notes = fields.Text(translate=True,string="")

    financial_doc = fields.One2many("wenk.fdocuments","doc_id") # name of the model
    technical_doc = fields.One2many("wenk.tdocuments","doc_id") 
    competitor_notes = fields.One2many("wenk.competitor","info_id")
    


                            
class WenkFinDocuments(models.Model):

   
   _name = "wenk.fdocuments"
   #_inherit = ['mail.thread']

   #rel_field= fields.Many2one("crm.lead") -I thought we need it, tf man
   doc_id = fields.Char(string="DOC ID",readonly=True,invisible=True)
   name = fields.Char(string="Document Name")
   upload_date = fields.Date(string="Uploaded at",default=datetime.today(),readonly=True,invisible=True)
   uploader = fields.Many2one('res.users','Uploader', default=lambda self: self.env.user,readonly=True,invisible=True)
   comment = fields.Char(string="Comments")
   document = fields.Binary(string="Document")
   #notify = fields.Many2one("res.users","User to notify")

#    @api.onchage(notify)
#    def notify_func(self,notify):
#     if self.notify:
#         self.message_post(body="Please see document", partner_ids=self.notify,message_type='notification')
#     else:
#         pass

   
class WenkTechDocuments(models.Model):

   _name = "wenk.tdocuments"

   doc_id = fields.Char(string="DOC ID",readonly=True,invisible=True)
   name = fields.Char(string="Document Name")
   upload_date = fields.Date(string="Uploaded at",default=datetime.today(),readonly=True,invisible=True)
   uploader = fields.Many2one('res.users','Uploader', default=lambda self: self.env.user,readonly=True,invisible=True)
   comment = fields.Char(string="Comments")
   document = fields.Binary(string="Document")
    


class WenkCompetitorModel(models.Model):
   _name = "wenk.competitor"

   info_id = fields.Char(string="INFO ID",readonly=True,invisible=True)
   content = fields.Char(string="Note")
   upload_date = fields.Date(string="Date Logged",default=datetime.today(),readonly=True,invisible=True)
   uploader = fields.Many2one('res.users','Noted By', default=lambda self: self.env.user,readonly=True,invisible=True)
   

