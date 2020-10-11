#include "Employment.hpp"
#include <iostream>

Employment::Employment(
		std::string       _area_fips,
		unsigned      _annual_avg_estabs,
		unsigned      _annual_avg_emplvl,
		long unsigned _total_annual_wages
		) {
	this->area_fips          =  _area_fips;
	this->annual_avg_estabs  =  _annual_avg_estabs;
	this->annual_avg_emplvl  =  _annual_avg_emplvl;
	this->total_annual_wages =  _total_annual_wages;
}

std::ostream& operator<<(std::ostream& os, const Employment& emp) {
	os << "[" << emp.area_fips << "]"
		<< "\tEstablishments:     " << emp.annual_avg_estabs  << std::endl
		<< "\tEmployment Level:   " << emp.annual_avg_emplvl  << std::endl
		<< "\tTotal Annual Wages: " << emp.total_annual_wages << std::endl;
	return os;  
}
