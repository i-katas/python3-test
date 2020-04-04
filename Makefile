SHELL=bash
.PHONY: test
#PY_FLAGS=-OO #-OO makes the pytest.raises work incorrectly

test:
	-@tput reset
	@source .bashrc && python3 ${PY_FLAGS} setup.py test

clean:
	@find . -name __pycache__ -type d | xargs rm -rf
	@rm *.egg-info dist build .pytest_cache -rf 
