#include <iostream>

#include "Loop.hpp"

void print_every_empl(Employment *array) {
	for (int i = 0; array[i].area_fips != "END"; ++i)
		std::cout << array[i] << std::endl;
}

int count_all_empl(Employment *array) {
	int i = 0;
	for (; array[i].area_fips != "END"; ++i)
		;
	return i;
}

void print_every_area(Area *array) {
	for (int i = 0; array[i].area_fips != "END"; ++i)
		std::cout << array[i] /* << std::endl */ ;
}

int count_all_areas(Area *array) {
	int i = 0;
	for (; array[i].area_fips != "END"; ++i)
		;
	return i;
}
