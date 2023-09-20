#include <stdio.h>
#include <string.h>

 int main() {
	 int a = 2;
	 int b = 2;
	 int c = a + b;
	
	 char myStrings[3][50];

	 strcpy(myStrings[0], "abby");
	 strcpy(myStrings[1], "soko");
	 strcpy(myStrings[2], "motoo");

	 for (int i = 0; i< 3; i++){
		 printf("%s\n", myStrings[i]);}

	 printf("C says: Hello, World!\n");
	 printf("%d + %d = %d\n",a,b,c);

	 return 0;
 }
