
#utliser la commande make run oubien mingw32-make run pour compiler et executer le fichier application
push:
	git add .
	git commit -m "update"
	git push

#creer les fichiers objets a partir des fichiers sources
src/speech_to_text.o: src/speech_to_text.c include/speech_to_text.h
	gcc -c src/speech_to_text.c -o src/speech_to_text.o

src/text_to_command.o: src/text_to_command.c include/text_to_command.h
	gcc -c src/text_to_command.c -o src/text_to_command.o

main.o: main.c include/speech_to_text.h include/text_to_command.h
	gcc -c main.c -o main.o

#creer le fichier app executable en utilisant les fichiers objets
app: src/speech_to_text.o src/text_to_command.o main.o
	gcc -o app src/speech_to_text.o src/text_to_command.o main.o
#pour le mode IHM
ihm.o: src/ModeManuel.c 
	gcc -c src/ModeManuel.c -o ihm.o
ihm: ihm.o
	gcc -o ihm ihm.o



#compiler et executer le fichier application
run: app
	./app
#supprimer les fichiers objets et l'application executable
clean:
	del /f src\speech_to_text.o src\text_to_command.o main.o app.exe

