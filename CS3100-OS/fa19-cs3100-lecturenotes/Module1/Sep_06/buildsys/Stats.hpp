#pragma once

#include <string>

#include "Employment.hpp"
#include "Area.hpp"

// These functions have been written for you
unsigned long total_employment_level(Employment *array);
float         average_employment_level(Employment *array);
unsigned long total_annual_wages(Employment *array);
float         mean_annual_wages(Employment *array);


// You must provide implementations for these functions
unsigned long minimum_annual_wages(Employment *array);
unsigned long maximum_annual_wages(Employment *array);
unsigned long median_annual_wages(Employment *array);
unsigned long mode_annual_wages(Employment *array);
float         stdev_annual_wages(Employment *array);
unsigned long unique_annual_wages(Employment *array);

// These functions find certain a statistical point and return
// the associated FIPS Area Title
std::string   loc_max_wages(Employment *array, Area *fips);
std::string   loc_min_wages(Employment *array, Area *fips);
std::string   loc_med_wages(Employment *array, Area *fips);

void          top_10_fips_areas_by_salary(Employment *array, Area *fips);
void          bot_10_fips_areas_by_salary(Employment *array, Area *fips);


// These functions are nice helpers
std::string area_fips_To_area_title(Area *fips, std::string code);
