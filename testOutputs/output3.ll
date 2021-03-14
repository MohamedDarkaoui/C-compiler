%1 = alloca float, align 4
store float 14.5, float* %a, align 4
%2 = alloca float, align 4
%3 = load float, float* %1, align 4
%4 = add nsw float %3, 12.0
%5 = sub nsw float %4, 2.0
store float %5, float* %2, align 4
%6 = alloca i8, align 1
store i8 112, i8* %c, align 1
%7 = alloca i32, align 4
store i32 -3, i32* %7, align 4
