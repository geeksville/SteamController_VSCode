# PluginTemplate

A simple plugin you can use as a starting point for your amazing creations!

For more information checkout [the docs](https://streamcontroller.github.io/docs/latest/).

## Developing

If you'd like to modify this plugin.  Use these [instructions](https://streamcontroller.github.io/docs/latest/plugin_dev/setup/#8-rename-the-plugintemplate-directory).  The stock StreamController github project includes a working devcontainer.  Run the following to test this plugin in your IDE:

```
mkdir -p ./data/pages/backups ./data/plugins
git clone <this repo> ./data/plugins/com_geeksville_vscode
python3 main.py --data ./data/
```
