#!/usr/bin/python
import sys
import os
import getpass
from OpenSSL import crypto
from OpenSSL.crypto import PKCS12

#Lets see how we are called in
if (len(sys.argv) != 2) : 
	print "Incorrect number of arguements, expected 1, received ", len(sys.argv) - 1 
	print "Usage: python extract_pkcs12.py <filename.pfx>"
	sys.exit(-1)

fileName, fileExtension = os.path.splitext(sys.argv[1])
if (fileExtension != ".pfx") :
	print "Incorrect file, expected pfx file"
        print "Usage: python extract_pkcs12.py <filename.pfx>"	
	sys.exit(-2)

passphrase = getpass.getpass('Passphrase: ')

with open(sys.argv[1], 'rb') as f:
	data = f.read()
	p12 = crypto.load_pkcs12(data, passphrase)

x509string = crypto.dump_certificate(crypto.FILETYPE_PEM, p12.get_certificate())
x509 = crypto.load_certificate(crypto.FILETYPE_PEM, x509string)
	
print "\nSummary"
print "Subject"
print str(x509.get_subject())
print "\nValid From:"
print x509.get_notBefore()
print "\nValid Till:"
print x509.get_notAfter()
print "\nIssuer"
print str(x509.get_issuer())

print "\n\nCertificate"
print crypto.dump_certificate(crypto.FILETYPE_PEM, p12.get_certificate())
print "\nKey"
print crypto.dump_privatekey(crypto.FILETYPE_PEM, p12.get_privatekey())
