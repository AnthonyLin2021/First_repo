#include "header.hpp"
#include <iostream> 
#include <sstream>
#include <algorithm> 
#include <vector> 

int wordcount(std::string line){
    std::istringstream iss(line);
    int count{0};
    std::string word;
    while(iss >> word){
        ++count;
    }
    return count;
}


int main (){
    std::vector<std::pair<int,std::string>> lines;
    std::string line;

    while(std::getline(std::cin,line)){
        int count=wordcount(line);
        lines.push_back(std::pair<int,std::string>(count,line));
    }

    std::stable_sort(lines.begin(), lines.end(),
     [](std::pair<int,std::string> pair1, std::pair<int,std::string> pair2 ){
        return pair1.first < pair2.first;
    });


    for(std::pair<int,std::string> pair : lines){
        std::cout<< pair.first << " " << pair.second << std::endl; 
    }

    return 0; 
}