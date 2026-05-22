# Stable QGIS Projects

## Plugin archived with QGIS 4

This plugin is [no longer needed with QGIS 4 since Qt6 provides a stable XML order](https://github.com/qgis/QGIS/issues/29192#issuecomment-2346274750) out of the box 🎉.
The QGIS 3 version of the plugin is still available.

## What 

QGIS project files (.qgs) are XML  files. They tend to change a lot when saving them on different machines. And therefore are hard to track in versioning systems like GIT because the XML attributes are ordered differently every time.

Install this plugin and it will make sure that attributes are ordered alphabetically whenever you save a QGIS file.

The plugin works best if it's used with QGIS ≥ 3.6.
