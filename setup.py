from setuptools import setup, find_packages


setup(
    name="spoken_time",
    version="0.1.0",
    description="Format dates and times for TTS",
    license="MIT",
    author="dnknth",
    url="https://github.com/dnknth/spoken_time.git",
    packages=find_packages('.'),
    package_dir={ 'spoken_time': 'spoken_time' },
    package_data = { 'spoken_time': ['locale/*/LC_MESSAGES/*.mo'] },
    py_modules=[ "spoken_time.__init__" ],
    install_requires=[ 'num2words==0.5.*' ],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries'
    ],
)
