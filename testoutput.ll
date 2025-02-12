; ModuleID = "my_module"
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"main"()
{
entry:
  %"multmp" = mul i32 3, 3
  %"addtmp" = add i32 12, %"multmp"
  ret i32 %"addtmp"
}
