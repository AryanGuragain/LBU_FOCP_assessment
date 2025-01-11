from shutil import copyfile
from sys import argv
origin_filename=None
try:
    origin_filename=argv[1]
    filename,extension=origin_filename.split('.')
    target_filename=(f"{filename}_backup.{extension}")

    copyfile(origin_filename,target_filename)
    print("file copied")

except IndexError as i:
    print("file name not given", i)
except ValueError as v:
    print("cannot find file extension", v)
except FileNotFoundError as f:
    filename=origin_filename
    print(f"Cannot open {filename}.",f)