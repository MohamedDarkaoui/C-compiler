@.strs = private unnamed_addr constant [3 x i8] c"%s\00", align 1
@.stri = private unnamed_addr constant [3 x i8] c"%i\00", align 1
@.strd = private unnamed_addr constant [3 x i8] c"%d\00", align 1
@.strf = private unnamed_addr constant [3 x i8] c"%f\00", align 1
@.strc = private unnamed_addr constant [3 x i8] c"%c\00", align 1
declare i32 @printf(i8*, ...) #1
@.str.1 = private unnamed_addr constant [21 x i8] c"Something went wrong\00", align 1
@.str.2 = private unnamed_addr constant [14 x i8] c"Hello world! \00", align 1
@.str.3 = private unnamed_addr constant [14 x i8] c"Hello world! \00", align 1

define i32 @main() #0 {
%.1 = alloca i32, align 4
store i32 5, i32* %.1, align 4
%.2 = load i32, i32* %.1, align 4
%.3 = icmp slt i32 %.2, 5
br i1 %.3, label %label0, label %label1

label0:
%.4 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.strs, i32 0, i32 0), i8* getelementptr inbounds ([21 x i8], [21 x i8]* @.str.1, i32 0, i32 0))
br label %label1

label1:
%.5 = load i32, i32* %.1, align 4
%.6 = icmp sge i32 %.5, 5
br i1 %.6, label %label2, label %label3

label2:
%.7 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.strs, i32 0, i32 0), i8* getelementptr inbounds ([14 x i8], [14 x i8]* @.str.2, i32 0, i32 0))
br label %label3

label3:
%.8 = load i32, i32* %.1, align 4
%.9 = icmp eq i32 %.8, 5
br i1 %.9, label %label4, label %label5

label4:
%.10 = load i32, i32* %.1, align 4
%.11 = icmp ne i32 %.10, 4
br i1 %.11, label %label6, label %label7

label6:
%.12 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.strs, i32 0, i32 0), i8* getelementptr inbounds ([14 x i8], [14 x i8]* @.str.3, i32 0, i32 0))
br label %label7

label7:
br label %label5

label5:
ret i32 1
ret i32 0}
