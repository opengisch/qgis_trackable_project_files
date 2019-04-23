# encoding: utf-8
# -----------------------------------------------------------
# Copyright (C) 2019 Matthias Kuhn
# -----------------------------------------------------------
# Licensed under the terms of GNU GPL 2
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# ---------------------------------------------------------------------


try:
    import lxml.etree as ET
except ImportError as e:
    message = "Missing lxml dependency. You can install by executing the following code in the QGIS Python console: "
    message += "import subprocess; "
    message += "subprocess.check_call(['python', '-m', 'pip', 'install', 'lxml'])"
    raise ImportError(message)

from qgis.core import QgsProject


def classFactory(iface):
    return StableProjectFile(iface)


class StableProjectFile:
    def __init__(self, iface):
        self.iface = iface

    def normalize_xml(self):
        fn = QgsProject.instance().fileName()
        with open(fn, "r") as file:
            et = ET.parse(file)
        et.write_c14n(fn)

    def initGui(self):
        self.project_saved_connection = QgsProject.instance().projectSaved.connect(
            self.normalize_xml
        )

    def unload(self):
        QgsProject.instance().projectSaved.disconnect(self.project_saved_connection)
