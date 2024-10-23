#include <iostream>
using namespace std;
#include <vector>

int main() {
    int n;
    cout << "Enter the number of elememts: ";
    cin >> n;

    vector<int> arr(n);

    cout << "Enter the elements of the array: ";
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    cout << "Your array is :";

    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }

    for (int i = 0; i < n - 1; i++) {
        int smallest_idx = i;
        for (int j = i+1; j < n; j++) {
            if (arr[j] < arr[smallest_idx]) {
                smallest_idx = j;
            }
        }
        int temp = arr[i];
        arr[i] = arr[smallest_idx];
        arr[smallest_idx] = temp;
    }

    cout << endl << "Sorted array is : ";

    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
}