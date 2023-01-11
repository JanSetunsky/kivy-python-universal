class SharedEvents():
    def build(self):
        shared_events = {
            "main_app_config":{
                "app_name":"Python Universal",
                "root_name":"python_uni"
                },                
            "spy_app_config":{
                "app_name":"Spy App",
                "root_name":"spy_app"
                },            
            "web_server":{
                "event_status":False,
                "event_list":{
                    ""
                    }
                },
            "authentication":{
                "event_status":False,
                "event_list":{
                    ""
                    }
                }
            }
        return shared_events
