from odoo import api, fields, models, _


class Product(models.Model):
    _inherit = "product.product"

    def _where_calc(self, domain, active_test=True):
        """ In case we need an analytic column in an account_report, we shadow the account_move_line table
        with a temp table filled with analytic data, that will be used for the analytic columns.
        We do it in this function to only create and fill it once for all computations of a report.
        The following analytic columns and computations will just query the shadowed table instead of the real one.
        """
        new_domain = domain
        try:
            if len(domain) > 1:
                for d in domain:
                    if d[0] == 'default_code':
                        search_value = d[2].upper().replace(' ',',').split(',')
                        while '' in search_value:
                            search_value.remove('')
                        new_domain = ['|'] + domain + [['default_code', 'in', tuple(search_value)]]
                        break
        except:
            # avoid affect other search types
            pass
        query = super()._where_calc(new_domain, active_test)
        return query