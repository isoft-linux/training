/* 
 * Copyright (C) 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn>
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

#include <iostream>
#include <bitset>

#define N sizeof(int) * 8

int main(int argc, char* argv[]) 
{
    int x = argv[1] ? atoi(argv[1]) : 2;
    int y = 3;

    std::cout << "x = " << x << std::endl;
    std::bitset<N> x2(x);
    std::cout << "x(2)  = " << x2 << std::endl;
    std::bitset<N> y2(y);
    std::cout << "y(2)  = " << y2 << std::endl;
    std::cout << "----------------------------------------------" << std::endl;
    std::bitset<N> oR(x | y);
    std::cout << "x | y = " << oR << std::endl;
    std::bitset<N> xoR(x ^ y);
    std::cout << "x ^ y = " << xoR << std::endl;
    return 0;
}
