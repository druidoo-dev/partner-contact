# Copyright (C) 2019-Today: Druidoo (<https://www.druidoo.io>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.exceptions import ValidationError
from odoo.tests.common import TransactionCase


class TestRespartnerAgeRange(TransactionCase):
    def test_overlap(self):
        self.env["res.partner.age.range"].create(
            {"name": "0-10", "age_from": 0, "age_to": 10}
        )
        with self.assertRaises(ValidationError):
            self.env["res.partner.age.range"].create(
                {"name": "5-15", "age_from": 5, "age_to": 15}
            )
