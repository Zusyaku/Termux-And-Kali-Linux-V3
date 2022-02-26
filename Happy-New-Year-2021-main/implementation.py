import zlib
import base64
import time
from itertools import zip_longest, cycle, chain, repeat
import os

CITY = """



                      .|
                      | |
                      |'|            ._____
              ___    |  |            |.   |' .---\"|
      _    .-'   '-. |  |     .--'|  ||   | _|    |
   .-'|  _.|  |    ||   '-__  |   |  |    ||      |
   |' | |.    |    ||       | |   |  |    ||      |
___|  '-'     '    \"\"       '-'   '-.'    '`      |____
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

FIREWORKS = """
eJzFV73O6yAM3fsUbLSVQnakLizZ7sCGFCmP0PffrjEBzJ9Jv96fRF+SrzkYnxMbm9vNH2J8WMm8tYp
/+Wtm/LC7Xe3BYQQA9r/qIWf76f84E8/IYQJDGrytONv3PoXrBYgwh9nNasgX2I5t39bt6E0KDwCmXw
OQ+48cjhO3Himj4STfbVObhFOFySsOArCnKaPTmE1HGpvu8TBaeFPFCOQiKrxwb5xEolMk0rxDHeLgv
YRT0RlLCPW3GdtlDj8H5tWA8G/JAa/eAe9IJrE76VZmRMH45UnDdcBaVIdbnXIYBPUbIoJPkkcn1Ru9
AHOv8z26XQ6NX7gNlAbvwiMGa029EguEUkEuuEtOKLdEpdzCKeTtBI2c5tIEvAQROQC/mH0osch6TdS
2XhuaURM8qp3zqXan1RsuqBKK550a00TRRaV5A1JoUFzRu4nauJ6Xv/alEqE6VdAzVNi5PwNmYfgAOR
O9ofRMqyWCzrC91ahcyjIWA3dEP5e1K7wqNzhoe1xTYJC9XQf6+ZuABEoyGOzzWCE6YXdWwG98L5BsE
ph3wg39tu923CRb8IAvoDtJ0OIk4C58q5j5LQ5KpDRrhC7njeAgVKX1APPylM3rhMbcLxjbl6dsPQYq
qSJdBK5WSEtX1CCyVZ3bgZym50Ux9FAQU5iwPiNwjUQB/EqZXgNhFWjDXZolMjcLna3lYpfI3y5YDdb
TPKlUA1J+oiCEn1w0VXisha3K9T8QQ1At3JMRQ8y1kKern0mhzin/hBL5uUreqApcRCql7oA0f0C6H4
VEvnoHgYLVUx7A3WFdjwu7LAQ6b2gaZ0niQG7FJqhSRuBUfV1qPKuJulbp+FUIe5UH3cZc2mrCgPvmU
57sTmbbT+803nBnNPU6P2M8SbanK3ikPs7qVKj51SfSoVsOED6U7MnChaTIxgPTTTV7bdcpJKnFm6lB
jitiROtZBxzJESGb2dim9kfFHVIeuWIg5O62K0DeKxEqsYFMMpQzhY6qODDG2A3UoAFzJI1GHXrZVyQ
wMgRCupad9kXJNkw9CruyyyCkRpHmqtxPyn6vQLheYY8h1+cuOtQDoYu0G+z/IJ02VVPK9DYhHDurn9
P9DXABY6g=
"""

fireworks = zlib.decompress(base64.b64decode(FIREWORKS)).decode("utf-8")

BANNER = r"""
         _    ,                    _ __            _    ,
        ' )  /                    ' )  )          ' )  /             /
         /--/ __.  _   _   __  ,   /  / _  , , ,   /  / _  __.  __  /
        /  (_(_/|_/_)_/_)_/ (_/_  /  (_</_(_(_/_  (__/_</_(_/|_/ (_'
                 /   /       /                     //             o
                '   '       '                     (/  @ˡᶦⁿᵘˣ_ʳᵉᵖᵒ
                                                    
                           
                           ___    ___/  ___   . 
                          /   \ .'  /\ /   \ /| 
                            _-' |  / |   _-'  | 
                           /    |,'  |  /     | 
                          /___, /`---' /___, _|_
                                            
"""

COLOURS = {"R": 91, "G": 92, "B": 94, "Y": 93, None: 0}

if os.name == "nt":
    import ctypes
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)


print("\033[2J\033[2;1H\033[?25l")
city = [list(map(lambda c: (c, None), list(cty_line))) for cty_line in CITY.split("\n")]
for frame, banner_colour in zip(cycle(fireworks.split("N")), cycle(chain(*(repeat(c, 7) for c in COLOURS if c)))):
    try:
        frame = list(frame)
        firework = []
        frame_line = []
        while frame:
            char = frame.pop(0)
            if char in "RGBY":
                frame_line.append((frame.pop(0), char))
            elif char == "\n":
                firework.append(frame_line)
                frame_line = []
            else:
                frame_line.append((char, None))
        final_frame = []
        for final_frame_line, cty_line in zip_longest(firework, city, fillvalue=[]):
            fw_line = " " * 10
            for (fw_char, fw_colour), (cty_char, _) in zip_longest(final_frame_line, cty_line, fillvalue=(' ', None)):
                if fw_char != " ":
                    fw_line += f"\033[{COLOURS[fw_colour]}m{fw_char}\033[0m"
                else:
                    fw_line += cty_char
            final_frame.append(fw_line)
        final_frame = "\n".join(final_frame)
        print("\033[2J\033[2;1H")
        print(f"\033[{COLOURS[banner_colour]}m{BANNER}\033[0m")
        print(final_frame, end="\033[2;1H", flush=True)
        time.sleep(.2)
    except KeyboardInterrupt:
        print("\033c")
        break
