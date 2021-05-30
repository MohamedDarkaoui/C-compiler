@.strs = private unnamed_addr constant [3 x i8] c"%s\00", align 1
@.stri = private unnamed_addr constant [3 x i8] c"%i\00", align 1
@.strd = private unnamed_addr constant [3 x i8] c"%d\00", align 1
@.strf = private unnamed_addr constant [3 x i8] c"%f\00", align 1
@.strc = private unnamed_addr constant [3 x i8] c"%c\00", align 1
declare i32 @printf(i8*, ...) #1

define i32 @fibonacci(i32) #0 {
%.1 = alloca i32, align 4
store i32 %0, i32* %.1, align 4
%.2 = load i32, i32* %.1, align 4
%.3 = icmp slt i32 %.2, 2
br i1 %.3, label %label0, label %label1

label0:
ret i32 1
br label %label1

label1:
%.5 = load i32, i32* %.1, align 4
%.6 = sub nsw i32 %.5, 1
%.4 = call i32 @fibonacci(i32 %.6)
%.8 = load i32, i32* %.1, align 4
%.9 = sub nsw i32 %.8, 2
%.7 = call i32 @fibonacci(i32 %.9)
%.10 = add nsw i32 %.4, %.7
ret i32 %.10
ret i32 0}

define i32 @main() #0 {
%.11 = alloca i32, align 4
%.12 = call i32 @fibonacci(i32 5)
store i32 %.12, i32* %.11, align 4
%.14 = load i32, i32* %.11, align 4
%.13 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.stri, i32 0, i32 0), i32 %.14)
ret i32 0
ret i32 0}
