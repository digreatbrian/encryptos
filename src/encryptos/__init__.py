'''Best way to encrypt and decrypt strings using different secret keys.This secret key is used to decrypt given string.

example::
	key="encrypt"
	s="unencrypted"
	
	en=encrypt(s ,key)
	de=decrypt(en, key)
	
First the string "s" is encrypted to "en" and then decrypted back to "s" by "de".

'''
__author__='Brian Musakwa' 
__email__='digreatbrian@gmail.com'
from .en import *