import sys
import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw

# Construct GTK Window
class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Things will go here

        # Main Window Layout Box
        self.box_main = Gtk.Box()
        self.set_child(self.box_main)

        # Button
        self.button_hello = Gtk.Button(label='Hello')
        self.button_hello.connect('clicked', self.hello_world)
        self.box_main.append(self.button_hello)

    # Window Functions

    def hello_world(self, button):
        """ Print 'Hello, World!' to stdout """
        print('Hello, World!')
        
# Libadwaita
class MyApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()

# Run App
app = MyApp(application_id='io.github.thekrafter.LearningGTK')
app.run(sys.argv)