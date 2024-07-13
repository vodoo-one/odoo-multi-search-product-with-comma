# Copyright © 2024 Vodoo One, LLC
# See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def _where_calc(self, domain, active_test=True):
        """ In case we need an analytic column in an account_report, we shadow the account_move_line table
        with a temp table filled with analytic data, that will be used for the analytic columns.
        We do it in this function to only create and fill it once for all computations of a report.
        The following analytic columns and computations will just query the shadowed table instead of the real one.
        """
        new_domain = domain
        try:
            if len(domain) == 1 and domain[0][0] == 'product_variant_ids.barcode':
                search_value_list = domain[0][2].upper().replace(' ',',').split(',')
                while '' in search_value_list:
                    search_value_list.remove('')
                new_domain = ['|', list(domain[0]), ['product_variant_ids.default_code', 'in', tuple(search_value_list)]]
        except:
            # avoid affect other search types
            pass
        query = super()._where_calc(new_domain, active_test)
        return query
