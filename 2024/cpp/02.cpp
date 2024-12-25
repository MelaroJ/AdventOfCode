#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <string>
#include <chrono>
#include <iomanip>

// AOC Day 2
// https://adventofcode.com/2024/day/2

// check if levels are 'safe'
bool safe(const std::vector<int>& levels) {
    std::vector<int> diffs;
    
    // consecutive level diffs
    for (size_t i = 0; i < levels.size() - 1; ++i) {
        diffs.push_back(levels[i] - levels[i + 1]);
    }

    // Flags - all diffs monotonic
    bool all_positive = true;
    bool all_negative = true;

    // Check diffs validity
    for (int diff : diffs) {
        if (diff < 1 || diff > 3) {  // Check for [1, 3] range
            all_positive = false;
        }
        if (diff > -1 || diff < -3) {  // Check for [-3, -1] range
            all_negative = false;
        }
    }

    // Return true if either monotonic
    return all_positive || all_negative;
}

int main() {
    auto start = std::chrono::high_resolution_clock::now();
    
    int p1_count = 0;
    int p2_count = 0;

    // Read infile
    std::ifstream file("02.in");
    std::vector<std::vector<int>> reports;

    if (!file) {
        std::cerr << "Error opening file!" << std::endl;
        return 1;
    }

    std::string line;
    while (std::getline(file, line)) {
        std::istringstream iss(line);
        std::vector<int> levels;
        int num;
        while (iss >> num) {
            levels.push_back(num);
        }
        reports.push_back(levels);
    }

    // P1: Count "safe" reports
    for (const auto& levels : reports) {
        if (safe(levels)) {
            ++p1_count;
        }
    }

    // Part 2: Count reports where removing one level makes it "safe"
    for (const auto& levels : reports) {
        bool is_safe_with_removal = false;

        for (size_t i = 0; i < levels.size(); ++i) {
            // Check safety by skipping the i-th element
            std::vector<int> diffs;
            for (size_t j = 0; j < levels.size() - 1; ++j) {
                if (j == i || j + 1 == i) {
                    continue; // Skip the "removed" element
                }
                diffs.push_back(levels[j] - levels[j + 1]);
            }

            // Check if the resulting diffs are valid
            bool all_positive = true;
            bool all_negative = true;
            for (int diff : diffs) {
                if (diff < 1 || diff > 3) {
                    all_positive = false;
                }
                if (diff > -1 || diff < -3) {
                    all_negative = false;
                }
            }

            if (all_positive || all_negative) {
                is_safe_with_removal = true;
                break;
            }
        }

        if (is_safe_with_removal) {
            ++p2_count;
        }
    }

    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed = end - start;

    std::cout << "p1: \n" << p1_count << std::endl;
    std::cout << "p2: \n" << p2_count << std::endl;
    std::cout << "Elapsed time: " << std::fixed << std::setprecision(3) 
          << elapsed.count() << " seconds\n";

    return 0;
}
