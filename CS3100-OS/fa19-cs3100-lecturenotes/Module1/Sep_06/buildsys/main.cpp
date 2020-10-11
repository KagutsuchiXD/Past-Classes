#include <iostream>
#include <iomanip>

#include "Database.hpp"
#include "Loop.hpp"
#include "Stats.hpp"
#include "Sort.hpp"
#include "Report.hpp"

void srt_fips_areas(Area* array, int n) {
	std::cout << n << " unsorted FIPS areas:\n";
	for (int i = 0; i < n; ++i)
		std::cout << array[i];

	// sort the first n fips areas
	sort_area_by_fips_code(array, n);

	std::cout << "\n\n" << n << " sorted FIPS areas:\n";
	for (int i = 0; i < n; ++i)
		std::cout << array[i];

	std::cout << std::endl << std::endl;
}

void print_n_employments(std::string desc, Employment* array, int start, int n) {
	std::cout << desc << std::endl;

	int end = start + n;
	for (int i = start; i < end; ++i)
		std::cout << array[i];
	
	std::cout << std::endl << std::endl;
}



int main(void) {
	Report rpt;
	int len;

	rpt.all.stdev_annual_wages                       = stdev_annual_wages(all_industries);
	rpt.all.unique_annual_wages                      = unique_annual_wages(all_industries);
	rpt.all.median_annual_wage_area.area_title       = loc_med_wages(all_industries, fips_areas);
	rpt.all.median_annual_wage_area.stat             = median_annual_wages(all_industries);

    len = count_all_empl(all_industries);
    sort_employment_by_total_annual_wages(all_industries, len);
	for (int i = 0; i < 10; i++) {
		rpt.all.top_10_annual_wages[i].stat       = all_industries[(len - 1) - i].total_annual_wages;
		rpt.all.top_10_annual_wages[i].area_title = area_fips_To_area_title(fips_areas, all_industries[(len - 1) - i].area_fips);
		rpt.all.bot_10_annual_wages[i].stat       = all_industries[i].total_annual_wages;
		rpt.all.bot_10_annual_wages[i].area_title = area_fips_To_area_title(fips_areas, all_industries[i].area_fips);
	}

	sort_employment_by_annual_avg_estabs(all_industries, len);
	for (int i = 0; i < 10; i++) {
		rpt.all.top_10_annual_avg_estabs[i].stat       = all_industries[(len - 1) - i].annual_avg_estabs;
		rpt.all.top_10_annual_avg_estabs[i].area_title = area_fips_To_area_title(fips_areas, all_industries[(len - 1) - i].area_fips);
		rpt.all.bot_10_annual_avg_estabs[i].stat       = all_industries[i].annual_avg_estabs;
		rpt.all.bot_10_annual_avg_estabs[i].area_title = area_fips_To_area_title(fips_areas, all_industries[i].area_fips);
	}

	sort_employment_by_annual_avg_emplvl(all_industries, len);
	for (int i = 0; i < 10; i++) {
		rpt.all.top_10_annual_avg_emplvl[i].stat       = all_industries[(len - 1) - i].annual_avg_emplvl;
		rpt.all.top_10_annual_avg_emplvl[i].area_title = area_fips_To_area_title(fips_areas, all_industries[(len - 1) - i].area_fips);
		rpt.all.bot_10_annual_avg_emplvl[i].stat       = all_industries[i].annual_avg_emplvl;
		rpt.all.bot_10_annual_avg_emplvl[i].area_title = area_fips_To_area_title(fips_areas, all_industries[i].area_fips);
	}


	rpt.soft.stdev_annual_wages                       = stdev_annual_wages(software_publishing);
	rpt.soft.unique_annual_wages                      = unique_annual_wages(software_publishing);
	rpt.soft.median_annual_wage_area.area_title       = loc_med_wages(software_publishing, fips_areas);
	rpt.soft.median_annual_wage_area.stat             = median_annual_wages(software_publishing);

    len = count_all_empl(software_publishing);
    sort_employment_by_total_annual_wages(software_publishing, len);
	for (int i = 0; i < 10; i++) {
		rpt.soft.top_10_annual_wages[i].stat       = software_publishing[(len - 1) - i].total_annual_wages;
		rpt.soft.top_10_annual_wages[i].area_title = area_fips_To_area_title(fips_areas, software_publishing[(len - 1) - i].area_fips);
		rpt.soft.bot_10_annual_wages[i].stat       = software_publishing[i].total_annual_wages;
		rpt.soft.bot_10_annual_wages[i].area_title = area_fips_To_area_title(fips_areas, software_publishing[i].area_fips);
	}

	sort_employment_by_annual_avg_estabs(software_publishing, len);
	for (int i = 0; i < 10; i++) {
		rpt.soft.top_10_annual_avg_estabs[i].stat       = software_publishing[(len - 1) - i].annual_avg_estabs;
		rpt.soft.top_10_annual_avg_estabs[i].area_title = area_fips_To_area_title(fips_areas, software_publishing[(len - 1) - i].area_fips);
		rpt.soft.bot_10_annual_avg_estabs[i].stat       = software_publishing[i].annual_avg_estabs;
		rpt.soft.bot_10_annual_avg_estabs[i].area_title = area_fips_To_area_title(fips_areas, software_publishing[i].area_fips);
	}

	sort_employment_by_annual_avg_emplvl(software_publishing, len);
	for (int i = 0; i < 10; i++) {
		rpt.soft.top_10_annual_avg_emplvl[i].stat       = software_publishing[(len - 1) - i].annual_avg_emplvl;
		rpt.soft.top_10_annual_avg_emplvl[i].area_title = area_fips_To_area_title(fips_areas, software_publishing[(len - 1) - i].area_fips);
		rpt.soft.bot_10_annual_avg_emplvl[i].stat       = software_publishing[i].annual_avg_emplvl;
		rpt.soft.bot_10_annual_avg_emplvl[i].area_title = area_fips_To_area_title(fips_areas, software_publishing[i].area_fips);
	}


	std::cout << rpt << std::endl;
}
