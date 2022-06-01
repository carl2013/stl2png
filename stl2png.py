import os
import sys
import subprocess


def make_pngs(parent_folder, fullPicDirectory):
    if not os.path.exists(fullPicDirectory):
        os.mkdir(fullPicDirectory)
    for dirName, subdirs, fileList in os.walk(parent_folder):
        print('Scanning %s...' % dirName)
        for filename in fileList:
            filepath = os.path.join(dirName, filename)
            from pathlib import Path
            if Path(filepath).suffix == '.stl':
                filename = filepath + ".scad"
                pic1 = filepath + '.scad1.png'
                pic2 = filepath + '.scad2.png'
                pic3 = filepath + '.scad3.png'
                pic4 = filepath + '.scad4.png'
                if os.path.exists(os.path.join(fullPicDirectory, os.path.basename(pic1))):
                    continue
                with open(filename, 'w') as scadFile:
                    scadFile.write('import ("{}");\n'.format(os.path.abspath(filepath)))
                subprocess.run('/Applications/OpenSCAD.app/Contents/MacOS/OpenSCAD -o "{}1".png --projection=ortho --autocenter --imgsize=900,900 "{}"'.format(filename, filename), shell=True)
                subprocess.run('/Applications/OpenSCAD.app/Contents/MacOS/OpenSCAD -o "{}2".png --projection=ortho --camera=3.3,0.91,-10.7,90,0,0,4 --viewall --autocenter --imgsize=900,900 "{}"'.format(filename, filename), shell=True)
                subprocess.run('/Applications/OpenSCAD.app/Contents/MacOS/OpenSCAD -o "{}3".png --projection=ortho --camera=3.3,0.91,-10.7,0,90,0,4 --viewall --autocenter --imgsize=900,900 "{}"'.format(filename, filename), shell=True)
                subprocess.run('/Applications/OpenSCAD.app/Contents/MacOS/OpenSCAD -o "{}4".png --projection=ortho --camera=3.3,0.91,-10.7,0,0,90,4 --viewall --autocenter --imgsize=900,900 "{}"'.format(filename, filename), shell=True)
                os.remove(filename)
                pic1NewPath = os.path.join(fullPicDirectory, os.path.basename(pic1))
                os.replace(pic1, pic1NewPath)
                pic2NewPath = os.path.join(fullPicDirectory, os.path.basename(pic2))
                os.replace(pic2, pic2NewPath)
                pic3NewPath = os.path.join(fullPicDirectory, os.path.basename(pic3))
                os.replace(pic3, pic3NewPath)
                pic4NewPath = os.path.join(fullPicDirectory, os.path.basename(pic4))
                os.replace(pic4, pic4NewPath)


if __name__ == '__main__':
    make_pngs(sys.argv[1], sys.argv[2])
