#include <iostream>
using namespace std;
#include <vector>


// bubble sort

int main() {
    int n;
    cout << "Enter size of array: ";
    cin >> n;
    
    vector<int> arr(n);

    cout << "Enter the elements of the array: ";

    for(int i = 0; i<n; i++) {
        cin >> arr[i];
    }

    cout << "The array you entered is: ";
    for(int i = 0; i<n; i++) {
        cout << arr[i] << " ";
    }

    for(int i = 0; i < n - 1; i++) {
        for(int j = 0; j < n - i - 1; j++) {
            if (arr[j+1] < arr[j]) {
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }

    cout << "sorted array is :";

    for(int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    return 0;

}