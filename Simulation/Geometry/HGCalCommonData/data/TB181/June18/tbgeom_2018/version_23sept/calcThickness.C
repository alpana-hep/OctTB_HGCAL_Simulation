#include <map>
#include <iostream>
#include <fstream>
#include <vector>

#include "TSystem.h"

#pragma link C++ operators map<int, vector<double>>;
#pragma link C++ operator map<int, vector<double>>::iterator; 
#pragma link C++ operator map<int, vector<double>>::const_iterator;
#pragma link C++ operator map<int, vector<double>>::reverse_iterator;


double interactionLength(string mat);
double radiationLength(string mat);

#define FATAL(msg) do { fprintf(stderr, "FATAL: %s\n", msg); gSystem->Exit(1); } while (0)

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
			    {12, {4, 5, 4,10, 0, 7,7,7, 1, 3}},
			      {13, {6, 4, 5, 4}},
				{14, {6, 4, 5, 4}},
				  {15, {6, 11, 14, 8}},
				    };
  
  


  int lay_si[] = {4,12,15};
  int lay_size = sizeof(lay_si)/sizeof(lay_si[0]);


  
  ///FH
  /*
  map<int, vector<float> > line_el {
    {0, {7, 14, 0, 3, 2, 5, 4, 4, 4, 1}},
      {1, {11, 0, 0, 0, 3, 2, 5, 4, 4, 4, 1}},
	{2, {6,  0, 7, 15, 7, 0, 0, 3, 2, 5, 4, 4, 4, 1}},
	  {3, {13, 0, 0, 0, 3, 2, 5, 4, 4, 4, 1}},
	    {4, {12, 0, 10, 7}}
  };
  

  int lay_si[] = {0,1,2,3,4};
  int lay_size = sizeof(lay_si)/sizeof(lay_si[0]);
  */

  /*
  ///AHCAL
  map<int, vector<float> > line_el {
    {0, {7, 1, 2, 3, 4, 5, 6, 5, 2, 1}},
      {1, {0, 1, 2, 3, 4, 5, 6, 5, 2, 1}},
	{2, {0, 1, 2, 3, 4, 5, 6, 5, 2, 1}},
	  {3, {0, 1, 2, 3, 4, 5, 6, 5, 2, 1}},
	    {4, {0, 1, 2, 3, 4, 5, 6, 5, 2, 1}},
	      {5, {0, 1, 2, 3, 4, 5, 6, 5, 2, 1}},
		{6, {0, 1, 2, 3, 4, 5, 6, 5, 2, 1}},
		  {7, {0, 1, 2, 3, 4, 5, 6, 5, 2, 1}},
		    {8, {0, 1, 2, 3, 4, 5, 6, 5, 2, 1}},
		      {9, {0, 1, 2, 3, 4, 5, 6, 5, 2, 1}},
			{10, {0, 1, 2, 3, 4, 5, 6, 5, 2, 1}},
			  {11, {0, 1, 2, 3, 4, 5, 6, 5, 2, 1, 8}},



  };


  int lay_si[] = {0,1,2,3,4, 5, 6, 7, 8, 9, 10, 11};
  int lay_size = sizeof(lay_si)/sizeof(lay_si[0]);
  */


  double detLength = 0;
  
  vector<float> sum_l;


  vector<float> intL;
  vector<float> radL;
  
  
  double tmpintL = 0;
  double tmpradL = 0;

  ////file for Arabella
  TString matlist;
  
  for(map<int,vector<float>>::iterator it = line_el.begin(); it != line_el.end(); ++it) {
    
    double tmpsum = 0;

    
    for(int ii=0; ii<line_el[it->first].size(); ii++){
      //sum_l[it->first] += line_el[it->first][ii];

      double len = thick[line_el[it->first][ii]];
      tmpsum += len;
      
      string tmpmat = mat[line_el[it->first][ii]];
      
      matlist += Form("%1.3f,%s\n",len,tmpmat.c_str());

      double intlength = interactionLength(tmpmat);
      double radlength = radiationLength(tmpmat);
      
      if(intlength!=0)
	tmpintL += len/intlength;
      
      if(radlength!=0)
	tmpradL += len/radlength;
    }
    detLength += tmpsum;
    sum_l.push_back(tmpsum);
    cout<<"length of layer "<<it->first<<" is "<<sum_l[it->first]<<endl;

    for(int il=0; il<lay_size; il++){
      if(it->first == lay_si[il]){
	intL.push_back(tmpintL);
	radL.push_back(tmpradL);

      }//if(it->first == lay_size[il])

    }//for(int il=0; il<lay_size(); il++)
  }


  FILE* out = fopen(TString::Format("%s_Full.txt",inputFile_name.c_str()).Data(), "w");
  if (!out) FATAL("fopen() failed");
  if (fputs(matlist.Data(), out) < 0) FATAL("fputs() failed");
  if (fclose(out) != 0) FATAL("fclose() failed");

  
  cout<<"Detector length is "<<detLength<<endl;
  
  double totintL = 0;
  double totradL = 0;
  
  for(int ii=0; ii<intL.size(); ii++){

    //totintL += intL[ii];
    //totradL += radL[ii];

    cout<<"Radiation length : Interaction L of layer "<<ii<<" is "<<radL[ii]<<" "<<intL[ii]<<endl;
  }
  

  totintL = intL[intL.size()-1];  
  totradL = radL[radL.size()-1];     

  cout<<"Total radiation length and interaction length "<<totradL<<" "<<totintL<<endl;

}





double interactionLength(string mat){

  std::map<string,double> len;

  ///here the names have to be similar as in mat.list
  /*
  ///pion interaction length
  len["Cu"] = 18.51; //cm
  len["W"] = 11.33; //cm

  len["Fe"] = 20.42; //cm
  len["Steel"] = 20.42; //cm

  len["Lead"] = 19.93; //cm
  len["CuW"] = 12.55; //cm
  len["Al"] = 50.64; //cm
  */

  ///nuclear interaction length
  
  len["Cu"] = 15.32; //cm
  len["W"] = 9.946; //cm

  len["Fe"] = 16.77; //cm
  len["Steel"] = 16.77; //cm

  len["Lead"] = 17.59; //cm
  len["CuW"] = 10.9; //cm
  len["Al"] = 39.70; //cm
  
  bool found = false;
  for(map<string,double>::iterator it = len.begin(); it != len.end(); ++it) {
    
    if(mat.compare(it->first) == 0 )
      {
	found = true;
	break;
      }//if(mat.compare(it->first) == 0 ) 

  }//for(map<string,double>::iterator it = len.begin(); it != len.end(); ++it)

  if(found) return len[mat]*10; ///in mm as mats are in mm

  else 
    {
      cout<<"material "<<mat<<" not found in the list"<<endl;
      return 0;
    }

}


double radiationLength(string mat){

  std::map<string,double> len;

  ///here the names have to be similar as in mat.list
  len["Cu"] = 1.44; //cm
  len["W"] = 0.35; //cm

  len["Fe"] = 1.76; //cm
  len["Steel"] = 1.76; //cm

  len["Lead"] = 0.56; //cm
  len["CuW"] = 0.43; //cm
  len["Al"] = 8.897; //cm


  bool found = false;
  for(map<string,double>::iterator it = len.begin(); it != len.end(); ++it) {
    
    if(mat.compare(it->first) == 0 )
      {
	found = true;
	break;
      }//if(mat.compare(it->first) == 0 ) 

  }//for(map<string,double>::iterator it = len.begin(); it != len.end(); ++it)

  if(found) return len[mat]*10; ///in mm as mats are in mm
  else 
    {
      cout<<"material "<<mat<<" not found in the list"<<endl;
      return 0;
    }
}
