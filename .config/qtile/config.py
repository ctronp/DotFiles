from typing import List  # noqa: F401

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal


from os import path
import subprocess

from libqtile.widget.currentlayout import CurrentLayoutIcon

from itertools import zip_longest

from libqtile.widget.textbox import TextBox

# autostart
@hook.subscribe.startup_once
def autostart():
    subprocess.call([path.join(path.expanduser(r'~'),'.config' ,'qtile' , 'autostart.sh')])


mod,shift,ctrl = "mod4","shift","control"
terminal = guess_terminal()

keys = [
    # Cambiar de focus
    Key([mod], "j", lazy.layout.down(),
        desc="Move focus down in stack pane"),
    Key([mod], "k", lazy.layout.up(),
        desc="Move focus up in stack pane"),
    Key([mod], "h", lazy.layout.left(),
        desc="Move focus left in stack pane"),
    Key([mod], "l", lazy.layout.right(),
        desc="Move focus right in stack pane"),
    
    # Cambiar de grupo
    Key([mod, ctrl], "h", lazy.screen.prev_group()),
    Key([mod, ctrl], "l", lazy.screen.next_group()),

    # Cambiar ancho focus
    Key([mod, ctrl], "k", lazy.layout.grow()),
    Key([mod, ctrl], "j", lazy.layout.shrink()),

    # Toggle floating
    Key([mod, "shift"], "f", lazy.window.toggle_floating()),

    # Mover paneles
    Key([mod, shift], "j", lazy.layout.shuffle_down(),
        desc="Move window down in current stack "),
    Key([mod, shift], "k", lazy.layout.shuffle_up(),
        desc="Move window up in current stack "),
    Key([mod, shift], "h", lazy.layout.shuffle_left(),
        desc="Move window left in current stack "),
    Key([mod, shift], "l", lazy.layout.shuffle_right(),
        desc="Move window right in current stack "),

    # Terminal y firefox
    Key([mod], "Return", lazy.spawn(terminal), desc="Inicia terminal"),
    Key([mod], "b", lazy.spawn("firefox"), desc="Inicia firefox"),

    # Cambiar Layout, y Eliminar ventanas.
    Key([mod], "Tab", lazy.next_layout(), desc="Cambia layout"),
    Key([mod, "shift"], "Tab", lazy.prev_layout(),
        desc="cambiar layout anterior"),
    Key([mod], "w", lazy.window.kill(), desc="Cerrar ventana"),

    # Reiniciar Qtile, Ejecutar comando
    Key([mod, ctrl], "r", lazy.restart(), desc="Reiniciar qtile"),
    
    
    # Explorador de archivos
    Key([mod], "e", lazy.spawn("pcmanfm-qt")),
    
    # Switch focus of monitors
    Key([mod], "period", lazy.next_screen()),
    Key([mod], "comma", lazy.prev_screen()),
    
    # rofi
    Key([mod], 'q', lazy.spawn("rofi -show drun")),
    Key([mod], 'r', lazy.spawn("rofi -show run")),
    Key([mod, shift], 'q', lazy.spawn("rofi -show")),
    #Key([mod], "r", lazy.spawncmd(), desc="ejecucion"),
    
    # Audios de teclado/notebook
    Key([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%")),
    Key([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),
    
    # Brillo pantalla
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
    
    # Screenshot
    Key([mod], "s", lazy.spawn("flameshot gui")),
    Key([mod, shift], "s", lazy.spawn("flameshot full -c")),
    
    # test
    #Key([mod], "t", lazy.screen.next_group()),
]

# se pueden remplazar por iconos en nerdfonts cheat sheet
groups = ["   ", " 2 ", " 3 ", " 4 ", " 5 ", " 6 ", " 7 "]


groups = [Group(i) for i in groups]

for enum,i in enumerate(groups):
    enum += 1
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], str(enum), lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, shift], str(enum), lazy.window.togroup(i.name, switch_group=False),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])


layout_conf = {
    'border_focus': "#a151d3",
    'border_width': 3,
    'margin': 5
}

layouts = [
    layout.MonadTall(**layout_conf),
    layout.Max(**layout_conf),
    # layout.Stack(**layout_conf, num_stacks=3),
    # Try more layouts by unleashing below layouts.
    # layout.Bsp(),
    layout.Columns(**layout_conf,
                   num_columns=3),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='UbuntuMono Nerd Font',
    fontsize=17,
    padding=0,
)
extension_defaults = widget_defaults.copy()

backgroundColor = ["#0f101a","#0f101a"]


screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    foreground=[ "#f1ffff", "#f1ffff"],
                    background=backgroundColor,
                    font='UbuntuMono Nerd Font',
                    fontsize=19,
                    margin_y=3,
                    margin_x=0,
                    padding_y=8,
                    padding_x=5,
                    borderwidth=1,
                    active=[ "#f1ffff", "#f1ffff"],
                    inactive=[ "#4c566a", "#4c566a"],
                    rounded=False,
                    highlight_method='block',
                    urgent_alert_method='block',
                    urgent_border=["#F07178","#F07178"],
                    this_current_screen_border=["#a151d3","#a151d3"],
                    this_screen_border=["#353c4a","#353c4a"],
                    other_current_screen_border=["#0f101a","#0f101a"],
                    other_screen_border=["#0f101a","#0f101a"],
                    disable_drag=True
                ),
                widget.Sep(
                    linewidth=0,
                    padding=6,
                    background=backgroundColor,
                    ),
                widget.Prompt(
                    fontsize=18,
                    font='UbuntuMono Nerd Font Bold',
                    foreground='#6ae6d3',
                    cursor_color='#6ae6d3',
                    background=backgroundColor
                ),
                widget.WindowName(
                        foreground=["#a151d3","#a151d3"],
                        background=backgroundColor,
                        fontsize=18,
                        font='UbuntuMono Nerd Font Bold',
                        ),
                widget.Systray(
                    background=backgroundColor,
                    padding=6
                    ),
                widget.Sep(
                    linewidth=0,
                    padding=6,
                    background=backgroundColor,
                    ),
                widget.TextBox(
                    background=backgroundColor,
                    foreground=["#F07178","#F07178"],
                    text="",
                    fontsize=37,
                    padding=-2
                ),
                widget.Sep(
                    linewidth=0,
                    padding=4,
                    background=["#F07178","#F07178"]
                    ),
                widget.CurrentLayoutIcon(
                    background=["#F07178","#F07178"],
                    foreground=["#0f101a","#0f101a"],
                    scale=0.65,
                    ),
                widget.CurrentLayout(
                    background=["#F07178","#F07178",],
                    foreground=["#0f101a","#0f101a"],
                    ),
                widget.Sep(
                    linewidth=0,
                    padding=5,
                    background=["#F07178","#F07178"]
                    ),
                widget.TextBox(
                    background=["#F07178","#F07178"],
                    foreground=["#a151d3","#a151d3"],
                    text="",
                    fontsize=37,
                    padding=-2
                ),
                widget.Sep(
                    linewidth=0,
                    padding=8,
                    background=["#a151d3","#a151d3"]
                    ),
                widget.TextBox(
                    background=["#a151d3","#a151d3"],
                    foreground=["#0f101a","#0f101a"],
                    text=' '                    
                ),
                widget.Clock(
                    background=["#a151d3","#a151d3"],
                    foreground=["#0f101a","#0f101a"],
                    padding=5,
                    format='%d-%m-%Y %I:%M %p'),
            ],
            26,
            opacity=0.92,
        ),
    ),Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    foreground=[ "#f1ffff", "#f1ffff"],
                    background=["#0f101a","#0f101a"],
                    font='UbuntuMono Nerd Font',
                    fontsize=19,
                    margin_y=3,
                    margin_x=0,
                    padding_y=8,
                    padding_x=5,
                    borderwidth=1,
                    active=[ "#f1ffff", "#f1ffff"],
                    inactive=[ "#4c566a", "#4c566a"],
                    rounded=False,
                    highlight_method='block',
                    urgent_alert_method='block',
                    urgent_border=["#F07178","#F07178"],
                    this_current_screen_border=["#a151d3","#a151d3"],
                    this_screen_border=["#353c4a","#353c4a"],
                    other_current_screen_border=["#0f101a","#0f101a"],
                    other_screen_border=["#0f101a","#0f101a"],
                    disable_drag=True
                ),
                widget.Prompt(),
                widget.WindowName(
                        foreground=["#a151d3","#a151d3"],
                        background=["#0f101a","#0f101a"],
                        fontsize=18,
                        font='UbuntuMono Nerd Font Bold',
                        ),
                widget.Sep(
                    linewidth=0,
                    padding=4,
                    background=["#F07178","#F07178"]
                    ),
                widget.CurrentLayoutIcon(
                    background=["#F07178","#F07178"],
                    foreground=["#0f101a","#0f101a"],
                    scale=0.65,
                    ),
                widget.CurrentLayout(
                    background=["#F07178","#F07178",],
                    foreground=["#0f101a","#0f101a"],
                    ),
                widget.Sep(
                    linewidth=0,
                    padding=5,
                    background=["#F07178","#F07178"]
                    ),
                widget.Sep(
                    linewidth=0,
                    padding=8,
                    background=["#a151d3","#a151d3"]
                    ),
                widget.TextBox(
                    background=["#a151d3","#a151d3"],
                    foreground=["#0f101a","#0f101a"],
                    text=' '                    
                ),
                widget.Clock(
                    background=["#a151d3","#a151d3"],
                    foreground=["#0f101a","#0f101a"],
                    padding=5,
                    format='%d-%m-%Y %I:%M %p'),
            ],
            26,
            opacity=0.92,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
], 
    border_focus="#a151d3",
                                  )
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
