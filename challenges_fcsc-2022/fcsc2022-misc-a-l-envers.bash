#!/bin/bash

echo "Connexion à localhost:4000..."

exec 3<>/dev/tcp/localhost/4000

while read line <&3; do
    echo $line
    if [[ $line == \>\>\>* ]]; then
        nline=$(echo $line |rev |tr -d '>>>')
        echo $nline
        echo $nline >&3
    fi
done

echo "Fermeture de la connexion..."
exec 3<&-
