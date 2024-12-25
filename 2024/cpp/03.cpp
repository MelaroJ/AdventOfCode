#include <iostream>
#include <fstream>
#include <string>
#include <regex>
#include <chrono>
#include <iomanip>

int main() {
    // Start timing
    auto start = std::chrono::high_resolution_clock::now();

    // Read the file content
    std::ifstream inputFile("../03.in");
    if (!inputFile.is_open()) {
        std::cerr << "Error opening file.\n";
        return 1;
    }

    std::string memory((std::istreambuf_iterator<char>(inputFile)),
                        std::istreambuf_iterator<char>());
    inputFile.close();

    // Part 1: Count mul operations
    std::regex mulRegex(R"(mul\(\d{1,3},\d{1,3}\))");
    auto mulBegin = std::sregex_iterator(memory.begin(), memory.end(), mulRegex);
    auto mulEnd = std::sregex_iterator();

    int p1_count = 0;
    for (auto it = mulBegin; it != mulEnd; ++it) {
        std::string match = it->str(); // Extract matched string
        size_t commaPos = match.find(',');
        int x = std::stoi(match.substr(4, commaPos - 4)); // Extract first number
        int y = std::stoi(match.substr(commaPos + 1, match.size() - commaPos - 2)); // Extract second number
        p1_count += x * y;
    }

    // Part 2: Process do(), don't(), and mul()
    std::regex commandRegex(R"(do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\))");
    auto commandBegin = std::sregex_iterator(memory.begin(), memory.end(), commandRegex);
    auto commandEnd = std::sregex_iterator();

    bool on = true;
    int p2_count = 0;

    for (auto it = commandBegin; it != commandEnd; ++it) {
        std::string match = it->str();
        if (match == "do()") {
            on = true;
        } else if (match == "don't()") {
            on = false;
        } else if (on) {
            size_t commaPos = match.find(',');
            int x = std::stoi(match.substr(4, commaPos - 4)); // Extract first number
            int y = std::stoi(match.substr(commaPos + 1, match.size() - commaPos - 2)); // Extract second number
            p2_count += x * y;
        }
    }

    // Output results
    std::cout << "p1: \n" << p1_count << '\n';
    std::cout << "p2: \n" << p2_count << '\n';

    // End timing
    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed = end - start;
    std::cout << "Elapsed time: " << std::fixed << std::setprecision(3) 
          << elapsed.count() << " seconds\n";

    return 0;
}

