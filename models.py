# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Especie (models.Model):
	_name = 'starWars.especie'

	name = fields.Char(string="Nombre", required=True)

	servivo_id = fields.One2many('starWars.servivo','especie_id', string="Ser Vivo")

class Servivo (models.Model):
	_name = 'starWars.servivo'

	name = fields.Char(string="Nombre", required=True)

	especie_id = fields.Many2one('starWars.especie', string="Especie")