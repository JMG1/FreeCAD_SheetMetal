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
import FreeCAD, FreeCADGui
import commands as CM

App = FreeCAD
__dir__ = os.path.dirname(__file__)


class CreateSMP:
  def GetResources(self):
    return {'Pixmap' : __dir__ + '/icons/icon_newproject.png', 
            'MenuText' : 'New sheet metal project',
            'ToolTip': 'Adds a new sheet metal project to the document'}
  
  def IsActive(self):
    if FreeCADGui.ActiveDocument:
      return True
    else:
      return False
  
  def Activated(self):
    CM.NewSMP()
    


class CreateRootFace:
  # Create a face that would behave as the root of the project. Every new face,
  # flange or feature should be linked to this base face
  def GetResources(self):
    return {'Pixmap' : __dir__ + '/icons/icon_addbase.png',
            'MenuText' : 'Create Face',
            'ToolTip' : 'Create a new root face from sketch' }
  
  def IsActive(self):
    if FreeCADGui.ActiveDocument:
      return True
    else:
      return False
  
  def Activated(self):
    pass


class FlangedFace:
  # Create a new face with flange
  def GetResources(self):
    return {'Pixmap' : __dir__ + '/icons/icon_addflange.png',
            'MenuText' : 'Create Flanged Face',
            'ToolTip' : 'Create a new flanged face from sketch' }
  
  def IsActive(self):
    if FreeCADGui.ActiveDocument:
      return True
    else:
      return False
  
  def Activated(self):
    pass



if FreeCAD.GuiUp:
  FreeCADGui.addCommand('CreateSMP', CreateSMP() )
  FreeCADGui.addCommand('CreateRootFace', CreateRootFace() )
  FreeCADGui.addCommand('FlangedFace', FlangedFace() )
