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

#Lancement du script "01_create_database_nba" : crée la base d_nba
if [ $verif -eq 0 ]; then
	mysql --defaults-extra-file=$credentials <01_create_database_nba.sql 
		if [ $? -eq 0 ]; then
    			echo "La création de la base de données est terminée" 
		else
			echo "[Error] Création de la base de données"
			verif=1
		fi
fi