import sys
import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw, Gio

# Construct GTK Window
class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Things will go here

        # Main Window Layout 
        self.box_meta = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.box_main = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.box_sub = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        #self.box_meta.append(self.box_main)
        #self.box_meta.append(self.box_sub)
        self.set_child(self.box_meta)

        #self.set_default_size(600, 250)
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
        self.radio_a.connect('toggled', self.radio_handle, 'A')
        self.radio_b = Gtk.CheckButton(label='Radio B')
        self.radio_b.connect('toggled', self.radio_handle, 'B')
        self.radio_c = Gtk.CheckButton(label='Radio C')
        self.radio_c.connect('toggled', self.radio_handle, 'C')

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

        # Switch
        ## Switch
        self.switch = Gtk.Switch()
        self.switch.set_active(True) # Manually change value
        self.switch.connect("state-set", self.switch_handler, 'Switch')

        ## Style
        self.switch_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.switch_box.append(self.switch)
        self.margin_around(self.switch_box, 5)
        self.box_main.append(self.switch_box)

        ## Label
        self.label_switch = Gtk.Label(label='Turn it on or off!')
        self.switch_box.append(self.label_switch)
        self.switch_box.set_spacing(5)

        # Slider
        ## Scale
        self.scale = Gtk.Scale()
        self.scale.set_digits(0) # Number of decimal places
        self.scale.set_range(0, 10)
        self.scale.set_draw_value(True) # Show label with value of scale
        self.scale.set_value(5) # Manually change what its set to
        self.scale.connect('value-changed', self.slider_handler, 'Slider')
        
        ## Style
        self.margin_around(self.scale, 8)
        self.box_main.append(self.scale)

        # Button in Header Bar
        ## Header Bar
        self.header = Gtk.HeaderBar()
        self.set_titlebar(self.header)

        ## Button
        self.button_header = Gtk.Button(label='Click Me!')
        self.button_header.connect('clicked', self.button_handler, 'Home Button')
        self.header.pack_start(self.button_header)
        self.button_header.set_icon_name('user-home-symbolic') # Icon for button, from /usr/share/icons/Adwaita/scalable/*

        self.button_header_end = Gtk.Button()
        self.button_header_end.connect('clicked', self.button_handler, 'Open Button')
        self.header.pack_end(self.button_header_end)
        self.button_header_end.set_icon_name('folder-symbolic')

        # Adwaita Flap
        ## Flap
        self.flap_adw = Adw.Flap.new()
        self.flap_adw.set_reveal_flap(False)
        self.flap_adw.set_locked(True)

        ## Pages
        ### Stack of Pages
        self.flap_stack = Gtk.Stack.new()
        self.flap_adw.set_content(self.flap_stack)

        ### Page A
        self.page_a_content = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.page_a_content.append(self.box_main)
        self.flap_stack.add_titled(self.page_a_content, name='page_a', title='Page A')

        ### Page B
        self.page_b_content = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.page_b_content.append(self.box_sub)
        self.flap_stack.add_titled(self.page_b_content, name='page_b', title='Page B')




        ## Button
        self.button_flap = Gtk.ToggleButton.new()
        self.button_flap.set_icon_name('open-menu-symbolic')
        self.header.pack_start(self.button_flap)

        self.button_flap.connect('clicked', self.toggle_flap, self.flap_adw)


        # Open File
        ## Dialog
        self.open_dialog = Gtk.FileDialog.new()
        self.open_dialog.set_title('Pick a file!')

        ## File Filter
        self.filter = Gtk.FileFilter()
        self.filter.set_name('Image Files')
        self.filter.add_mime_type('image/jpeg')
        self.filter.add_mime_type('image/png')
        self.filter.add_mime_type('image/gif')
        self.filter.add_mime_type('image/tiff')

        self.filters = Gio.ListStore.new(Gtk.FileFilter)
        self.filters.append(self.filter)

        self.open_dialog.set_filters(self.filters)
        self.open_dialog.set_default_filter(self.filter)




    # Window Functions

    def hello_world(self, button):
        """ Print 'Hello, World!' to stdout """
        if self.check_bye.get_active():
            print("Goodbye, World!")
            self.close()
        else:
            print('Hello, World!')
    
    def button_handler(self, button, name):
        print(f'> {name} was pressed!')
        if name == 'Open Button':
            self.open_dialog.open(self, None, self.file_dialog_callback)

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

    def radio_handle(self, widget, radio):
        print(f'> Radio {radio} Toggled {"On" if widget.get_active() else "Off"}!')

    def switch_handler(self, switch, state, name):
        print(f"> {name} has been turned {'on' if state else 'off'}")

    def slider_handler(self, slider, name):
        print(f'> {name} set to {slider.get_value()}')

    def file_dialog_callback(self, dialog, result):
        try:
            file = dialog.open_finish(result)
            if file is not None:
                print(f'> Got file path {file.get_path()}')
                # Handle Loading File
        
        except BaseException as error:
            print(f'Error Opening File: {error.message}')

    def toggle_flap(self, button, flap):
        flap.set_reveal_flap(not flap.get_reveal_flap())
        print(f'> Flap is now {"visible" if flap.get_reveal_flap() else "hidden"}.')

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
