# -*- coding: utf-8 -*-
"""
Python Markdown

A Python implementation of John Gruber's Markdown.

Documentation: https://python-markdown.github.io/
GitHub: https://github.com/Python-Markdown/markdown/
PyPI: https://pypi.org/project/Markdown/

Started by Manfred Stienstra (http://www.dwerg.net/).
Maintained for a few years by Yuri Takhteyev (http://www.freewisdom.org).
Currently maintained by Waylan Limberg (https://github.com/waylan),
Dmitry Shachnev (https://github.com/mitya57) and Isaac Muse (https://github.com/facelessuser).

Copyright 2007-2019 The Python Markdown Project (v. 1.7 and later)
Copyright 2004, 2005, 2006 Yuri Takhteyev (v. 0.2-1.6b)
Copyright 2004 Manfred Stienstra (the original version)

License: BSD (see LICENSE.md for details).
"""

from markdown.test_tools import TestCase


class TestNotEmphasis(TestCase):

    def test_standalone_asterisk(self):
        self.assertMarkdownRenders(
            '*',
            '<p>*</p>'
        )

    def test_standalone_understore(self):
        self.assertMarkdownRenders(
            '_',
            '<p>_</p>'
        )

    def test_standalone_asterisk_in_text(self):
        self.assertMarkdownRenders(
            'foo * bar',
            '<p>foo * bar</p>'
        )

    def test_standalone_understore_in_text(self):
        self.assertMarkdownRenders(
            'foo _ bar',
            '<p>foo _ bar</p>'
        )

    def test_standalone_asterisks_in_text(self):
        self.assertMarkdownRenders(
            'foo * bar * baz',
            '<p>foo * bar * baz</p>'
        )

    def test_standalone_understores_in_text(self):
        self.assertMarkdownRenders(
            'foo _ bar _ baz',
            '<p>foo _ bar _ baz</p>'
        )

    def test_standalone_asterisks_with_newlines(self):
        self.assertMarkdownRenders(
            'foo\n* bar *\nbaz',
            '<p>foo\n* bar *\nbaz</p>'
        )

    def test_standalone_understores_with_newlines(self):
        self.assertMarkdownRenders(
            'foo\n_ bar _\nbaz',
            '<p>foo\n_ bar _\nbaz</p>'
        )

    def test_standalone_asterisks_at_end(self):
        self.assertMarkdownRenders(
            'foo * bar *',
            '<p>foo * bar *</p>'
        )

    def test_standalone_understores_at_begin_end(self):
        self.assertMarkdownRenders(
            '_ bar _',
            '<p>_ bar _</p>'
        )
