class WebServer():
    def __init__(self, **kwargs):
        self.event_arguments = kwargs
    def build(self):
        def start_web_server(arguments):
            from os.path import join, exists, abspath
            from os import mkdir
            from flask import Flask, render_template, redirect, url_for, request
            spy_app_name = arguments["spy_app_config"]["app_name"]
            spy_app_root = arguments["spy_app_config"]["root_name"]
            global_path = abspath('d:\\python_kivy\\projects\\python_BrowserApp-v.0.3.1\\data')
            templates_path = global_path+'\\www\\templates\\'
            static_path = global_path+'\\www\\static\\'
            api = Flask(__name__, template_folder=templates_path, static_folder=static_path)            

            @api.route('/'+spy_app_root, methods=['GET'])
            def page_preloader_index():
                return render_template(spy_app_root+"/preloader/index.html")
            
            @api.route('/'+spy_app_root+'/home', methods=['GET'])
            def page_home_index():
                return render_template(spy_app_root+"/home/index.html").format(AppName=spy_app_name)
            
            @api.route('/'+spy_app_root+'/dashboard', methods=['GET'])
            def page_dashboard_index():
                return render_template(spy_app_root+"/dashboard/index.html").format(AppName=spy_app_name)
            
            @api.route('/'+spy_app_root+'/terminal', methods=['GET'])
            def page_terminal_index():
                return render_template(spy_app_root+"/terminal/index.html").format(AppName=spy_app_name)
            
            @api.route('/'+spy_app_root+'/tools', methods=['GET'])
            def page_tools_index():
                return render_template(spy_app_root+"/tools/index.html").format(AppName=spy_app_name)
            
            @api.route('/'+spy_app_root+'/exit', methods=['GET'])
            def page_exit_index():
                shutdown = request.environ.get('werkzeug.server.shutdown')
                if shutdown is None:
                    raise RuntimeError('Not running with the Werkzeug Server')
                shutdown()
                return 'exit'
     


                
            api.run('127.0.0.1', port=5000, threaded=True, debug=False)
        from threading import Thread
        self.server_thread = Thread(target=start_web_server, args=(self.event_arguments, ))
        return self.server_thread
    

from app_events import SharedEvents
global shared_events
shared_events = SharedEvents().build()
test = WebServer(**shared_events).build().start()

"""
from multiprocessing import Process

server = Process(target=WebServer().build().start())
server.start()
# ...
server.terminate()
server.join()
"""


