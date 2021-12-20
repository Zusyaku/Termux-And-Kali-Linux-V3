from os import get_terminal_size, system as sys
from . import OtakuDesu
import itertools
from time import sleep
from subprocess import call
from platform import system
from threading import Thread
from random import choice
from textwrap import wrap
otak = OtakuDesu()

class Base:

    def __init__(self):
        self.contact = "https://wa.me/6285892766102"
        self.clear = (lambda : sys("cls" if system() == "Windows" else "clear"))

    def randco(self, text):
        lcol = ["\x1b[1;31m","\x1b[1;32m","\x1b[1;33m","\x1b[1;34m","\x1b[1;35m","\x1b[1;36m"]
        return "%s%s\x1b[0m" % (choice(lcol), text)

    def chotto(self):
        global matte
        matte = []
        for c in itertools.cycle(["■□□□□□□□□□","■■□□□□□□□□", "■■■□□□□□□□", "■■■■□□□□□□", "■■■■■□□□□□", "■■■■■■□□□□", "■■■■■■■□□□", "■■■■■■■■□□", "■■■■■■■■■□", "■■■■■■■■■■"]):
            if bool(matte) is True:
                break
            print(f"  ╳ Wait {self.randco(c)}\r", end="")
            sleep(0.1)

    def show(self, obj):
        # self.clear()
        print("""
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  ➯ Title : %s
  ➯ Japanese Title : %s
  ➯ Score : %s
  ➯ Producers : %s
  ➯ Studio : %s
  ➯ Type : %s
  ➯ Status : %s
  ➯ Episodes : %s
  ➯ Duration : %s
  ➯ Release Date : %s
  ➯ Genre : %s
  ➯ Synopsis : %s
  """ % (obj.title, obj.jp_title, obj.rating, obj.producers, obj.studio, obj.type, obj.status, obj.episodes, obj.duration, obj.release_date, ", ".join(obj.genres), "\n           ".join(wrap(obj.synopsis, get_terminal_size()[0]-12))))

    def showeps(self, obj):
        eps = list(obj.downloads.__dict__.keys())[::-1]
        for k, v in enumerate(eps, 1):
            print("  %s. %s" % (k, v.replace("eps","Episode ").title()))
        chos = int(input("\n  ➯ Choose : "))
        if chos == 99:Main().__main__()
        if chos > 0 and chos-1 < len(eps):
            self.showdl(obj.downloads.__dict__.get(eps[chos-1]))
        else:
            print("  ╳ Invalid Input")

    def showdl(self, obj):
        qlt = list(obj.__dict__.keys())[::-1]
        print("\n")
        for k, v in enumerate(qlt, 1):
            print("  %s.%s" % (k, v.replace("_"," ")))
        chos = int(input("\n  ➯ Choose : "))
        if chos == 99:Main().__main__()
        if chos > 0 and chos-1 < len(qlt):
            self.showlink(obj.__dict__.get(qlt[chos-1]))
        else:
            print("  ╳ Invalid Input")

    def showlink(self, obj):
        deel = list(obj.__dict__.keys())
        print("\n")
        for k, v in enumerate(deel, 1):
            print("  %s. %s" % (k, v))
        chos = int(input("\n  ➯ Choose : "))
        if chos == 99:Main().__main__()
        if chos > 0 and chos-1 < len(deel):
            try:
                call(["termux-clipboard-set", obj.__dict__.get(deel[chos-1])]) # Only work on termux
                print(f"  {obj.__dict__.get(deel[chos-1])}\n  Copied To Clipboard")
                exit(0)
            except:
                print(f"  Result: {obj.__dict__.get(deel[chos-1])}")
                exit(0)
        else:
            print("  ╳ Invalid Input")

class Main(Base):
    loads = (lambda x: Thread(target=Base().chotto).start())
    logo = """
   _ \   |           |                |
  |   |  __|   _` |  |  /  |   |   _` |   _ \   __|  |   |
  |   |  |    (   |    <   |   |  (   |   __/ \__ \  |   |
 \___/  \__| \__,_| _|\_\ \__,_| \__,_| \___| ____/ \__,_| .moe
  ⚘ MhankBarBar | © 2021
  ⚘ Search And Get Direct Download Link From Otakudesu.moe

  1. Search
  2. From Url
  3. From Schedule (It's taking a long time)
  4. Contact
  """
    def __main__(self):
        self.clear()
        print(self.logo)
        try:
            if (mek := int(input("  ➯ Choose : "))):
                if mek == 1:
                    quer = input("  ➯ Query : ")
                    print("\n")
                    self.loads()
                    if (hasil := otak.search(quer).result):
                        matte.insert(0, True)
                        sus = []
                        for k, v in enumerate(hasil, 1):
                            print("  %s. %s" % (k, v.title))
                            sus.append(v)
                        print("  99. Back to main menu")
                        while(True):
                            if (pil := int(input("\n  ➯ Choose : "))):
                                if pil == 99:self.__main__()
                                if pil > 0 and pil-1 < len(sus):
                                    self.show(sus[pil-1])
                                    self.showeps(sus[pil-1])
                                else:
                                    print("  ╳ Invalid Input")
                            else:
                                print("  ╳ Invalid Input")
                    else:
                        matte.insert(0, True)
                        sleep(0.5)
                        print("  ╳ Anime not found")
                elif mek == 2:
                    url = input("  ➯ Url : ")
                    print("\n")
                    self.loads()
                    if (hasil := otak.byUrl(url)):
                        matte.insert(0, True)
                        # self.clear()
                        self.show(hasil)
                        self.showeps(hasil)
                    else:
                        matte.insert(0, True)
                        print("  ╳ Error while scraping")
                elif mek == 3:
                    print("\n")
                    self.loads()
                    if (hasil := otak.getSchedule.result):
                        matte.insert(0, True)
                        sus = []
                        print("\n")
                        for k, v in enumerate(list(hasil.keys()), 1):
                            print("  %s. %s" % (k, v))
                            sus.append(v)
                        print("  99. Back to main menu")
                        while(True):
                            if (pil := int(input("  ➯ Choose : "))):
                                if pil == 99:self.__main__()
                                if pil > 0 and pil-1 < len(sus):
                                    sis = []
                                    for k, v in enumerate(hasil[sus[pil-1]], 1):
                                        print("  %s. %s" % (k, v.title))
                                        sis.append(v)
                                    if (pul := int(input("  ➯ Choose : "))):
                                        if pul == 99:self.__main__()
                                        if pul > 0 and pul-1 < len(sis):
                                            self.show(sis[pul-1])
                                            self.showeps(sis[pul-1])
                                        else:
                                            print("  ╳ Invalid Input")
                                    else:
                                        print("  ╳ Invalid Input")
                                else:
                                    print("  ╳ Invalid Input")
                            else:
                                print("  ╳ Invalid Input")
                    else:
                        matte.insert(0, True)
                        print("  ╳ Error while scraping")
                elif mek == 4:
                    call(["xdg-open", self.contact])
                    self.__main__()
                else:
                    pass
            else:
                print("  ╳ Invalid Input")
        except Exception as e:
            print(e)
            exit("  ╳ An error occurred")

if __name__ == "__main__":
    Main().__main__()
