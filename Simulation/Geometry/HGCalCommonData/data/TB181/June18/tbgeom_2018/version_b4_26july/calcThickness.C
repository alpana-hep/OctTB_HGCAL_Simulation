#include <map>
#include <iostream>
#include <fstream>
#include <vector>

#pragma link C++ operators map<int, vector<double>>;
#pragma link C++ operator map<int, vector<double>>::iterator; 
#pragma link C++ operator map<int, vector<double>>::const_iterator;
#pragma link C++ operator map<int, vector<double>>::reverse_iterator;

void calcThickness(string inputFile_name){


  ifstream file;
  std::vector <int> ind;
  std::vector <string> mat;
  std::vector <double> thick;
  
  file.open(inputFile_name.c_str(), ifstream::in );
  char filename[200];

  int tmpind = -99;
  string tmpmat = "aa";
  double tmpthick = -99.0;
  
  int imat = 0;
  
  while(!file.eof()){
    //file >> filename >> type >> tmpxsec;
    file >> tmpind;
    file >> tmpmat;
    file >> tmpthick;
    std::cout<<"tmpind = "<<tmpind<<std::endl;
    std::cout<<"tmpmat = "<<tmpmat<<std::endl;
    std::cout<<"tmpthick = "<<tmpthick<<std::endl;

    if(strncmp(filename,"#",1)==0)
      {
	string line;
        getline(file,line);
	cout<<"getline .... "<<line<<endl;
        continue;
      }
    
    ind.push_back(tmpind);
    mat.push_back(tmpmat);
    thick.push_back(tmpthick);
    
    std::cout<<"File name and itype and xsec "<<filename<<" "<<ind[imat]<<" "<<mat[imat]<<" "<<thick[imat]<<std::endl;
    imat++;
  }//while(!datafile.eof())                                                                                                                                                          
  /*
  ///EE 
  map<int, vector<float> > line_el {
    {0, {8, 12, 0, 7,7,7, 1, 3, 6, 13}},
      {1, {4, 5, 4, 6}},
	{2, {4, 5, 4, 6}},
	  {3, {4, 5, 4, 6}},
	    {4, {4, 5, 4, 6, 3, 1, 7, 7, 7, 0, 9}},
	      {5, {4, 5, 4, 6}},
		{6, {4, 5, 4, 6}},
		  {7, {4, 5, 4, 6}},
		    {8, {4, 5, 4, 6}},
		      {9, {4, 5, 4, 6}},
			{10, {4, 5, 4, 6}},
			  {11, {4, 5, 4, 6}},
			    {12, {4, 5, 4, 10}},
			      {13, {6, 4, 5, 4}},
				{14, {6, 4, 5, 4}},
				  {15, {6, 11, 14, 8}},
				    };

  */


  ///FH
  map<int, vector<float> > line_el {
    {0, {9, 7, 14, 0, 3, 2, 5, 4, 4, 4, 1}},
      {1, {11, 0, 0, 0, 3, 2, 5, 4, 4, 4, 1}},
	{2, {6, 0, 0, 0, 3, 2, 5, 4, 4, 4, 1}},
	  {3, {13, 0, 0, 0, 3, 2, 5, 4, 4, 4, 1}},
	    {4, {12, 0, 10, 7, 8}}
  };
				   
  

  vector<float> sum_l;
  for(map<int,vector<float>>::iterator it = line_el.begin(); it != line_el.end(); ++it) {
    
    double tmpsum = 0;

    for(int ii=0; ii<line_el[it->first].size(); ii++){
      //sum_l[it->first] += line_el[it->first][ii];

      tmpsum += thick[line_el[it->first][ii]];
    }

    sum_l.push_back(tmpsum);
    cout<<"length of layer "<<it->first<<" is "<<sum_l[it->first]<<endl;
  }


  


}
