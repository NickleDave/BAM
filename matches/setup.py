import os, sys
from distutils.core import setup
from distutils.command.install import install as _install


def _post_install(dir):
    from subprocess import call
    call([sys.executable, 'install_fixtures.py'],
         cwd=os.path.join(dir, 'matches'))


class install(_install):
    def run(self):
        _install.run(self)
        self.execute(_post_install, (self.install_lib,),
                     msg="Running post install task")


setup(
    ...
    cmdclass={'install': install},
)
