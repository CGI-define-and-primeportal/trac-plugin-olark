# -*- coding: utf-8 -*-

from trac.core import *
from trac.web import ITemplateStreamFilter
from trac.config import Option
from trac.web.chrome import ITemplateProvider, Chrome
from trac.util.text import javascript_quote

from genshi.filters.transform import Transformer
from genshi.core import Markup

import pkg_resources

class olark(Component):

    implements(ITemplateStreamFilter,
               ITemplateProvider)

    olark_identity = Option("olark","identity")


    # ITemplateProvider
    def get_htdocs_dirs(self):
        yield 'olark', pkg_resources.resource_filename(__name__,
                                                       'htdocs')

    def get_templates_dirs(self):
        yield pkg_resources.resource_filename(__name__, 'templates')

    
    # ITemplateStreamFilter

    def filter_stream(self, req, method, filename, stream, data):
        if self.olark_identity:

            template = Chrome(self.env).load_template('olark.html')
            shortname = self.env.path.split("/")[-1]
            jsblock = template.generate(visitor_name=javascript_quote("%s (%s) in %s" % (req.session.get('name'),
                                                                                         req.authname,
                                                                                         shortname)),
                                        identity=self.olark_identity)
            stream |= Transformer("//body").append(jsblock)

        return stream
