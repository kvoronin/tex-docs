import three_slices_sigma_withfunc
import three_slices_u_withfunc
import argparse
import os.path
import sys
from paraview.simple import *

def ResetSession():
    pxm = servermanager.ProxyManager()
    pxm.UnRegisterProxies()
    del pxm
    Disconnect()
    Connect()

def service_func():
    print 'service func in paraview_draw.py'

if __name__ == '__main__':
	# service.py executed as script
	# do something
	service_func()

	# Parsing the script input arguments
	parser = argparse.ArgumentParser(description='Processing multiple VTK outputs from MFEM for visualization via ParaView.')

	parser.add_argument('filename_root', type=str, help='filename root (for input)')

	parser.add_argument('-o','--out', dest='output_filename', type=str,
		           help='output filename', default="")

	parser.add_argument('-st','--step', dest='step', type=int,
		           help='step for the pictures', default="1")

	parser.add_argument('-stcnt','--start-count', dest='start_count', type=int,
		           help='starting count', default="0")

	parser.add_argument('-nst','--nsteps', dest='nsteps', type=int,
		           help='nsteps', default="1")

	parser.add_argument('-t','--type', dest='type', type=int,
		           help='type: 0(scalar) or 1(vector)', required=True,
			   default=0)

	parser.add_argument('-bot','--iso-bot', dest='iso_bot', type=float,
		           help='lowest margin for the iso volume', default=0)

	parser.add_argument('-top','--iso-top', dest='iso_top', type=float,
		           help='highest margin for the iso volume', default=10000)

	parser.add_argument('-rel','--iso-relative', dest='relative', type=bool,
		           help='Flag to treat iso-volume bounds as relative to data range if true, or not otherwise.', default=False)

	args = parser.parse_args()

	for i in xrange(args.start_count, args.start_count + args.nsteps*args.step, args.step):
		filename = args.filename_root + str(i) + '.vtk'
		#my_file = Path(filename)
		print(filename)

		if os.path.exists(filename):
			if args.type == 0:
				#call
				three_slices_u_withfunc.draw(filename,"", 					args.iso_bot, args.iso_top, args.relative)
			else:
				three_slices_sigma_withfunc.draw(filename,"", 					args.iso_bot, args.iso_top, args.relative)
		else:
			sys.exit("File cannot be opened")
			
		ResetSession()
	

