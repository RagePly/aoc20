#include <stdio.h>

int main() {
	FILE *fIn = fopen("../aoc20data/day5.txt", "r");
	if (!fIn) {
		printf("FNF\n");
		return -1;
	}

	unsigned int 	seats[8*128];
	int 			i;
	for (i = 0 ; i < 8*128 ; i++) {
		seats[i] = 0;
	}

	char 			buffer[11]; // 10 + 1 so as to compensate for \0
	unsigned int 	path;
	unsigned int 	max = 0;

	while (fscanf(fIn," %10s", buffer) != EOF) {
		path = 0;
		for (i = 0; i < 10; i++) {
			if (buffer[i] == 'B' || buffer[i] == 'R') path = path | 1 << (9-i);
		}
		if (path > max) max = path;
		seats[path]	= 1;
	}
	
	fclose(fIn);
	
	// Answers
	printf("Task one: %u\n", max);

	for (i = 1 ; i < 8*128 - 1; i++) {
		if (!seats[i] & seats[i+1] & seats[i-1]) {
			printf("Task two: %u\n", i);
			break;
		}
	}
	return 0;
}
