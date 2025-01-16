
#utliser la commande make run oubien mingw32-make run pour compiler et executer le fichier application


#creer les fichiers objets a partir des fichiers sources
speech_to_text.o: src/speech_to_text.c include/speech_to_text.h
	gcc -c src/speech_to_text.c -o src/speech_to_text.o

text_to_command.o: src/text_to_command.c include/text_to_command.h
	gcc -c src/text_to_command.c -o src/text_to_command.o

synonyme.o: src/synonyme.c include/synonyme.h
	gcc -c src/synonyme.c -o src/synonyme.o


main.o: main.c include/speech_to_text.h include/text_to_command.h include/synonyme.h
	gcc -c main.c -o main.o

#creer le fichier app executable en utilisant les fichiers objets
#src/speech_to_text.o src/text_to_command.o main.o synonyme.o
app: speech_to_text.o text_to_command.o main.o synonyme.o
	gcc -o app src/speech_to_text.o src/text_to_command.o src/synonyme.o main.o 


	
#pour le mode IHM
ihm.o: src/ModeManuel.c 
	gcc -c src/ModeManuel.c -o ihm.o
ihm: ihm.o
	gcc -o ihm ihm.o



#compiler et executer le fichier application
run: vocal
	./vocal

#supprimer les fichiers objets et l'application executable
clean:
	del /f src\speech_to_text.o src\text_to_command.o main.o app.exe

