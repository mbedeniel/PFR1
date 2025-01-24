SRC := src
INCLUDE := include

########################################################
#faite 'make run' pour creer le fichier excecutable (main_test_image.exe)
#exe file

main_test_image.o:main_test_image.c pre_processing.o color_treatment.o shape_treatment.o image_interface.o object.o position_treatment.o
	gcc -c main_test_image.c -o main_test_image.o -W -Wall -ansi -pedantic -lm
run: main_test_image.o
	gcc -o main_test_image.exe main_test_image.o pre_processing.o color_treatment.o shape_treatment.o image_interface.o object.o position_treatment.o -W -Wall -ansi -pedantic -lm
##########################################################

#############################
########### IMAGE ###########
#############################

main_test_image.out: main_test_image.c pre_processing.o color_treatment.o shape_treatment.o image_interface.o object.o position_treatment.o file_dynamique.o pile.o element.o 
	gcc -o main_test_image.out main_test_image.c pre_processing.o color_treatment.o shape_treatment.o image_interface.o object.o position_treatment.o file_dynamique.o pile.o element.o -W -Wall -ansi -pedantic -lm

image_interface.o: $(SRC)/image_interface.c $(INCLUDE)/image_interface.h $(INCLUDE)/position_treatment.h $(INCLUDE)/shape_treatment.h $(INCLUDE)/color_treatment.h $(INCLUDE)/pre_processing.h $(INCLUDE)/object.h $(INCLUDE)/file_dynamique.h 
	gcc -o image_interface.o -c $(SRC)/image_interface.c -W -Wall -ansi -pedantic -lm

pre_processing.o: $(SRC)/pre_processing.c $(INCLUDE)/pre_processing.h
	gcc -o pre_processing.o -c $(SRC)/pre_processing.c -W -Wall -ansi -pedantic -lm

color_treatment.o: $(SRC)/color_treatment.c $(INCLUDE)/color_treatment.h
	gcc -o color_treatment.o -c $(SRC)/color_treatment.c -W -Wall -ansi -pedantic -lm

shape_treatment.o: $(SRC)/shape_treatment.c $(INCLUDE)/shape_treatment.h
	gcc -o shape_treatment.o -c $(SRC)/shape_treatment.c -W -Wall -ansi -pedantic -lm

position_treatment.o: $(SRC)/position_treatment.c $(INCLUDE)/position_treatment.h
	gcc -o position_treatment.o -c $(SRC)/position_treatment.c -W -Wall -ansi -pedantic -lm

object.o: $(SRC)/object.c $(INCLUDE)/color_treatment.h $(INCLUDE)/shape_treatment.h $(INCLUDE)/position_treatment.h
	gcc -o object.o -c $(SRC)/object.c -W -Wall -ansi -pedantic -lm

clean_o:
	rm -rf *.o

clean_out:
	rm -rf *.out

clean_out_o:
	rm -rf *.o *.outtst_file_dynamique.out : tst_file_dynamique.c element.o file_dynamique.o
	gcc -o tst_file_dynamique.out tst_file_dynamique.c element.o file_dynamique.o

######################################
########### FILE DYNAMIQUE ###########
######################################

file_dynamique.o : $(SRC)/file_dynamique.c $(INCLUDE)/file_dynamique.h $(INCLUDE)/element.h
	gcc -o file_dynamique.o -c $(SRC)/file_dynamique.c -W -Wall -ansi -pedantic -lm

element.o : $(SRC)/element.c $(INCLUDE)/element.h
	gcc -o element.o -c $(SRC)/element.c -W -Wall -ansi -pedantic -lm

######################################
########### PILE DYNAMIQUE ###########
######################################

pile.o : $(SRC)/pile.c $(INCLUDE)/pile.h $(INCLUDE)/file_dynamique.h
	gcc -o pile.o -c $(SRC)/pile.c -W -Wall -ansi -pedantic -lm
