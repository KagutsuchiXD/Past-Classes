#include <iostream>
#include <iomanip>
#include <cstring>
#include <sstream>

#include "Report.hpp"


std::ostream& operator<<(std::ostream& os, const AreaTitleWithStat& atws) {
	os << std::left << std::setw(34) << atws.area_title << atws.stat << std::endl;
	return os;
}

Report::Report() {
}

const int width = 35;

template<typename T>
void printLine(std::ostream& os, std::string label, T item) {
	os << std::left << std::setw(width) << label << item << std::endl;
}

template<typename T>
void printLine(std::ostream& os, std::string label, char prefix, T item) {
	os << std::left << std::setw(width) << label << prefix << item << std::endl;
}

std::ostream& operator<<(std::ostream& os, const Report& rpt) {
	os  << "[============]\n"
		   "[Final Report]\n"
		   "[============]\n\n"
		   "Statistics over all industries in 2017:\n"
		   "=======================================\n"
		<< std::setprecision(12);

	printLine(os, "Population STDDEV of Annual Wages", '$', rpt.all.stdev_annual_wages);
	printLine(os, "Number of unique Annual Wages", rpt.all.unique_annual_wages);
	os << "FIPS area with median annual wage: " << rpt.all.median_annual_wage_area << std::endl;

	os  << "Top 10 areas by Total Annual Wages" << std::endl
		<< "--------------------------------------------------" << std::endl;
	for (int i = 0; i < 10; i++)
		os << '\t' <<  std::setw(2) << std::right << i+1 << ". " << rpt.all.top_10_annual_wages[i];
	os << std::endl;

	os  << "Bottom 10 areas by Total Annual Wages" << std::endl
		<< "--------------------------------------------------" << std::endl;
	for (int i = 0; i < 10; i++)
		os << '\t' <<  std::setw(2) << std::right << i+1 << ". " << rpt.all.bot_10_annual_wages[i];
	os << std::endl;

	os  << "Top 10 areas by Annual Average Establishments" << std::endl
		<< "--------------------------------------------------" << std::endl;
	for (int i = 0; i < 10; i++)
		os << '\t' <<  std::setw(2) << std::right << i+1 << ". " << rpt.all.top_10_annual_avg_estabs[i];
	os << std::endl;

	os  << "Bottom 10 areas by Annual Average Establishments" << std::endl
		<< "--------------------------------------------------" << std::endl;
	for (int i = 0; i < 10; i++)
		os << '\t' <<  std::setw(2) << std::right << i+1 << ". " << rpt.all.bot_10_annual_avg_estabs[i];
	os << std::endl;

	os  << "Top 10 areas by Annual Average Employment Level" << std::endl
		<< "--------------------------------------------------" << std::endl;
	for (int i = 0; i < 10; i++)
		os << '\t' <<  std::setw(2) << std::right << i+1 << ". " << rpt.all.top_10_annual_avg_emplvl[i];
	os << std::endl;

	os  << "Bottom 10 areas by Annual Average Employment Level" << std::endl
		<< "--------------------------------------------------" << std::endl;
	for (int i = 0; i < 10; i++)
		os << '\t' <<  std::setw(2) << std::right << i+1 << ". " << rpt.all.bot_10_annual_avg_emplvl[i];
	os << std::endl;



	os << "Statistics over the software publishing industry in 2017:\n"
		  "=========================================================\n";

	printLine(os, "Population STDDEV of Annual Wages", '$', rpt.soft.stdev_annual_wages);
	printLine(os, "Number of unique Annual Wages", rpt.soft.unique_annual_wages);
	os << "FIPS area with median annual wage: " << rpt.soft.median_annual_wage_area << std::endl;

	os  << "Top 10 areas by Total Annual Wages" << std::endl
		<< "--------------------------------------------------" << std::endl;
	for (int i = 0; i < 10; i++)
		os << '\t' <<  std::setw(2) << std::right << i+1 << ". " << rpt.soft.top_10_annual_wages[i];
	os << std::endl;

	os  << "Bottom 10 areas by Total Annual Wages" << std::endl
		<< "--------------------------------------------------" << std::endl;
	for (int i = 0; i < 10; i++)
		os << '\t' <<  std::setw(2) << std::right << i+1 << ". " << rpt.soft.bot_10_annual_wages[i];
	os << std::endl;

	os  << "Top 10 areas by Annual Average Establishments" << std::endl
		<< "--------------------------------------------------" << std::endl;
	for (int i = 0; i < 10; i++)
		os << '\t' <<  std::setw(2) << std::right << i+1 << ". " << rpt.soft.top_10_annual_avg_estabs[i];
	os << std::endl;

	os  << "Bottom 10 areas by Annual Average Establishments" << std::endl
		<< "--------------------------------------------------" << std::endl;
	for (int i = 0; i < 10; i++)
		os << '\t' <<  std::setw(2) << std::right << i+1 << ". " << rpt.soft.bot_10_annual_avg_estabs[i];
	os << std::endl;

	os  << "Top 10 areas by Annual Average Employment Level" << std::endl
		<< "--------------------------------------------------" << std::endl;
	for (int i = 0; i < 10; i++)
		os << '\t' <<  std::setw(2) << std::right << i+1 << ". " << rpt.soft.top_10_annual_avg_emplvl[i];
	os << std::endl;

	os  << "Bottom 10 areas by Annual Average Employment Level" << std::endl
		<< "--------------------------------------------------" << std::endl;
	for (int i = 0; i < 10; i++)
		os << '\t' <<  std::setw(2) << std::right << i+1 << ". " << rpt.soft.bot_10_annual_avg_emplvl[i];
	os << std::endl;


	return os;  
}
