# Tone Master #

* Auteurs : Hrvoje Katić
* Télécharger [version stable][1]

Bienvenue à Tone Master ! J'ai créé ce petit module complémentaire NVDA juste pour le plaisir, mais aussi pour que vous ayez du plaisir tout en l'utilisant.

J'ai toujours voulu créer des mélodies musicales avec NVDA, plutôt que de simplement écouter les bips de progression et d'erreur de NVDA. Cependant, il n'est pas trop facile à faire, alors tout d'abord j'ai voulu le rendre plus facile. C'est pourquoi j'ai écrit Tone Master. Imaginez comment il pourrait être pour vous faire entendre NVDA jouant la musique de Mozzart ou Beethoven, ou peut être les meilleurs tubes des Rolling Stones. Bien que le résultat final ressemble  à ces sonneries ringtones sur les téléphones mobiles anciens, il peut toujours être amusant.

Tone Master simplifie le processus de lecture des séquences de tonalité en mettant en place des fichiers de données de tonalité. Ces fichiers peuvent être édités avec votre éditeur de texte favori et puis enregistrés pour une lecture avec NVDA. Pour obtenir des instructions, lisez la suite !

## Fichiers de données de tonalité

Avant que vous puissiez jouer votre première melody musicale avec Tone Master vous devez créer et charger votre fichier de données de tonalité en premier. Les fichiers de données de tonalité sont simplement des fichiers texte pour Tone Master avec l'extension.tdf. Tone Master utilise ces fichiers pour le traitement et la lecture des séquences de tonalité. Pour créer le fichier de données de tonalité pour Tone Master pour pouvoir jouer correctement, vous devez suivre les règles simples décrites ci-dessous.

1. Chaque ligne dans le fichier .tdf *doit* contenir trois paramètres, séparés par deux-points (:). Le premier paramètre est la hauteur de tonalité, le second paramètre est la durée de tonalité, et le troisième est le temps de silence entre chaque tonalité. Les trois paramètres sont nécessaires pour déterminer ceux-ci, sinon Tone Master ne sera pas en mesure de jouer vos données de tonalité.
2. Les paramètres hauteur et la durée doivent être spécifiés comme inscrit en nombre entier et le silence doit être spécifié comme valeur  réelle virgule flottante.
3. Un signe dièse (#) au début de n’importe quelle ligne dans le fichier .tdf sera traité comme un commentaire et sera ignoré par Tone Master.

Exemple: Jouer une séquence de 3 tonalités

1500:100:0.5

1000:100:0.09

500:100:0.7

Dans cet exemple, la première tonalité dans une séquence a une hauteur de 1500, une durée en silence de 100 et 0.5. La deuxième tonalité en hauteur est de 1000, la durée est de 100, et le silence est de 0.09. La dernière tonalité dans une séquence  a une hauteur de 500, la durée est de 100, et le silence est de 0.7.

Notez que le paramètre silence est nécessaire de le déterminer, même si vous pensez qu'il n'est pas indispensable, parce que si celuici n'est pas spécifié, NVDA remplacera la tonalité précédente par celle qui suit et vous obtiendrez des résultats inattendus. C'est pourquoi j'ai fait qu'il soit nécessaire.

Pour se familiariser avec la syntaxe de fichiers de données de tonalité, s’il vous plaît voir et essayez de modifier le fichier d'exemple fourni avec ce module complémentaire. Il est situé dans le sous-dossier "tones", où tous vos fichiers .tdf doivent être situés aussi bien.

## Touches de raccourci

* Alt+NVDA+T : Joue les données de tonalité actuellement chargé si tout est bien.
* Alt+Maj+NVDA+T : Arrête la lecture pour les données de tonalité actuellement chargé si n'importe quelles données de tonalité sont en cours de lecture.
* Alt+NVDA+N : Crée et ouvre un nouveau fichier de données de tonalité vierge dans le Bloc-notes pour l'édition.
* Alt+NVDA+L : Ouvre une boîte de dialogue qui vous permet de choisir un de vos fichiers de données de tonalité disponible afin d'être  charger pour la lecture.
* Alt+NVDA+E : Ouvre le fichier de données de tonalité actuellement chargé dans le Bloc-notes pour l'édition.
* Alt+NVDA+O : Ouvre un dossier avec les fichiers de données de tonalité où vous devez également les enregistrer dans l'ordre afin d'être localiser par Tone Master.

## Autres notes

Vous pouvez également créer, éditer et charger des fichiers de données de tonalité ou ouvrir un dossier de tonalité où ces fichiers se trouvent en allant dans le menu NVDA, sous-menu Outils, sous-menu Tone Master.

Lorsque la boîte de dialogue pour créer le nouveau fichier de données de tonalité s’affiche, tapez le nom sans l'extension .tdf. L'extension sera automatiquement ajoutée par Tone Master. Si aucun nom n'a été spécifiée, Tone Master utilisera le nom par défaut "untitled.tdf". Tone Master va créer automatiquement et charger le nouveau fichier pour vous, et il sera également ouvert dans le Bloc-notes pour l’édition. Appuyez sur ÉCHAP à l'invite du nom de fichier pour annuler la nouvelle création de fichier.

Note : Tone Master utilise le Bloc-notes pour éditer les fichiers de données de tonalité, puisqu’il est livré avec Windows par défaut et par conséquent n'importe quel ordinateur devrait l'avoir disponible.

Lorsque la boîte de dialogue pour charger un fichier de données de tonalité est ouverte, utilisez les touches fléchées pour sélectionner un fichier à charger et puis appuyez sur entrée. Appuyez sur ÉCHAP pour annuler le chargement.

Lorsque vous ouvrez un dossier avec les fichiers .tdf, vous pouvez ensuite les charger dans votre éditeur de texte pour le visionnage ou l'édition. Toutefois, afin d’entendre vos résultats à la volée, je vous recommande fortement de charger le fichier dans Tone Master tout d'abord si possible. Vous pouvez éditer le fichier, enregistrer vos progrès, et après chaque enregistrement vous pouvez utiliser la commande de lecture pour entendre votre dernier résultat.

## Changements pour la version 1.3

* Corrigé : Correction d'un problème de compatibilité avec les nouvelles versions de NVDA.

## Changements pour la version 1.2

* Corrigé : Majeur problem adressé lorsque en sélectionnant une données de tonalité vide puis en sélectionnant une autre et en essayant de jouer celle-ci les résultats dans les données de tonalité n'étant pas en cours de lecture.

## Changements pour la version 1.1

* Ajoutée : Une option pour créer un nouveau fichier de données de tonalité et ouvrir celui-ci dans le Bloc-notes.
* Ajoutée : Une option pour éditer actuellement le fichier de données de tonalité chargé dans le Bloc-notes.
* Amélioré : Messages d'erreur sont maintenant plus convivial pour l'utilisateur.
* Amélioré : Certaines fonctionnalités du module complémentaire comme louverture du dossier de données de tonalité ou de la modification des fichiers de données de tonalité dans le bloc-notes sont maintenant interdites sur écrans sécurisés.
* Amélioré : L'utilisateur sera notifié par NVDA si la lecture de données de tonalité est stoppée.
* Corrigée : Lecture non autorisée de données de tonalité lorsque celui-ci déjà joue.

## Changements pour la version 1.0

* Première version

[1]: https://github.com/nvdaaddons/toneMaster/releases/download/v1.2/toneMaster-1.2.nvda-addon
