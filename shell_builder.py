from commands import ChangeDirectory, Clear, Exit, Export, List, PrintEnv, Speak


def build(shell):
    shell.add_command(ChangeDirectory(shell))
    shell.add_command(Clear(shell))
    shell.add_command(Exit(shell))
    shell.add_command(Export(shell))
    shell.add_command(List(shell))
    shell.add_command(PrintEnv(shell))
    shell.add_command(Speak(shell))
