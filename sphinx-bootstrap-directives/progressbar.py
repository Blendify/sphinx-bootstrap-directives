#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import division

import re
from docutils import nodes
from docutils.parsers.rst import directives, Directive

_re_size = re.compile("(\d+)(|%|px)$")


def get_size(d, key):
    if key not in d:
        return None
    m = _re_size.match(d[key])
    if not m:
        raise ValueError("invalid size %r" % d[key])
    return int(m.group(1)), m.group(2) or "px"


def css(d):
    return "; ".join(sorted("%s: %s" % kv for kv in d.items()))


class progressbar(nodes.General, nodes.Element):
    pass


def visit_progressbar_node(self, node):
    width = node["width"]

    self.body.append(self.starttag(node, "div", class="progress"))
    style = {
        "width": "%d%s" % width,
    }
    attrs = {
        "style": css(style),
    }
    self.body.append(self.starttag(node, "div", class="progress-bar", **attrs))
    self.body.append("</div></div>")


def depart_progressbar_node(self, node):
    pass


def nop_node(self, node):
    pass


class ProgressBar(Directive):
    has_content = True
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {
        "width": directives.unchanged,
    }

    def run(self):
        width = get_size(self.options, "width")
        return [
            progressbar(
                id=self.arguments[0],
                width=width,
                )
            ]


def setup(app):
    app.add_node(
            progressbar,
            html=(visit_progressbar_node, depart_progressbar_node),
            latex=(nop_node, nop_node),
            text=(nop_node, nop_node),
            )
    app.add_directive("progressbar.", ProgressBar)
    return {
        "parallel_read_safe": True,
    }
