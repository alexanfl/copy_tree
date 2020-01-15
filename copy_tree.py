import os
import sys
import shutil

from pathlib import Path

source = Path(sys.argv[1])
target = Path(sys.argv[2])

def ignore_files(folder, files):
    return [f for f in files if not (Path(folder) / f).is_dir()]

if __name__ == "__main__":
    shutil.copytree(source, target,symlinks=False, ignore=ignore_files)
