# Compilation de l'exécutable de test

# Compilation des fichiers objets
src/pre_processing.o: src/pre_processing.c include/pre_processing.h
	gcc -c src/pre_processing.c -o src/pre_processing.o

src/color_treatment.o: src/color_treatment.c include/color_treatment.h
	gcc -c src/color_treatment.c -o src/color_treatment.o

src/position_treatment.o: src/position_treatment.c include/position_treatment.h
	gcc -c src/position_treatment.c -o src/position_treatment.o

src/shape_treatment.o: src/shape_treatment.c include/shape_treatment.h
	gcc -c src/shape_treatment.c -o src/shape_treatment.o

src/object.o: src/object.c include/object.h
	gcc -c src/object.c -o src/object.o


main.o: main.c include/pre_processing.h include/color_treatment.h include/position_treatment.h include/shape_treatment.h include/object.h
	gcc -c main.c -o main.o

# Compilation de l'exécutable
main.exe: src/pre_processing.o src/color_treatment.o src/position_treatment.o src/shape_treatment.o src/object.o main.o
	gcc src/pre_processing.o src/color_treatment.o src/position_treatment.o src/shape_treatment.o src/object.o main.o -o main.exe 
run: main.exe
	./main.exe



# Nettoyage
clean:
	rm -rf src/*.o pre_processing_test
