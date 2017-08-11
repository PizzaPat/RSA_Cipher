from setuptools import setup, find_packages

setup(
	name='RSA-Cipher',
	packages=find_packages(),
	version='1.0.9',
	description='Generate encrypted/decrypted text using RSA method',
	author='PizzaPat',
	url='https://github.com/PizzaPat/RSA-Cipher',
	download_url = 'https://github.com/PizzaPat/RSA_Cipher/tarball/1.0.9',
	keywords=['RSA'],
	entry_points={
		'console_scripts':[
			'rsa=RSA_Cipher.RSA:main'
			]},
	install_requires=['pyperclip']
)