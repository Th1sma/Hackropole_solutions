# Analyse
J'ai commencé par faire une analyse de la page web :

Je remarque ici qu'il y a une balise href en commentaire:
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
J'ai donc enlevé les commentaires afin de me rendre sur le lien. Une fois sur la nouvelle page. Du php apparait : 
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
