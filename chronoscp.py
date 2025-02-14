import os
import subprocess

print("""

   тσσℓ мα∂є ву ¢няσиσѕ         

""")

def baixar_site(url, destino):
    """Executa o wget para copiar o site conforme a URL fornecida."""
    comando = [
        "wget", "--mirror", "--convert-links", "--adjust-extension", "--page-requisites", "--no-parent",
        "-P", destino, url
    ]
    
    print(f" Iniciando Download do site {url}\n")
    
    try:
        process = subprocess.Popen(comando, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        for line in process.stdout:
            print(line, end="")  
        process.wait()
        
        if process.returncode == 0:
            print("✅ Download concluído! Site copiado para:", destino)
        else:
            print("❌ Erro durante o download. Verifique a saída acima.")
    except Exception as e:
        print(f"❌ Erro: {str(e)}\n")

def main():
    url = input("Digite a URL do site: ").strip()
    destino = input("📂 Nome da pasta para salvar os arquivos: ").strip()
    baixar_site(url, destino)

if __name__ == "__main__":
    main()