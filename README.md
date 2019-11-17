# RFC1751 encoding/decoding

Python scripts for encoding arbitrary data to human-readable list of words and decoding it. They are useful when transferring keys from/to air-gapped computers with keyboard and monitor, and also writing the keys on paper by hand or with printer.

Other practical methods for [binary-to-text encoding](https://en.wikipedia.org/wiki/Binary-to-text_encoding) are base58, base64. PGP's ASCII armor is based on base64. It have problems with using similar-looking symbols like zero and O, small L (l) and big I.

[RFC1751](https://tools.ietf.org/html/rfc1751) is a predecessor of the [BIP39 mnemonic seed phrases](https://en.bitcoin.it/wiki/Seed_phrase).

The RFC1751 wordlist is optimized by the size of the words (short words are preferred, biggest words are with 4 letters).

The BIP39 wordlist consists of bigger words, they are optimized to make it difficult to confuse two words with each other (this is why longer words are used, despite that only first 4 letters are enough to recover the key - you can technically write only the first 4 letters, although this is not recommended).

Don't forget that the written words will be visible on the bottom page, so don't write on a notebook, put the sheet of paper on a hard surface instead. For longevity use pencil instead of pen and right type of paper. Or write with pen and pencil (separately), just in case (the pencil's writing can be erased by rubbing, the pen's writing can be damaged by water). Don't forget the backups.

Example
=======

Creating a file with 128 random bytes:

```
$ dd if=/dev/urandom of=random.dat bs=128 count=1
1+0 records in
1+0 records out
128 bytes copied, 0.000205547 s, 623 kB/s
```
Checking the input file:

```
$ hexdump random.dat 
0000000 3903 9676 d7a9 89eb 7a8d beb1 1636 bd14
0000010 4431 cad1 2829 6ce9 4b83 c6df d504 925d
0000020 099c 5930 3d44 a887 6d77 9e8a 442b 876f
0000030 badd 7ab5 5f43 2fec 5243 02e4 f41b f0b4
0000040 7255 3d6d 748b 91f1 ebfc af37 5d88 c9d0
0000050 4def a8ff 0368 73e7 d965 9e4a ff4e 5060
0000060 3209 2e08 be59 8484 ffe4 751c 06f2 b77b
0000070 fb1a c3b1 b00d d847 380a bd31 9c4e ae6e
0000080
```

Converting it to RFC1751 English words:

```
$ ./data-to-english.py < random.dat  > example.txt
```

Checking the output file:

```
$ cat example.txt ; echo
ARE RAGE KEEN BASS FEED NINA GLUT SAGE DARN CRAM BUSH BREW OX MA DESK BANG GONG MAIN FLUE BREW TUSK BUY BELA ORAL HUFF AHEM GAY GAIT SEED RUNS DUAL CRAY KNEW BERN YEA NEST SKID SAID BRAN FROG YANK GUM USE HERO AD RIO ALOE DULL BEEN HANG AVER GIG AUNT ONTO WITH BLOW TILT ED SITE CEIL TREE DATA THEE RINK SUE MELD CHEW OVEN KNEW ICON WAIL MEL BUM GRID COO LOWE TEAR TUB SULK WEAL IKE STIR CLOD SIFT HIS SKEW DEAF HOC AUK TIME CAL NAIL DARE HURL OBOE BIAS BOG THY ANA DUE FINE AT
```

Converting the RFC1751 English words to binary file:

```
$ ./english-to-data.py < example.txt > data.dat
```

Checking the output file:

```
$ hexdump data.dat 
0000000 3903 9676 d7a9 89eb 7a8d beb1 1636 bd14
0000010 4431 cad1 2829 6ce9 4b83 c6df d504 925d
0000020 099c 5930 3d44 a887 6d77 9e8a 442b 876f
0000030 badd 7ab5 5f43 2fec 5243 02e4 f41b f0b4
0000040 7255 3d6d 748b 91f1 ebfc af37 5d88 c9d0
0000050 4def a8ff 0368 73e7 d965 9e4a ff4e 5060
0000060 3209 2e08 be59 8484 ffe4 751c 06f2 b77b
0000070 fb1a c3b1 b00d d847 380a bd31 9c4e ae6e
0000080
$ cmp random.dat data.dat
```

It works.
