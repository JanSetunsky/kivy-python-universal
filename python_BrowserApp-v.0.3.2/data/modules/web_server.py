class WebServer():
    def __init__(self, App, **kwargs):
        self.event_arguments = kwargs
        self.App = App
    def build(self):
        def start_web_server(arguments):
            from os.path import join, exists, abspath
            from os import mkdir
            from flask import Flask, render_template, request
            global path
            path = abspath('.')
            templates_path = path+'/www/templates/'
            static_path = path+'/www/static/'
            api = Flask(__name__, template_folder=templates_path, static_folder=static_path)            

            spy_app_name = arguments["spy_app_config"]["app_name"]
            spy_app_root = arguments["spy_app_config"]["root_name"]
            arguments["web_server"]["event_status"] = True

            @api.route('/'+spy_app_root, methods=['GET'])
            def page_preloader_index():
                return render_template(spy_app_root+"/preloader/index.html").format(AppName=spy_app_name)
            
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
                app = self.App.get_running_app()
                app.browser.global_dismiss()
                return 'exit'
            
            api.run('0.0.0.0', port=5000, threaded=True, debug=False)       
        from threading import Thread, Event
        event = Event()
        self.server_thread = Thread(target=start_web_server, args=(self.event_arguments, ))
        return self.server_thread    
