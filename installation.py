import os
import subprocess
import platform

system = platform.system()
print(f"O sistema e {system}")

directory_path = os.path.dirname(__file__)
os.chdir(directory_path)

try:
    subprocess.run(["python", "-m", "venv", "venv"], check=True)
except subprocess.CalledProcessError as e:
    print(f"Erro ao criar ambiente virtual: {e}")
    exit(1)  # Sair do script em caso de erro

print("Ambiente criado!")

activate_script = os.path.join("venv", "Scripts", "activate") if system == "Windows" else os.path.join("venv", "bin", "activate")

try:
    subprocess.run([activate_script], check=True, shell=True)
except subprocess.CalledProcessError as e:
    print(f"Erro ao ativar ambiente virtual: {e}")
    exit(1)  # Sair do script em caso de erro

print("Ambiente virtual ativado!")

try:
    subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)
except subprocess.CalledProcessError as e:
    print(f"Não foi possível instalar as dependências: {e}")
    exit(1)  # Sair do script em caso de erro

print("Dependencias instaladas com sucesso!")
