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
    			echo "Creation base de données OK" 
		else
			echo "[Error] Création de la base de données"
			verif=1
		fi
fi

#Lancement du script "02_create_table_match_nba" : crée la base d_nba
if [ $verif -eq 0 ]; then
	mysql --defaults-extra-file=$credentials <02_create_table_match_nba.sql 
		if [ $? -eq 0 ]; then
    			echo "Creation table match_nba OK" 
		else
			echo "[Error] Création table match_nba "
			verif=1
		fi
fi

#Lancement du script "03_create_table_equipe" : crée la base d_nba
if [ $verif -eq 0 ]; then
	mysql --defaults-extra-file=$credentials <03_create_table_equipe.sql 
		if [ $? -eq 0 ]; then
    			echo "Creation table equipe OK" 
		else
			echo "[Error] Création table equipe"
			verif=1
		fi
fi

#Lancement du script "04_create_table_saison" : crée la base d_nba
if [ $verif -eq 0 ]; then
	mysql --defaults-extra-file=$credentials <04_create_table_saison.sql 
		if [ $? -eq 0 ]; then
    			echo "Creation table saison OK" 
		else
			echo "[Error] Création table saison"
			verif=1
		fi
fi

#Lancement du script "05_create_table_stat_equipe" : crée la base d_nba
if [ $verif -eq 0 ]; then
	mysql --defaults-extra-file=$credentials <05_create_table_stat_equipe.sql 
		if [ $? -eq 0 ]; then
    			echo "Creation table stat_equipe OK" 
		else
			echo "[Error] Création table stat_equipe"
			verif=1
		fi
fi

#Lancement du script "06_create_table_joueur" : crée la base d_nba
if [ $verif -eq 0 ]; then
	mysql --defaults-extra-file=$credentials <06_create_table_joueur.sql 
		if [ $? -eq 0 ]; then
    			echo "Creation table joueur OK" 
		else
			echo "[Error] Création table joueur"
			verif=1
		fi
fi

#Lancement du script "07_create_table_stat_joueur" : crée la base d_nba
if [ $verif -eq 0 ]; then
	mysql --defaults-extra-file=$credentials <07_create_table_stat_joueur.sql 
		if [ $? -eq 0 ]; then
    			echo "Creation table stat_joueur OK" 
		else
			echo "[Error] Création table stat_joueur"
			verif=1
		fi
fi

#Lancement du script "08_create_foreign_keys" : crée les clés étrangères
if [ $verif -eq 0 ]; then
	mysql --defaults-extra-file=$credentials <08_create_foreign_keys.sql 
		if [ $? -eq 0 ]; then
    			echo "Creation foreign keys OK" 
		else
			echo "[Error] Création foreign keys"
			verif=1
		fi
fi