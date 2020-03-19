# hsimpy




<p align="center">
    <img src ="./doc/img/logo.png" />
</p>


> **web page:** https://howsecureismypassword.net/

> **client-side:** https://github.com/howsecureismypassword/hsimp



## ABOUT hsimpy

> How Secure Is My Password?

Running on Python3.
Rather than just saying a password is "weak" or "strong", *How Secure is My Password?* lets your users know how long it would take someone to crack their password.




## EASY TO USE

### INSTALLING

hsimpy is a python package to be used called by a python module. It is needed to install the package to the usage.
In you *requirements.txt* file. Should be declared.

In your project where hsimpy is a dependencia, enter the command.

```bash
pip3 install -r requirements.txt
```


### USAGE

``` python
from hsimpy import Hsimpy

PWD = Hsimpy('Passw0rd!')

print('possible_characters: ' + PWD.possible_characters)
print('possible_combinations: ' + PWD.possible_combinations)
print('time_in_seconds: ' + PWD.time_in_seconds)
print('security_level: ' + PWD.security_level)
```


#### hsmipy.Hsimpy module configuration
hsmip module has a small config. We are using:

``` python
 {
    "calculationsPerSecond": 1e10, # 10 billion
    "good": 31557600e6, # 1 million years
    "ok": 31557600 # 1 year
}
```

Today, the data used is:

``` python
self.conf = {
    "calculations_per_second": 3900000,  # 1e10 10 billion
    "good": 31557600e3,  # 31557600e6 1 million years
    "ok": 31557600e1  # 31557600 1 year
}

```

#### character.Character module configuration
Sharacter module has a small config. We are using:

``` python
 {
    "ASCII Control Character": ["[\\u0000-\\u001F]", 32],
    "ASCII Lowercase": ["[a-z]", 26],
    "ASCII Uppercase": ["[A-Z]", 26],
    "ASCII Numbers": ["\\d", 10],
    "ASCII Top Row Symbols": ["[-!@£#$%^&*()=+_]", 15],
    "ASCII Other Symbols": ["[\\s\\?\\/\\.>,<`~\\|;:\\]}\\[{'\"\\\\]", 19],
    "Unicode Latin 1 Supplement": ["[\\u00A1-\\u00A2\\u00A4-\\u00FF]", 93],
    "Unicode Latin 1 Supplement Non Standard": ["[\\u0080-\\u00A0]", 33],
    "Unicode Latin Extended A": ["[\\u0100-\\u017F]", 128],
    "Unicode Latin Extended B": ["[\\u0180-\\u024F]", 208],
    "Unicode Latin Extended C": ["[\\u2C60-\\u2C7F]", 32],
    "Unicode Latin Extended D": ["[\\uA720-\\uA7FF]", 29],
    "Unicode Cyrillic Uppercase": ["[\\u0410-\\u042F]", 32],
    "Unicode Cyrillic Lowercase": ["[\\u0430-\\u044F]", 32]
}
```




## DEVELOPMENT

When not exist a pylintrc file. We can create using command below:

``` bash
pylint --generate-rcfile > ~/.

```




### USING PYLINT AND PYCODESTYLE

``` bash
pylint ./hsimpy/*.py
pycodestyle ./hsimpy/*.py
```




### TESTS

After package installing, into folder of project enter below command.

``` bash
virtualenv hsimp_env
pip3 install -r requirements-test.txt
python3 -m unittest discover tests  # will discover al tests

```




## REFERENCES

- https://howsecureismypassword.net/
- https://github.com/howsecureismypassword/



## AUTOR

> [contribuidores](./CONTRIBUTING.md)
