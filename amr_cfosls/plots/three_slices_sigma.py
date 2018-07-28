import argparse
#### import the simple module from the paraview
from paraview.simple import *

#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# Parsing the script input arguments
parser = argparse.ArgumentParser(description='Processing VTK output from MFEM for visualization via ParaView.')

parser.add_argument('input_filename', type=str, help='input filename')

parser.add_argument('-o','--out', dest='output_filename', type=str,
                   help='output filename', default="")

args = parser.parse_args()

if len(args.output_filename) == 0:
        #print("No output filename was provided as an input!")
        output_filename = ".".join(args.input_filename.split(".")[:-1]) + ".png"
else:
        output_filename = args.output_filename

# create a new 'Legacy VTK Reader'
sigma_test_it0vtk = LegacyVTKReader(FileNames=[args.input_filename])

# set active source
SetActiveSource(sigma_test_it0vtk)

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [794, 699]

# get display properties
sigma_test_it0vtkDisplay = GetDisplayProperties(sigma_test_it0vtk, view=renderView1)

# change representation type
sigma_test_it0vtkDisplay.SetRepresentationType('Outline')

# Properties modified on renderView1.AxesGrid
renderView1.AxesGrid.Visibility = 1

# get color transfer function/color map for 'material'
materialLUT = GetColorTransferFunction('material')

# show data in view
sigma_test_it0vtkDisplay = Show(sigma_test_it0vtk, renderView1)
# trace defaults for the display properties.
sigma_test_it0vtkDisplay.Representation = 'Surface'
sigma_test_it0vtkDisplay.ColorArrayName = ['CELLS', 'material']
sigma_test_it0vtkDisplay.LookupTable = materialLUT
sigma_test_it0vtkDisplay.OSPRayScaleArray = 'material'
sigma_test_it0vtkDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
sigma_test_it0vtkDisplay.SelectOrientationVectors = 'sigma_h'
sigma_test_it0vtkDisplay.ScaleFactor = 0.2
sigma_test_it0vtkDisplay.SelectScaleArray = 'material'
sigma_test_it0vtkDisplay.GlyphType = 'Arrow'
sigma_test_it0vtkDisplay.PolarAxes = 'PolarAxesRepresentation'
sigma_test_it0vtkDisplay.ScalarOpacityUnitDistance = 0.23829607324923416
sigma_test_it0vtkDisplay.GaussianRadius = 0.1
sigma_test_it0vtkDisplay.SetScaleArray = ['POINTS', 'material']
sigma_test_it0vtkDisplay.ScaleTransferFunction = 'PiecewiseFunction'
sigma_test_it0vtkDisplay.OpacityArray = ['POINTS', 'material']
sigma_test_it0vtkDisplay.OpacityTransferFunction = 'PiecewiseFunction'

# show color bar/color legend
sigma_test_it0vtkDisplay.SetScalarBarVisibility(renderView1, True)

# reset view to fit data
renderView1.ResetCamera()

# show data in view
sigma_test_it0vtkDisplay = Show(sigma_test_it0vtk, renderView1)

# reset view to fit data
renderView1.ResetCamera()

# show color bar/color legend
sigma_test_it0vtkDisplay.SetScalarBarVisibility(renderView1, True)

# create a new 'Slice'
slice1 = Slice(Input=sigma_test_it0vtk)
slice1.SliceType = 'Plane'
slice1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [0.0, 0.0, 1.0]

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.01]
slice1.SliceType.Normal = [0.0, 0.0, 1.0]

# Properties modified on slice1
slice1.Triangulatetheslice = 0

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 0.0, 0.01]
slice1.SliceType.Normal = [0.0, 0.0, 1.0]

# show data in view
slice1Display = Show(slice1, renderView1)
# trace defaults for the display properties.
slice1Display.Representation = 'Surface'
slice1Display.ColorArrayName = ['CELLS', 'material']
slice1Display.LookupTable = materialLUT
slice1Display.OSPRayScaleArray = 'material'
slice1Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice1Display.SelectOrientationVectors = 'sigma_h'
slice1Display.ScaleFactor = 0.2
slice1Display.SelectScaleArray = 'material'
slice1Display.GlyphType = 'Arrow'
slice1Display.PolarAxes = 'PolarAxesRepresentation'
slice1Display.GaussianRadius = 0.1
slice1Display.SetScaleArray = ['POINTS', 'material']
slice1Display.ScaleTransferFunction = 'PiecewiseFunction'
slice1Display.OpacityArray = ['POINTS', 'material']
slice1Display.OpacityTransferFunction = 'PiecewiseFunction'

# hide data in view
Hide(sigma_test_it0vtk, renderView1)

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# change representation type
slice1Display.SetRepresentationType('Surface With Edges')

# set scalar coloring
ColorBy(slice1Display, ('POINTS', 'sigma_h', 'Magnitude'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(materialLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
slice1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'sigma_h'
sigma_hLUT = GetColorTransferFunction('sigma_h')

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=slice1.SliceType)

# set active source
SetActiveSource(sigma_test_it0vtk)

# create a new 'Slice'
slice2 = Slice(Input=sigma_test_it0vtk)
slice2.SliceType = 'Plane'
slice2.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice2.SliceType.Origin = [0.0, 0.0, 1.0]

# Properties modified on slice2.SliceType
slice2.SliceType.Normal = [0.0, 0.0, 1.0]

# Properties modified on slice2
slice2.Triangulatetheslice = 0

# Properties modified on slice2.SliceType
slice2.SliceType.Normal = [0.0, 0.0, 1.0]

# show data in view
slice2Display = Show(slice2, renderView1)
# trace defaults for the display properties.
slice2Display.Representation = 'Surface'
slice2Display.ColorArrayName = ['CELLS', 'material']
slice2Display.LookupTable = materialLUT
slice2Display.OSPRayScaleArray = 'material'
slice2Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice2Display.SelectOrientationVectors = 'sigma_h'
slice2Display.ScaleFactor = 0.2
slice2Display.SelectScaleArray = 'material'
slice2Display.GlyphType = 'Arrow'
slice2Display.PolarAxes = 'PolarAxesRepresentation'
slice2Display.GaussianRadius = 0.1
slice2Display.SetScaleArray = ['POINTS', 'material']
slice2Display.ScaleTransferFunction = 'PiecewiseFunction'
slice2Display.OpacityArray = ['POINTS', 'material']
slice2Display.OpacityTransferFunction = 'PiecewiseFunction'

# hide data in view
Hide(sigma_test_it0vtk, renderView1)

# show color bar/color legend
slice2Display.SetScalarBarVisibility(renderView1, True)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=slice2.SliceType)

# change representation type
slice2Display.SetRepresentationType('Surface With Edges')

# set scalar coloring
ColorBy(slice2Display, ('POINTS', 'sigma_h', 'Magnitude'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(materialLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
slice2Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
slice2Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(sigma_test_it0vtk)

# create a new 'Slice'
slice3 = Slice(Input=sigma_test_it0vtk)
slice3.SliceType = 'Plane'
slice3.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice3.SliceType.Origin = [0.0, 0.0, 1.0]

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=slice3.SliceType)

# Properties modified on slice3.SliceType
slice3.SliceType.Origin = [0.0, 0.0, 2.0]
slice3.SliceType.Normal = [0.0, 0.0, 1.0]

# Properties modified on slice3
slice3.Triangulatetheslice = 0

# Properties modified on slice3.SliceType
slice3.SliceType.Origin = [0.0, 0.0, 2.0]
slice3.SliceType.Normal = [0.0, 0.0, 1.0]

# show data in view
slice3Display = Show(slice3, renderView1)
# trace defaults for the display properties.
slice3Display.Representation = 'Surface'
slice3Display.ColorArrayName = ['CELLS', 'material']
slice3Display.LookupTable = materialLUT
slice3Display.OSPRayScaleArray = 'material'
slice3Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice3Display.SelectOrientationVectors = 'sigma_h'
slice3Display.ScaleFactor = 0.2
slice3Display.SelectScaleArray = 'material'
slice3Display.GlyphType = 'Arrow'
slice3Display.PolarAxes = 'PolarAxesRepresentation'
slice3Display.GaussianRadius = 0.1
slice3Display.SetScaleArray = ['POINTS', 'material']
slice3Display.ScaleTransferFunction = 'PiecewiseFunction'
slice3Display.OpacityArray = ['POINTS', 'material']
slice3Display.OpacityTransferFunction = 'PiecewiseFunction'

# hide data in view
Hide(sigma_test_it0vtk, renderView1)

# show color bar/color legend
slice3Display.SetScalarBarVisibility(renderView1, True)

# change representation type
slice3Display.SetRepresentationType('Surface With Edges')

# set scalar coloring
ColorBy(slice3Display, ('POINTS', 'sigma_h', 'Magnitude'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(materialLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
slice3Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
slice3Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(sigma_test_it0vtk)

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [5.63, 1.68, 4.204]
renderView1.CameraFocalPoint = [0.0, 0.0, 1.0]
renderView1.CameraViewUp = [-0.462, -0.126, 0.878]
renderView1.CameraParallelScale = 1.7320508075688772
renderView1.CameraViewAngle = 30.00

# create a new 'Iso Volume'
isoVolume1 = IsoVolume(Input=sigma_test_it0vtk)
isoVolume1.InputScalars = ['POINTS', 'sigma_h_Magnitude']
isoVolume1.ThresholdRange = [0.008444670236178347, 0.03598026663305522]

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [794, 699]

# show data in view
isoVolume1Display = Show(isoVolume1, renderView1)

# set active source
SetActiveSource(isoVolume1)

# get color transfer function/color map for 'sigma_h_Magnitude'
sigma_h_MagnitudeLUT = GetColorTransferFunction('sigma_h_Magnitude')

# set scalar coloring
#ColorBy(isoVolume1Display, ('POINTS', 'sigma_h_Magnitude'))

# get color transfer function/color map for 'element_coloring'
#element_coloringLUT = GetColorTransferFunction('element_coloring')

# Hide the scalar bar for this color map if no visible data is colored by it.
#HideScalarBarIfNotNeeded(element_coloringLUT, renderView1)


# save screenshot
SaveScreenshot(output_filename, magnification=1, quality=100, view=renderView1)

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).

