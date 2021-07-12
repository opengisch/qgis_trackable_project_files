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

import lxml.etree as ET
from qgis.core import QgsProject


def classFactory(iface):
    return StableProjectFile(iface)


class StableProjectFile:
    def __init__(self, iface):
        self.iface = iface

    def normalize_xml(self):
        project = QgsProject.instance()

        #  We don't do anything with qgz projects
        if project.isZipped():
            return

        # Anything but local files will return a pointer to the storage
        if project.projectStorage():
            return

        fn = project.fileName()
        try:
            with open(fn, 'r', encoding='utf-8') as file:
                et = ET.parse(file)
            et.write_c14n(fn)
        except FileNotFoundError:
            QgsMessageLog.logMessage(f"File {fn} not found, skipping normalisation.", 'trackable project files plugin', level=Qgis.Info)

    def initGui(self):
        self.project_saved_connection = \
            QgsProject.instance().projectSaved.connect(self.normalize_xml)

    def unload(self):
        p = QgsProject.instance()
        if p and self.project_saved_connection:
            p.projectSaved.disconnect(self.project_saved_connection)
