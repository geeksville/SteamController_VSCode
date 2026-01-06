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

        hostname = Adw.EntryRow.new()
        hostname.set_title("Hostname")
        hostname.set_text(settings["hostname"])
        hostname.connect("changed", self.on_hostname_changed)

        port_spin = Adw.SpinRow.new_with_range(1, 65535, 1) 
        port_spin.set_title("Port number")
        port_spin.set_value(settings["port"])
        port_spin.connect("changed", self.on_port_changed)

        return [hostname, port_spin]

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

DEFAULT_COMMAND = "workbench.action.terminal.new"
class CustomCommand(VSMisc):
    def __init__(self, *args, **kwargs):
        super().__init__(DEFAULT_COMMAND, "code.png", None, *args, **kwargs)

    def on_key_down(self):
        settings = self.settings
        cmd = settings.get("command", DEFAULT_COMMAND)
        
        # Parse args from JSON string
        import json
        args_str = settings.get("args", "[]")
        try:
            cmd_args = json.loads(args_str)
            if not isinstance(cmd_args, list):
                cmd_args = None
        except (json.JSONDecodeError, ValueError):
            cmd_args = None
        
        run_vscode(cmd, cmd_args, hostname=settings["hostname"], port=settings["port"])

    def get_config_rows(self) -> list:
        settings = self.settings 

        command = Adw.EntryRow.new()
        command.set_title("Command")
        command.set_text(settings.get("command", DEFAULT_COMMAND))
        command.connect("changed", self.on_command_changed)

        args = Adw.EntryRow.new()
        args.set_title("Args")
        args.set_text(settings.get("args", "[]"))
        args.connect("changed", self.on_args_changed)

        return super().get_config_rows() + [command, args]

    def on_command_changed(self, command):
        settings = self.get_settings()
        settings["command"] = command.get_text()
        self.set_settings(settings)

    def on_args_changed(self, args):
        settings = self.get_settings()
        settings["args"] = args.get_text()
        self.set_settings(settings)

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