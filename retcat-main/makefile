SOURCES = main.sh
PKG_NAME = retcat
SUPPORT = .version

# author : polygon
# pkg    : retcat
# me Team: Helixs-crew & COINTER
# github : https://github.com/Bayu12345677

default:
	@echo "Hint: use make install"


install: unlink uninstall
			@echo "installing"
			chmod 777 main.sh
			cp ${SOURCES} ${PKG_NAME}
			mv ${PKG_NAME} /data/data/com.termux/files/usr/bin/


uninstall: unlink
	@echo "uninstall"
	rm -rf /data/data/com.termux/files/usr/bin/${PKG_NAME}

unlink:
	rm -f /data/data/com.termux/files/usr/bin/${PKG_NAME}


update:
		@echo "updating.."
		curl -s --request GET --location --url "https://raw.githubusercontent.com/HELIXS-TEAM/retcat/main/main.sh" > /data/data/com.termux/files/usr/bin/${PKG_NAME}
		@echo "berhasil di update"
