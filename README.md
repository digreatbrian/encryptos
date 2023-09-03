![icon](https://github.com/digreatbrian/encryptos/blob/main/assets/encryptos.jpg)

# Encryptos Description

Get to encrypt data easily using a unique algorithm.

## Getting Started

Encryptos requires secret ,which is ,secret key/passcode to decrypt or encrypt data just in simple steps.

Install encryptos using pip::
          
        python -m pip install encryptos

### Prerequisites

No extra modules have to be installed to use this module but only python built-in modules will be used.

## Deployment

After installation,just use this module like this::
     
     from encryptos import encrypt,decrypt

     key="secret_key"
     string_="unencrypted_string"

     encrypted=encrypt(string_,key)
     decrypted=decrypt(encrypted, key)
	
First the string "string_" is encrypted to "encrypted" varible and then decrypted back to "string_" by "decrypt" function ,that is to "decrypted".

## Contributing

Please read [CONTRIBUTING.md](https://github.com/digreatbrian/encryptos/contributers) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Brian Musakwa** - *Initial work* - [digreatbrian](https://github.com/digreatbrian)

See also the list of [contributors](https://github.com/digreatbrian/encryptos/contributors) who participated in this project.

## License

This project is licensed under the Lesser General Public License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* I hereby thank everyone who has contributed to this software as any contribution is regarded good for better performance of the software.








