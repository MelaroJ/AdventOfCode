#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <chrono>
#include <iomanip>

int main() {
    auto start = std::chrono::high_resolution_clock::now();

    // Reading the input file
    std::ifstream file("../04.in");
    std::vector<std::string> grid;
    std::string line;
    while (std::getline(file, line)) {
        grid.push_back(line);
    }

    int p1_count = 0;
    int p2_count = 0;

    // Part 1
    for (int r = 0; r < grid.size(); ++r) {
        for (int c = 0; c < grid[0].size(); ++c) {
            if (grid[r][c] != 'X') continue;

            for (int dr = -1; dr <= 1; ++dr) {
                for (int dc = -1; dc <= 1; ++dc) {
                    if (dr == 0 && dc == 0) continue;

                    if (0 <= r + 3 * dr && r + 3 * dr < grid.size() &&
                        0 <= c + 3 * dc && c + 3 * dc < grid[0].size()) {
                        if (grid[r + dr][c + dc] == 'M' &&
                            grid[r + 2 * dr][c + 2 * dc] == 'A' &&
                            grid[r + 3 * dr][c + 3 * dc] == 'S') {
                            ++p1_count;
                        }
                    }
                }
            }
        }
    }

    // Part 2
    for (int r = 1; r < grid.size() - 1; ++r) {
        for (int c = 1; c < grid[0].size() - 1; ++c) {
            if (grid[r][c] != 'A') continue;

            std::vector<char> corners = {
                grid[r - 1][c - 1],
                grid[r - 1][c + 1],
                grid[r + 1][c + 1],
                grid[r + 1][c - 1]
            };

            std::string corners_str(corners.begin(), corners.end());
            if (corners_str == "MMSS" || corners_str == "MSSM" ||
                corners_str == "SSMM" || corners_str == "SMMS") {
                ++p2_count;
            }
        }
    }

    // Output results
    std::cout << "p1: " << p1_count << "\n";
    std::cout << "p2: " << p2_count << "\n";

    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed = end - start;
    std::cout << "Elapsed time: " << std::fixed << std::setprecision(4) 
          << elapsed.count() << " seconds\n";
    
    return 0;
}

