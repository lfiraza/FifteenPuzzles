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

using namespace std;

bool ifSolvable(int [], int, int);
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

bool ifSolvable(int puzzle[], int row, int col){
    int parity = 0;
    int gridWidth = col;
    int helperRow = 0;
    int blankRow = 0; 
    int length = row * col;
    
  

    for (int i = 0; i < length; i++)
    {
        if (i % gridWidth == 0) { 
            helperRow++;
        }
        if (puzzle[i] == 0) { 
            blankRow = helperRow; 
            continue;
        }
        for (int j = i + 1; j < length; j++)
        {
            if (puzzle[i] > puzzle[j] && puzzle[j] != 0)
            {
                parity++;
            }
        }
    }

    if (gridWidth % 2 == 0) {
        if (blankRow % 2 == 0) { 
            return (parity % 2 == 0);
        } else { 
            return (parity % 2 != 0);
        }
    } else {
        return (parity % 2 == 0);
    }
    
}

