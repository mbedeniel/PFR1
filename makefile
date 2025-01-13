start:
	python -m simulation.main

bd : 
	cd ./vocal
	make app
	cd ..


#a supprimer
test:
	python -m simulation.test_mode_auto

push:
	git add .
	git commit -m "update"
	git push origin simulation