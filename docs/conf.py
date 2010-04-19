# -*- coding: utf-8 -*-
#
# Astropysics documentation build configuration file, created by
# sphinx-quickstart on Wed Feb 24 00:07:20 2010.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.append(os.path.abspath('.'))

sys.path.insert(1,os.path.abspath('..')) #make sure it's on top except maybe local dirs

#with open(os.path.join('..','setup.py')) as f:
#    for l in f:
#        if 'version' in l:
#            break
#    else:
#        raise RuntimeError('could not locate setup.py to determine version')
#setup_version = l.split("'")[1]

from astropysics.version import version as setup_version

# -- General configuration -----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.intersphinx', 'sphinx.ext.todo', 
              'sphinx.ext.pngmath', 'sphinx.ext.inheritance_diagram',
              'sphinx.ext.coverage','sphinx.ext.ifconfig','sphinx.ext.doctest']
              #'matplotlib.sphinxext.plot_directive','matplotlib.sphinxext.ipython_console_highlighting']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Astropysics'
copyright = u'2010, Erik Tollerud'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '.'.join(setup_version.split('.')[:2])
# The full version, including alpha/beta/rc tags.
release = setup_version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = 'en'

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of documents that shouldn't be included in the build.
#unused_docs = []

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = ['_build']

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  Major themes that come with
# Sphinx are currently 'default' and 'sphinxdoc'.
html_theme = 'default'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {'rightsidebar':True,'stickysidebar':True}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = '../logo/logo.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_use_modindex = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = 'Astropysicsdoc'


# -- Options for LaTeX output --------------------------------------------------

# The paper size ('letter' or 'a4').
#latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
#latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'Astropysics.tex', u'Astropysics Documentation',
   u'Erik Tollerud', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# Additional stuff for the LaTeX preamble.
#latex_preamble = ''

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_use_modindex = True


intersphinx_mapping = {'http://docs.python.org/': None,
                       'http://docs.scipy.org/doc/numpy/': None,
                       'http://docs.scipy.org/doc/scipy/reference/': None,
                       'http://matplotlib.sourceforge.net/': None,
                       'http://pymc.googlecode.com/svn/doc/': None}

autoclass_content = 'both'

todo_include_todos = 'dev' in release

#<-------------Custom extension functionality-------------->
from sphinx.ext.todo import Todo,todo_node,nodes
from sphinx.pycode import ModuleAnalyzer,PycodeError

class TodoModule(Todo):
    required_arguments = 1
    has_content = True
    
    def run(self):        
        try:
            modfn = ModuleAnalyzer.for_module(self.arguments[0]).srcname
        except PycodeError,e:
            warnstr = "can't find module %s for todomodule: %s"%(self.arguments[0],e)
            return [self.state.document.reporter.warning(warnstr,lineno=self.lineno)]
        
        todolines = []
        with open(modfn) as f:
            for l in f:
                if l.startswith('#TODO'):
                    todolines.append(l)
                    
        todoreses = []
        for tl in todolines:
            text = tl.replace('#TODO:','').replace('#TODO','').strip()
            env = self.state.document.settings.env

            targetid = "todo-%s" % env.index_num
            env.index_num += 1
            targetnode = nodes.target('', '', ids=[targetid])
            
            td_node = todo_node(text)
            
            title_text = _('Module Todo')
            textnodes, messages = self.state.inline_text(title_text, self.lineno)
            td_node += nodes.title(title_text, '', *textnodes)
            td_node += messages
            if 'class' in self.options:
                classes = self.options['class']
            else:
                classes = ['admonition-' + nodes.make_id(title_text)]
            td_node['classes'] += classes
            
            td_node.append(nodes.paragraph(text,text))
            td_node.line = self.lineno
            
            todoreses.append(targetnode)
            todoreses.append(td_node)
        return todoreses


def setup(app):

    app.add_directive('todomodule', TodoModule) #add this directive to document TODO comments in the root of the module
