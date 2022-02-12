package_1 = "vim"
package_2 = "curl"
package_3 = "figlet"
package_4 = "toilet"

install:
	for asu in $(package_1) $(package_2) $(package_3) $(package_4) ; do \
		apt-get --fix-missing install $(asu) ; \
	done
	@echo
	@echo "Done install"

run:
	chmod 0755 Stress_domain.sh.bash
	chmod +x Stress_domain.sh.bash
	./Stress_domain.sh.bash
