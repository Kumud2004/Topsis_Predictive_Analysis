from setuptools import setup, find_packages

setup(
    name="Topsis_Predictive_Analysis-102316088",
    version="1.0.0",
    author="Kumud",
    description="TOPSIS Implementation",
    packages=find_packages(),
    install_requires=["pandas", "numpy"],
    entry_points={
        'console_scripts': [
            'topsis=topsis.topsis:main',
        ],
    },
)
