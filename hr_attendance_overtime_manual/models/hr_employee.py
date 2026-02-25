# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import models


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    def action_open_last_month_overtime_legacy(self):
        self.ensure_one()
        view_name = "hr_attendance_overtime_manual.view_attendance_overtime_tree"
        return {
            "type": "ir.actions.act_window",
            "name": self.env._("Overtime"),
            "res_model": "hr.attendance.overtime.line",
            "views": [
                [
                    self.env.ref(view_name).id,
                    "list",
                ]
            ],
            "context": {"create": 0},
            "domain": [("employee_id", "=", self.id)],
        }
