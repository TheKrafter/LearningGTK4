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

        # Main Window Layout 
        self.box_meta = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.box_main = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.box_sub = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.box_meta.append(self.box_main)
        self.box_meta.append(self.box_sub)
        self.set_child(self.box_meta)

        self.set_default_size(600, 250)
        self.set_title('Learning GTK4')

        # Button Boxes
        self.box_horiz = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.box_main.append(self.box_horiz)

        # Button
        self.button_hello = Gtk.Button(label='Hello')
        self.button_hello.connect('clicked', self.hello_world)
        self.box_horiz.append(self.button_hello)

        ## Button Padding
        self.margin_around(self.button_hello, 10)

        # Check Button
        ## Box
        self.check_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        ## Button
        self.check_bye = Gtk.CheckButton(label='And goodbye?')

        ## Styling
        self.margin_around(self.check_bye, 10)
        self.check_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.check_box.append(self.check_bye)
        self.box_main.append(self.check_box)

        # Radio Button
        ## Buttons
        self.radio_a = Gtk.CheckButton(label='Radio A')
        self.radio_b = Gtk.CheckButton(label='Radio B')
        self.radio_c = Gtk.CheckButton(label='Radio C')

        ## Create Group
        self.radio_b.set_group(self.radio_a)
        self.radio_c.set_group(self.radio_a)

        ## Style
        self.margin_around(self.radio_a, 10, vert=3)
        self.margin_around(self.radio_b, 10, vert=3)
        self.margin_around(self.radio_c, 10, vert=3)
        self.radio_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.radio_box.append(self.radio_a)
        self.radio_box.append(self.radio_b)
        self.radio_box.append(self.radio_c)
        self.box_sub.append(self.radio_box)



    # Window Functions

    def hello_world(self, button):
        """ Print 'Hello, World!' to stdout """
        if self.check_bye.get_active():
            print("Goodbye, World!")
            self.close()
        else:
            print('Hello, World!')

    def margin_around(self, widget, margin: int, vert=None, horiz=None):
        if vert != None:
            widget.set_margin_top(vert)
            widget.set_margin_bottom(vert)
        else:
            widget.set_margin_top(margin)
            widget.set_margin_bottom(margin)
        if horiz != None:
            widget.set_margin_start(horiz)
            widget.set_margin_end(horiz)
        else:
            widget.set_margin_start(margin)
            widget.set_margin_end(margin)

    def radio_handle(self, radio):
        print(f'> Radio {radio} Toggled!')
        
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