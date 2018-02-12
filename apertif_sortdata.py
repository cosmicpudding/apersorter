# apertif_sortdata.py: sort APERTIF MS into source folders based on input schedule file
# V.A. Moss (vmoss.astro@gmail.com)
__author__ = "V.A. Moss"
__date__ = "$12-feb-2018 17:00:00$"
__version__ = "0.1"

import os
import sys

try: 
	fname = sys.argv[1]
except:
        print 'Second argument should be the parameter file!'
        sys.exit()

# Which beam to copy
try:
        beams = sys.argv[2]
except:
        beams = 'all'  # can be '0' or 'all', all files is the default

# Which range of IDs to copy
try:
        idrange = sys.argv[3]
except:
        idrange = None  # can be None or a specific range: format '23,50'

# Only process this if the idrange is specified
if idrange != None:
        t1 = int(idrange.split(',')[0])
        t2 = int(idrange.split(',')[1])
        copylist = range(t1,t2+1)
        print 'Only copying: %s' % copylist
        
# Main path
path = '/data/apertif'

# Go through the schedule file
for line in open(fname,'rU'):
	if line.startswith('TASKIDS'):
		tid = line.split("'")[1]
	if line.startswith('SOURCENAMES'):
		sid = line.split("'")[1]

		# Now, you have the tid and sid
		print '#'*20
		print tid,sid

                # Skip if the file is not in the list of sources to move
                if idrange != None:
                        if int(tid[-2:]) not in copylist:
                                print 'Not moving this source! Continuing...'
                                continue
           
		# Make the directory
		print 'Running: mkdir %s/%s_%s' % (path,tid,sid)
		os.system('mkdir %s/%s_%s' % (path,tid,sid))

                # Copy only the chosen beams
                # Fixed to account for > 100 task ids 24/01/18 VM
                if beams == 'all':
		        # Move the files to the folder
		        print 'Running: mv %s/temp/*%s_* %s/%s_%s' % (path,tid,path,tid,sid)
		        os.system('mv %s/temp/*%s_* %s/%s_%s' % (path,tid,path,tid,sid))
                elif beams == '0':
                        print 'Running: mv %s/temp/*%s_*B000* %s/%s_%s' % (path,tid,path,tid,sid)
                        os.system('mv %s/temp/*%s_*B000* %s/%s_%s' % (path,tid,path,tid,sid))
                        
print '... all files moved!'
print '#'*20		
