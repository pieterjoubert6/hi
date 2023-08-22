import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='toolbox',
    version='0.0.3',
    author='Pieter Joubert',
    author_email='pieter@jedimindtricks.co.za',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/pieterjoubert6/moment',
    project_urls = {
        "Bug Tracker": "https://github.com/Muls/toolbox/issues"
    },
    license='MIT',
    packages=['toolbox'],
    install_requires=['requests'],
)