from distutils.core import setup

files = ["engbase/files/*"]


setup(name="engbase",
      version="010",
      description="Base repository for any engineering calculations",
      author="Matias Nyman",
      author_email="matianym@gmail.com",
      url="-",

      # (If you have other packages (dirs) or modules (py files) then
      # put them into the package directory - they will be found
      # recursively.)

      packages=['engbase'],

      # 'package' package must contain files (see list above)
      # This dict maps the package name =to=> directories
      package_data={'engbase': files},


      # scripts = ["somescript"],
      #classifiers = [],

      long_description="""TODO: Very descriptive description."""

      )
