#include<iostream>
using namespace std;

class Cube{
private:

    int m_a,m_b,m_c;

public:

    void setParameter(int a,int b,int c){
        m_a = a; //do not start with "int m_a"
        m_b = b;
        m_c = c;
    }

    int getVolume(){
        int volume = m_a * m_b * m_c;
        return volume;
    }
};

int main(){
    Cube a;
    a.setParameter(2,3,4);
    cout<<a.getVolume()<<endl;
}