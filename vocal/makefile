
#utliser la commande make run oubien mingw32-make run pour compiler et executer le fichier application


#creer les fichiers objets a partir des fichiers sources
src/speech_to_text.o: src/speech_to_text.c include/speech_to_text.h
	gcc -c src/speech_to_text.c -o src/speech_to_text.o

src/text_to_command.o: src/text_to_command.c include/text_to_command.h
	gcc -c src/text_to_command.c -o src/text_to_command.o

src/synonyme.o: src/synonyme.c include/synonyme.h
	gcc -c src/synonyme.c -o src/synonyme.o


main.o: main.c include/speech_to_text.h include/text_to_command.h include/synonyme.h
	gcc -c main.c -o main.o

#creer le fichier app executable en utilisant les fichiers objets
#src/speech_to_text.o src/text_to_command.o main.o synonyme.o
app: src/speech_to_text.o src/text_to_command.o main.o src/synonyme.o
	gcc -o app src/speech_to_text.o src/text_to_command.o src/synonyme.o main.o 
	make clean


	
#pour le mode IHM
src/ihm.o: src/ModeManuel.c  include/text_to_command.h include/synonyme.h
	gcc -c src/ModeManuel.c -o src/ihm.o
ihm: src/ihm.o src/text_to_command.o src/synonyme.o
	gcc -o ihm src/ihm.o src/text_to_command.o src/synonyme.o
	make clean


#compiler et executer le fichier application
run: vocal
	./vocal

#supprimer les fichiers objets et l'application executable
clean:
	del /f src\*.o

