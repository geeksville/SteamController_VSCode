# Import StreamController modules
import os
from src.backend.PluginManager.ActionBase import ActionBase

class NewTerminal(ActionBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.counter: int = 0

    def on_ready(self) -> None:
        icon_path = os.path.join(self.plugin_base.PATH, "assets", "info.png")
        self.set_media(media_path=icon_path, size=0.75)
        self.set_center_label(str(self.counter))

    def on_key_down(self):
        self.counter += 1
        self.set_center_label(str(self.counter))