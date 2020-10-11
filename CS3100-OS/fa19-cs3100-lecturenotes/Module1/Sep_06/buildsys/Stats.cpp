#include <iomanip>
#include <cmath>

#include "Stats.hpp"
#include "Sort.hpp"
#include "Loop.hpp"

// total employment level across all FIPS areas in this dataset
long unsigned total_employment_level(Employment *array) {
	unsigned long emp = 0;

	for (int i = 0; array[i].area_fips != "END"; ++i)
		emp += array[i].annual_avg_emplvl;

	return emp;
}

// average employees per FIPS area
float average_employment_level(Employment *array) {
	int n = count_all_empl(array);
	unsigned long emp = total_employment_level(array);

	return static_cast<float>(emp) / static_cast<float>(n);
}


// total wages paid across all FIPS areas in this dataset
long unsigned total_annual_wages(Employment *array) {
	unsigned long wages = 0;

	for (int i = 0; array[i].area_fips != "END"; ++i)
		wages += array[i].total_annual_wages;

	return wages;
}


// average wage per employee represented in this dataset
float mean_annual_wages(Employment *array) {
	unsigned long n = total_employment_level(array);
	unsigned long wages = total_annual_wages(array);

	return static_cast<float>(wages) / static_cast<float>(n);
}


unsigned long minimum_annual_wages(Employment *array) {
    // sort the Employment array
    int len = count_all_empl(array);
    sort_employment_by_total_annual_wages(array, len);
    // return the 1st annual wage
    return array[0].total_annual_wages;
}


unsigned long maximum_annual_wages(Employment *array) {
    // sort the Employment array
    int len = count_all_empl(array);
    sort_employment_by_total_annual_wages(array, len);
    // return the last annual wage
    return array[len-1].total_annual_wages;
}


unsigned long median_annual_wages(Employment *array) {
    // sort the Employment array
    int len = count_all_empl(array);
    sort_employment_by_total_annual_wages(array, len);
    // return the middle annual wage
    return array[len / 2].total_annual_wages;
}


/* TODO - implement me
unsigned long mode_annual_wages(Employment *array) {
	return 0UL;
}
*/


float stdev_annual_wages(Employment *array) {
	unsigned long wages = total_annual_wages(array);
    int n = count_all_empl(array);
	float mean = static_cast<float>(wages) / static_cast<float>(n);
	float sos = 0.0;

	for (int i = 0; i < n; ++i) {
		float diff = array[i].total_annual_wages - mean;
		sos += diff * diff;
	}

	return sqrt(sos / n);
}


// Two counties have identical software wages: $227365
// Gaston County, North Carolina
// Morgan County, Alabama
unsigned long unique_annual_wages(Employment *array) {
	// sort the Employment array
	int len = count_all_empl(array);
	sort_employment_by_total_annual_wages(array, len);

	unsigned long prev = -1,
				  curr,
				  unique = 0,
				  seen = 0;

	for (int i = 0; i < len; i++) {
		curr = array[i].total_annual_wages;
		if (curr != prev) {
			if (seen == 1)
				unique++;
			seen = 1;
			prev = curr;
		}
		else {
			seen++;
		}
	}
	if (seen == 1)
		unique++;

	return unique;
}


std::string area_fips_To_area_title(Area *fips, std::string code) {
	int i = 0;
	for (; fips[i].area_fips != "END"
			&& fips[i].area_fips != code; ++i)
		;

	return fips[i].area_title;
}

std::string loc_max_wages(Employment *array, Area *fips) {
    // sort the Employment array
    int len = count_all_empl(array);
    sort_employment_by_total_annual_wages(array, len);

    // Now find the name of the related FIPS area
    std::string code = array[len-1].area_fips;
	return area_fips_To_area_title(fips, code);
}


std::string loc_min_wages(Employment *array, Area *fips) {
    // sort the Employment array
    int len = count_all_empl(array);
    sort_employment_by_total_annual_wages(array, len);

    // Now find the name of the related FIPS area
    std::string code = array[0].area_fips;
	return area_fips_To_area_title(fips, code);
}


std::string loc_med_wages(Employment *array, Area *fips) {
    // sort the Employment array
    int len = count_all_empl(array);
    sort_employment_by_total_annual_wages(array, len);

    // Now find the name of the related FIPS area
    std::string code = array[len/2].area_fips;
	return area_fips_To_area_title(fips, code);
}


void top_10_fips_areas_by_salary(Employment *array, Area *fips) {
    // sort the Employment array
    int len = count_all_empl(array);
    sort_employment_by_total_annual_wages(array, len);

    std::cout << "The top 10 areas by salary are" << std::endl
	<< "------------------------------" << std::endl;

    // fill in the top10 areas by counting from the top
    for (int i = 0; i < 10; i++) {
	std::string code = array[(len - 1) - i].area_fips;

	// Now find the name of the related FIPS area
	int j = 0;
	for (; fips[j].area_fips != "END"
		&& fips[j].area_fips != code; ++j)
	    ;

	std::cout << '\t' << fips[j].area_title <<
	    std::setw(20) <<
	    "[$" << array[(len - 1) - i].total_annual_wages << "]\n";
    }
}


void bot_10_fips_areas_by_salary(Employment *array, Area *fips) {
    // sort the Employment array
    int len = count_all_empl(array);
    sort_employment_by_total_annual_wages(array, len);

    std::cout << "The bottom 10 areas by salary are" << std::endl
	<< "---------------------------------" << std::endl;

    // fill in the top10 areas by counting from the top
    for (int i = 0; i < 10; i++) {
	std::string code = array[i].area_fips;

	// Now find the name of the related FIPS area
	int j = 0;
	for (; fips[j].area_fips != "END"
		&& fips[j].area_fips != code; ++j)
	    ;

	std::cout << '\t' << fips[j].area_title << "     [$" << array[i].total_annual_wages << "]\n";
    }
}
