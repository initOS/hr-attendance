# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import _, models


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    def action_open_last_month_overtime_legacy(self):
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "name": _("Overtime"),
            "res_model": "hr.attendance.overtime",
            "views": [
                [self.env.ref("hr_attendance.view_attendance_overtime_tree").id, "list"]
            ],
            "context": {"create": 0},
            "domain": [("employee_id", "=", self.id)],
        }
