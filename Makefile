pre_processing_test.out: pre_processing_test.c pre_processing.o
	gcc -o pre_processing_test.out pre_processing_test.c pre_processing.o -W -Wall -ansi -pedantic -lm

pre_processing.o: pre_processing.c
	gcc -o pre_processing.o -c pre_processing.c -W -Wall -ansi -pedantic -lm

clean:
	rm -rf *.o