SHELL=bash
.PHONY: test
.DEFAULT_GOAL=test
#PY_FLAGS=-OO #-OO makes the pytest.raises work incorrectly
GCC_COMPILE_FLAGS=$(shell python3-config --includes) -fPIC
GCC_FLAGS=$(shell python3-config --ldflags) -shared
SO_EXTENSION=.so


test/cmath.o:
	$(CXX) ${GCC_COMPILE_FLAGS} -c $*.c -o $@

test/cmath${SO_EXTENSION}: test/cmath.o
	$(CXX) ${GCC_FLAGS} $< -o $@
	rm $<

test: checkstyle test/cmath${SO_EXTENSION}
	@source .bashrc && python3 ${PY_FLAGS} setup.py test

checkstyle:
	@-tput reset
	@source .bashrc && flake8

clean:
	@find . -name __pycache__ -type d | xargs rm -rf
	@find test -name '*.o' -o -name '*.so' -type f | xargs rm -rf
	@rm *.egg-info dist build .pytest_cache -rf 

