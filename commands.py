# -*- coding: utf-8 -*-
# FreeCAD Sheet Metal workbench
# (c) 2015 Javier Martínez García

#***************************************************************************
#*   (c) Javier Martínez García 2015s                                       *   
#*                                                                         *
#*   This program is free software; you can redistribute it and/or modify  *
#*   it under the terms of the GNU Lesser General Public License (LGPL)    *
#*   as published by the Free Software Foundation; either version 2 of     *
#*   the License, or (at your option) any later version.                   *
#*   for detail see the LICENCE text file.                                 *
#*                                                                         *
#*   This macro is distributed in the hope that it will be useful,         *
#*   but WITHOUT ANY WARRANTY; without even the implied warranty of        * 
#*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
#*   GNU Lesser General Public License for more details.                   *
#*                                                                         *
#*   You should have received a copy of the GNU Library General Public     *
#*   License along with FreeCAD; if not, write to the Free Software        * 
#*   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
#*   USA                                                                   *
#*                                                                         *
#***************************************************************************/

import os
__dir__ = os.path.dirname(__file__)

import FreeCAD
App = FreeCAD
AAD = App.ActiveDocument

if FreeCAD.GuiUp:
	import FreeCADGui
	from FreeCADGui import PySideUic as uic
  
def NewSMP():
  # A dialog window to set the sheet metal project parameters will show up
  # All this parameters can be changed later without dialog by checking this
  # object features.
  # User accesible features: Thickness, bend radius, K factor, relief slot dimension
  # Operative features: base face, position, childs, bends, special geometries...
  # NewSheetMetalProject (NSMP)
  class NSMP:
    def __init__(self, obj):
      obj.addProperty("App::PropertyString",
                      "ProjectName",
                      "Project Data",
                      "SheetMetal Project Name").ProjectName = "SM_Project"
      
      #User accesible features:
      obj.addProperty("App::PropertyFloat",
                      "SheetThickness",
                      "Project Data",
                      "Sheet thickness")
      
      obj.addProperty("App::PropertyFloat",
                      "BendRadius",
                      "Project Data",
                      "Sheet bend radius")
      
      obj.addProperty("App::PropertyFloat",
                      "KFactor",
                      "Project Data",
                      "bend K factor" )
      
      #Data stored for algorithms
      obj.addProperty("App::PropertyMap",
                      "DataDictionaryA",
                      "Project Data"
                      "Internal data" )
      
      obj.addProperty("App::PropertyMap",
                      "DataDictionaryB",
                      "Project Data"
                      "Internal data" )
      
      obj.setEditorMode("DataDictionaryB", 2 )
      obj.Proxy = self

    def onChanged(self, fp, prop):
      pass

    def execute(self, fp):
      pass

  class ViewProviderNSMP:
    def __init__(self, obj):
      obj.Proxy = self
    
    def getIcon(self):
      return """
            /* XPM */
            static char *dummy[]={
            "32 32 2 1",
            ". c None",
            "# c #303030",
            "................................",
            "........#############...........",
            "........#............#..........",
            "........#....###......#.........",
            "........#...#...#......#........",
            "........#...#...#.......#.......",
            "........#....###.........#......",
            "........#.................#.....",
            "........####################....",
            "......###..................#....",
            "....##..#..................#....",
            "..##....#..................#....",
            ".#...##.#..................#....",
            ".#..#.#.#..................#....",
            ".#.#..#.#..................#....",
            ".#.#..#.#..................#....",
            ".#.#..#.#..................#....",
            ".#.#..#.#..................#....",
            ".#.#..#.#..................#....",
            ".#.####.#..................#....",
            ".#......#..................#....",
            ".###########################....",
            ".............#............#.....",
            ".............#.##########.#.....",
            ".............#.#........#.#.....",
            ".............#.#........#.#.....",
            ".............#.#........#.#.....",
            ".............#.#........#.#.....",
            ".............#.##########.#.....",
            ".............#............#.....",
            ".............##############.....",
            "................................"};
            """
    

  a=AAD.addObject("App::DocumentObjectGroupPython","SM_Project")
  NSMP(a)
  ViewProviderNSMP(a.ViewObject)
  AAD.recompute()


def NewSMPDialog():
  Dialog = uic.loadUi( __dir__ + '/gui/NewSMP.ui' )
  Dialog.show()
