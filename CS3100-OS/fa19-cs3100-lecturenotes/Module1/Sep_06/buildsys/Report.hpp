#pragma once
#include <string>
#include <ostream>

struct AreaTitleWithStat {
	std::string area_title;
	long unsigned stat;

	friend std::ostream& operator<<(std::ostream& os, const AreaTitleWithStat& atws);
};

struct EmploymentDataSet {
	float         stdev_annual_wages;
	unsigned long unique_annual_wages;
	AreaTitleWithStat top_10_annual_wages[10];
	AreaTitleWithStat bot_10_annual_wages[10];
	AreaTitleWithStat top_10_annual_avg_estabs[10];
	AreaTitleWithStat bot_10_annual_avg_estabs[10];
	AreaTitleWithStat top_10_annual_avg_emplvl[10];
	AreaTitleWithStat bot_10_annual_avg_emplvl[10];
	AreaTitleWithStat median_annual_wage_area;
};

class Report {
	public:
		EmploymentDataSet all;
		EmploymentDataSet soft;

		Report();
		~Report() { };

		friend std::ostream& operator<<(std::ostream& os, const Report& rpt);  
};
