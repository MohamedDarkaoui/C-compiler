@.strs = private unnamed_addr constant [3 x i8] c"%s\00", align 1
@.stri = private unnamed_addr constant [3 x i8] c"%i\00", align 1
@.strd = private unnamed_addr constant [3 x i8] c"%d\00", align 1
@.strf = private unnamed_addr constant [3 x i8] c"%f\00", align 1
@.strc = private unnamed_addr constant [3 x i8] c"%c\00", align 1
declare i32 @printf(i8*, ...) #1

define i32 @main() #0 {
%.1 = alloca i32, align 4
store i32 0, i32* %.1, align 4
br label %label0

label0:
%.2 = load i32, i32* %.1, align 4
%.3 = icmp slt i32 %.2, 10
br i1 %.3, label %label1, label %label2

label1:
%.5 = load i32, i32* %.1, align 4
%.4 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.stri, i32 0, i32 0), i32 %.5)
%.6 = load i32, i32* %.1, align 4
%.7 = add nsw i32 %.6, 1
store i32 %.7, i32* %.1, align 4
br label %label0
%.8 = load i32, i32* %.1, align 4
%.9 = add nsw i32 %.8, 1
store i32 %.9, i32* %.1, align 4
br label %label0

label2:
ret i32 0}
