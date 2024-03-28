#include <iostream>
#include <string>
#include <vector>

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
    void CreateSequence(int elem) {
        int counter = 0, Code = 1;
        string Word;
        while (true) {
            Word = GetAWordOutOfACode(Code);
            if (IsValidSequence(Word)) {
                counter++;
                cout << Word;
                if (counter == elem) break;
                cout << "|";
            }
            Code++;
        }
    }

    ~Alphabet()
    {
        alphabet.shrink_to_fit();
    }

private:
    int size;
    char letter;

    string GetAWordOutOfACode(int Code) {
        string Word;
        while (Code > alphabet.size()) {
            if (Code % alphabet.size() != 0) {
                Word += alphabet[Code % alphabet.size() - 1];
                Code = Code / alphabet.size();
            }
            else {
                Word += alphabet[alphabet.size() - 1];
                Code = Code / alphabet.size() - 1;
            }
        }
        Word += alphabet[Code - 1];
        return Word;
    }

    bool IsValidSequence(const string& sequence) {
        for (int i = 0; i < sequence.size() - 1; ++i) {
            if (sequence[i] == 'a' && sequence[i + 1] == 'a') {
                return false;
            }
        }
        return true;
    }
};


int main()
{
    setlocale(LC_ALL, "ru");
    Alphabet a;
    cout << "Введите сколько элементов необходимо вывести:\n";
    int elem;
    cin >> elem;
    a.CreateSequence(elem);
    return 0;
}