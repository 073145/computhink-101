#include <iostream>
#include <climits>
#include <cfloat>

int main() {
    std::cout << "Check the upper and lower limits of integer :\n";
    std::cout << "--------------------------------------------------\n";
    std::cout << "The maximum limit of int data type : " << INT_MAX << std::endl;
    std::cout << "The minimum limit of int data type : " << INT_MIN << std::endl;
    std::cout << "The maximum limit of unsigned int data type : " << UINT_MAX << std::endl;
    std::cout << "The maximum limit of long long data type : " << LLONG_MAX << std::endl;
    std::cout << "The minimum limit of long long data type : " << LLONG_MIN << std::endl;
    std::cout << "The maximum limit of unsigned long long data type : " << ULLONG_MAX << std::endl;
    std::cout << "The Bits contain in char data type : " << CHAR_BIT << std::endl;
    std::cout << "The maximum limit of char data type : " << static_cast<int>(CHAR_MAX) << std::endl;
    std::cout << "The minimum limit of char data type : " << static_cast<int>(CHAR_MIN) << std::endl;
    std::cout << "The maximum limit of signed char data type : " << static_cast<int>(SCHAR_MAX) << std::endl;
    std::cout << "The minimum limit of signed char data type : " << static_cast<int>(SCHAR_MIN) << std::endl;
    std::cout << "The maximum limit of unsigned char data type : " << static_cast<unsigned int>(UCHAR_MAX) << std::endl;
    std::cout << "The minimum limit of short data type : " << SHRT_MIN << std::endl;
    std::cout << "The maximum limit of short data type : " << SHRT_MAX << std::endl;
    std::cout << "The maximum limit of unsigned short data type : " << USHRT_MAX << std::endl;

    std::cout << "\nCheck the upper and lower limits of floating-point types :\n";
    std::cout << "--------------------------------------------------\n";
    std::cout << "The maximum limit of float data type : " << FLT_MAX << std::endl;
    std::cout << "The minimum limit of float data type : " << -FLT_MAX << std::endl;
    std::cout << "The maximum limit of double data type : " << DBL_MAX << std::endl;
    std::cout << "The minimum limit of double data type : " << -DBL_MAX << std::endl;
    std::cout << "The maximum limit of long double data type : " << LDBL_MAX << std::endl;
    std::cout << "The minimum limit of long double data type : " << -LDBL_MAX << std::endl;

    return 0;
}
