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
    grid.reserve(100); // Preallocate for 100 lines
    while (std::getline(file, line)) {
        grid.push_back(line);
    }

    int p1_count = 0;
    int p2_count = 0;

    // Part 1
    for (int r = 0; r < grid.size(); ++r) {
        for (int c = 0; c < grid[0].size(); ++c) {
            if (grid[r][c] != 'X') continue;

            // Precompute bounds for this position
            for (int dr = -1; dr <= 1; ++dr) {
                for (int dc = -1; dc <= 1; ++dc) {
                    if (dr == 0 && dc == 0) continue;

                    // Calculate the target positions once
                    int r1 = r + dr, r2 = r + 2 * dr, r3 = r + 3 * dr;
                    int c1 = c + dc, c2 = c + 2 * dc, c3 = c + 3 * dc;

                    if (0 <= r3 && r3 < grid.size() && 0 <= c3 && c3 < grid[0].size() &&
                        grid[r1][c1] == 'M' && grid[r2][c2] == 'A' && grid[r3][c3] == 'S') {
                        ++p1_count;
                    }
                }
            }
        }
    }

    // Part 2
    for (int r = 1; r < grid.size() - 1; ++r) {
        for (int c = 1; c < grid[0].size() - 1; ++c) {
            if (grid[r][c] != 'A') continue;

            // Direct string construction for corners
            std::string corners;
            corners += grid[r - 1][c - 1];
            corners += grid[r - 1][c + 1];
            corners += grid[r + 1][c + 1];
            corners += grid[r + 1][c - 1];

            if (corners == "MMSS" || corners == "MSSM" || corners == "SSMM" || corners == "SMMS") {
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

