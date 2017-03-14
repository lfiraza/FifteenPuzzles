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

#define N_ITEMS( array )   (sizeof( array )/sizeof( array[0] ))

#include <cstdlib>
#include <cmath>
#include<iostream>

using namespace std;

bool ifSolvable(int []);
/*
 * 
 */
int main(int argc, char** argv) {

    int test[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 14, 0};
    
    cout<<ifSolvable(test);
    
    return 0;
}

bool ifSolvable(int puzzle[]){
    int parity = 0;
    int const length = 16;
    int gridWidth = (int) sqrt(length);
    int row = 0; 
    int blankRow = 0; 

    for (int i = 0; i < length; i++)
    {
        if (i % gridWidth == 0) { 
            row++;
        }
        if (puzzle[i] == 0) { 
            blankRow = row; 
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

