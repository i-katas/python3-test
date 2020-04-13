from setuptools import setup

setup(
    setup_requires=['setuptools', 'pytest-runner'],
    install_requires=['numpy'],
    tests_require=['pytest'],
    extras_require=dict(
        dev=['flake8']
    )
)
