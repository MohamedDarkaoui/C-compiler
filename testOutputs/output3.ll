
define i32 @main() #0 {
%.1 = alloca [5 x i8], align 16
%.2 = getelementptr inbounds [5 x i8], [5 x i8]* %.1, i64 0, i64 0
store i8 97, i8* %.2, align 1
%.3 = getelementptr inbounds [5 x i8], [5 x i8]* %.1, i64 0, i64 1
store i8 98, i8* %.3, align 1
%.4 = getelementptr inbounds [5 x i8], [5 x i8]* %.1, i64 0, i64 2
store i8 99, i8* %.4, align 1
%.5 = getelementptr inbounds [5 x i8], [5 x i8]* %.1, i64 0, i64 3
store i8 100, i8* %.5, align 1
%.6 = getelementptr inbounds [5 x i8], [5 x i8]* %.1, i64 0, i64 4
store i8 101, i8* %.6, align 1
%.7 = getelementptr inbounds [5 x i8], [5 x i8]* %.1, i64 0, i64 2
store i8 100, i8* %.7, align 1
ret i32 0
ret i32 0}
