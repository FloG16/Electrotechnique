#include <stdio.h>
#include <conio.h>
    
int main ()
{
printf("\n#### Programme en C pour trouver la tension en utilisant la loi d'ohm\n");

float I, R, V;

printf("\n Entrez la valeur de l'intensité I = ");
scanf("%f",&I);
printf("\n Entrez la valeur de la Resistance R = ");
scanf("%f",&R);

V=I*R;

printf("\n La Tension est de  = %f", V);

return 0;
}
