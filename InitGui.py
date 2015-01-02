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

class SheetMetalWorkbench( Workbench ):
  "Sheet Metal Workbench"
  Icon = """
/* XPM */
static char *dummy[]={
"32 32 3 1",
". c None",
"a c #0000ff",
"# c #303030",
"................................",
"........#############...........",
"........#aaaaaaaaaaaa#..........",
"........#aaaa###aaaaaa#.........",
"........#aaa#...#aaaaaa#........",
"........#aaa#...#aaaaaaa#.......",
"........#aaaa###aaaaaaaaa#......",
"........#aaaaaaaaaaaaaaaaa#.....",
"........####################....",
"......###aaaaaaaaaaaaaaaaaa#....",
"....##aa#aaaaaaaaaaaaaaaaaa#....",
"..##aaaa#aaaaaaaaaaaaaaaaaa#....",
".#aaa##a#aaaaaaaaaaaaaaaaaa#....",
".#aa#.#a#aaaaaaaaaaaaaaaaaa#....",
".#a#..#a#aaaaaaaaaaaaaaaaaa#....",
".#a#..#a#aaaaaaaaaaaaaaaaaa#....",
".#a#..#a#aaaaaaaaaaaaaaaaaa#....",
".#a#..#a#aaaaaaaaaaaaaaaaaa#....",
".#a#..#a#aaaaaaaaaaaaaaaaaa#....",
".#a####a#aaaaaaaaaaaaaaaaaa#....",
".#aaaaaa#aaaaaaaaaaaaaaaaaa#....",
".###########################....",
".............#aaaaaaaaaaaa#.....",
".............#a##########a#.....",
".............#a#........#a#.....",
".............#a#........#a#.....",
".............#a#........#a#.....",
".............#a#........#a#.....",
".............#a##########a#.....",
".............#aaaaaaaaaaaa#.....",
".............##############.....",
"................................"};"""
  
  MenuText = "Sheet Metal"
  ToolTip = "Sheet metal workbench"
  
  def GetClassName( self ):
    return "Gui::PythonWorkbench"
  
  def Initialize( self ):
    import SheetMetal
    
    self.tools = [ "CreateSMP",
                   "CreateRootFace",
                   "FlangedFace" ]
    
    FreeCAD.t = self.appendToolbar( "SheetMetalWorkbench", self.tools )
    self.appendMenu("SheetMetalWorkbench", self.tools )
    pass
  
  def Activated( self ):
    pass
  
  def Deactivated( self ):
    pass


FreeCADGui.addWorkbench( SheetMetalWorkbench )
