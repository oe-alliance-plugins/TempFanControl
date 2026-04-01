from setuptools import setup
import setup_translate

pkg = 'SystemPlugins.TempFanControl'
setup(name='enigma2-plugin-systemplugins-fancontrol',
       version='3.0',
       description='Control your internal system fan.',
       package_dir={pkg: 'TempFanControl'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
