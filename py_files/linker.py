from llvmlite import ir
import subprocess

def compile_and_link(ir_file):
    # Generate Bitcode from LLVM IR
    subprocess.run(["/opt/homebrew/opt/llvm/bin/llvm-as", ir_file, "-o", "output.bc"])

    # Link and compile into executable
    subprocess.run(["clang", "output.bc", "-o", "output_executable"])

    # Run the executable
    subprocess.run(["./output_executable"])