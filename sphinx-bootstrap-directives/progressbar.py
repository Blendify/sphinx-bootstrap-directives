#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from docutils import nodes
from docutils.parsers.rst import Directive


def setup(app):
    app.add_node(progressbar,
                 html=(visit_progressbar_node, depart_progressbar_node))

    app.add_directive('progressbar', ProgressbarDirective)

    return {'version': '0.0.1'}   # identifies the version of our extension

class progressbar(nodes.container, nodes.Element):
    pass

def visit_progressbar_node(self, node):
    self.visit_container(node)

def depart_progressbar_node(self, node):
    self.depart_container(node)


class ProgressbarDirective(Directive):

    # this disables content in the directive
    has_content = False

    def run(self):
        env = self.state.document.settings.env

        progressbar_node = progressbar('\n'.join(self.content))
        self.state.nested_parse(self.content, self.content_offset, progressbar_node)

        return [progressbar_node]
