# -*- coding: utf-8 -*-
#
#
#    Copyright 2013-2014 Camptocamp SA
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#
from openerp.osv import fields, orm


class logistic_requisition_line_assign(orm.TransientModel):
    _name = 'logistic.requisition.line.assign'
    _description = 'Assign a logistic requisition line'

    _columns = {
        'logistic_user_id': fields.many2one(
            'res.users',
            'Logistic Specialist',
            required=True,
            help="Logistic Specialist in charge of the "
                 "Logistic Requisition Line"),
    }

    def assign(self, cr, uid, ids, context=None):
        if context is None:
            context = {}
        line_ids = context.get('active_ids')
        if not line_ids:
            return
        form = self.browse(cr, uid, ids[0], context=context)
        line_obj = self.pool.get('logistic.requisition.line')
        line_obj.write(cr, uid, line_ids,
                       {'logistic_user_id': form.logistic_user_id.id},
                       context=context)
        return {'type': 'ir.actions.act_window_close'}
