
> git init
	# initialize repository

> git status
	#  display the current state of the working directory and the staging area

> git config user.name "Your Name"
	# set your local username, you provide the name as an argument within quotes:

> git config user.name "youremail@example.com"
	# set your local email 

> git add README.md
> git add . (all files)
	# add files to the staging area

> git commit -m "A brief description of the changes"
	# recording a snapshot of your repository at a specific moment in time

> git remote add origin <remote_repository_URL>
	# links your local Git repository to a remote server, with "origin" used as a conventional shortcut name for that URL.
	This enables pushing and pulling changes between your local machine and the cloud-based repository.

> git branch -M main
	# Change the name of the current branch

> git push -u origin <branch_name>
	# push your local changes to your online repository.

> git config --global credential.helper 'cache --timeout=3600' 
	# Caches credentials for 1 hour (3600 seconds)

> git config --local --unset credential.helper
	# remove the credential helper setting specifically for the current local Git repository



Configuracion previa colaboracion

1. Limpiar config global

git config --global --unset user.email
git config --global --unset-all user.name

2. Accede a tu carpeta local (desde la Terminal)

3. Clonar Repositorio.

> git clone https://github.com/rmzneydev/economy-survival-simulator.git

4. Acceder Repositorio:
cd economy-survival-simulator

Hacer estos comandos dentro de su carpeta en terminal:

cd economy-survival-simulator

hacer el push de la rama:
git push origin branch_name

ir a la rama:
git switch "feature-nombre-tarea"

https://git-scm.com/cheat-sheet
