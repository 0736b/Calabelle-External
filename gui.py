import tkinter as tk
from tkinter import ttk
from threading import Thread
from core.core import Core, Process
from time import sleep


class App(ttk.Frame):

    def __init__(self, parent):

        ttk.Frame.__init__(self)

        # variables
        self.var_level = tk.StringVar()
        self.var_str = tk.StringVar()
        self.var_int = tk.StringVar()
        self.var_dex = tk.StringVar()
        self.var_pos = tk.StringVar()
        self.var_mapname = tk.StringVar()
        self.var_charname = tk.StringVar()
        self.var_proc = tk.StringVar()

        self.var_level.set('Level: ?')
        self.var_str.set('STR: ?')
        self.var_int.set('INT: ?')
        self.var_dex.set('DEX: ?')
        self.var_pos.set('X: ?, Y: ?')
        self.var_mapname.set('Map: ?')
        self.var_charname.set('Name: ?')
        self.var_proc.set('Process: NOT CONNECT')

        self.proc_connected = False

        self.setup_widgets()

    def setup_widgets(self):

        # Player
        self.check_frame = ttk.LabelFrame(
            self, text="[Player]", padding=(20, 10))
        self.check_frame.grid(
            row=0, column=1, padx=(20, 20), pady=(20, 10), sticky="nsew"
        )

        self.switch = ttk.Checkbutton(
            self.check_frame, text="GM", style="Switch.TCheckbutton"
        )
        self.switch.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

        self.switch = ttk.Checkbutton(
            self.check_frame, text="AOE", style="Switch.TCheckbutton"
        )
        self.switch.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

        self.switch = ttk.Checkbutton(
            self.check_frame, text="Range", style="Switch.TCheckbutton"
        )
        self.switch.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")

        self.switch = ttk.Checkbutton(
            self.check_frame, text="No Cooldown (BM)", style="Switch.TCheckbutton"
        )
        self.switch.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")

        self.switch = ttk.Checkbutton(
            self.check_frame, text="No Cooldown (Aura)", style="Switch.TCheckbutton"
        )
        self.switch.grid(row=4, column=0, padx=5, pady=5, sticky="nsew")

        self.switch = ttk.Checkbutton(
            self.check_frame, text="Killgate", style="Switch.TCheckbutton"
        )
        self.switch.grid(row=5, column=0, padx=5, pady=5, sticky="nsew")

        self.switch = ttk.Checkbutton(
            self.check_frame, text="NSD", style="Switch.TCheckbutton"
        )
        self.switch.grid(row=6, column=0, padx=5, pady=5, sticky="nsew")

        self.switch = ttk.Checkbutton(
            self.check_frame, text="Autocast", style="Switch.TCheckbutton"
        )
        self.switch.grid(row=7, column=0, padx=5, pady=5, sticky="nsew")

        self.switch = ttk.Checkbutton(
            self.check_frame, text="Movespeed (600)", style="Switch.TCheckbutton"
        )
        self.switch.grid(row=8, column=0, padx=5, pady=5, sticky="nsew")

        # Map
        self.map_frame = ttk.LabelFrame(self, text="[-]", padding=(20, 10))
        self.map_frame.grid(row=0, column=0, padx=(
            30, 30), pady=20, sticky="nsew")

        self.switch = ttk.Checkbutton(
            self.map_frame, text="Wallhack", style="Switch.TCheckbutton"
        )
        self.switch.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")

        self.accentbutton = ttk.Button(
            self.map_frame, text="Warp to dungeon", style="Accent.TButton"
        )
        self.accentbutton.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")

        self.label_map_name = ttk.Label(
            self.map_frame,
            text="Map: Desert Scream",
            justify="center",
            font=("-size", 8, "-weight", "normal"),
        )
        self.label_map_name.grid(row=2, column=0, pady=10, columnspan=2)

        self.label_pos = ttk.Label(
            self.map_frame,
            textvariable=self.var_pos,
            justify="center",
            font=("-size", 8, "-weight", "normal"),
        )
        self.label_pos.grid(row=3, column=0, pady=10, columnspan=2)

        self.label_level = ttk.Label(
            self.map_frame,
            textvariable=self.var_level,
            justify="center",
            font=("-size", 8, "-weight", "normal"),
        )
        self.label_level.grid(row=4, column=0, pady=10, columnspan=2)

        self.label_STR = ttk.Label(
            self.map_frame,
            textvariable=self.var_str,
            justify="center",
            font=("-size", 8, "-weight", "normal"),
        )
        self.label_STR.grid(row=5, column=0, pady=10, columnspan=2)

        self.label_INT = ttk.Label(
            self.map_frame,
            textvariable=self.var_int,
            justify="center",
            font=("-size", 8, "-weight", "normal"),
        )
        self.label_INT.grid(row=6, column=0, pady=10, columnspan=2)

        self.label_DEX = ttk.Label(
            self.map_frame,
            textvariable=self.var_dex,
            justify="center",
            font=("-size", 8, "-weight", "normal"),
        )
        self.label_DEX.grid(row=7, column=0, pady=10, columnspan=2)

        # Process
        self.proc_frame = ttk.LabelFrame(
            self, text="[Process]", padding=(20, 10))
        self.proc_frame.grid(
            row=3, column=0, padx=(20, 20), pady=20, sticky="nsew", columnspan=2
        )

        self.entry = ttk.Entry(self.proc_frame)
        self.entry.insert(0, "CabalMain.exe")
        self.entry.grid(row=0, column=0, padx=5, pady=(0, 10), sticky="ew")

        self.proc_connect_btn = ttk.Button(
            self.proc_frame, text="Connect", style="Accent.TButton", command= lambda: proc_attach_callback(self)
        )
        self.proc_connect_btn.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

        self.label = ttk.Label(
            self.proc_frame,
            textvariable=self.var_proc,
            justify="center",
            font=("-size", 8, "-weight", "bold"),
        )
        self.label.grid(row=2, column=0, pady=10)

        self.logo_img = tk.PhotoImage(file='gui/img/calabelle.PNG')
        self.label_logo = ttk.Label(
            self.proc_frame,
            image=self.logo_img
        )
        self.label_logo.grid(row=1, column=1, padx=10)

    def set_show_player_stats(self, p_level, p_str, p_int, p_dex, p_pos_x, p_pos_y):
        self.var_level.set('Level: ' + p_level)
        self.var_str.set('STR: ' + p_str)
        self.var_int.set('INT: ' + p_int)
        self.var_dex.set('DEX: ' + p_dex)
        self.var_pos.set('X: ' + p_pos_x + ', Y: ' + p_pos_y)
        self.var_mapname.set('Map: ?')
        self.var_charname.set('Name: ?')

def proc_attach_callback(app):
    global proc_name
    global is_attached
    global core_with_proc
    if not is_attached:
        proc_name = app.entry.get()
        core_with_proc = Core(proc_name)
        core_with_proc.get_addresses()
        app.var_proc.set('Process: CONNECTED')
        is_attached = True

def run_core(app):
    global core_with_proc
    while True:
        if core_with_proc != 0:
            if core_with_proc.is_game_running():
                Process.sleep(1)
                core_with_proc.gm_on()
                core_with_proc.range_on()
                core_with_proc.aoe_on()
                core_with_proc.movespd_on()
                core_with_proc.autocast_on()
                core_with_proc.auracd_on()
                core_with_proc.bm1cd_on()
                core_with_proc.bm2cd_on()
                core_with_proc.bm3cd_on()
                core_with_proc.wallhack_on()


def update_player_stat(app):
    global core_with_proc
    while True:
        if core_with_proc != 0:
            if core_with_proc.is_game_running():
                Process.sleep(1)
                t_level, t_str, t_int, t_dex, t_pos_x, t_pos_y = core_with_proc.get_player_stats()
                app.set_show_player_stats(t_level, t_str, t_int, t_dex, t_pos_x, t_pos_y)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Calabelle-External")

    root.tk.call("source", "gui/azure.tcl")
    root.tk.call("set_theme", "light")

    app = App(root)
    app.pack(fill="both", expand=True)

    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    root.maxsize(root.winfo_width(), root.winfo_height())
    x_cordinate = int((root.winfo_screenwidth() / 2) -
                      (root.winfo_width() / 2))
    y_cordinate = int((root.winfo_screenheight() / 2) -
                      (root.winfo_height() / 2))
    root.geometry("+{}+{}".format(x_cordinate, y_cordinate-20))
    root.resizable(False, False)

    proc_name = ""
    is_attached = False
    core_with_proc = 0

    core_thread = Thread(target=run_core, args=(app, ))
    core_thread.daemon = True
    update_p_stats = Thread(target=update_player_stat, args=(app, ))
    update_p_stats.daemon = True
    core_thread.start()
    update_p_stats.start()


    root.mainloop()