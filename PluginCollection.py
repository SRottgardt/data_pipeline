import inspect
import os
import pkgutil
from modules.IPlugin import IPlugin

# Credits https://github.com/gdiepen/python_plugin_example

class PluginCollection(object):

    def __init__(self, plugin_package):
        self.plugin_package = plugin_package
        self.loading_plugins()

    def loading_plugins(self):
        """Loading all Plugins"""
        self.loadedPlugins = []
        self.searchedPaths = []
        print()
        print("Searching Plugins")
        self.searchPlugins(self.plugin_package)

    def getLoadedPlugins(self):
        return self.loadedPlugins

    def getPluginsCommands(self):
        plugincommands = []
        for plugin in self.loadedPlugins:
            plugincommands.append(plugin.pluginCommand)
        return plugincommands

    def getPluginByCommand(self, _command):
        _plugin = None
        for plugin in self.loadedPlugins:
            if (plugin.pluginCommand == _command):
                _plugin = plugin
        return _plugin
        
        
    def searchPlugins(self, package):
        """Plugin search Method - """
        imported_package = __import__(package, fromlist=[""])

        for _, pluginname, ispkg in pkgutil.iter_modules(imported_package.__path__, imported_package.__name__ + "."):
            if not ispkg:
                plugin_module = __import__(pluginname, fromlist=[""])
                clsmembers = inspect.getmembers(plugin_module, inspect.isclass)
                for (_, c) in clsmembers:
                    # Only add classes that are a sub class of Plugin, but NOT Plugin itself
                    if issubclass(c, IPlugin) & (c is not IPlugin):
                        print("    Found plugin: %s" % (c.__name__))
                        self.loadedPlugins.append(c())

        all_current_paths = []
        if isinstance(imported_package.__path__, str):
            all_current_paths.append(imported_package.__path__)
        else:
            all_current_paths.extend([x for x in imported_package.__path__])

        for pkg_path in all_current_paths:
            if pkg_path not in self.searchedPaths:
                self.searchedPaths.append(pkg_path)

                # Get all sub directory of the current package path directory
                child_pkgs = [p for p in os.listdir(pkg_path) if os.path.isdir(os.path.join(pkg_path, p))]

                for child_pkg in child_pkgs:
                    self.searchPlugins(package + "." + child_pkg)
