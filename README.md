# Chronoscp - Website Mirror Tool

### тσσℓ мα∂є ву ¢няσиσѕ

ChronoSCP é uma ferramenta poderosa para **clonar e armazenar sites**, permitindo que profissionais de **Segurança da Informação** analisem aplicações web, realizem auditorias e preservem conteúdo de forma segura.

## 🚀 Objetivo da Ferramenta

A ferramenta foi desenvolvida com foco em:
- 🛡 **Testes de Segurança e Auditoria Web** - Clonagem para análise de vulnerabilidades.
- 📂 **Arquivamento e Preservação** - Backup de páginas importantes.
- 🔍 **Engenharia Reversa** - Estudo da estrutura de aplicações web.
- 🏴‍☠️ **Simulação de Phishing** - Testes internos para conscientização de segurança.
- 🏗 **Ambientes Offline** - Execução de aplicações sem conexão com a web.

## 📌 Recursos

✅ Download completo de um site com **todos os arquivos essenciais**.
✅ Mantém links internos ajustados automaticamente.
✅ Suporte a **HTML, CSS, JS, imagens e fontes**.
✅ Funciona em **Linux e macOS** (Windows pode exigir ajustes).
✅ Exibe logs detalhados em tempo real.

## 📥 Instalação

1️⃣ **Clone este repositório**
```bash
 git clone https://github.com/shacrony/chronoscp
 cd chronoscp
```

2️⃣ **Dê permissão de execução**
```bash
chmod +x chronoscp.py
```

3️⃣ **Instale o Wget (caso não tenha)**
```bash
# Debian/Ubuntu
sudo apt install wget

# Arch Linux
sudo pacman -S wget

# macOS
brew install wget
```

## 🛠 Como Usar

1️⃣ **Execute o script**
```bash
python3 chronoscp.py
```

2️⃣ **Insira os dados solicitados**
```bash
🔗 Digite a URL do site: https://exemplo.com
📂 Nome da pasta para salvar os arquivos: exemplo_site
```

3️⃣ **Aguarde o processo**
O download será iniciado e os arquivos serão armazenados conforme a estrutura original do site.

## 🖥 Exemplo de Saída
```
--2025-02-13 19:54:14--  https://exemplo.com
Resolving exemplo.com (exemplo.com)... 192.168.1.1
Connecting to exemplo.com|192.168.1.1|:443... connected.
HTTP request sent, awaiting response... 200 OK
Saving to: 'exemplo.com/index.html'
```
## ⚠️ Aviso Legal

Esta ferramenta **não deve ser utilizada para fins ilegais ou não autorizados**. O uso indevido pode violar **leis de privacidade e segurança digital**. Utilize apenas para **fins educacionais, auditoria de segurança e análise legítima**.

## 📜 Licença

Esta ferramenta é distribuída sob a licença **MIT**. Sinta-se livre para contribuir e melhorar o projeto!

---
### 💡 **Dúvidas ou sugestões?**
Entre em contato ou contribua com melhorias neste repositório! 🚀
