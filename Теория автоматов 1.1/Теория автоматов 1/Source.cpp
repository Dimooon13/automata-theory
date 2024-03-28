#include <iostream>
#include <string>
#include <vector>
#include <cmath>
using namespace std;

class Alphabet
{
public:
    vector<char> alphabet;
    Alphabet()
    {
        do {
            cout << "Введите размер алфавита (не меньше 2 букв):" << endl;
            cin >> size;
        } while (size <= 1);
        cout << "Введите значения:" << endl;
        for (int i = 0; i < size;) {
            cout << (i + 1) << ")";
            cin >> letter;
            if (isalpha(letter) && find(alphabet.begin(), alphabet.end(), letter) == alphabet.end()) {
                alphabet.push_back(letter);
                i++;
            }
            else if (isalpha(letter)) {
                cout << "Эта буква уже была введена. Попробуйте ещё раз" << endl;
            }
            else {
                cout << "Вы ввели не букву. Попробуйте ещё раз" << endl;
            }
        }
    }
    int numbering(string word) {
        int lengthstring = word.size();
        int lengthvector = alphabet.size();
        int result = 0;
        for (int i = lengthstring - 1; i >= 0; i--) {
            bool found = false;
            for (int j = 0; j < lengthvector; j++) {
                if (word[i] == alphabet[j]) {
                    found = true;
                    int power = lengthstring - 1 - i;
                    result += pow(lengthvector, power) * (j + 1);
                    break;
                }
            }
            if (!found) {
                cout << word[i] << " не принадлежит алфавиту." << endl;
                return -1;
            }
        }
        return result;
    }
    ~Alphabet()
    {
        alphabet.shrink_to_fit();
    }

private:
    int size;
    char letter;
};

int main()
{
    setlocale(LC_ALL, "ru");
    Alphabet a;
    string word;
    cout << "Введите слово" << endl;
    cin >> word;
    int result = a.numbering(word);
    if (result != -1) {
        cout << "Результат: " << result << endl;
    }
    return 0;
}