#include <iostream>
using namespace std;
#include <vector>

int main() {
    int n;
    cout << "Enter the length of array: ";

    cin >> n;
    vector<int> arr(n);

    cout << "Enter the values of the array: ";
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    cout << "Your array is: ";
    for (int i = 0; i < n; i++) {
        cout << arr[i];
    }

    for (int i = 1; i < n; i++) {
        int curr = arr[i];
        for (int prev = i - 1; prev > 0; prev--) {
            if (arr[prev] > arr[prev+1]) {
                arr[prev + 1] = arr[prev];
                arr[prev] = curr;
            }
        }

    }

    cout << "sorted array is :";

    for(int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    return 0;

}