"""

Simple example:

.. UIExample:: 50
    
    label = ui.Label(text='This is a label')

Interactive example:

.. UIExample:: 50
    from flexx import app, ui, event
    
    class Example(ui.Widget):
    
        def init(self):
            with ui.HBox():
                self.but = ui.Button(text='Push me')
                self.label = ui.Label(flex=1, wrap=True, text='This is a label. ')
        
        class JS:
            @event.connect('but.mouse_down')
            def _add_label_text(self, *events):
                self.label.text = self.label.text + 'Yes it is. '

"""

from ... import event
from ...pyscript import window
from . import Widget


class Label(Widget):
    """ Widget to show text/html.
    """
    
    CSS = """
        .flx-Label {
            border: 0px solid #454;
            /* phosphor sets this to none */
            user-select: text;
            -moz-user-select: text;
            -webkit-user-select: text;
            -ms-user-select: text;
        }"""
    
    @event.prop(both=True)
    def text(self, v=''):
        """ The text on the label.
        """
        return str(v)
    
    @event.prop(both=True)
    def wrap(self, v=False):
        """ Whether the content is allowed to be wrapped on multiple
        lines. Set to 0/False for no wrap, 1/True for word-wrap, 2 for
        character wrap.
        """
        return {0: 0, 1: 1, 2: 2}.get(v, int(bool(v)))
    
    class JS:
        
        def _init_phosphor_and_node(self):
            self.phosphor = window.phosphor.createWidget('div')
            self.node = self.phosphor.node
        
        @event.connect('text')
        def _text_changed(self, *events):
            self.node.innerHTML = self.text
        
        @event.connect('wrap')
        def _wrap_changed(self, *events):
            wrap = self.wrap
            self.node.style['word-wrap'] = ['initial', 'normal', 'break-word'][wrap]
            self.node.style['white-space'] = ['no-wrap', 'normal', 'normal'][wrap]
