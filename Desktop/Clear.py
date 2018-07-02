import os
import shutil
import re

#
# Must make backup func!!!
#


if __name__ == '__main__':
        delay = 0
        count = 0
        path = []
        target = ''
        fcount = 0
        scount = 0
        try:
                setfile = open('C://Settings//Settings.txt', 'r')
        except IOError as e:
                print(e)
        else:
                fpaths = setfile.read().split()
                for strs in fpaths:
                        if "Target:" in strs:
                                target = strs[7:]
                                temp = strs
                                del fpaths[fpaths.index(temp)]
                for strs in fpaths:
                        if "Time:" in strs:
                                delay  = re.findall("\d+", strs)
                                tempd = strs
                                del fpaths[fpaths.index(tempd)]
                for itpath in fpaths:
                        path.append(itpath)
        try:
            for dir in path:
                for file in os.listdir(dir):
                    if (
                            file.endswith(".png")  or file.endswith(".mp4")or
                            file.endswith(".gif")  or file.endswith(".JPG") or
                            file.endswith(".jpg")):
                        src = dir + "\\" + file
                        dsc = target + "\\" + file
                        print(src, dsc)
                        shutil.move(src, target)
                        scount += 1
        except Exception as e:
                if e == FileExistsError:
                        srcfilesize = os.stat(src).st_size
                        dscfilesize = os.stat(dsc).st_size
                        if dscfilesize == srcfilesize:
                                #os.remove(dsc)
                                scount += 1
                        else:
                                print(target[:4] + "d")
        finally:
            print("Success : %d   :   Failed : %d" % (scount, fcount))