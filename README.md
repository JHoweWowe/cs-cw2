# Computer Security 2020-21 Coursework 2

**Idea**: Gained practical experience into an introduction to cryptography and learned the ideas of crafting a man-in-middle attack using existing Python libraries and functions.

**Final Grade**: 100% (A1)

**Programming Language**: Python

## Some Commands Used:
### Asymmetric Encryption with GPG
Decryption Message: `gpg -d coded.asc > decoded.txt`

Recieve Specific Key: `gpg --keyserver keys.gnupg.net --recv-key 96CB3DC2AFCA575FEA2AAB3F000B2EDC21F6F23D`

Encrypt File: `gpg --recipient (user) --encrypt (filename)`

Other commands can be found in the coursework document.

### Spoofing Email Sender
`mailx -r "darth.vader@starwars.com" -s s1840358 "s1840358" cw-2@ed.ac.uk`

## Code Organization:
**While the majority of files for Section 1 and 2 are located in the main directory, section 3 is located in mitm folder.**
* [Coursework 2 Document](https://github.com/JHoweWowe/cs-cw2/blob/master/cw2.pdf): Coursework instruction document
* [mitm](https://github.com/JHoweWowe/cs-cw2/tree/master/mitm): Contains files and Python libraries for execution of man-in-the-middle (mitm) attack. 
* [feedback.txt](https://github.com/JHoweWowe/cs-cw2/blob/master/feedback.txt): Coursework grading feedback
