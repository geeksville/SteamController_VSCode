# Import StreamController modules
import os
from src.backend.PluginManager.ActionBase import ActionBase
from .vs_client import run_vscode

# Import gtk
import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw

class VSCodeAction(ActionBase):
    def __init__(self, cmd: str | None, icon: str | None = None, cmd_args: list[str] | None = None, *args, **kwargs):
        self.icon = icon
        self.cmd = cmd
        self.cmd_args = cmd_args
        super().__init__(*args, **kwargs)

    def on_ready(self) -> None:
        if self.icon:
            icon_path = os.path.join(self.plugin_base.PATH, "assets", self.icon)
            self.set_media(media_path=icon_path, size=0.75)
        # self.set_center_label(str(self.counter))

    def on_key_down(self):
        # self.set_center_label(str(self.counter))
        settings = self.settings
        run_vscode(self.cmd, self.cmd_args, hostname=settings["hostname"], port=settings["port"])

    def get_config_rows(self) -> list:
        settings = self.settings 

        self.hostname = Adw.EntryRow.new()
        self.hostname.set_title("Hostname")
        self.hostname.set_text(settings["hostname"])
        self.hostname.connect("changed", self.on_hostname_changed)

        self.port_spin = Adw.SpinRow.new_with_range(1, 65535, 1) 
        self.port_spin.set_title("Port number")
        self.port_spin.set_value(settings["port"])
        self.port_spin.connect("changed", self.on_port_changed)

        return [self.hostname, self.port_spin]

    @property
    def settings(self):
        s = {
            "hostname": "localhost",
            "port": 3710,
        }
        s.update(self.get_settings())
        return s

    def on_hostname_changed(self, hostname):
        settings = self.get_settings()
        settings["hostname"] = hostname.get_text()
        self.set_settings(settings)

    def on_port_changed(self, port):
        settings = self.get_settings()
        settings["port"] = int(port.get_value())
        self.set_settings(settings)        

class VSMisc(VSCodeAction):
    def on_ready(self) -> None:
        super().on_ready()
        self.set_background_color([0x42, 0xa2, 0x32])  # Green background

class VSDebug(VSCodeAction):
    def on_ready(self) -> None:
        super().on_ready()
        self.set_background_color([0x4d, 0x1e, 0x89])  # Purple background

class NewTerminal(VSMisc):
    def __init__(self, *args, **kwargs):
        super().__init__("workbench.action.terminal.new", "terminal.png", None, *args, **kwargs)

class Restart(VSDebug):
    def __init__(self, *args, **kwargs):
        super().__init__("workbench.action.debug.restart", "replay.png", None, *args, **kwargs)

class Pause(VSDebug):
    def __init__(self, *args, **kwargs):
        super().__init__("workbench.action.debug.pause", "pause.png", None, *args, **kwargs)   

class Continue(VSDebug):
    def __init__(self, *args, **kwargs):
        super().__init__("workbench.action.debug.continue", "resume.png", None, *args, **kwargs)

class StepIn(VSDebug):
    def __init__(self, *args, **kwargs):
        super().__init__("workbench.action.debug.stepInto", "step_into.png", None, *args, **kwargs)

class StepOut(VSDebug):
    def __init__(self, *args, **kwargs):
        super().__init__("workbench.action.debug.stepOut", "step_out.png", None, *args, **kwargs)

class StepOver(VSDebug):
    def __init__(self, *args, **kwargs):
        super().__init__("workbench.action.debug.stepOver", "step_over.png", None, *args, **kwargs)     

class Stop(VSDebug):
    def __init__(self, *args, **kwargs):
        super().__init__("workbench.action.debug.stop", "stop.png", None, *args, **kwargs)                             