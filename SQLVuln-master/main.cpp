#include <iostream>
#include <fstream>
#include <regex>
#include <cstdlib>
#include <string>
#include <vector>
#include <sstream>
#include <stdio.h>
#include <curl/curl.h>

#define MX(mxNumb) ((mxNumb < 1 || mxNumb > 8) ? 0 : 1)
#define HELP "ambari.developer@gmail.com"
#define SAVEFILENAME "sql_vuln.txt"
#define RD "\033[31m"
#define RS "\033[0m"
#define GR "\033[32m"
#define YL "\033[33m"

struct L{
    int log;
}log_ok,log_no;
static std::string code;
static std::string ER[] = {
    "You have an error in your SQL syntax",
    "MySQL server version for the right syntax to use near",
    "SELECT * FROM"
};
int REQ(const char*);
template<typename T> int writeToFiles(T filename, const char *data) {
    std::ofstream files(filename,std::ios::app);
    files << data << std::endl;
    files.close();
    return 0;
}
template<typename S, size_t n> int array_count(S const(&arr)[n]) {
    return (sizeof(arr)/sizeof(*arr));
}
int writedata(void *buffer, size_t size, size_t sizem, void *m) {
    code.append((char*)buffer,size*sizem);
    return (size*sizem);
}
int CAMN(std::vector<std::string> data) {
    std::smatch rs;
    if(!data.size()) {
        return 0;
    }
    for(auto u : data) {
        std::string LE = u+"'";
        REQ((char*)LE.c_str());
        for(int x = 0; x < (sizeof(ER)/sizeof(*ER)); x++) {
            bool console_show = ((log_ok.log != 0 || log_no.log != 0) ? 1 : 0);
            if(std::regex_search(code,rs,std::regex(ER[x]))) {
                if(!console_show) {
                    writeToFiles(SAVEFILENAME,(char*)u.c_str());
                    std::cout << "[ " << GR << "OK" << RS << "  ] " << YL 
                              << "=> " << RS << u << std::endl;
                }
                log_ok.log = 1;
            }else {
                if(!console_show) {
                    std::cout << "[ " << RD << "NOT "<< RS <<"]" << YL 
                              << " => " << RS << u << std::endl;
                }
                log_no.log = 1;
            }
        }
        code.clear(); log_no.log = 0; log_ok.log = 0;
    }
    return 0;
}
int REQ(const char *url) {
    curl_global_init(CURL_GLOBAL_ALL);
    CURL *curl = curl_easy_init();
    if(!curl) {
        return 0;
    }
    CURLcode resp;
    long http_code;
    curl_easy_setopt(curl,CURLOPT_URL,url);
    curl_easy_setopt(curl,CURLOPT_WRITEFUNCTION,writedata);
    resp = curl_easy_perform(curl);
    if(resp != CURLE_OK) {
        return 0;
    }
    curl_easy_getinfo(curl,CURLINFO_RESPONSE_CODE,&http_code);
    return http_code;
}
int DORKING(const char *DRK, int max=1) {
    std::vector<std::string> tmp;
    std::smatch RxHasil;
    if(!MX(max)) {
        std::cout << "MAX PAGE [1/8]" << std::endl;
        return 0;
    }
    for(int counter = 1; counter <= max; counter++) {
        std::string SEARCH_URL = "http://www1.search-results.com/web?q="+std::string(DRK)+"&page="+std::to_string(counter);
        char SUL[SEARCH_URL.length()];
        strcpy(SUL,SEARCH_URL.c_str());
        if(!REQ(SUL)) {
            return 0;
        }
        std::istringstream ssr(code);
        std::string lines;
        while(getline(ssr,lines)) {
            if(std::regex_search(lines,RxHasil,std::regex("algo-display-url\">(.*?)</cite>"))) {
                tmp.push_back(RxHasil[1]);
            }
        }
        code.clear();
    }
    CAMN(tmp);
    return 0;
}
int main(int argc, const char *argv[]) {
    char dr[100];
    short int mx;
    if(argc != 3) {
        std::cout << 
            "[ ? ] DORK: "; std::cin.getline(dr,sizeof(dr));
        std::cout << 
            "[ ? ] MAX PAGE [1/8]: "; std::cin >> mx;
    }else {
        strcpy(dr,argv[1]);
        mx = static_cast<int>(atoi(argv[2]));
    }
    DORKING(dr,mx);
}