from setuptools import setup, find_packages

files = ["engbase/files/*"]


setup(name="engbase",
      version="010",
      description="Base repository for any engineering calculations",
      author="Matias Nyman",
      author_email="matianym@gmail.com",
      url="https://github.com/matianym-eng/engbase",

      # (If you have other packages (dirs) or modules (py files) then
      # put them into the package directory - they will be found
      # recursively.)

      packages=find_packages(),

      # This dict maps the package name =to=> directories
      # package_data={'engbase': files},

      include_package_data=True,
      

      # wntr will not work as of now(19.04.2021) if newer python version is used
      python_requires='~=3.8',
      

      # scripts = ["somescript"],
      #classifiers = [],

      # long_description="""TODO: Very descriptive description."""

      # 

      )
