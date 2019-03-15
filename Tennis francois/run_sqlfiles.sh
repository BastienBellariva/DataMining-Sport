#!/bin/bash

#A decommenter si la distrib linux n'est pas a jour
#apt-get update && apt-get upgrade -y
#echo "Mise à jour packages système done"

echo "Veuillez saisir le nom d'utilisateur de la BDD :"
read -r USER

echo -n "Votre mot de passe : "
trap "stty echo" EXIT HUP INT QUIT
stty -echo
read -r PASS
stty echo
trap - EXIT HUP INT QUIT
echo "-----------------------------------------"


credentials=/mysql-credentials.cnf
echo "[client]" > $credentials
echo "user=$USER" >> $credentials
echo "password=$PASS" >> $credentials

verif=0

#Lancement du script "1_create_database_tennis" : crée la base d_tennis
if [ $verif -eq 0 ]; then
	mysql --defaults-extra-file=$credentials </1_create_database_tennis.sql 
		if [ $? -eq 0 ]; then
    			echo "La création de la base de données est terminée" 
		else
			echo "[Error] Création de la base de données"
			verif=1
		fi
fi

#Lancement du script "2_schema_tennis" : Créer les tables de la base d_tennis
if [ $verif -eq 0 ]; then
	mysql --defaults-extra-file=$credentials </2_schema_tennis.sql 
		if [ $? -eq 0 ]; then
    			echo "La schema de la base d_tennis est crée" 
		else
			echo "[Error] Création du schéma"
			verif=1
		fi
fi

#Lancement du script "3_foreign_key_tennis" : Créer les tables de la base d_tennis
if [ $verif -eq 0 ]; then
	mysql --defaults-extra-file=$credentials </3_foreign_key_tennis.sql 
		if [ $? -eq 0 ]; then
    			echo "Création des clés étrangères reussi" 
		else
			echo "[Error] Création des clés étrangères"
			verif=1
		fi
fi

#Lancement du script "4_import_comment_match" : import des données comment_match
if [ $verif -eq 0 ]; then
	mysql --defaults-extra-file=$credentials </4_import_comment_match.sql 
		if [ $? -eq 0 ]; then
    			echo "Import des données comment_match OK" 
		else
			echo "[Error] Import des données comment_match"
			verif=1
		fi
fi

#Lancement du script "5_import_location" : import des locations
if [ $verif -eq 0 ]; then
	mysql --defaults-extra-file=$credentials </5_import_location.sql 
		if [ $? -eq 0 ]; then
    			echo "Import des données locations OK" 
		else
			echo "[Error] Import des données locations"
			verif=1
		fi
fi

#Lancement du script "6_import_match" : import des données matchs
if [ $verif -eq 0 ]; then
	mysql --defaults-extra-file=$credentials </6_import_match.sql 
		if [ $? -eq 0 ]; then
    			echo "Import des données match OK" 
		else
			echo "[Error] Import des données match"
			verif=1
		fi
fi

#Lancement du script "7_import_players" : import des données players
if [ $verif -eq 0 ]; then
	mysql --defaults-extra-file=$credentials </7_import_players.sql 
		if [ $? -eq 0 ]; then
    			echo "Import des données players OK" 
		else
			echo "[Error] Import des données players"
			verif=1
		fi
fi

#Lancement du script "8_import_round" : import des données round
if [ $verif -eq 0 ]; then
	mysql --defaults-extra-file=$credentials </8_import_round.sql 
		if [ $? -eq 0 ]; then
    			echo "Import des données round OK" 
		else
			echo "[Error] Import des données round"
			verif=1
		fi
fi

#Lancement du script "9_import_series" : import des données series
if [ $verif -eq 0 ]; then
	mysql --defaults-extra-file=$credentials </9_import_series.sql 
		if [ $? -eq 0 ]; then
    			echo "Import des données series OK" 
		else
			echo "[Error] Import des données series"
			verif=1
		fi
fi

#Lancement du script "10_import_surface" : import des données surface
if [ $verif -eq 0 ]; then
	mysql --defaults-extra-file=$credentials </10_import_surface.sql 
		if [ $? -eq 0 ]; then
    			echo "Import des données surface OK" 
		else
			echo "[Error] Import des données surface"
			verif=1
		fi
fi

#Lancement du script "11_import_tournament" : import des données tournament
if [ $verif -eq 0 ]; then
	mysql --defaults-extra-file=$credentials </11_import_tournament.sql 
		if [ $? -eq 0 ]; then
    			echo "Import des données tournament OK" 
		else
			echo "[Error] Import des données tournament"
			verif=1
		fi
fi