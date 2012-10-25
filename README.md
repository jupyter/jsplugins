# JavaScript Plugins for the IPython Notebook


## Overview

The IPython Notebook supports JavaScript plugins that extend the capabilities of the Notebook. This allows third party developers to create packages of code that can be easily installed and plugged into the Notebook by users.

A plugin is simply a directory with JavaScript and CSS files.  These files can be organized in any manner; as long as they are installed in the proper location, they will be loaded into the Notebook.

## Plugin installation

The IPython Notebook allows the user to provide their own assets in the `static` directory of any IPython profile. The `static` directory has a special subdirectory, `jsplugins`, where you can install your plugins. As a concrete example, let say you have a plugin with the following structure:

    /myplugin
        /js
            foo.js
            bar.js
        /css
            foo.css
            bar.css

To install this, you would simply cp this into your `/static/jsplugins` directory:
            
    $ cp -r myplugin ~/.ipython/profile_default/static/jsplugins

There are situations where a plugin will require additional Python code to work properly. In these cases, you should install that Python code just like you would any other Python code. Either run `setup.py install` or put it somewhere on your `PYTHONPATH`. If the code is an IPython extension, you can copy it into `~./ipython/extensions`.

## Plugin development

To create a plug in you should go through the following steps:

1. Clone this repository and create a branch.
2. Create a subdirectory for your plugin.
3. Put the needed JavaScript and CSS files in that subdirectory. Organize these files in any way you want.
4. You may also want to include Python code in your plugin.
4. Create a README.md that describes the plugin along with instructions for its installation. 
5. Send us a pull request.

Have a look at our existing plugins for examples.