from mako.template import Template
from mako.runtime import Context
import os

class mako:
    def __init__(self,name):
        self.name = name
        self.mako_file = "test1"

    def genhtml(self):
        mako_file = os.path.join(os.path.dirname(__file__),self.mako_file + ".mako")
        output_file = open(os.path.join(os.path.curdir,self.name + ".html"),"w")
        template_handle = Template(filename = mako_file)
        context = Context(output_file, component = self)
        template_handle.render_context(context)
        output_file.colse()

if __name__ == "__main__":
   
    name = "testhtml" 
    obj = mako()
    obj.genhtml()
