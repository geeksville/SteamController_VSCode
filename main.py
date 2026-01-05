# Import StreamController modules

from .actions.new_terminal import NewTerminal
from src.backend.PluginManager.PluginBase import PluginBase
from src.backend.PluginManager.ActionHolder import ActionHolder

class PluginTemplate(PluginBase):
    def __init__(self):
        super().__init__()

        ## Register actions
        self.counter_action_holder = ActionHolder(
            plugin_base = self,
            action_base = NewTerminal,
            action_id = "com_geeksville_vscode::NewTerminal", # Change this to your own plugin id
            action_name = "New Terminal",
        )
        self.add_action_holder(self.counter_action_holder)

        # Register plugin
        self.register(
            plugin_name = "SteamController VSCode",
            github_repo = "https://github.com/geeksville/SteamController_VSCode",
            plugin_version = "1.0.0",
            app_version = "1.1.1-alpha"
        )