#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#define LENTH 10000

int main(void){
    time_t time_start = clock();
    int num_list[LENTH] = {0}, num_dict[2][LENTH] = {1};
    for(int i=0; i<LENTH; i++){
        num_list[i] = 3+i;
        num_dict[0][i] = 3+i;
        if(num_list[i]%2 != 0){
            num_dict[1][i] = 1;
        }
        else{
            num_dict[1][i] = 0;
        }
    }
    //check
    //for(int i = 0;i<sizeof(num_list[LENTH]);i++){printf("%d\n",num_list[i]);}
    short check = 0;
    printf("2\n");
    for(int i = 0; i<LENTH; i++){
        if(num_dict[1][i]){
            for(int j = 3, len = (int)(num_list[i]/2); j<len; j++){
                if((int)(num_list[i]%j) == 0){
                    check = 1;
                    break;
                }
            }
            if(check){
                for(int k = 1,len = (int)(LENTH/num_list[i]); k<len; k++){
                    num_dict[1][i*k] = 0;
                }
                check = 0;
            }
            else{
                printf("%d\n",num_list[i]);
            }
        }
        
    }

    time_t time_end = clock();
    time_t time = time_end - time_start;
    printf("time cost:%fms\n",((double)(time_end - time_start)) / CLOCKS_PER_SEC * 100);

    system("pause");
    return 0;
}
