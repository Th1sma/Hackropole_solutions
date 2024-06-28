# Analyse
J'ai commencé par faire une analyse du fichier :
```sh
file aaarg.txt # ou alors cat aaarg.txt
```
Je remarque ici que c'est un fichier ***".elf"*** :
```
aaarg.txt: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=f5b07c01242cc5987bed7730c2762ae0491b5ddc, stripped
```
# Solution
Après quelques recherches, j'ai trouvé l'utilitaire ***readelf*** qui va me permettre de faire de l'analyse sur ce fichier afin de trouver le flag.
Je commence donc par faire une analyse des sections du fichier :
```sh
readelf -S aaarg.txt
```
```
Il y a 28 en-têtes de section, débutant à l'adresse de décalage 0x3180:

En-têtes de section :
  [Nr] Nom               Type             Adresse           Décalage
       Taille            TaillEntrée      Fanion Lien  Info  Alignement
  [ 0]                   NULL             0000000000000000  00000000
       0000000000000000  0000000000000000           0     0     0
  [ 1] .interp           PROGBITS         00000000004002a8  000002a8
       000000000000001c  0000000000000000   A       0     0     1
  [ 2] .note.ABI-tag     NOTE             00000000004002c4  000002c4
       0000000000000020  0000000000000000   A       0     0     4
  [ 3] .note.gnu.bu[...] NOTE             00000000004002e4  000002e4
       0000000000000024  0000000000000000   A       0     0     4
  [ 4] .hash             HASH             0000000000400308  00000308
       000000000000002c  0000000000000004   A       6     0     8
  [ 5] .gnu.hash         GNU_HASH         0000000000400338  00000338
       0000000000000024  0000000000000000   A       6     0     8
  [ 6] .dynsym           DYNSYM           0000000000400360  00000360
       0000000000000090  0000000000000018   A       7     1     8
  [ 7] .dynstr           STRTAB           00000000004003f0  000003f0
       000000000000004c  0000000000000000   A       0     0     1
  [ 8] .gnu.version      VERSYM           000000000040043c  0000043c
       000000000000000c  0000000000000002   A       6     0     2
  [ 9] .gnu.version_r    VERNEED          0000000000400448  00000448
       0000000000000020  0000000000000000   A       7     1     8
  [10] .rela.dyn         RELA             0000000000400468  00000468
       0000000000000048  0000000000000018   A       6     0     8
  [11] .rela.plt         RELA             00000000004004b0  000004b0
       0000000000000030  0000000000000018  AI       6    23     8
  [12] .init             PROGBITS         0000000000401000  00001000
       0000000000000017  0000000000000000  AX       0     0     4
  [13] .plt              PROGBITS         0000000000401020  00001020
       0000000000000030  0000000000000010  AX       0     0     16
  [14] .text             PROGBITS         0000000000401050  00001050
       0000000000000231  0000000000000000  AX       0     0     16
  [15] .fini             PROGBITS         0000000000401284  00001284
       0000000000000009  0000000000000000  AX       0     0     4
  [16] .rodata           PROGBITS         0000000000402000  00002000
       0000000000000126  0000000000000000   A       0     0     16
  [17] .eh_frame_hdr     PROGBITS         0000000000402128  00002128
       0000000000000044  0000000000000000   A       0     0     4
  [18] .eh_frame         PROGBITS         0000000000402170  00002170
       0000000000000120  0000000000000000   A       0     0     8
  [19] .init_array       INIT_ARRAY       0000000000403e00  00002e00
       0000000000000008  0000000000000008  WA       0     0     8
  [20] .fini_array       FINI_ARRAY       0000000000403e08  00002e08
       0000000000000008  0000000000000008  WA       0     0     8
  [21] .dynamic          DYNAMIC          0000000000403e10  00002e10
       00000000000001e0  0000000000000010  WA       7     0     8
  [22] .got              PROGBITS         0000000000403ff0  00002ff0
       0000000000000010  0000000000000008  WA       0     0     8
  [23] .got.plt          PROGBITS         0000000000404000  00003000
       0000000000000028  0000000000000008  WA       0     0     8
  [24] .data             PROGBITS         0000000000404028  00003028
       0000000000000010  0000000000000000  WA       0     0     8
  [25] .bss              NOBITS           0000000000404038  00003038
       0000000000000010  0000000000000000  WA       0     0     8
  [26] .comment          PROGBITS         0000000000000000  00003038
       0000000000000053  0000000000000001  MS       0     0     1
  [27] .shstrtab         STRTAB           0000000000000000  0000308b
       00000000000000f3  0000000000000000           0     0     1
Clé des fanions :
  W (écriture), A (allocation), X (exécution), M (fusion), S (chaînes), I (info),
  L (ordre des liens), O (traitement supplémentaire par l'OS requis), G (groupe),
  T (TLS), C (compressé), x (inconnu), o (spécifique à l'OS), E (exclu),
  D (mbind), l (grand), p (processor specific)
```
Je vais donc commencer par analyser certains sections qui me semble intéressantes :

- .text
- .data
- .rodata

Je trouve donc le flag dans la section ***".rodata"*** via cette commande :
```sh
readelf -x .rodata aaarg.txt
```
```
Vidange hexadécimale de la section « .rodata » :
  0x00402000 01000200 00000000 00000000 00000000 ................
  0x00402010 46e2808d 43e2808d 53e2808d 43e2808d F...C...S...C...
  0x00402020 7be2808d 66e2808d 39e2808d 61e2808d {...f...9...a...
  0x00402030 33e2808d 38e2808d 61e2808d 64e2808d 3...8...a...d...
  0x00402040 61e2808d 63e2808d 65e2808d 39e2808d a...c...e...9...
  0x00402050 64e2808d 64e2808d 61e2808d 33e2808d d...d...a...3...
  0x00402060 61e2808d 39e2808d 61e2808d 65e2808d a...9...a...e...
  0x00402070 35e2808d 33e2808d 65e2808d 37e2808d 5...3...e...7...
  0x00402080 61e2808d 65e2808d 63e2808d 31e2808d a...e...c...1...
  0x00402090 38e2808d 30e2808d 63e2808d 35e2808d 8...0...c...5...
  0x004020a0 61e2808d 37e2808d 33e2808d 64e2808d a...7...3...d...
  0x004020b0 62e2808d 62e2808d 37e2808d 63e2808d b...b...7...c...
  0x004020c0 33e2808d 36e2808d 34e2808d 66e2808d 3...6...4...f...
  0x004020d0 65e2808d 31e2808d 33e2808d 37e2808d e...1...3...7...
  0x004020e0 66e2808d 63e2808d 36e2808d 37e2808d f...c...6...7...
  0x004020f0 32e2808d 31e2808d 64e2808d 37e2808d 2...1...d...7...
  0x00402100 39e2808d 39e2808d 37e2808d 63e2808d 9...9...7...c...
  0x00402110 35e2808d 34e2808d 65e2808d 38e2808d 5...4...e...8...
  0x00402120 64e2808d 7d00                       d...}.
```
Le flag apparait ici en ASCII ***"FCSC{...}"***
Pour mieux le visualiser le flag, on va utilisé l'argument ***"-p"*** fourni par l'utilitaire readself.
```sh
readelf -p .rodata aaarg.txt
```
```
Vidange textuelle de la section « .rodata » :
  [    10]  FCSC{f9a38adace9dda3a9ae53e7aec180c5a73dbb7c364fe137fc6721d7997c54e8d}

```
