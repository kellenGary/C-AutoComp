from llvmlite import binding

def generate(module):
    binding.initialize()
    binding.initialize_native_target()
    binding.initialize_native_asmprinter()

    target = binding.Target.from_default_triple()
    target_machine = target.create_target_machine()

    llvm_ir = str(module)
    llvm_module = binding.parse_assembly(llvm_ir)
    llvm_module.verify()

    # JIT Compile
    engine = binding.create_mcjit_compiler(llvm_module, target_machine)
    engine.finalize_object()

    # Save as object file or execute
    with open("output.o", "wb") as obj_file:
        obj_file.write(target_machine.emit_object(llvm_module))
