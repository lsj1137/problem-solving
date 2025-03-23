#include <iostream>

using namespace std;

char** star(char** arr, int sx, int sy, int n);

int main(){
	int N;
	cin >> N;
	char** arr = new char*[N];
	for(int i = 0; i < N; i++) 
		arr[i] = new char[N];
	for (int i = 0; i < N; i++)
		for (int j = 0; j < N; j++)
			arr[i][j] = '*';
	arr = star(arr, 0, 0, N);
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++)
			cout << arr[i][j];
		cout << '\n';
	}
	delete[] arr;
	return 0;
}

char** star(char** arr, int sx, int sy, int n) {
	for (int i = sx; i < sx+n; i += n / 3)
		for (int j = sy; j < sy+n; j += n / 3) {
			if (i == sx + n / 3 && j == sy + n / 3) {
				for (int k = 0; k < n / 3; k++)
					for (int l = 0; l < n / 3; l++)
						arr[i + k][j + l] = ' ';
			}
			else if (n > 3) {
				arr = star(arr, i, j, n / 3);
			}
		}
	return arr;
}