import cherrypy
import glob
import os

class HelloWorld(object):

    def repositories(self):        
        myFiles = [] 
        for dirpaths, dirnames, filenames in os.walk('/home/mars/gitTests'):
            for name in dirnames:
                if name.endswith('.git') and name != '.git':
                    myFiles.append('git clone mars@mars-pc:' +  os.path.join(dirpaths, name)+'<br />')

                       
        return myFiles        
    
    def index(self):
        #superRoot = os.getcwd()
        #os.chdir("/home/mars/programmieren/python/")

        return self.repositories()         

    index.exposed = True


cherrypy.quickstart(HelloWorld())