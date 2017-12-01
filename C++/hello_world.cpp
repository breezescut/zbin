#include<stdio.h>

#if __cplusplus <= 199711L
  #error This library needs at least a C++11 compliant compiler
#endif

int main(int argc, char** argv){
	printf("Hello world!\n");
}
