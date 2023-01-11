from plyer import notification

import os
import sys
import signal
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.config import Config

Config.set('graphics', 'resizable', True)
from os import listdir
from textwrap import fill
from threading import Thread, Event

from modules.app_events import SharedEvents
#from modules.web_browser import WebView
from modules.web_server import WebServer

global shared_events
shared_events = SharedEvents().build()

from kivy.uix.modalview import ModalView
from kivy.clock import Clock
from android.runnable import run_on_ui_thread
from jnius import autoclass, cast, PythonJavaClass, java_method

R = autoclass('android.R')
WebViewA = autoclass('android.webkit.WebView')
WebViewClient = autoclass('android.webkit.WebViewClient')
WebViewBackForwardList = autoclass('android.webkit.WebBackForwardList')

LayoutParams = autoclass('android.view.ViewGroup$LayoutParams')
LinearLayout = autoclass('android.widget.LinearLayout')
KeyEvent = autoclass('android.view.KeyEvent')
ViewGroup = autoclass('android.view.ViewGroup')
DownloadManager = autoclass('android.app.DownloadManager')
DownloadManagerRequest = autoclass('android.app.DownloadManager$Request')
Uri = autoclass('android.net.Uri')
Environment = autoclass('android.os.Environment')
Context = autoclass('android.content.Context')
PythonActivity = autoclass('org.kivy.android.PythonActivity')

from kivy.graphics import RenderContext
from kivy.uix.widget import Widget
from kivy.properties import ListProperty

class MainEventCatcher(Widget):
    events = ListProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(on_touch_down=self.catch_touch_event)
        self.bind(on_touch_move=self.catch_touch_event)
        self.bind(on_touch_up=self.catch_touch_event)
        self.bind(on_key_down=self.catch_key_event)
        self.bind(on_key_up=self.catch_key_event)
        self.size_hint = (1, 1)

        Window.bind(on_key_down=self.catch_key_down_event)
        
    def catch_key_down_event(self, window, key, *args):
        self.events.append(key)
        from os.path import exists
        from datetime import datetime
        time = datetime.now()
        string_time = time.strftime("%H-%M-%S---%f")
        command_name = 'MainEventCatcher_button'
        filename = '/storage/emulated/0/Download/app/log/'+command_name+string_time+'.txt'
        if not exists(filename):
            with open(filename, "w") as f_catch_key_down_event:
                f_catch_key_down_event.write("{} --- {} --- {} \n".format(string_time, str(window), str(key)))
                f_catch_key_down_event.close()
        else:
            with open(filename, "a") as f_catch_key_down_event:
                f_catch_key_down_event.write("{} --- {} --- {} \n".format(string_time, str(window), str(key)))
                f_catch_key_down_event.close()

    def catch_touch_event(self, instance, touch):
        self.events.append(touch)
        from os.path import exists
        from datetime import datetime
        time = datetime.now()
        string_time = time.strftime("%H-%M-%S---%f")
        command_name = 'MainEventCatcher_touch'
        filename = '/storage/emulated/0/Download/app/log/'+command_name+string_time+'.txt'
        if not exists(filename):
            with open(filename, "w") as f_catch_touch_event:
                f_catch_touch_event.write("{} --- {} --- {} \n".format(string_time, str(instance), str(touch)))
                f_catch_touch_event.close()
        else:
            with open(filename, "a") as f_catch_touch_event:
                f_catch_touch_event.write("{} --- {} --- {} \n".format(string_time, str(instance), str(touch)))
                f_catch_touch_event.close()

    def catch_key_event(self, instance, key):
        self.events.append(key)
        from os.path import exists
        from datetime import datetime
        time = datetime.now()
        string_time = time.strftime("%H-%M-%S---%f")
        command_name = 'MainEventCatcher_key'
        filename = '/storage/emulated/0/Download/app/log/'+command_name+string_time+'.txt'
        if not exists(filename):
            with open(filename, "w") as f_catch_key_event:
                f_catch_key_event.write("{} --- {} --- {} \n".format(string_time, str(instance), str(key)))
                f_catch_key_event.close()
        else:
            with open(filename, "a") as f_catch_key_event:
                f_catch_key_event.write("{} --- {} --- {} \n".format(string_time, str(instance), str(key)))
                f_catch_key_event.close()


class Spy_App_WebView(ModalView):
    # https://developer.android.com/reference/android/webkit/WebView
    
    def __init__(self, url, enable_javascript = False, enable_downloads = False,
                 enable_zoom = False, **kwargs):
        super().__init__(**kwargs)
        self.url = url
        self.enable_javascript = enable_javascript
        self.enable_downloads = enable_downloads
        self.enable_zoom = enable_zoom
        self.webview = None
        self.enable_dismiss = True
        self.open()
        
    @run_on_ui_thread        
    def on_open(self):
        mActivity = PythonActivity.mActivity
        webview = WebViewA(mActivity)
        webview.setWebViewClient(WebViewClient())
        webview.getSettings().setJavaScriptEnabled(self.enable_javascript)
        webview.getSettings().setBuiltInZoomControls(self.enable_zoom)
        webview.getSettings().setDisplayZoomControls(False)
        webview.getSettings().setAllowFileAccess(True) #default False api>29

        

        def Start_StopWatch():
            from datetime import datetime
            time_utc = datetime.utcnow() - datetime(1970, 1, 1)
            global global_stopwatch
            global_stopwatch = round((time_utc.total_seconds())*1000)
            
        def Refresh_StopWatch(ticks):
            global global_stopwatch
            global_stopwatch = ticks
            
        def Get_StopWatch():
            global global_stopwatch
            return global_stopwatch
        
        def Limit_StopWatch():
            return 1000       
            
        def WebViewEventCatcher_on_key(v, key_code, event):
            from datetime import datetime
            time_now = datetime.utcnow() - datetime(1970, 1, 1)
            ticks = round((time_now.total_seconds())*1000)
            string_time = str(ticks)
            command_name = 'WebViewEventCatcher_on_key'
            filenametest = '/storage/emulated/0/Download/app/log/'+command_name+string_time+'.txt'
            with open(filenametest, "x") as f_WebViewEventCatcher_on_key:
                f_WebViewEventCatcher_on_key.write("{} \n".format(str(key_code)))
            global_stopwatch_limit = Limit_StopWatch()
            global_stopwatch = Get_StopWatch()
            if ticks - global_stopwatch_limit > global_stopwatch:
                Refresh_StopWatch(ticks)            
                if key_code == 4:
                    history_instance = webview.copyBackForwardList()
                    current_index = history_instance.getCurrentIndex()
                    remaining_index = current_index - 1
                    if remaining_index > 0:
                        webview.goBackOrForward(-1)
                    elif webview.is_running:
                        webview.is_running = False
                        app = App.get_running_app()
                        app.delete_self_browser()
                        self.dismiss()
                        return False
                    else:
                        return True
                return False
            return True
        
        def WebViewEventCatcher_on_touch(v, event):
            from datetime import datetime
            time_now = datetime.utcnow() - datetime(1970, 1, 1)
            ticks = round((time_now.total_seconds())*1000)
            string_time = str(ticks)
            command_name = 'WebViewEventCatcher_on_touch'
            filenametest = '/storage/emulated/0/Download/app/log/'+command_name+string_time+'.txt'
            with open(filenametest, "x") as f_WebViewEventCatcher_on_touch:
                f_WebViewEventCatcher_on_touch.write("{} \n".format(str(event)))
            return False

        Start_StopWatch()
        webview.setOnKeyListener(WebViewEventCatcher_on_key)
        webview.setOnTouchListener(WebViewEventCatcher_on_touch)
        webview.is_running = True
        layout = LinearLayout(mActivity)
        layout.setOrientation(LinearLayout.VERTICAL)
        layout.addView(webview, self.width, self.height)
        mActivity.addContentView(layout, LayoutParams(-1,-1))
        self.webview = webview
        self.layout = layout
        try:
            webview.loadUrl(self.url)
        except Exception as e:            
            print('Webview.on_open(): ' + str(e))
            self.dismiss()
        
    @run_on_ui_thread        
    def on_dismiss(self):
        if self.enable_dismiss:
            self.enable_dismiss = False
            parent = cast(ViewGroup, self.layout.getParent())
            if parent is not None: parent.removeView(self.layout)
            self.webview.clearHistory()
            self.webview.clearCache(True)
            self.webview.clearFormData()
            self.webview.destroy()
            self.layout = None
            self.webview = None


    @run_on_ui_thread
    def on_size(self, instance, size):
        if self.webview:
            params = self.webview.getLayoutParams()
            params.width = self.width
            params.height = self.height
            self.webview.setLayoutParams(params)

    def global_dismiss(self):
        self.webview.is_running = False
        app = App.get_running_app()
        app.delete_self_browser()
        self.dismiss()

    def pause(self):
        if self.webview:
            self.webview.pauseTimers()
            self.webview.onPause()

    def resume(self):
        if self.webview:
            self.on_ui_thread_resume()       

    @run_on_ui_thread
    def on_ui_thread_resume(self):
        self.webview.onResume()       
        self.webview.resumeTimers()
        MotionEvent = autoclass('android.view.MotionEvent')

        # Create a motion event
        event = MotionEvent.obtain(
            0, 0, MotionEvent.ACTION_DOWN, 0, 0, 0
        )
        # Dispatch the event to the webview
        self.webview.dispatchTouchEvent(event)
        # Recycle the event
        event.recycle()

    def on_back(self):
        if self.webview.canGoBack():
            self.webview.goBack()
        else:
            self.dismiss()  
        return True


class BrowserApp(App):
    def build(self):
        # Create main files and paths for handling
        from android.storage import app_storage_path
        from jnius import autoclass
        from os.path import join, exists, abspath
        from os import mkdir
        Environment = autoclass('android.os.Environment')
        root_app_path = join(app_storage_path(), Environment.DIRECTORY_DOCUMENTS)
        if not exists(root_app_path):
            mkdir(root_app_path)        
        
        main_app_name = shared_events["main_app_config"]["app_name"]
        main_root_name = shared_events["main_app_config"]["root_name"]

        spy_app_app_name = shared_events["spy_app_config"]["app_name"]
        spy_app_root_name = shared_events["spy_app_config"]["root_name"]
        
        main_app_logo_path = 'www/static/'+spy_app_root_name+'/assets/img/brand/light_logo.png'
        
        spy_app_preloader_space = join(root_app_path,'spy_app_space.html')
        spy_app_preloader_index = abspath('.')+'/www/templates/'+spy_app_root_name+'/preloader/index.html'

        self.server_build = WebServer(App,**shared_events)
        self.server_build.build().start()
        event_catcher = MainEventCatcher()
        self.browser = None
        self.main_layout = BoxLayout(orientation='vertical')
        self.box_layout = BoxLayout(orientation='vertical', spacing=10)
   
        main_app_logo = Image(source = main_app_logo_path)
        main_app_logo.allow_stretch = False
        main_app_logo.keep_ratio = False
        main_app_logo.size_hint = (1, None)
        main_app_logo.height = 300
        main_app_logo.width = 300
        
        main_app_label = Label(text = main_app_name)
        main_app_label.size_hint = (1, None)
        main_app_label.font_size = Window.width/15
        main_app_label.height = 150
        main_app_label.width = 300   
           
        b1 = Button(text = spy_app_app_name,
                    on_press = lambda *args: self.spy_app_start('b', spy_app_preloader_space,spy_app_preloader_index),
                    size_hint = (1, None),
                    height = 100)
        b2 = Button(text='TEST',
                    on_press = lambda *args: self.empty_button('b', main_app_name),
                    size_hint = (1, None),
                    height = 100)
        b3 = Button(text = 'Exit',
                    on_press = self.on_exit,
                    size_hint = (1, None),
                    height = 100)
        self.box_layout.add_widget(main_app_logo)
        self.box_layout.add_widget(main_app_label)
        self.box_layout.add_widget(b1)
        self.box_layout.add_widget(b2)
        self.box_layout.add_widget(b3)
        
        widget_count = 3
        #computing_height = (b1.height+b2.height+app_logo.height+(self.box_layout.spacing*2))/2
        #self.main_layout.pos = (0, (Window.height / 2 - self.main_layout.height / 2)*2-computing_height)
        computing_height = main_app_logo.height+main_app_label.height+b1.height+b2.height+b3.height
        self.main_layout.pos = (0, (Window.height / 2 - self.main_layout.height / 2)*2-computing_height)
        self.main_layout.size = (Window.width, Window.height)          
        self.main_layout.add_widget(self.box_layout)
        container = Widget()
        container.add_widget(event_catcher)
        event_catcher.add_widget(self.main_layout)
        float_layout = FloatLayout()
        float_layout.add_widget(container)
        self.update_layout()
        event_catcher.pos = (0, 0)
        event_catcher.size = (Window.width, Window.height)
        Window.bind(on_size=self.update_layout)
        self.bind(on_start=self.on_start)
        return float_layout
    
    def update_layout(self, *args):
        self.box_layout.pos = (0, 0)

    
    def on_start(self, *args):
        self.Start_StopWatch()
        Window.bind(on_key_down=self.on_key_down)    
    
    def Start_StopWatch(self):
        from datetime import datetime
        time_utc = datetime.utcnow() - datetime(1970, 1, 1)
        global global_stopwatch
        global_stopwatch = round((time_utc.total_seconds())*1000)
            
    def Refresh_StopWatch(self, ticks):
        global global_stopwatch
        global_stopwatch = ticks
            
    def Get_StopWatch(self):
        global global_stopwatch
        return global_stopwatch
        
    def Limit_StopWatch(self):
        return 1000         
    
    def on_key_down(self, instance, keycode, text, modifiers, *args):
        from datetime import datetime
        global_stopwatch_limit = self.Limit_StopWatch()
        global_stopwatch = self.Get_StopWatch()
        time_now = datetime.utcnow() - datetime(1970, 1, 1)
        ticks = round((time_now.total_seconds())*1000)
        if ticks - global_stopwatch_limit > global_stopwatch:
            self.Refresh_StopWatch(ticks)
            if keycode == 27:
                if self.browser:
                    self.browser = None
                    from datetime import datetime
                    time = datetime.now()
                    string_time = time.strftime("%H-%M-%S---%f")
                    command_name = 'back1111111'
                    filenametest = '/storage/emulated/0/Download/app/log/'+string_time+'---'+command_name+'.txt'
                    with open(filenametest, "x") as f:
                        f.write("{} \n".format('aaaaaaa'))
                    return False
                else:
                    from datetime import datetime
                    time = datetime.now()
                    string_time = time.strftime("%H-%M-%S---%f")
                    command_name = 'back222222'
                    filenametest = '/storage/emulated/0/Download/app/log/'+string_time+'---'+command_name+'.txt'
                    with open(filenametest, "x") as f:
                        f.write("{} \n".format('aaaaaaa'))            
                    return True
            elif keycode == 4:
                from datetime import datetime
                time = datetime.now()
                string_time = time.strftime("%H-%M-%S---%f")
                command_name = 'back333333333'
                filenametest = '/storage/emulated/0/Download/app/log/'+string_time+'---'+command_name+'.txt'
                with open(filenametest, "x") as f:
                    f.write("{} \n".format('aaaaaaa'))            
                return True 
            else:
                from datetime import datetime
                time = datetime.now()
                string_time = time.strftime("%H-%M-%S---%f")
                command_name = 'back4444444444'
                filenametest = '/storage/emulated/0/Download/app/log/'+string_time+'---'+command_name+'.txt'
                with open(filenametest, "x") as f:
                    f.write("{} \n".format('aaaaaaa'))            
                return True 
        return True
    
    def delete_self_browser(self):
        self.browser = None   

    def on_pause(self):
        if self.browser:
            self.browser.pause()
        return True

    def on_resume(self):
        if self.browser:
            self.browser.resume()
        pass

    def on_exit(self,b):
        #sys.exit(0)
        
        #app_pid = os.getpid()
        #os.kill(app_pid, signal.SIGKILL)  
        self.stop()
        
        os._exit(0)

    
    
    def send_notification(self, tag, app_name, title, message, ticker):
        from plyer import notification        
        
        def callback1():
            print('Button 1 clicked')
        
        def callback2():
            print('Button 2 clicked')
        
        buttons = [{'title': 'Button 1', 'callback': callback1},
                   {'title': 'Button 2', 'callback': callback2}]        
        
        hints = [{'urgency':bytes(1),
                  'category':'test category',
                  'resident':True}]
        
        notification.notify(
            app_name = app_name,
            title = title,
            message = message,
            ticker = ticker,
            toast = False,
            hints = hints,
            timeout = 5
        )

    def empty_button(self,b ,app_name):
        self.send_notification(app_name, 'Notifikace', 'Klikni pro otevření stránky WebView','Krátká zpráva ticket', 'unique_tag')

    def spy_app_start(self, b, preloader_space, preloader_index):
        from datetime import datetime
        global_stopwatch_limit = self.Limit_StopWatch()
        global_stopwatch = self.Get_StopWatch()
        time_now = datetime.utcnow() - datetime(1970, 1, 1)
        ticks = round((time_now.total_seconds())*1000)
        if ticks - global_stopwatch_limit > global_stopwatch:
            self.Refresh_StopWatch(ticks)
            self.spy_app_create_local_file(preloader_space, preloader_index)
            self.spy_app_view_local_file()
        pass

    def spy_app_view_local_file(self):
        self.browser = Spy_App_WebView('file://'+self.filename,
                               enable_javascript = True,
                               enable_downloads = True,
                               enable_zoom = True)

    def spy_app_create_local_file(self, preloader_space, preloader_index):
        self.filename = preloader_space
        with open(self.filename, "w") as f_preloader_path:
            f_preloader_path.write(open(preloader_index, "r").read())
            

from datetime import datetime
import logging
import os

# Nastavte logger na úroveň debug
logging.basicConfig(level=logging.DEBUG)

# Zkontrolujte, zda existuje složka pro ukládání logovacích souborů
log_folder = '/storage/emulated/0/Download/app/log/'
if not os.path.exists(log_folder):
    # Vytvořte složku pro ukládání logovacích souborů, pokud neexistuje
    os.makedirs(log_folder)

# Vytvořte logovací soubor s unikátním názvem
log_file = log_folder + 'app_' + datetime.now().strftime("%Y%m%d_%H%M%S") + '.txt'

# Vytvořte logger pro zápis do souboru
file_logger = logging.getLogger('file_logger')
file_logger.setLevel(logging.DEBUG)

# Přidejte logger pro zápis do souboru
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
file_logger.addHandler(file_handler)

# Zaznamenejte zprávu o spuštění aplikace
file_logger.debug('Spouštění aplikace')

try:
    # Spusťte aplikaci
    BrowserApp().run()
except Exception as e:
    # Zaznamenejte chybu do logu
    file_logger.exception(e)
finally:
    # Zaznamenejte zprávu o ukončení běhu aplikace
    file_logger.debug('Aplikace ukončena')
    