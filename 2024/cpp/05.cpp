#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <chrono>
#include <iomanip>

void parseRules(std::ifstream &file, std::map<std::pair<int, int>, bool> &cache_p1, std::map<std::pair<int, int>, int> &cache_p2) {
    std::string line;
    while (std::getline(file, line)) {
        if (line.empty()) break;
        std::istringstream iss(line);
        int x, y;
        char sep;
        iss >> x >> sep >> y;
        cache_p1[{x, y}] = true;
        cache_p1[{y, x}] = false;
        cache_p2[{x, y}] = -1;
        cache_p2[{y, x}] = 1;
    }
}

bool isOrderedP1(const std::vector<int> &update, const std::map<std::pair<int, int>, bool> &cache_p1) {
    for (size_t i = 0; i < update.size(); ++i) {
        for (size_t j = i + 1; j < update.size(); ++j) {
            auto key = std::make_pair(update[i], update[j]);
            if (cache_p1.count(key) && !cache_p1.at(key)) {
                return false;
            }
        }
    }
    return true;
}

bool isOrderedP2(const std::vector<int> &update, const std::map<std::pair<int, int>, int> &cache_p2) {
    for (size_t i = 0; i < update.size(); ++i) {
        for (size_t j = i + 1; j < update.size(); ++j) {
            auto key = std::make_pair(update[i], update[j]);
            if (cache_p2.count(key) && cache_p2.at(key) == 1) {
                return false;
            }
        }
    }
    return true;
}

bool cmp(const int &x, const int &y, const std::map<std::pair<int, int>, int> &cache_p2) {
    auto key = std::make_pair(x, y);
    return cache_p2.count(key) ? cache_p2.at(key) < 0 : x < y;
}

int main() {
    // Start timing
    auto start_time = std::chrono::high_resolution_clock::now();

    std::ifstream file("../05.in");
    if (!file.is_open()) {
        std::cerr << "Error: Could not open file." << std::endl;
        return 1;
    }

    // Caches for part 1 and part 2
    std::map<std::pair<int, int>, bool> cache_p1;
    std::map<std::pair<int, int>, int> cache_p2;

    // Parse rules
    parseRules(file, cache_p1, cache_p2);

    // Process updates
    std::string line;
    int p1 = 0, p2 = 0;
    while (std::getline(file, line)) {
        if (line.empty()) continue;

        std::istringstream iss(line);
        std::vector<int> update;
        int num;
        char sep;

        while (iss >> num) {
            update.push_back(num);
            iss >> sep; // Skip commas
        }

        // Part 1 calculation
        if (isOrderedP1(update, cache_p1)) {
            p1 += update[update.size() / 2];
        }

        // Part 2 calculation
        if (!isOrderedP2(update, cache_p2)) {
            std::sort(update.begin(), update.end(), [&](int a, int b) {
                return cmp(a, b, cache_p2);
            });
            p2 += update[update.size() / 2];
        }
    }

    // Print results
    std::cout << "p1: " << p1 << std::endl;
    std::cout << "p2: " << p2 << std::endl;

    // Stop timing
    auto end_time = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed = end_time - start_time;
    std::cout << "Elapsed time: " << std::fixed << std::setprecision(3) << elapsed.count() << " seconds" << std::endl;

    return 0;
}

