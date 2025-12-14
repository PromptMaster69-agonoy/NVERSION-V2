from kivy.core.text import LabelBase
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.properties import ObjectProperty, NumericProperty
from kivymd.theming import ThemeManager
from kivy.clock import Clock
from kivymd.uix.snackbar import MDSnackbar
from kivymd.uix.label import MDLabel
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.pickers import MDDatePicker, MDTimePicker
from kivy_garden.mapview import MapView, MapMarker, MapLayer
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp
from kivymd.uix.tooltip import MDTooltip
from kivymd.toast import toast
from kivy.graphics import Color, Line
import datetime
import sqlite3

Window.size = (360, 640)

LabelBase.register(
    name="OpenSans-VariableFont_wdth,wght",
    fn_regular="OpenSans-VariableFont_wdth,wght.ttf",
    fn_bold="OpenSans-Bold.ttf",
)

KV = """
MainWindow:
    id: manager
    LoginScreen:
        id: login
    SignupScreen:
    HomeScreen:
    ProfileScreen:
    ScheduleScreen:
        id: schedule_screen
    MapScreen:
    InboxScreen:
    PersonalInfoScreen:

<LoginScreen>
    name: "login"
    mobile_num: m_number
    password: password

    FloatLayout:
        FitImage:
            source: "login_bg.jpg"
        Image:
            source: "logo.png"
            size_hint: None, None
            size: "180dp", "180dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.86}

        MDLabel:
            text: "Log in"
            bold: True
            font_name: "OpenSans-VariableFont_wdth,wght"
            halign: "left"
            font_size: "22sp"
            valign: "center"
            size_hint: None, None
            pos_hint: {"x": 0.1, "top": 0.73}

        BoxLayout:
            orientation: "vertical"
            size_hint: 0.9, None
            height: self.minimum_height
            pos_hint: {"center_x": 0.5, "center_y": 0.43}
            padding: "20dp"
            spacing: "15dp"

            MDTextField:
                id: m_number
                hint_text: "Enter Student ID"
                font_name: "OpenSans-VariableFont_wdth,wght"
                font_size: "12sp"
                height: "50dp"
                mode: "fill"
                multiline: False
                pos_hint: {"center_x": 0.5}
                text_color_focus: 0, 0, 0, 1
                line_color_focus: 0, 0, 0, 1

            MDTextField:
                id: password
                hint_text: "Enter password"
                password: True
                font_name: "OpenSans-VariableFont_wdth,wght"
                font_size: "12sp"
                mode: "fill"
                pos_hint: {"center_x": 0.5}
                text_color_focus: 0, 0, 0, 1
                line_color_focus: 0, 0, 0, 1

            MDRectangleFlatButton:
                text: "Login"
                size_hint_x: 1
                height: "55dp"
                text_color: "black"
                font_name: "OpenSans-VariableFont_wdth,wght"
                pos_hint: {"center_x": 0.5}
                on_release: root.login_inter()

            MDRectangleFlatButton:
                text: "Signup"
                size_hint_x: 1
                height: "55dp"
                text_color: "black"
                font_name: "OpenSans-VariableFont_wdth,wght"
                pos_hint: {"center_x": 0.5}
                on_release: app.root.current = "signup"

<SignupScreen>
    name: "signup"
    create_num: c_number
    c_pass: c_pass
    v_pass: v_pass

    FloatLayout:
        FitImage:
            source: "signup_bg.jpg"
        MDLabel:
            text: "Sign in"
            bold: True
            font_name: "OpenSans-VariableFont_wdth,wght"
            halign: "left"
            font_size: "22sp"
            valign: "center"
            size_hint: None, None
            pos_hint: {"x": 0.1, "top": 0.73}
        Image:
            source: "logo.png"
            size_hint: None, None
            size: "180dp", "180dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.86}
        BoxLayout:
            orientation: "vertical"
            size_hint: 0.9, None
            height: self.minimum_height
            pos_hint: {"center_x": 0.5, "center_y": 0.38}
            padding: "20dp"
            spacing: "15dp"
            MDTextField:
                id: c_number
                hint_text: "Create mobile number"
                size_hint_x: None
                mode: "fill"
                font_name: "OpenSans-VariableFont_wdth,wght"
                pos_hint: {"center_x": 0.5}
                width: "280dp"
                font_size: "12sp"
                text_color_focus: 0, 0, 0, 1
                line_color_focus: 0, 0, 0, 1
            MDTextField:
                id: c_pass
                hint_text: "Create password"
                password: True
                mode: "fill"
                font_name: "OpenSans-VariableFont_wdth,wght"
                pos_hint: {"center_x": 0.5}
                size_hint_x: None
                width: "280dp"
                font_size: "12sp"
                text_color_focus: 0, 0, 0, 1
                line_color_focus: 0, 0, 0, 1
            MDTextField:
                id: v_pass
                hint_text: "Verify your password"
                font_name: "OpenSans-VariableFont_wdth,wght"
                pos_hint: {"center_x": 0.5}
                password: True
                mode: "fill"
                size_hint_x: None
                width: "280dp"
                font_size: "12sp"
                text_color_focus: 0, 0, 0, 1
                line_color_focus: 0, 0, 0, 1
            MDRectangleFlatButton:
                text: "Signup"
                size_hint_x: 1
                height: "55dp"
                font_name: "OpenSans-VariableFont_wdth,wght"
                pos_hint: {"center_x": 0.5}
                text_color: "black"
                on_release: root.signup_inter()
            MDRectangleFlatButton:
                text: "Back"
                size_hint_x: 1
                height: "55dp"
                text_color: "black"
                font_name: "OpenSans-VariableFont_wdth,wght"
                pos_hint: {"center_x": 0.5}
                on_release: root.go_back()

<HomeScreen>:
    name: "homepage"

    canvas.before:
        Color:
            rgba: 0.05, 0.06, 0.1, 1 
        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        orientation: "vertical"

        ScrollView:
            do_scroll_x: False

            BoxLayout:
                orientation: "vertical"
                padding: "20dp"
                spacing: "20dp"
                size_hint_y: None
                height: self.minimum_height
                width: root.width

                MDLabel:
                    id: welcome_label
                    text: "Welcome, Student!"
                    halign: "center"
                    font_style: "H5"
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1
                    bold: True
                    size_hint_y: None
                    height: dp(40)

                GridLayout:
                    cols: 1
                    spacing: "20dp"
                    size_hint_y: None
                    height: self.minimum_height

                    MDCard:
                        size_hint: None, None
                        size: root.width - dp(40), dp(80)  
                        elevation: 6
                        padding: "20dp"
                        radius: [15,]
                        md_bg_color: get_color_from_hex("#1F2937")
                        on_release: app.on_profile()

                        BoxLayout:
                            orientation: "vertical"
                            spacing: "5dp"

                            BoxLayout:
                                orientation: "horizontal"
                                spacing: "5dp"

                                MDLabel:
                                    text: "Profile"
                                    valign: "center"
                                    font_style: "H6"
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1
                                    pos_hint: {"center_y": 0.5}
                                    height: "40dp"

                            MDLabel:
                                text: "View and edit your profile information."
                                font_style: "Body2"
                                theme_text_color: "Custom"
                                text_color: 1, 1, 1, 1
                                size_hint_y: None
                                height: "20dp"
                                halign: "left"


                    MDCard:
                        size_hint: None, None
                        size: root.width - dp(40), dp(80)
                        elevation: 6
                        padding: "20dp"
                        radius: [15,]
                        md_bg_color: get_color_from_hex("#1F2937")
                        on_release: app.on_schedule()

                        BoxLayout:
                            orientation: "vertical"
                            spacing: "5dp"

                            BoxLayout:
                                orientation: "horizontal"
                                spacing: "5dp"

                                MDLabel:
                                    text: "Schedule"
                                    valign: "center"
                                    font_style: "H6"
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1
                                    pos_hint: {"center_y": 0.5}
                                    height: "40dp"

                            MDLabel:
                                text: "View and manage your daily events."
                                font_style: "Body2"
                                theme_text_color: "Custom"
                                text_color: 1, 1, 1, 1
                                size_hint_y: None
                                height: "20dp"
                                halign: "left"

                    MDCard:
                        size_hint: None, None
                        size: root.width - dp(40), dp(80)
                        elevation: 6
                        padding: "20dp"
                        radius: [15,]
                        md_bg_color: get_color_from_hex("#1F2937")
                        on_release: app.on_map()

                        BoxLayout:
                            orientation: "vertical"
                            spacing: "5dp"

                            BoxLayout:
                                orientation: "horizontal"
                                spacing: "5dp"

                                MDLabel:
                                    text: "Map"
                                    valign: "center"
                                    font_style: "H6"
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1
                                    pos_hint: {"center_y": 0.5}
                                    height: "40dp"

                            MDLabel:
                                text: "Locate places and navigate easily."
                                font_style: "Body2"
                                theme_text_color: "Custom"
                                text_color: 1, 1, 1, 1
                                size_hint_y: None
                                height: "20dp"
                                halign: "left"

                MDLabel:
                    text: "Pathfinding System"
                    font_style: "H5"
                    bold: True
                    halign: "left"
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1
                    padding_y: "10dp"
                    size_hint_y: None
                    height: dp(35)

                MDLabel:
                    text: "An intelligent campus navigation support system that guides users through a structured digital map. It interprets campus layout data to display connected campus paths between key locations such as academic buildings, offices, facilities, and landmarks. The system helps users better understand campus structure, explore possible directions, and recognize access points through clear visual path markers on the map."
                    font_style: "Caption"
                    halign: "left"
                    theme_text_color: "Custom"
                    text_color: 0.85, 0.85, 0.9, 1
                    size_hint_y: None
                    text_size: root.width - dp(40), None
                    max_lines: 8
                    shorten: False
                    height: dp(90)  


<ProfileScreen>:
    name: "profile"

    canvas.before:
        Color: 
            rgba: 10/255, 13/255, 20/255, 1
        Rectangle:
            pos: self.pos
            size: self.size    

    BoxLayout:
        orientation: "vertical"
        size_hint_y: None
        height: self.minimum_height        
        padding: "10dp"
        spacing: "10dp"
        pos_hint: {"top": 0.88}
        width: self.parent.width
        size_hint_x: 1

        OneLineListItem:
            text: "Personal Info"
            on_release: app.root.current = "information"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1

        OneLineListItem:
            text: "Logout"
            on_release: app.root.current = "login"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1


    MDTopAppBar:
        title: "Profile"
        pos_hint: {"top": 1}
        md_bg_color: get_color_from_hex("#0A0D14")
        specific_text_color: 1, 1, 1, 1
        elevation: 0

    BoxLayout:
        size_hint_y: None
        height: "56dp"
        pos_hint: {"y": 0}
        md_bg_color: 0.10, 0.13, 0.20, 1
        padding: "10dp"
        MDIconButton:
            icon: "home"
            on_release: app.on_home()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1
        MDIconButton:
            icon: "account"
            on_release: app.on_profile()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1
        MDIconButton:
            icon: "calendar"
            on_release: app.on_schedule()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1
        MDIconButton:
            icon: "map"
            on_release: app.on_map()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1
        MDIconButton:
            icon: "email"
            on_release: app.on_inbox()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1

<PersonalInfoScreen>:
    name: "information"

    canvas.before:
        Color:
            rgba: 10/255, 13/255, 20/255, 1
        Rectangle:
            pos: self.pos
            size: self.size

    ScrollView:
        do_scroll_x: False

        BoxLayout:
            orientation: "vertical"
            size_hint_y: None
            height: self.minimum_height
            padding: "20dp"
            spacing: "14dp"
            width: root.width

            MDLabel:
                text: "Personal Information"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                halign: "center"
                font_style: "H6"
                size_hint_y: None
                height: dp(20)

            BoxLayout:
                orientation: "horizontal"
                spacing: "12dp"
                size_hint_y: None
                height: dp(60)

                MDTextField:
                    id: last_name
                    hint_text: "First Name"
                    halign: "left"
                    mode: "fill"
                    size_hint_x: 0.5
                    text_color_normal: 1, 1, 1, 1
                    text_color_focus: 1, 1, 1, 1
                    hint_text_color_normal: 0.7, 0.7, 0.7, 1
                    hint_text_color_focus: 1, 1, 1, 1

                MDTextField:
                    id: first_name
                    hint_text: "Last Name"
                    halign: "left"
                    mode: "fill"
                    size_hint_x: 0.5
                    text_color_normal: 1, 1, 1, 1
                    text_color_focus: 1, 1, 1, 1
                    hint_text_color_normal: 0.7, 0.7, 0.7, 1
                    hint_text_color_focus: 1, 1, 1, 1

            MDLabel:
                text: "Course"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                halign: "left"
                font_style: "H6"
                size_hint_y: None
                height: dp(24)

            MDTextField:
                id: course
                hint_text: "Course"
                mode: "fill"
                text_color_normal: 1, 1, 1, 1
                text_color_focus: 1, 1, 1, 1
                hint_text_color_normal: 0.7, 0.7, 0.7, 1
                hint_text_color_focus: 1, 1, 1, 1
                max_lines: 2
                shorten: True
                shorten_from: "right"

            MDLabel:
                text: "Section"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                halign: "left"
                font_style: "H6"
                size_hint_y: None
                height: dp(24)

            MDTextField:
                id: section
                hint_text: "Section"
                mode: "fill"
                text_color_normal: 1, 1, 1, 1
                text_color_focus: 1, 1, 1, 1
                hint_text_color_normal: 0.7, 0.7, 0.7, 1
                hint_text_color_focus: 1, 1, 1, 1
                max_lines: 1
                shorten: True
                shorten_from: "right"

            MDLabel:
                text: "Year"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                halign: "left"
                font_style: "H6"
                size_hint_y: None
                height: dp(24)

            MDTextField:
                id: year
                hint_text: "Year (e.g., 2nd Year)"
                mode: "fill"
                text_color_normal: 1, 1, 1, 1
                text_color_focus: 1, 1, 1, 1
                hint_text_color_normal: 0.7, 0.7, 0.7, 1
                hint_text_color_focus: 1, 1, 1, 1
                max_lines: 1
                shorten: True
                shorten_from: "right"

            Widget:
                size_hint_y: None
                height: dp(10)  

    BoxLayout:
        size_hint_y: None
        height: "56dp"
        pos_hint: {"y": 0}
        md_bg_color: 0.10, 0.13, 0.20, 1
        padding: "10dp"

        MDIconButton:
            icon: "home"
            on_release: app.on_home()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1

        MDIconButton:
            icon: "account"
            on_release: app.on_profile()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1

        MDIconButton:
            icon: "calendar"
            on_release: app.on_schedule()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1

        MDIconButton:
            icon: "map"
            on_release: app.on_map()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1

        MDIconButton:
            icon: "email"
            on_release: app.on_inbox()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1

<ScheduleScreen>:
    name: "schedule"
    subject: subject
    building: building
    room: room
    day: day
    time_start: time_s
    time_end: time_e
    table_box: table_box

    canvas.before:
        Color: 
            rgba: 10/255, 13/255, 20/255, 1
        Rectangle:
            pos: self.pos
            size: self.size

    MDBoxLayout:
        orientation: "vertical"

        MDTopAppBar:
            title: "Class Schedule"
            md_bg_color: get_color_from_hex("#0A0D14")
            specific_text_color: 1, 1, 1, 1
            elevation: 0

        ScrollView:
            MDBoxLayout:
                orientation: "vertical"
                padding: "20dp"
                spacing: "15dp"
                size_hint_y: None
                height: self.minimum_height

                MDLabel:
                    text: "Schedule Details"
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1
                    font_style: "H6"
                    halign: "center"
                    size_hint_y: None
                    height: dp(30)

                MDLabel:
                    text: "Subject"
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1
                    font_style: "Body1"
                    halign: "left"
                    size_hint_y: None
                    height: dp(20)

                MDTextField:
                    id: subject
                    hint_text: "Enter Subject"
                    mode: "fill"
                    text_color_normal: 1, 1, 1, 1
                    text_color_focus: 1, 1, 1, 1
                    line_color_normal: 1, 1, 1, 1
                    line_color_focus: 1, 1, 1, 1
                    hint_text_color_normal: 0.7, 0.7, 0.7, 1
                    hint_text_color_focus: 1, 1, 1, 1

                MDLabel:
                    text: "Building"
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1
                    font_style: "Body1"
                    halign: "left"
                    size_hint_y: None
                    height: dp(20)

                MDTextField:
                    id: building
                    hint_text: "Select Building"
                    mode: "fill"
                    on_focus: if self.focus: root.building_picker()
                    text_color_normal: 1, 1, 1, 1
                    text_color_focus: 1, 1, 1, 1
                    line_color_normal: 1, 1, 1, 1
                    line_color_focus: 1, 1, 1, 1
                    hint_text_color_normal: 0.7, 0.7, 0.7, 1
                    hint_text_color_focus: 1, 1, 1, 1

                MDLabel:
                    text: "Room"
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1
                    font_style: "Body1"
                    halign: "left"
                    size_hint_y: None
                    height: dp(20)

                MDTextField:
                    id: room
                    hint_text: "Select Room"
                    readonly: True
                    mode: "fill"
                    on_touch_down:
                        if self.collide_point(*args[1].pos): root.room_picker()
                    read_only: True
                    text_color_normal: 1, 1, 1, 1
                    text_color_focus: 1, 1, 1, 1
                    line_color_normal: 1, 1, 1, 1
                    line_color_focus: 1, 1, 1, 1
                    hint_text_color_normal: 0.7, 0.7, 0.7, 1
                    hint_text_color_focus: 1, 1, 1, 1

                MDLabel:
                    text: "Day"
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1
                    font_style: "Body1"
                    halign: "left"
                    size_hint_y: None
                    height: dp(20)

                MDTextField:
                    id: day
                    hint_text: "Select Day"
                    readonly: True
                    mode: "fill"
                    on_focus: if self.focus: root.day_picker()
                    text_color_normal: 1, 1, 1, 1
                    text_color_focus: 1, 1, 1, 1
                    line_color_normal: 1, 1, 1, 1
                    line_color_focus: 1, 1, 1, 1
                    hint_text_color_normal: 0.7, 0.7, 0.7, 1
                    hint_text_color_focus: 1, 1, 1, 1

                MDBoxLayout:
                    spacing: "10dp"
                    size_hint_y: None
                    height: dp(60)

                    MDTextField:
                        id: time_s
                        hint_text: "Start Time"
                        readonly: True
                        mode: "fill"
                        on_focus: if self.focus: root.show_start_time()
                        text_color_normal: 1, 1, 1, 1
                        text_color_focus: 1, 1, 1, 1
                        line_color_normal: 1, 1, 1, 1
                        line_color_focus: 1, 1, 1, 1
                        hint_text_color_normal: 0.7, 0.7, 0.7, 1
                        hint_text_color_focus: 1, 1, 1, 1

                    MDTextField:
                        id: time_e
                        hint_text: "End Time"
                        readonly: True
                        mode: "fill"
                        on_focus: if self.focus: root.show_end_time()
                        text_color_normal: 1, 1, 1, 1
                        text_color_focus: 1, 1, 1, 1
                        line_color_normal: 1, 1, 1, 1
                        line_color_focus: 1, 1, 1, 1
                        hint_text_color_normal: 0.7, 0.7, 0.7, 1
                        hint_text_color_focus: 1, 1, 1, 1

                MDRaisedButton:
                    text: "Add Schedule"
                    md_bg_color: get_color_from_hex("#81C784")
                    pos_hint: {"center_x": 0.5}
                    on_release: root.add_schedule()

                MDLabel:
                    text: "Your Schedule"
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1
                    halign: "center"
                    font_style: "Subtitle1"
                    padding_y: "10dp"

                MDBoxLayout:
                    id: table_box
                    orientation: "vertical"
                    size_hint_y: None
                    height: dp(300)

    MDBoxLayout:
        size_hint_y: None
        height: "56dp"
        pos_hint: {"y": 0}
        md_bg_color: get_color_from_hex("#0A0D14")
        padding: "10dp"
        MDIconButton:
            icon: "home"
            on_release: app.on_home()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1
        MDIconButton:
            icon: "account"
            on_release: app.on_profile()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1
        MDIconButton:
            icon: "calendar"
            on_release: app.on_schedule()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1
        MDIconButton:
            icon: "map"
            on_release: app.on_map()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1
        MDIconButton:
            icon: "email"
            on_release: app.on_inbox()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1

<MapScreen>:
    name: "map"

    canvas.before:
        Color: 
            rgba: 10/255, 13/255, 20/255, 1
        Rectangle:
            pos: self.pos
            size: self.size     

    MapView:
        id: mapview
        lat: 16.93804
        lon: 121.76454
        zoom: 18  
        on_zoom:
            if self.zoom > 18: self.zoom = 18
            if self.zoom < 18: self.zoom = 18


    MDTopAppBar:
        id: toolbar
        title: "Map"
        pos_hint: {"top": 1}
        md_bg_color: get_color_from_hex("#0A0D14")
        specific_text_color: 1, 1, 1, 1
        elevation: 0
        left_action_items: [["menu", lambda x: root.create_menu(x)]]

    MDBoxLayout:
        size_hint_y: None
        height: "56dp"
        pos_hint: {"y": 0}
        md_bg_color: get_color_from_hex("#0A0D14")
        padding: "10dp"
        MDIconButton:
            icon: "home"
            on_release: app.on_home()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1
        MDIconButton:
            icon: "account"
            on_release: app.on_profile()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1
        MDIconButton:
            icon: "calendar"
            on_release: app.on_schedule()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1
        MDIconButton:
            icon: "map"
            on_release: app.on_map()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1
        MDIconButton:
            icon: "email"
            on_release: app.on_inbox()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1 


<InboxScreen>:
    name: "inbox"

    canvas.before:
        Color: 
            rgba: 10/255, 13/255, 20/255, 1
        Rectangle:
            pos: self.pos
            size: self.size    

    MDTopAppBar:
        title: "Inbox"
        pos_hint: {"top": 1}
        md_bg_color: get_color_from_hex("#0A0D14")
        specific_text_color: 1, 1, 1, 1
        elevation: 0


    BoxLayout:
        size_hint_y: None
        height: "56dp"
        pos_hint: {"y": 0}
        md_bg_color: 0.10, 0.13, 0.20, 1
        padding: "10dp"
        MDIconButton:
            icon: "home"
            on_release: app.on_home()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1
        MDIconButton:
            icon: "account"
            on_release: app.on_profile()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1
        MDIconButton:
            icon: "calendar"
            on_release: app.on_schedule()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1
        MDIconButton:
            icon: "map"
            on_release: app.on_map()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1
        MDIconButton:
            icon: "email"
            on_release: app.on_inbox()
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_x: 1
"""

VALID_ROOMS = {
    "Ramon Magsaysay": {
        "rooms": {"1st Floor": ["RM101", "RM102", "RM103"],
                  "2nd Floor": ["Abbreviation Room"]},
        "coords": (16.937715315657673, 121.76392437370077)
    },
    "CCSICT Building": {
        "rooms": {"1st Floor": ["IT101", "IT102", "IT103", "IT104"],
                  "2nd Floor": ["IT201", "IT202", "IT203", "IT204"],
                  "3rd Floor": ["IT301", "IT302", "IT303", "IT304"]},
        "coords": (16.938197528772875, 121.764063538908)
    },
    "CBM Building": {
        "rooms": {"2nd Floor": ["NB101"],
                  "3rd Floor": ["NB201"],
                  "4th Floor": ["NB301"]},
        "coords": (16.936043364524572, 121.76446658242533)
    },
    "CED Building": {
        "rooms": {"1st Floor": ["UBA", "UBB", "OB101"]},
        "coords": (16.93736905890547, 121.76374652183607)
    },
}


INTERSECTIONS = {
    "Int1_guardpost": (16.935905, 121.764017),
    "Int2_administrationB": (16.936217, 121.764092),
    "Int3_inside_building_left": (16.936343, 121.763921),
    "int4_volly_court": (16.936759, 121.764020),
    "Int5_left_road": (16.936779, 121.763883),
    "int6_left_road_to_chapel": (16.936138, 121.763760),
    "int6_front_sas": (16.937271, 121.763996),
    "Int7_front_magsaysay": (16.937844, 121.764130),
    "Int8_front_ccsict_near_gym": (16.938324, 121.764229),
    "Int9_front_poly_room": (16.938213, 121.764876),
    "Int10_front_educ_faculty": (16.937747, 121.764766),
    "Int11_front_cbm": (16.937077, 121.764618),
    "Int12_front_educ_elem": (16.936674, 121.764519),
    "Int13_basketball_court": (16.936697, 121.764414),
    "Int14_inside_building_right": (16.936220, 121.764259),
    "Int15_front_cbm_building": (16.936017, 121.764347),
    "front_of_ccscit_midman": (16.938095, 121.764178),
    "front_of_magsaysay_midman": (16.937580, 121.764060),
}

GRAPH = {
    "Int1_guardpost": {
        "Int2_administrationB": 36,
        "int6_left_road_to_chapel": 38,
        "Int15_front_cbm_building": 38
    },
    "Int2_administrationB": {
        "Int1_guardpost": 36,
        "Int3_inside_building_left": 23,
        "Int14_inside_building_right": 19
    },
    "Int3_inside_building_left": {
        "Int2_administrationB": 23,
        "int4_volly_court": 47,
    },
    "Int14_inside_building_right": {
        "Int2_administrationB": 19,
        "Int13_basketball_court": 55
    },
    "int4_volly_court": {
        "Int3_inside_building_left": 47,
        "Int5_left_road": 18
    },
    "Int5_left_road": {
        "int4_volly_court": 18,
        "int6_left_road_to_chapel": 72,
        "int6_front_sas": 56
    },
    "int6_left_road_to_chapel": {
        "Int1_guardpost": 38,
        "Int5_left_road": 72
    },
    "int6_front_sas": {
        "Int5_left_road": 56,
        "Int11_front_cbm": 73,
        "front_of_magsaysay_midman": 35,
        "SAS Building": 6,
    },
    "SAS Building": {
        "int6_front_sas": 6
    },
    "front_of_magsaysay_midman": {
        "Int7_front_magsaysay": 33,
        "int6_front_sas": 35,
        "Ramon Magsaysay": 12
    },
    "Ramon Magsaysay": {
        "front_of_magsaysay_midman": 12
    },
    "Int7_front_magsaysay": {
        "front_of_magsaysay_midman": 33,
        "front_of_ccscit_midman": 29,
        "Int10_front_educ_faculty": 70
    },
    "front_of_ccscit_midman": {
        "Int7_front_magsaysay": 33,
        "Int8_front_ccsict_near_gym": 26,
        "CCSICT Building": 9
    },
    "CCSICT Building": {
        "front_of_ccscit_midman": 9
    },
    "Int8_front_ccsict_near_gym": {
        "front_of_ccscit_midman": 26,
        "Int9_front_poly_room": 74
    },
    "Int9_front_poly_room": {
        "Int8_front_ccsict_near_gym": 74,
        "Int10_front_educ_faculty": 53
    },
    "Int10_front_educ_faculty": {
        "Int9_front_poly_room": 53,
        "Int11_front_cbm": 76,
        "Int7_front_magsaysay": 70
    },
    "Int11_front_cbm": {
        "Int10_front_educ_faculty": 76,
        "CED Building": 9,
        "int6_front_sas": 73,
        "Int12_front_educ_elem": 46,
    },
    "CED Building": {
        "Int11_front_cbm": 9
    },
    "Int12_front_educ_elem": {
        "Int11_front_cbm": 46,
        "Int13_basketball_court": 15,
        "Int15_front_cbm_building": 75
    },
    "Int13_basketball_court": {
        "Int12_front_educ_elem": 15,
        "Int14_inside_building_right": 55
    },
    "Int15_front_cbm_building": {
        "Int12_front_educ_elem": 75,
        "Int1_guardpost": 38,
        "CBM Building": 7
    },
    "CBM Building": {
        "Int15_front_cbm_building": 7
    }
}

ALL_NODES = {**INTERSECTIONS}
for building, data in VALID_ROOMS.items():
    ALL_NODES[building] = data["coords"]

def dijkstra(graph, start, end):
    if start not in graph or end not in graph:
        return [], float("inf")

    dist = {node: float("inf") for node in graph}
    prev = {node: None for node in graph}
    dist[start] = 0
    unvisited = set(graph.keys())

    while unvisited:
        current = min(unvisited, key=lambda node: dist[node])
        unvisited.remove(current)

        if dist[current] == float("inf"):
            break

        for neighbor, cost in graph.get(current, {}).items():
            alt = dist[current] + cost
            if alt < dist[neighbor]:
                dist[neighbor] = alt
                prev[neighbor] = current

    path = []
    node = end
    while node is not None:
        path.insert(0, node)
        node = prev.get(node)

    return path, dist.get(end, float("inf"))

class Database:
    def __init__(self):
        self.db = sqlite3.connect('login_db')
        self.cursor = self.db.cursor()
        self.create_table()

    def create_table(self):
        query1 = """CREATE TABLE IF NOT EXISTS users (
                                    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    stud_num INTEGER UNIQUE NOT NULL,
                                    password TEXT NOT NULL)"""

        self.cursor.execute(query1)
        self.db.commit()

    def sign_up(self, stud_num, password):
        query = "INSERT INTO users (stud_num, password) VALUES (?, ?)"
        self.cursor.execute(query, (stud_num, password))
        self.db.commit()

    def check_existing(self, stud_num):
        query = "SELECT stud_num FROM users WHERE stud_num=?"
        self.cursor.execute(query, (stud_num,))
        return self.cursor.fetchone()

    def log_in(self, stud_num, password):
        query = "SELECT user_id FROM users WHERE stud_num=? AND password=?"
        self.cursor.execute(query, (stud_num, password))
        result = self.cursor.fetchone()

        if result:
            self.current_user_id = result[0]
        else:
            self.current_user_id = None

        return result


class RouteLine(MapLayer):
    def __init__(self, points, **kwargs):
        super().__init__(**kwargs)
        self.points = points

    def reposition(self):
        self.canvas.clear()
        if not self.points or len(self.points) < 2:
            return

        mapview = self.parent
        if not mapview:
            return

        with self.canvas:
            Color(1, 0, 0, 1)
            line_points = []

            for node in self.points:
                if node in ALL_NODES:
                    lat, lon = ALL_NODES[node]
                    x, y = mapview.get_window_xy_from(lat, lon, mapview.zoom)
                    line_points.extend([x, y])

            if len(line_points) >= 4:
                Line(points=line_points, width=dp(3))
class LoginScreen(Screen):
    mobile_num = ObjectProperty(None)
    password = ObjectProperty(None)

    def __init__(self, data=None, **kwargs):
        super().__init__(**kwargs)
        self.db = data if data else Database()

    def login_inter(self):
        stud_num = self.mobile_num.text
        passw = self.password.text

        if not stud_num or not passw:
            self.manager.show_message("Please fill in all fields.")
            return

        if not stud_num.isdigit():
            self.manager.show_message("Student number must be digits only.")
            return

        stud_num = int(stud_num)

        result = self.db.log_in(stud_num, passw)

        if result:
            self.manager.show_message("Welcome to Homepage!")
            self.manager.current = "homepage"
            self.mobile_num.text = ""
            self.password.text = ""
        else:
            self.manager.show_message("Invalid credentials.")
            self.password.text = ""
class SignupScreen(Screen):
    create_num = ObjectProperty(None)
    c_pass = ObjectProperty(None)
    v_pass = ObjectProperty(None)

    def __init__(self, data=None, **kwargs):
        super().__init__(**kwargs)
        self.db = data if data else Database()

    def signup_inter(self):
        stud_num = self.create_num.text
        pw1 = self.c_pass.text
        pw2 = self.v_pass.text

        if not stud_num or not pw1 or not pw2:
            self.manager.show_message("Please fill in all fields.")
            return

        if not stud_num.isdigit():
            self.manager.show_message("Student number must be digits only.")
            return

        stud_num = int(stud_num)

        if self.db.check_existing(stud_num):
            self.manager.show_message("Account already exists.")
            return

        if pw1 != pw2:
            self.manager.show_message("Passwords do not match.")
            self.v_pass.text = ""
            return

        self.db.sign_up(stud_num, pw1)
        self.manager.show_message("Account created successfully!")
        self.create_num.text = ""
        self.c_pass.text = ""
        self.v_pass.text = ""

    def go_back(self):
        self.manager.current = "login"
class HomeScreen(Screen):
    pass
class ProfileScreen(Screen):
    pass
class PersonalInfoScreen(Screen):
    pass
class ScheduleScreen(Screen):
    subject = ObjectProperty(None)
    building = ObjectProperty(None)
    room = ObjectProperty(None)
    day = ObjectProperty(None)
    time_start = ObjectProperty(None)
    time_end = ObjectProperty(None)
    table_box = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dialog = None

    def on_pre_enter(self):
        if not hasattr(self, "table_created"):
            self.table_created = True
            self.create_table()

    def create_table(self):
        self.table = MDDataTable(
            use_pagination=True,
            check=False,
            column_data=[
                ("Subject", dp(30)),
                ("Building", dp(25)),
                ("Room", dp(20)),
                ("Day", dp(20)),
                ("Start", dp(20)),
                ("End", dp(20)),
                ("", dp(20)),
            ],
            row_data=[],
            size_hint=(1, 0.45),
            pos_hint={"center_x": 0.5},
            rows_num=4,
        )
        self.table.bind(on_row_press=self.on_row_press)
        self.table_box.add_widget(self.table)

    def on_row_press(self, instance_table, instance_row):
        row_index = instance_row.index // 7
        col_index = instance_row.index % 7

        if col_index == 6 and row_index < len(self.table.row_data):
            row_data = self.table.row_data[row_index]
            self.show_delete_dialog(row_data, row_index)

    def show_delete_dialog(self, row_data, row_index):

        subject, building_name, room, day, time_start, time_end, _ = row_data

        self.dialog = MDDialog(
            title="Delete Schedule",
            text=f"Delete schedule for {subject} at {building_name} ({room})?",
            buttons=[
                MDFlatButton(
                    text="CANCEL",
                    on_release=lambda x: self.dialog.dismiss()
                ),
                MDRaisedButton(
                    text="DELETE",
                    md_bg_color=(1, 0, 0, 1),
                    on_release=lambda x: self.delete_selected_schedule(row_index)
                ),
            ],
        )
        self.dialog.open()

    def delete_selected_schedule(self, row_index):
        if 0 <= row_index < len(self.table.row_data):
            deleted_schedule = self.table.row_data.pop(row_index)

            self.table.row_data = self.table.row_data.copy()

            map_screen = self.manager.get_screen("map")
            if hasattr(map_screen, 'current_day') and map_screen.current_day == deleted_schedule[
                3]:
                map_screen.update_map_markers()

            self.manager.show_message("Schedule deleted!")

        if self.dialog:
            self.dialog.dismiss()

    def show_start_time(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(time=self.set_time)
        time_dialog.open()

    def set_time(self, instance, time_obj):
        self.ids.time_s.text = time_obj.strftime("%I:%M %p")

    def show_end_time(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(time=self.end_set_time)
        time_dialog.open()

    def end_set_time(self, instance, time_obj):
        self.ids.time_e.text = time_obj.strftime("%I:%M %p")

    def add_schedule(self):
        subject = self.ids.subject.text.strip()
        building_name = self.ids.building.text.strip()
        room = self.ids.room.text.strip().upper()
        day = self.ids.day.text.strip()
        time_start = self.ids.time_s.text.strip()
        time_end = self.ids.time_e.text.strip()

        if all([subject, building_name, room, day, time_start, time_end]):
            room_valid = False
            if building_name in VALID_ROOMS:
                for floor_rooms in VALID_ROOMS[building_name]["rooms"].values():
                    if room in floor_rooms:
                        room_valid = True
                        break

            if not room_valid:
                self.manager.show_message(f"Room {room} not in {building_name}")
                return

            self.table.row_data.append((subject, building_name, room, day, time_start, time_end, "Delete"))
            self.table.row_data = self.table.row_data.copy()

            self.ids.subject.text = ""
            self.ids.building.text = ""
            self.ids.room.text = ""
            self.ids.day.text = ""
            self.ids.time_s.text = ""
            self.ids.time_e.text = ""

            self.manager.show_message("Schedule added!")
        else:
            self.manager.show_message("Fill all fields")

    def day_picker(self):
        day_field = self.ids.day
        menu_items = [
            {
                "text": day,
                "viewclass": "OneLineListItem",
                "height": dp(48),
                "on_release": lambda x=day: self.set_day_value(x)
            }
            for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        ]

        self.day_menu = MDDropdownMenu(
            caller=day_field,
            items=menu_items,
            width_mult=4,
            radius=[24, 0, 24, 0],
            position="auto",
            max_height=dp(200)
        )
        self.day_menu.open()

    def set_day_value(self, value):
        self.ids.day.text = value
        if hasattr(self, "day_menu"):
            self.day_menu.dismiss()

    def building_picker(self):
        building_field = self.ids.building
        menu_items = [
            {
                "text": building,
                "viewclass": "OneLineListItem",
                "height": dp(48),
                "on_release": lambda x=building: self.set_building_value(x)
            }
            for building in VALID_ROOMS.keys()
        ]

        self.building_menu = MDDropdownMenu(
            caller=building_field,
            items=menu_items,
            width_mult=4,
            radius=[24, 0, 24, 0],
            position="auto",
            max_height=dp(200)
        )
        self.building_menu.open()

    def room_picker(self):
        building_name = self.ids.building.text.strip()
        if not building_name:
            self.manager.show_message("Select building first")
            return

        self.prepare_rooms_menu(building_name)

    def set_building_value(self, value):
        self.ids.building.text = value
        if hasattr(self, "building_menu") and self.building_menu:
            self.building_menu.dismiss()

        Clock.schedule_once(lambda dt: self.room_picker(), 0.1)

    def set_room_value(self, value):
        self.ids.room.text = value
        if hasattr(self, "room_menu") and self.room_menu:
            self.room_menu.dismiss()

    def prepare_rooms_menu(self, building_name):
        rooms_list = []
        building_data = VALID_ROOMS.get(building_name, {})
        if building_data:
            for floor_rooms in building_data["rooms"].values():
                rooms_list.extend(floor_rooms)

        if not rooms_list:
            self.manager.show_message("No rooms found")
            return

        menu_items = [
            {
                "text": room,
                "viewclass": "OneLineListItem",
                "height": dp(48),
                "on_release": lambda x=room: self.set_room_value(x)
            }
            for room in rooms_list
        ]

        self.room_menu = MDDropdownMenu(
            caller=self.ids.room,
            items=menu_items,
            width_mult=4,
            radius=[24, 0, 24, 0],
            position="auto",
            max_height=dp(200)
        )

        Clock.schedule_once(lambda dt: self.room_menu.open(), 0.1)
class BuildingMarker(MapMarker):
    def __init__(self, building_name="", **kwargs):
        super().__init__(**kwargs)
        self.size = (dp(30), dp(30))
        self.building_name = building_name

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            if self.on_release:
                self.on_release()
            return True
        return super().on_touch_down(touch)


class MapScreen(Screen):
    mapview = ObjectProperty(None)
    menu = ObjectProperty(None)
    markers = []
    route_lines = []
    current_selected_building = None
    current_day = None

    def dijkstra(self):
        pass

    def on_pre_enter(self):
        if not hasattr(self, "menu_created"):
            self.menu_created = True
        self.mapview = self.ids.mapview
        self.markers = []

    def create_menu(self,caller_widget):
        menu_items = [
            {
                "text": day,
                "viewclass": "OneLineListItem",
                "height": dp(48),
                "on_release": lambda x=day: self.menu_callback(x),
            }
            for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        ]

        self.menu = MDDropdownMenu(
            caller=caller_widget,
            radius=[24,0,24,0],
            position="auto",
            items=menu_items,
            width_mult=3,
            max_height=dp(200)
        )

        self.menu.open()

    def menu_callback(self, day):
        self.menu.dismiss()
        self.current_day = day
        self.show_markers_for_day(day)
        self.manager.show_message(f"Showing schedule for {day}")

    def show_markers_for_day(self, day):
        for marker in self.markers[:]:
            if marker.parent:
                self.mapview.remove_widget(marker)
        self.markers.clear()
        self.clear_routes()

        schedule_screen = self.manager.get_screen("schedule")

        if not hasattr(schedule_screen, "table") or schedule_screen.table is None:
            self.manager.show_message("No schedule table found")
            return

        buildings_with_classes = {}

        for entry in schedule_screen.table.row_data:
            # Now we have 7 columns: subject, building, room, day, start, end, delete_button
            if len(entry) >= 7:
                subject, building_name, room, sched_day, time_start, time_end, _ = entry[:7]
            else:
                continue

            if sched_day != day or not building_name:
                continue

            if building_name not in buildings_with_classes:
                buildings_with_classes[building_name] = []
            buildings_with_classes[building_name].append({
                "subject": subject,
                "room": room,
                "time": f"{time_start} - {time_end}"
            })

        for building_name, classes in buildings_with_classes.items():
            if building_name in VALID_ROOMS:
                lat, lon = VALID_ROOMS[building_name]["coords"]
                marker = BuildingMarker(lat=lat, lon=lon, building_name=building_name)
                marker.on_release = lambda b=building_name: self.show_building_dialog(b, classes)
                self.mapview.add_widget(marker)
                self.markers.append(marker)

        if not buildings_with_classes:
            self.manager.show_message(f"No classes found for {day}")
        else:
            self.manager.show_message(f"Found {len(buildings_with_classes)} building(s)")

    def update_map_markers(self):
        if self.current_day:
            self.show_markers_for_day(self.current_day)

    def show_building_dialog(self, building_name, classes=None):
        if building_name not in VALID_ROOMS:
            self.manager.show_message(f"Building {building_name} not found")
            return

        building = VALID_ROOMS[building_name]

        room_text = f"[b]{building_name}[/b]\n\n"

        for floor, rooms in building["rooms"].items():
            room_text += f"[b]{floor}[/b]\n"
            for r in rooms:
                room_text += f"• {r}\n"
            room_text += "\n"

        if classes:
            room_text += f"[b]Your Schedule Here[/b]\n"
            for cls in classes:
                room_text += f"{cls['subject']}\n"
                room_text += f"Room: {cls['room']}\n"
                room_text += f"Time: {cls['time']}\n\n"

        start_node = "Int1_guardpost"
        end_node = building_name

        path, distance = dijkstra(GRAPH, start_node, end_node)

        if path and distance < float("inf"):
            self.draw_route_to_building(building_name, path)

            path_text = f"\n[b]Path from Entrance[/b]\n"
            for i, node in enumerate(path):
                display_name = node.replace("_", " ").title()
                if node in VALID_ROOMS:
                    display_name = node
                path_text += f"{i + 1}. {display_name}\n"

            path_text += f"\nEstimated distance: {distance:.0f} meters"
            room_text += path_text
        else:
            room_text += "\n[b]No path found[/b]"

        dialog = MDDialog(
            title=f"",
            text=room_text,
            radius=[18, 18, 18, 18],
            size_hint=(0.9, 0.7),
            buttons=[
                MDRaisedButton(
                    text="CLOSE",
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def draw_route_to_building(self, building_name, path):
        self.clear_routes()

        self.current_selected_building = None

        for marker in self.markers:
            if marker.building_name == building_name:
                marker.size = (dp(20), dp(20))
                self.current_selected_building = building_name
            else:
                marker.size = (dp(15), dp(15))

        route_line = RouteLine(points=path)
        self.mapview.add_widget(route_line)
        self.route_lines.append(route_line)

        Clock.schedule_once(lambda dt: route_line.reposition(), 0.1)

        if building_name in VALID_ROOMS:
            lat, lon = VALID_ROOMS[building_name]["coords"]
            self.mapview.center_on(lat, lon)

    def clear_routes(self):
        for line in self.route_lines:
            if line in self.mapview.children:
                self.mapview.remove_widget(line)
        self.route_lines.clear()

        for marker in self.markers:
            marker.size = (dp(15), dp(15))

    def clear_all_markers(self):
        for marker in self.markers:
            if marker.parent:
                self.mapview.remove_widget(marker)
        self.markers.clear()
        self.clear_routes()
        self.current_selected_building = None


class InboxScreen(Screen):
    pass


class MainWindow(ScreenManager):
    students = {}

    def show_message(self, ms):
        MDSnackbar(MDLabel(text=ms)).open()

    def show_toast(self, ms):
        toast(text=ms, duration=1.5)

class ActuallyApp(MDApp):

    def build(self):
        root = Builder.load_string(KV)
        self.mapview = root.ids.mapview

        for name, (lat, lon) in VALID_ROOMS.items():
            marker1 = MapMarker(lat=lat, lon=lon)
            marker1.size = (dp(40), dp(40))
            marker1.size_hint = (None, None)
            self.mapview.add_widget(marker1)

        for name, (lat, lon) in INTERSECTIONS.items():
            marker = MapMarker(lat=lat, lon=lon)
            marker.size = (dp(40), dp(40))
            marker.size_hint = (None, None)
            self.mapview.add_widget(marker)

        return root

    def build_route(self, start, end):
        for layer in list(self.mapview.children):
            if isinstance(layer, RouteLine):
                self.mapview.remove_widget(layer)

        path = dijkstra(GRAPH, start, end)
        print("PATH:", path)
        route = RouteLine(path)
        self.mapview.add_widget(route)

    def build(self):
        self.theme_cls = ThemeManager()
        self.theme_cls.primary_palette = "Gray"
        root = Builder.load_string(KV)
        return root

    def on_home(self):
        self.root.current = "homepage"

    def on_profile(self):
        self.root.current = "profile"

    def on_information(self):
        self.root.current = "information"

    def on_schedule(self):
        self.root.current = "schedule"

    def on_map(self):
        self.root.current = "map"

    def on_inbox(self):
        self.root.current = "inbox"


if __name__ == "__main__":
    ActuallyApp().run()