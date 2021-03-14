%1 = alloca i32, align 4
store i32 3, i32* %1, align 4
%2 = alloca i32, align 4
%3 = load i32, i32* %1, align 4
%4 = load i32, i32* %1, align 4
%5 = sdiv i32 %4, 2
%6 = mul nsw i32 %3, %5
%7 = add nsw i32 14, %6
store i32 %7, i32* %2, align 4
%8 = alloca float, align 4
%9 = load i32, i32* %1, align 4
%10 = sitofp i32 %9 to float
store float %10, float* %8, align 4
%11 = alloca i8, align 1
store i8 47, i8* %11, align 1
