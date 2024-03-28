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
            cout << "������� ������ �������� (�� ������ 2 ����):" << endl;
            cin >> size;
        } while (size <= 1);
        cout << "������� ��������:" << endl;
        for (int i = 0; i < size;) {
            cout << (i + 1) << ")";
            cin >> letter;
            if (isalpha(letter) && find(alphabet.begin(), alphabet.end(), letter) == alphabet.end()) {
                alphabet.push_back(letter);
                i++;
            }
            else if (isalpha(letter)) {
                cout << "��� ����� ��� ���� �������. ���������� ��� ���" << endl;
            }
            else {
                cout << "�� ����� �� �����. ���������� ��� ���" << endl;
            }
        }
    }
    string wordFromNumber(int number) {
        string result;
        int lengthvector = alphabet.size();
        string intermediate;

        while (number > 0) {
            int remainder = number % lengthvector;
            if (remainder == 0) {
                remainder = lengthvector;
                number = (number - lengthvector) / lengthvector;
            }
            else {
                number = (number - remainder) / lengthvector;
            }
            result = alphabet[remainder - 1] + result;

            intermediate = "(" + to_string(number) + "*" + to_string(lengthvector) + "^" + to_string(result.size()) + " + " + to_string(remainder) + ")" + intermediate;
            
        }
        result = intermediate + " = " + result; 
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
    int number;
    cout << "������� �����" << endl;
    cin >> number;
    string result = a.wordFromNumber(number);
    cout << "���������: " << result << endl;
    return 0;
}