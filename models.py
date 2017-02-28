# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Especie (models.Model):
	_name = 'examen.especie'

	name = fields.Char(string="Especie", required=True)

	servivo_id = fields.One2many('examen.servivo','especie_id', string="Ser Vivo")
	sith_id = fields.One2many('examen.sith', 'especie_id', string ="Sith")
	planeta_id = fields.Many2one("examen.planeta", string="Planeta", domain=[('destruido','=',False)])

class Servivo (models.Model):
	_name = 'examen.servivo'

	name = fields.Char(string="Nombre", required=True)

	especie_id = fields.Many2one('examen.especie', string="Especie")

class Sith(models.Model):
	_inherit = 'examen.servivo'
	_name = 'examen.sith'

	name = fields.Char(string="Nombre", required=True)
	rabia = fields.Integer(string="Rabia", required=True)
	afinidadOscuridad = fields.Integer(string="Afinidad a la oscuridad", readonly=True, compute='_afinity')
	numeroSables = fields.Boolean(default=False)
	colorSable = fields.Selection([('rojo', "Rojo"),('rojoOscuro', "Rojo Oscuro")],'Color Sable')

	especie_id = fields.Many2one("examen.especie", string="Especie")
	jedi_id = fields.Many2one("examen.servivo", string="Jedi")

	@api.one
	def action_rojo(self):
		self.colorSable = 'rojo'

	@api.one
	def action_rojoOscuro(self):
		self.colorSable = 'rojoOscuro'

	@api.onchange('rabia')
	def set_afinity(self):
		self.afinidadOscuridad = self.rabia * 2

	@api.depends('rabia')
	def _afinity(self):
		for r in self:
		    if r.rabia:
		    	r.afinidadOscuridad = r.rabia * 2     
		        continue

class Planeta(models.Model):
	_name = 'examen.planeta'

	name = fields.Char(string="Nombre", required=True)
	distancia = fields.Float(string="Distancia en Parsecs", required=True)
	destruido = fields.Boolean(string="Destruido por la estrella de la muerte", default=False)
	destruidoDate = fields.Date(string="Fecha en la que fue destruido")
	jedi_id = fields.One2many('examen.servivo', 'planeta_id', string ="Jedis")
	especie_id = fields.One2many('examen.especie', 'planeta_id', string ="Especie")


class Jedi(models.Model):
	_inherit = 'examen.servivo'

	colorSable = fields.Selection([('azul', "Azul"),('verde', "Verde"),('morado', "Morado")],'Color Sable') 
	soldadosClon = fields.Integer(string="Soldados que le persiguen", required=True)
	vistoDate = fields.Date(string="Fecha en la que fue visto por ultima vez", required=True)
	midiclorianos = fields.Integer(string="Midiclorianos", required=True)
	nivelJedi = fields.Char(string='Nivel de Jedi', compute='_nivelJedi', readonly=True)
	sith_id = fields.One2many('examen.sith', 'jedi_id', string ="Sith")
	planeta_id = fields.Many2one("examen.planeta", string="Planeta", domain=[('destruido','=',False)])

	@api.depends('midiclorianos')
	def _nivelJedi(self):
		if self.midiclorianos < 100:
			self.nivelJedi = "Padawan"
		elif (self.midiclorianos >= 100) and (self.midiclorianos < 1000):
			self.nivelJedi = "Caballero Jedi"
		elif self.midiclorianos >= 1000:
			self.nivelJedi = "Consejero Jedi"


	@api.onchange('midiclorianos')
	def _nivelJedi(self):
		if self.midiclorianos < 100:
			self.nivelJedi = "Padawan"
		elif (self.midiclorianos >= 100) and (self.midiclorianos < 1000):
			self.nivelJedi = "Caballero Jedi"
		elif self.midiclorianos >= 1000:
			self.nivelJedi = "Consejero Jedi"

	@api.onchange('colorSable')
	def _sable(self):
		if (self.colorSable == 'morado') and (self.nivelJedi !=  "Consejero Jedi"):
			return {
                'warning': {
                'title': "Sable",
                'message': "Necesitas aprender los caminos de la fuerza para usar este sable",
                },
            }


	@api.one
	def action_azul(self):
		self.colorSable = 'azul'

	@api.one
	def action_verde(self):
		self.colorSable = 'verde'

	@api.one
	def action_morado(self):
		self.colorSable = 'morado'