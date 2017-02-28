# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Especie (models.Model):
	_name = 'examen.especie'

	name = fields.Char(string="Nombre", required=True)

	servivo_id = fields.One2many('examen.servivo','especie_id', string="Ser Vivo")
	sith_id = fields.One2many('examen.sith', 'especie_id', string ="Sith")

class Servivo (models.Model):
	_name = 'examen.servivo'

	name = fields.Char(string="Nombre", required=True)

	especie_id = fields.Many2one('examen.especie', string="Especie")

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

	@api.one
	def action_rojo(self):
		self.colorSable = 'rojo'

	@api.one
	def action_rojoOscuro(self):
		self.colorSable = 'rojoOscuro'

	@api.onchange('rabia')
	def set_afinity(self):
		self.afinidadOscuridad = self.rabia * 2

class Planeta(models.Model):
	_name = 'examen.planeta'

	name = fields.Char(string="Nombre", required=True)
	distancia = fields.Float(string="Distancia en Parsecs", required=True)
	destruido = fields.Boolean(string="Destruido por la estrella de la muerte", default=False)
	destruidoDate = fields.Date(string="Fecha en la que fue destruido")