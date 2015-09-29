from trac.core import *
from trac.admin import IAdminPanelProvider
from trac.web.chrome import add_notice

class OlarkAdmin(Component):
    implements(IAdminPanelProvider)

    # IAdminPanelProvider
    
    def get_admin_panels(self, req):
        if req.perm.has_permission('TRAC_ADMIN'):
            yield ('olark', 'Olark', 'olark', 'Olark')

    def render_admin_panel(self, req, cat, page, path_info):
        if req.method == 'POST':
            self.config.set('olark', 'identity', req.args.get('identity'))
            self.config.save()
            add_notice(req, "Saved Olark identity")
            req.redirect(req.href.admin(cat, page))
                
        return 'olark_admin.html', {'identity': self.config.get('olark','identity')}
