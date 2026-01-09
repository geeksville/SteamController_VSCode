import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")

from gi.repository import Gtk, Adw

from src.backend.PluginManager import PluginBase

KEY_HOSTNAME = "hostname"
KEY_PORT = "port"

DEFAULT_HOSTNAME = "localhost"
DEFAULT_PORT = 3710


class PluginSettings:
    _hostname: Adw.EntryRow
    _port_spin: Adw.SpinRow

    def __init__(self, plugin_base: PluginBase):
        self._plugin_base = plugin_base
        self._settings_cache = None

    def get_settings_area(self) -> Adw.PreferencesGroup:
        # Info row with hyperlink
        info_label = Gtk.Label(
            use_markup=True,
            label='Note: You must install <a href="https://marketplace.visualstudio.com/items?itemName=eliostruyf.vscode-remote-control">this VS Code extension</a> to use this plugin.',
        )
        info_label.set_wrap(True)

        self._hostname = Adw.EntryRow(title="Hostname")
        self._port_spin = Adw.SpinRow.new_with_range(1, 65535, 1)
        self._port_spin.set_title("Port number")

        self._hostname.connect("changed", self._on_hostname_changed)
        self._port_spin.connect("changed", self._on_port_changed)

        self._load_settings()

        pref_group = Adw.PreferencesGroup()
        pref_group.set_title("VS Code Connection Settings")
        pref_group.add(info_label)
        pref_group.add(self._hostname)
        pref_group.add(self._port_spin)
        return pref_group

    def _get_cached_settings(self):
        """Get settings from cache or load from storage."""
        if self._settings_cache is None:
            self._settings_cache = self._plugin_base.get_settings()
        return self._settings_cache

    def _invalidate_cache(self):
        """Invalidate settings cache after modifications."""
        self._settings_cache = None

    def _load_settings(self):
        settings = self._get_cached_settings()
        hostname = settings.get(KEY_HOSTNAME, DEFAULT_HOSTNAME)
        port = settings.get(KEY_PORT, DEFAULT_PORT)
        self._hostname.set_text(hostname)
        self._port_spin.set_value(port)

    def _update_settings(self, key: str, value):
        settings = self._get_cached_settings()
        settings[key] = value
        self._plugin_base.set_settings(settings)
        self._invalidate_cache()

    def _on_hostname_changed(self, entry):
        val = entry.get_text().strip()
        self._update_settings(KEY_HOSTNAME, val)

    def _on_port_changed(self, spin):
        val = int(spin.get_value())
        self._update_settings(KEY_PORT, val)
