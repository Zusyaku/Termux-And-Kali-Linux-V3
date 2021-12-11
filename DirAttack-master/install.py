from os import path, system, getuid, mkdir

platform = "linux" if path.exists("/usr/bin/") else "termux"
data = {
  "termux":"/data/data/com.termux/files/usr/share",
  "linux":"/usr/share",
  "dirname":"DirAttack"
}

if platform is "linux":
  if getuid() != 0:
    exit("Please run as root :)")
  if not path.exists("desktop"):
    exit("Install failed, directory 'desktop' not found")
  if path.exists("/usr/share/icons/dirattack.png"):
    system("rm -rf /usr/share/icons/dirattack.png")
  if path.exists("/usr/share/applications/dirattack.desktop"):
    system("rm -rf /usr/share/applications/dirattack.desktop")

  system("chmod 777 -R desktop/* && mv desktop/dirattack.png /usr/share/icons/")
  system("mv desktop/dirattack.desktop /usr/share/applications/")  
  pass

if not path.exists("config"):
  exit("Install failed, directory 'config' not found")
if path.exists(data[platform]+"/"+data["dirname"]):
  system("rm -rf %s"%data[platform]+"/"+data["dirname"])

mkdir(data[platform]+"/"+data["dirname"])
system("mv config %s"%data[platform]+"/"+data["dirname"])
system("mv dirattack.py dirattack && chmod 777 -R dirattack && mv dirattack "+path.dirname(data[platform])+"/bin/")
system("chmod 777 -R %s/*"%(data[platform]+"/"+data["dirname"]))