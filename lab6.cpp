#include <iostream>

double calculateSeries(int n) {
    
    if (n == 0) {
        return 0.0;
    }
    
    return (1.0 / (n * (n + 1))) + calculateSeries(n - 1);
}

int main() {
    
}

double calculateSeries() {
    int n;
    std::cout << "Enter the number of terms: ";
    std::cin >> n;
    
    if (n == 0) {
        return 0.0;
    }
    
    return calculateSeriesHelper(n);
}

double calculateSeriesHelper(int n) {
    // Base case
    if (n == 0) {
        return 0.0;
    }
    
    return (1.0 / (n * (n + 1))) + calculateSeriesHelper(n - 1);
}

int main() {
    double result = calculateSeries();
    std::cout << "Result: " << result << std::endl;
    
    int n;
    std::cout << "Enter the number of terms: ";
    std::cin >> n;
    
    double result = calculateSeries(n);
    std::cout << "Result: " << result << std::endl;
    
    return 0;
}

