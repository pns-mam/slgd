# slgd
Systèmes linéaires en grande dimension 

6 Janvier 2025 - 10 Javier 2025

## Intervenants

- [Jean-Luc Bouchot](https://jlbouchot.github.io)
- [Mahmoud Elsawy](https://www-sop.inria.fr/atlantis/perso/Mahmoud.Elsawy/elsawy.html). 

## Objectifs

L'objectif est pour l'étudiant.e d'obtenir une compréhension pratique et théorique des problèmes liés à la résolution de problèmes linéaires de grandes tailles. 

A la fin du projet il est attendu que l'apprenant.e aura
* une compréhension de comment les systèmes linéaires peuvent être résolus sur des architectures (relativement) modernes,
* une première expérience d'implémentation de méthode itérative,
* une intuition pour le besoin de développer des méthodes basées sur l'algèbre linéaire creuse,
* une idée de l'importance de la résolution des systèmes linéaires

## Quelques mots-clés

On liste ici des mots cléfs qui seront, traités, pour certains seulement superficiellement, dans le cours
* Linear solver
* Iterative methods
* Sparse linear algebra
* Jacobi, Gauss-Seidel, SOR
* (left/right) preconditioning
* Krylov solvers
* GMRES, restart, sliding window

## Ressources suggérées

* [Matrix computations, 3rd Ed., G.H. Golub and C.F. Van Loan](https://convexoptimization.com/TOOLS/MatrixComp.pdf)
* [Iterative methods for sparse linear systems, 2nd Ed., Y. Saad](https://www-users.cse.umn.edu/~saad/IterMethBook_2ndEd.pdf)
* [Computational Science and Engineering, G. Strang](https://math.mit.edu/~gs/cse/)
* [A theoretical introduction to numerical analysis, V.S. Ryaben'kil and S.V.Tsynkov](https://www.routledge.com/A-Theoretical-Introduction-to-Numerical-Analysis/Ryabenkii-Tsynkov/p/book/9781584886075)
* [Theoretical numerical analysis, K. Atkinson and W. Han](https://link.springer.com/book/10.1007/978-1-4419-0458-4)
* [Basic linear algebra in python](https://primer-computational-mathematics.github.io/book/c_mathematics/linear_algebra/5_Linear_Algebra_in_Python.html)

## Evaluation et organisation

On se retrouvera 8 fois à raison de 4h à chaque fois: 
* Lundi, Mardi, Jeudi, et Vendredi matin, 8h00 - 12h00
* Lundi, Mardi, Mercredi, et Vendredi après-midi, 13h30 - 17h30.

La dernière session (vendredi après-midi) est dédiée à la présentation des résultats. 

Les projets seront présentés en groupe de 2. 

Livrables suivants sont attendus par mail AVANT le début des soutenances (vendredi 13h30 dernier délai): 
* Un rapport décrivant et comparant les diverses approches présentées dans le cours (et plus...) et implémentées. On pourra par exemple choisir comme axe de comparaison la consommation mémoire, le temps de calcul, le nombre d'itérations, le nombre de flops, la qualité de la solution, les cas limites eu égard de la théorie spectrale ou encore en termes de dimensions... Le choix est libre pour présenter l'aspect qui semble le plus intéressant au groupe. 
* Tous les codes utilisés pour générer toutes les figures / résultats. 
* Une courte présentation, utilisée comme support.

La soutenance ne durera pas plus de 15 minutes par groupe  avec pas plus de 7 à 10 minutes de présentation et le reste dédié à la discussion.

## Environnement python

Il est attendu que le projet soit réalisé à l'aide de python et des librairies [scipy](https://docs.scipy.org/doc/scipy/reference/)/[numpy](https://numpy.org/doc/stable/reference/). 

Chaque partie mise en lumière lors des séances aura son propre fichier python lançable contenant toutes les fonctions utiles. 
Des exemples seront donnés afin d'aider à démarrer. 

Il est recommandé d'utiliser un environnement virtuel afin de s'habituer aux bonnes pratiques industrielles d'une part, et de ne pas polluer son environnement d'autres part. Les informations données ci-dessous sont pensées pour une utilisation sur une machine linux. Quelques adaptations seront nécessaires pour les faire fonctionner sur des machines windows -- ce qu'on ne recommande pas. 

### conda 
> conda create -n SLGD # Stands for Systemes Lineares en Grandes Dimensions
> conda actiate SLGD # Permet de s'isoler de l'environnement local pour se mettre dans l'environnement dédié que l'on vient de créer
> conda install scipy numpy matplotlib # Installe les librairies pour l'environnement actif uniquement

On peut ressortir d'un environnement fraichement créer via 
> conda deactivate

On script python peut ensuite être appelé avec 
> python nom_de_script.py

### venv

Une documentation peut être lue [ici](https://python.land/virtual-environments/virtualenv). 
> python -m venv /path/to/new/virtual/environment # Usually a local folder at root folder
> source /path/to/new/virtual/environment/bin/activate
> pip install scipy numpy matplotlib 

De même, on sort de l'environnement via 
> deactivate



## Misc

- [discussions](https://github.com/pns-mam/slgd/discussions/1)

