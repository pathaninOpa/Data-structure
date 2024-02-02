/*Pathanin Opachalearn 6481323*/
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void BuildHeap(int* A, int Currentsize);
void PercolateDown(int* A, int i, int Currentsize);
void Heapsort(int* A, int Currentsize);

int main(void) {
    int A[105], i, Currentsize;
    srand((unsigned int)time(NULL));

    for (i = 1; i <= 100; i++) {
        i == 1 ? printf("Before Heapsort:\n"):printf("");
        printf("%d, ",A[i] = rand() % 1000);
    }
    Currentsize = 100;
    Heapsort(A, Currentsize);
    for (i = 1; i <= Currentsize; i++) {
        i == 1 ? printf("\n\nAfter Sorted:\n"):printf("");
        printf("%d, ", A[i]);
    }
    return 0;
}

void BuildHeap(int* A, int Currentsize) {
    for (int i = Currentsize / 2; i > 0; i--) {
        PercolateDown(A, i, Currentsize);
    }
}

void PercolateDown(int* A, int i, int Currentsize) {
    int left = 2 * i;
    int right = 2 * i + 1;
    int largest = i;

    if (left <= Currentsize && A[left] > A[largest]) {
        largest = left;
    }

    if (right <= Currentsize && A[right] > A[largest]) {
        largest = right;
    }

    if (largest != i) {
        // Swap A[i] w/ A[largest]
        int temp = A[i];
        A[i] = A[largest];
        A[largest] = temp;
        PercolateDown(A, largest, Currentsize);
    }
}

void Heapsort(int* A, int Currentsize) {
    BuildHeap(A, Currentsize);

    for (int i = Currentsize; i > 1; i--) {
        // Swap A[1] w/ A[i]
        int temp = A[1];
        A[1] = A[i];
        A[i] = temp;
        Currentsize--;
        PercolateDown(A, 1, Currentsize);
    }
}
