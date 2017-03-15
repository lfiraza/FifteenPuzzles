/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   main.cpp
 * Author: Łukasz
 *
 * Created on 14 marca 2017, 13:19
 */

#include <cstdlib>
#include <cmath>
#include <iostream>
#include "solvablechecker.h"

using namespace std;
/*
 * 
 */
int main(int argc, char** argv) {

    int iloscWierszy = 4;
    int iloscKolumn = 4;
    
    int startUklad[iloscWierszy][iloscKolumn] = {
        {1,2,3,4},
        {5,6,7,8},
        {9,10,11,12},
        {13,15,14,0}
    };
    
    int startPlasko[iloscWierszy*iloscKolumn] = {0};
    
      for (int i = 0; i < iloscWierszy; i++){
    
        for (int j=0; j < iloscKolumn; j++){
            
            startPlasko[i*4+j] = startUklad[i][j];
        }
    
    }
    
    
    cout<<ifSolvable(startPlasko, iloscWierszy, iloscKolumn);
    
    return 0;
}