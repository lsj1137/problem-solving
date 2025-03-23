#include <stdio.h>
#include <math.h>
#include <stdlib.h>
struct point {
    int x;
    int y;
    int r;
};
int compute(struct point* p1, struct point* p2){
    double Sd = sqrt(pow(p1->x-p2->x,2)+pow(p1->y-p2->y,2));
    double Od = p1->r+p2->r;
    if (Sd == 0) {
        if(abs(p1->r-p2->r)>0)
            return 0;
        else
            return -1;
    }
    else {
        if(Sd == Od)
            return 1;
        else if(Sd>Od)
            return 0;
        else {
            if(abs(p1->r-p2->r)==Sd)
                return 1;
            else if(abs(p1->r-p2->r)>Sd)
            	return 0;
            else
                return 2;
        }
    }
}
int main()
{
    int a=0, time;
    int result;
    struct point p1, p2,*pp1,*pp2;
    pp1 = &p1;
    pp2 = &p2;
    scanf("%d",&time);
    getchar();
    for(a=0;a<time;a++){
        scanf("%d %d %d %d %d %d", &p1.x, &p1.y, &p1.r, &p2.x, &p2.y, &p2.r);
        getchar();
        result = compute(pp1,pp2);
        printf("%d\n",result);
    }
    return 0;
}