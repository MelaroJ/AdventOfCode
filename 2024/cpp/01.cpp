#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <chrono>
#include <cmath>
#include <iomanip>  // For std::fixed and std::setprecision

// AOC Day 1
// https://adventofcode.com/2024/day/1

int main() {
    std::ifstream file("01.in");
    std::vector<int> l, r;

    // Parse input
    for (std::string line; std::getline(file, line); ) {
        std::istringstream iss(line);
        int left, right;
        iss >> left >> right;  // Read two integers per line
        l.push_back(left);
        r.push_back(right);
    }

    auto start = std::chrono::high_resolution_clock::now();

    // Sort both lists
    std::sort(l.begin(), l.end());
    std::sort(r.begin(), r.end());

    // Part 1: Sum of absolute differences
    int pt1 = std::inner_product(l.begin(), l.end(), r.begin(), 0, std::plus<>(), [](int x, int y) {
        return std::abs(x - y);
    });

    // Part 2: Weighted sum
    int pt2 = std::accumulate(l.begin(), l.end(), 0, [&r](int acc, int x) {
        return acc + x * std::count(r.begin(), r.end(), x);
    });

    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed = end - start;

    // Output results
    std::cout << "pt 1: \n" << pt1 << '\n';
    std::cout << "pt 2: \n" << pt2 << '\n';
    std::cout << "Elapsed time: " << std::fixed << std::setprecision(3) 
          << elapsed.count() << " seconds\n";

    return 0;
}

