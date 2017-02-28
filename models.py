# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Especie (models.Model):
	_name = 'examen.especie'

	name = fields.Char(string="Nombre", required=True)

	servivo_id = fields.One2many('starWars.servivo','especie_id', string="Ser Vivo")

class Servivo (models.Model):
	_name = 'examen.servivo'

	name = fields.Char(string="Nombre", required=True)

	especie_id = fields.Many2one('starWars.especie', string="Especie")
	
class Sith(models.Model):
	_inherit = 'examen.servivo'
	_name = 'examen.sith'

	name = fields.Char(string="Nombre", required=True)
	rabia = fields.Integer(string="Rabia", required=True)
	afinidadOscuridad = fields.Integer(string="Afinidad a la oscuridad", readonly=True)
	numeroSables = fields.Boolean(default=False)
	colorSable = fields.Selection([
	('rojo', "Rojo"),
	('rojoOscuro', "Rojo Oscuro"),
	])

	especie_id = fields.Many2one("examen.especie", string="Especie")

