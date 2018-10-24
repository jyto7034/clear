import os
import shutil
import re

def Run():
        delay = 0
        count = 0
        path = []
        target = ''
        fcount = 0
        scount = 0
        filenamecount = 0
        try:
                setfile = open('C://Settings//Settings.txt', 'r')
        except IOError as e:
                print(e)
        else:
                fpaths = setfile.read().split()
                for strs in fpaths:
                        if "MoveTo:" in strs:
                                target = strs[7:]
                                temp = strs
                                del fpaths[fpaths.index(temp)]
                for strs in fpaths:
                        if "Time:" in strs:
                                delay = re.findall("\d+", strs)
                                tempd = strs
                                del fpaths[fpaths.index(tempd)]
                for itpath in fpaths:
                        path.append(itpath)

                for dir in path:
                        if os.path.isdir(dir):
                                for file in os.listdir(dir):
                                        try:
                                                if (
                                                        # file.endswith(".png") or file.endswith(".mp4") or
                                                        # file.endswith(".gif") or file.endswith(".JPG") or
                                                        # file.endswith(".jpg")):
                                                        file.endswith(".asd")):
                                                        # L:\ 에 있는 .asd 로 끝나는 파일을 바탕화면으로 옮김
                                                        src = dir + "\\" + file
                                                        dsc = target + "\\" + file
                                                        print(src, target)
                                                        shutil.move(src, target)
                                                        scount += 1
                                                # else:
                                                #         print("There is no file!")
                                        except Exception as e:
                                                if os.path.exists(dsc):
                                                        srcfilesize = os.stat(src).st_size
                                                        dscfilesize = os.stat(dsc).st_size
                                                        try:
                                                                if dscfilesize == srcfilesize:
                                                                        print(dsc, " and ", src, " is same")
                                                                        os.remove(dsc)
                                                                        shutil.move(src, dsc)
                                                                        scount += 1
                                                                else:
                                                                        while True:
                                                                                filenamecount += 1
                                                                                chgfile = file[
                                                                                          :file.__len__() - 4] + "(" + str(
                                                                                        filenamecount) + ")" + file[
                                                                                                               file.__len__() - 4:]
                                                                                checkfile = target + "\\" + chgfile
                                                                                # print("check :", checkfile)
                                                                                # print(src, dsc)
                                                                                if os.path.exists(checkfile):
                                                                                        srcfilesize = os.stat(
                                                                                                src).st_size
                                                                                        checkfilesize = os.stat(
                                                                                                checkfile).st_size
                                                                                        print(checkfile, src)

                                                                                        if srcfilesize == checkfilesize:
                                                                                                os.remove(checkfile)

                                                                                if not os.path.exists(checkfile):
                                                                                        print("Last Count")
                                                                                        break

                                                                        os.rename(dir + "\\" + file,
                                                                                  dir + "\\" + chgfile)
                                                                        print(file)
                                                                        src = dir + "\\" + chgfile
                                                                        stat = shutil.move(src, target)
                                                                        scount += 1
                                                        except Exception as e:
                                                                print("Exception" + e)
                                                                pass

                                                        # for tfile in os.listdir(target):
                                                        #         if "(" in tfile and ")" in tfile:
                                                        #                 print("sad")
                                                        #                 dscfile = os.stat(target + "\\" + tfile).st_size
                                                        #                 srcfile = os.stat(checkfile).st_size
                                                        #                 if dscfile == srcfile:
                                                        #                         os.remove(dsc)
                                                        #                         shutil.move(src, dsc)
                                                        #                         scount += 1
                                                        #                         print("sadd")
                        else:
                                print("No exist folder")
        print("Success : %d   :   Failed : %d" % (scount, fcount))

# if __name__ == '__main__':
        # delay = 0
        # count = 0
        # path = []
        # target = ''
        # fcount = 0
        # scount = 0
        # filenamecount = 0
        # try:
        #         setfile = open('C://Settings//Settings.txt', 'r')
        # except IOError as e:
        #         print(e)
        # else:
        #         fpaths = setfile.read().split()
        #         for strs in fpaths:
        #                 if "MoveTo:" in strs:
        #                         target = strs[7:]
        #                         temp = strs
        #                         del fpaths[fpaths.index(temp)]
        #         for strs in fpaths:
        #                 if "Time:" in strs:
        #                         delay  = re.findall("\d+", strs)
        #                         tempd = strs
        #                         del fpaths[fpaths.index(tempd)]
        #         for itpath in fpaths:
        #                 path.append(itpath)
        #
        #         for dir in path:
        #                 if os.path.isdir(dir):
        #                         for file in os.listdir(dir):
        #                                 try:
        #                                         if (
        #                                                 # file.endswith(".png") or file.endswith(".mp4") or
        #                                                 # file.endswith(".gif") or file.endswith(".JPG") or
        #                                                 # file.endswith(".jpg")):
        #                                                 file.endswith(".asd")):
        #                                                 src = dir + "\\" + file
        #                                                 dsc = target + "\\" + file
        #                                                 print(src, target)
        #                                                 shutil.move(src, target)
        #                                                 scount += 1
        #                                         # else:
        #                                         #         print("There is no file!")
        #                                 except Exception as e:
        #                                         if os.path.exists(dsc):
        #                                                 srcfilesize = os.stat(src).st_size
        #                                                 dscfilesize = os.stat(dsc).st_size
        #                                                 try:
        #                                                         if dscfilesize == srcfilesize:
        #                                                                 print(dsc, " and ", src, " is same")
        #                                                                 os.remove(dsc)
        #                                                                 shutil.move(src, dsc)
        #                                                                 scount += 1
        #                                                         else:
        #                                                                 while True:
        #                                                                         filenamecount += 1
        #                                                                         chgfile = file[ :file.__len__() - 4] + "(" +     str(filenamecount)     + ")" + file[file.__len__() - 4:]
        #                                                                         checkfile = target + "\\" + chgfile
        #                                                                         # print("check :", checkfile)
        #                                                                         # print(src, dsc)
        #                                                                         if os.path.exists(checkfile):
        #                                                                                 srcfilesize = os.stat(src).st_size
        #                                                                                 checkfilesize = os.stat(checkfile).st_size
        #                                                                                 print(checkfile ,src)
        #
        #                                                                                 if srcfilesize == checkfilesize:
        #                                                                                         os.remove(checkfile)
        #
        #                                                                         if not os.path.exists(checkfile):
        #                                                                                 print("Last Count")
        #                                                                                 break
        #
        #                                                                 os.rename(dir + "\\" + file, dir + "\\" + chgfile)
        #                                                                 print(file)
        #                                                                 src = dir + "\\" + chgfile
        #                                                                 stat = shutil.move(src, target)
        #                                                                 scount += 1
        #                                                 except Exception as e:
        #                                                         print("Exception" + e)
        #                                                         pass
        #
        #                                                 # for tfile in os.listdir(target):
        #                                                 #         if "(" in tfile and ")" in tfile:
        #                                                 #                 print("sad")
        #                                                 #                 dscfile = os.stat(target + "\\" + tfile).st_size
        #                                                 #                 srcfile = os.stat(checkfile).st_size
        #                                                 #                 if dscfile == srcfile:
        #                                                 #                         os.remove(dsc)
        #                                                 #                         shutil.move(src, dsc)
        #                                                 #                         scount += 1
        #                                                 #                         print("sadd")
        #                 else:
        #                         print("No exist folder")
        # print("Success : %d   :   Failed : %d" % (scount, fcount))