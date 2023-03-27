#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

//unsigned short orc = 4, clayc = 2, obs1 = 3, obs2 = 14, geo1 = 2, geo2 = 7;
unsigned short orc = 2, clayc = 3, obs1 = 3, obs2 = 8, geo1 = 3, geo2 = 12;
unsigned short morc = max(max(orc,obs1),geo1);
int MX = 24;


int min_turns_to_build(int have, int need, int gain) {
    if (gain == 0)
        return -2;
    if (have >= need)
        return 0;
    int t = (int)(need - have) / gain;
    if ((need - have) % gain != 0)
        t += 1;
    return t;
}


void cal_turns(unsigned short turns, int t, unsigned short gai0, unsigned short gai1, unsigned short gai2, unsigned short gai3,
    unsigned short& inv0, unsigned short& inv1, unsigned short& inv2, unsigned short& inv3,
    unsigned short hav0, unsigned short hav1, unsigned short hav2, unsigned short hav3) {
    t = min(t, MX  - turns);
    inv0 = hav0 + t * gai0;
    inv1 = hav1 + t * gai1;
    inv2 = hav2 + t * gai2;
    inv3 = hav3 + t * gai3;
}


int search(unsigned short turns,
    unsigned short gai0, unsigned short gai1, unsigned short gai2, unsigned short gai3,
    unsigned short hav0, unsigned short hav1, unsigned short hav2, unsigned short hav3,
    int progress = 0
) {
    unsigned short inv0, inv1, inv2, inv3;
    if (turns > MX ) //|| ((MX - turns) < 2 && gai3 == 0)
        return hav3;



    vector<int> scores = { hav3 + gai3 * (MX - turns) };
    int t, t2;


    //clay robot
    t = 1 + min_turns_to_build(hav0, clayc, gai0);
    if (turns + t < MX) {

        cal_turns(turns,t, gai0, gai1, gai2, gai3, inv0, inv1, inv2, inv3, hav0, hav1, hav2, hav3);
        inv0 -= clayc;
        scores.push_back(search(turns + t, gai0, gai1 + 1, gai2, gai3, inv0, inv1, inv2, inv3));
    }

    if (progress)  cout << "1/4" << endl;

    //obsi robot
    t = 1 + min_turns_to_build(hav0, obs1, gai0);
    t2 = 1 + min_turns_to_build(hav1, obs2, gai1);
    if (!(t == -1 or t2 == -1)) {
        t = max(t, t2);
        if (turns + t < MX) {
            cal_turns(turns,t, gai0, gai1, gai2, gai3, inv0, inv1, inv2, inv3, hav0, hav1, hav2, hav3);
            inv0 -= obs1;
            inv1 -= obs2;
            scores.push_back(search(turns + t, gai0, gai1, gai2 + 1, gai3, inv0, inv1, inv2, inv3));
        }
    }


    if (progress) cout << "2/4" << endl;

    //ore robot
    //only consider if gain-ore < max-ore
    if (gai0 <= morc) {

        t = 1 + min_turns_to_build(hav0, orc, gai0);
        if (turns + t < MX) {
            cal_turns(turns,t, gai0, gai1, gai2, gai3, inv0, inv1, inv2, inv3, hav0, hav1, hav2, hav3);
            inv0 -= orc;
            scores.push_back(search(turns + t, gai0 + 1, gai1, gai2, gai3, inv0, inv1, inv2, inv3));
        }

    }

    if (progress)       cout << "3/4" << endl;

    //geo robot
    t = 1 + min_turns_to_build(hav0, geo1, gai0);
    t2 = 1 + min_turns_to_build(hav2, geo2, gai2);
    if (!(t == -1 or t2 == -1)) {
        t = max(t, t2);
        if (turns + t < MX) {
            cal_turns(turns,t, gai0, gai1, gai2, gai3, inv0, inv1, inv2, inv3, hav0, hav1, hav2, hav3);
            inv0 -= geo1;
            inv2 -= geo2;
            scores.push_back(search(turns + t, gai0, gai1, gai2, gai3 + 1, inv0, inv1, inv2, inv3));
        }
    }

    if (progress)    cout << "4/4" << endl;

    return *max_element(scores.begin(), scores.end());



}



vector<int> split_toi(const string& str) {
    vector<int> tokens;

    string::size_type start = 0;
    string::size_type end = 0;

    while ((end = str.find(" ", start)) != string::npos) {
        tokens.push_back(stoi(str.substr(start, end - start)));

        start = end + 1;
    }

    tokens.push_back(stoi(str.substr(start)));

    return tokens;
}



int main()
{

    std::ifstream infile("E:\\trashprojekte\\aoc2022\\d19\\input.txt");
    string t_temp;
    int erg = 0;
    int i= 1;
    while (getline(infile, t_temp)){
           sscanf_s(t_temp.c_str(), "%*s %*s %*s %*s %*s %*s %hu %*s %*s %*s %*s %*s %hu %*s %*s %*s %*s %*s %hu %*s %*s %hu %*s %*s %*s %*s %*s %hu %*s %*s %hu %*s %*s", &orc, &clayc, &obs1, &obs2, &geo1, &geo2);   
    morc = max(max(orc, obs1), geo1);
    auto zw= search(0, 1, 0, 0, 0, 0, 0, 0, 0, 0);
    cout << zw << endl;
    erg += i * zw;
    i++;
    }
    cout << erg << endl;

    //part 2
    std::ifstream infile2("E:\\trashprojekte\\aoc2022\\d19\\input.txt");
    MX = 32;
    erg = 1;
     i = 1;
    while (getline(infile2, t_temp) and i<=3) {
        
        sscanf_s(t_temp.c_str(), "%*s %*s %*s %*s %*s %*s %hu %*s %*s %*s %*s %*s %hu %*s %*s %*s %*s %*s %hu %*s %*s %hu %*s %*s %*s %*s %*s %hu %*s %*s %hu %*s %*s", &orc, &clayc, &obs1, &obs2, &geo1, &geo2);
        morc = max(max(orc, obs1), geo1);
        auto zw = search(0, 1, 0, 0, 0, 0, 0, 0, 0, 0);
        cout << zw << endl;
        erg = erg * zw;
        i++;
    }
    cout << erg << endl;



    return 0;
}