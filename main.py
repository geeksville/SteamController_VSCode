# Import StreamController modules

from .actions.vs_actions import NewTerminal, CustomCommand, Restart, Pause, Continue, StepIn, StepOut, StepOver, Stop
from src.backend.PluginManager.PluginBase import PluginBase
from src.backend.PluginManager.ActionHolder import ActionHolder

class PluginTemplate(PluginBase):
    def __init__(self):
        super().__init__()

        ## Register actions
        self.add_action_holder(ActionHolder(
            plugin_base = self,
            action_base = NewTerminal,
            action_id = "com_geeksville_vscode::NewTerminal", # Change this to your own plugin id
            action_name = "New Terminal",
        ))
        self.add_action_holder(ActionHolder(
            plugin_base = self,
            action_base = CustomCommand,
            action_id = "com_geeksville_vscode::CustomCommand",
            action_name = "Custom Command",
        ))
        self.add_action_holder(ActionHolder(
            plugin_base = self,
            action_base = Restart,
            action_id = "com_geeksville_vscode::Restart", # Change this to your own plugin id
            action_name = "Restart Debugging",
        ))
        self.add_action_holder(ActionHolder(
            plugin_base = self,
            action_base = Pause,
            action_id = "com_geeksville_vscode::Pause",
            action_name = "Pause Debugging",
        ))
        self.add_action_holder(ActionHolder(
            plugin_base = self,
            action_base = Continue,
            action_id = "com_geeksville_vscode::Continue",
            action_name = "Continue Debugging",
        ))
        self.add_action_holder(ActionHolder(
            plugin_base = self,
            action_base = StepIn,
            action_id = "com_geeksville_vscode::StepIn",
            action_name = "Step Into",
        ))
        self.add_action_holder(ActionHolder(
            plugin_base = self,
            action_base = StepOut,
            action_id = "com_geeksville_vscode::StepOut",
            action_name = "Step Out",
        ))
        self.add_action_holder(ActionHolder(
            plugin_base = self,
            action_base = StepOver,
            action_id = "com_geeksville_vscode::StepOver",
            action_name = "Step Over",
        ))
        self.add_action_holder(ActionHolder(
            plugin_base = self,
            action_base = Stop,
            action_id = "com_geeksville_vscode::Stop",
            action_name = "Stop Debugging",
        ))


        # Register plugin
        self.register(
            plugin_name = "SteamController VSCode",
            github_repo = "https://github.com/geeksville/SteamController_VSCode",
            plugin_version = "1.0.0",
            app_version = "1.1.1-alpha"
        )