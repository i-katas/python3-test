.PHONY: test

test:
	-@tput reset
	@python3 setup.py test

clean:
	@find . -name __pycache__ -type d | xargs rm -rf
	@rm *.egg-info dist build -rf 
