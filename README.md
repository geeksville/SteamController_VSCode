# StreamController VSCode

A plugin to control Visual Studio Code from your [StreamController](https://streamcontroller.github.io/docs/latest/) device.  

This little plugin adds 'standard' VSCode opertions as buttons available for your Stream Deck.  Steps to install/use:

1. Install [StreamController](https://streamcontroller.github.io/docs/latest/installation/)
2. In VSCode install [this](https://marketplace.visualstudio.com/items?itemName=eliostruyf.vscode-remote-control) plugin (we need it to send commands to the VSCode process on port 3710).  Note: I am not authors of that plugin, but it seems fine to me.
2. Go to the StreamController 'store' inside the app and install "StreamController VSCode"
3. Click to add action buttons, a bunch of standard buttons are defined (Open terminal..., Step-In, Step-Over etc...).  But you can also use the "Any Command" action to run arbitrary VSCode commands.  After adding the action, set the command name to the foo.blah.blah VSCode command and add any (optional) arguments.
4. Actions have default icons and colors but you can change as you wish.

## Developing

If you'd like to modify this plugin.  Use these [instructions](https://streamcontroller.github.io/docs/latest/plugin_dev/setup/#8-rename-the-plugintemplate-directory).  The stock StreamController github project includes a working devcontainer.  Run the following to test this plugin in your IDE:

```
mkdir -p ./data/pages/backups ./data/plugins
git clone <this repo> ./data/plugins/com_geeksville_vscode
python3 main.py --data ./data/
```

## License and copyright

GPL V3 License, Copyright 2026 Kevin Hester, kevinh@geeksville.com

