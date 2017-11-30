import shutil
source="D:\\ht"
dest="D:\\test"
shutil.move(source,dest)
print('File moved successfully')

#import glob
#import shutil
#import os

#src_dir = "your/source/dir"
#dst_dir = "your/destination/dir"
#for jpgfile in glob.iglob(os.path.join(src_dir, "*.jpg")):
#    shutil.copy(jpgfile, dst_dir)
