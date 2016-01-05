Nasa GISS Surface Temperature (GISTEMP) Analysis. Four different series are provided: Global Annual Temperature Anomalies (Land) 1880-2014, Global Annual Temperature Anomalies (Land and Ocean) 1880-2014, Hemispheric Temperature Anomalies (Land+ Ocean) 1880-2014 and Annual Temperature anomalies (Land + Ocean) for three latitude bands that cover 30%, 40% and 30% of the global area, respectively, 1900-2014.

## Data

### Period of Record
> 1880-2014 (Anomalies are relative to the 1951-80 base period means.)

### Description

> The NASA GISS Surface Temperature (GISTEMP) analysis provides a measure of the changing global surface temperature with monthly resolution for the period since 1880, when a reasonably global distribution of meteorological stations was established. The input data Ruedy et al. use for the analysis, collected by many national meteorological services around the world, are the adjusted data of the [Global Historical Climatology Network (GHCN) Vs. 3](http://www.ncdc.noaa.gov/ghcnm/) (this represents a change from prior use of unadjusted Vs. 2 data) (Peterson and Vose, 1997 and 1998), [United States Historical Climatology Network (USHCN)](http://www.ncdc.noaa.gov/oa/climate/research/ushcn/) data, and [SCAR (Scientific Committee on Antarctic Research)](http://www.antarctica.ac.uk/met/READER/) data from Antarctic stations. Documentation of the basic analysis method is provided by Hansen et al. (1999), with several modifications described by Hansen et al. (2001). The GISS analysis is updated monthly, however CDIAC's presentation of the data here is updated annually.

### Key finding
> The global mean temperature for 2014 was the warmest on record (see [Trends section](http://cdiac.ornl.gov/trends/temp/hansen/hansen.html#trends) for further details)


### Sources
1.
  * Name: Global Annual Temperature Anomalies (Land), 1880-2014
  * Web: http://cdiac.ornl.gov/ftp/trends/temp/hansen/gl_land.txt
1.
  * Name: Global Annual Temperature Anomalies (Land+Ocean), 1880-2014
  * Web: http://cdiac.ornl.gov/ftp/trends/temp/hansen/gl_land_ocean.txt
1.
  * Name: Hemispheric Temperature Anomalies (Land+Ocean), 1880-2014
  * Web: http://cdiac.ornl.gov/ftp/trends/temp/hansen/nhsh.txt
1.
  * Name: Global Annual Temperature Anomalies (Land+Ocean) for three latitude bands, 1900-2014
  * Web: http://cdiac.ornl.gov/ftp/trends/temp/hansen/norlowsou.txt

## Data Preparation

### Requirements

Python 2 together with modules urllib and csv are required in order to process the data. 

### Processing

Run the following script from this directory to download and process the data:

```bash
make
```

### Resources

The raw data are stored in `./archive/`. The processed data can be found in `./data`.

## License

### Data

Data are sourced from US Federal government funded agency and no copyright restrictions are applied. More specifically:

> If you wish to use a diagram, image, graph, table, or other materials from the CDIAC website and are concerned with obtaining permission and possible copyright restrictions, there should be no concerns. All of the reports, graphics, data, and other information on the CDIAC website are freely and publicly available without copyright restrictions.[*][permissions]

### Additional work

> All the additional work made to build this Data Package is made available under the Public Domain Dedication and License v1.0 whose full text can be found at: http://www.opendatacommons.org/licenses/pddl/1.0/

## Citations

> Ruedy, R., M. Sato, and K. Lo. 2015. NASA GISS Surface Temperature (GISTEMP) Analysis. In Trends: A Compendium of Data on Global Change. Carbon Dioxide Information Analysis Center, Oak Ridge National Laboratory, U.S. Department of Energy, Oak Ridge, Tenn., U.S.A. doi: 10.3334/CDIAC/cli.001 .


[permissions]: http://cdiac.ornl.gov/permission.html
