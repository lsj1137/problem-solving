#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct planet {
	int x;
	int y;
	int r;
}PL;

int cal(PL p1, PL p2){
	double dist = sqrt(pow(p1.x-p2.x,2)+pow(p1.y-p2.y,2));
    if (p2.r>dist) return 1;
    else return 0;
}

int main() {
	int i,j, caseNum = 0, result = 0;
	scanf("%d", &caseNum);
	getchar();
	int reArr[caseNum];
	for (i=0;i<caseNum;i++){ 
		PL pS, pF;
		int plNum = 0;
		pS.r = 0;
		pF.r = 0;
		scanf("%d %d %d %d",&pS.x, &pS.y, &pF.x, &pF.y);
		getchar();
		scanf("%d",&plNum);
		getchar();
		PL plArr[plNum];
		for (j=0;j<plNum;j++){
			scanf("%d %d %d",&plArr[j].x,&plArr[j].y,&plArr[j].r);
			getchar();
		}
		result=0;
		for (j=0;j<plNum;j++){
			int a = cal(pS, plArr[j]);
			int b = cal(pF, plArr[j]);
			if (a*b == 0 && a+b == 1)
				result+=1;
		}
		printf("%d\n", result);
	}
	return 0;
}