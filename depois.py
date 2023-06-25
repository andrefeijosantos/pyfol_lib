from command_reader import CommandReader

import pyfol.env.environment as env

if __name__ == "__main__":
    environment = env.ProofEnvironment() # Define um ambiente de prova.

    # Recebe os comandos do usuário.
    reader = CommandReader(environment)
    reader.Execute()