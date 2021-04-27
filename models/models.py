# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime


class librarydetails(models.Model):
     
    _name = 'library.data'
    _description = 'library.data' 

    name = fields.Char('Name')
    date = fields.Date('date')
    state = fields.Selection([('draft', 'Draft'),('done', 'Done'),('cancel','Cancelled')],required =True, default='draft')

    def my_demo(self):
        self.date = datetime.datetime.now()
        
    
