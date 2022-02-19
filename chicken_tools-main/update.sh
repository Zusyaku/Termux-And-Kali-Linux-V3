. lib/moduler.sh

Bash.import: text_display/IO.ECHO text_display/colorama

Tulis.strN "$(mode.bold: kuning)[$(mode.bold: merah)!$(mode.bold: kuning)]$(mode.bold: putih) updating...$(default.color)\n"
cd ../
rm -rf chicken_tools
git clone https://github.com/Bayu12345677/chicken_tools/
cd chicken_tools
