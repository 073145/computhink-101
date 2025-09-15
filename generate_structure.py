import os

# --- CONFIGURAÇÃO ---
# Defina a estrutura completa do repositório aqui.
# Adicione ou remova módulos, temas e exercícios conforme desejar.
REPO_STRUCTURE = {
    "00-Language-Playground": {
        "README": "# 00 - Language Playground\n\nGuia rápido e sintaxe básica para cada linguagem.",
        "languages": [
            "c_cpp", "rust", "python", "java", "go", "csharp", "ruby",
            "typescript", "dart", "elixir", "haskell", "javascript",
            "julia-lang", "lua-lang", "php", "r-lang"
        ]
    },
    "01-Algoritmos-Universais": {
        "README": "# 01 - Algoritmos Universais\n\nA base da lógica e eficiência.",
        "sub_themes": {
            "sorting-algorithms": {
                "README": "# Algoritmos de Ordenação",
                "exercises": ["01.1.1-bubble-sort", "01.1.2-quick-sort", "01.1.3-merge-sort"]
            },
            "search-algorithms": {
                "README": "# Algoritmos de Busca",
                "exercises": ["01.2.1-linear-search", "01.2.2-binary-search"]
            }
        }
    },
    "02-Estruturas-de-Dados-Fundamentais": {
        "README": "# 02 - Estruturas de Dados Fundamentais\n\nAs formas de organizar e gerenciar dados.",
        "sub_themes": {
            "linked-lists": {
                "README": "# Listas Encadeadas",
                "exercises": ["02.2.1-singly-linked-list", "02.2.2-doubly-linked-list"]
            },
            "hashmaps-and-dictionaries": {
                "README": "# Hashmaps e Dicionários",
                "exercises": ["02.4.1-basic-hashmap-implementation"]
            }
        }
    },
    "03-Sistemas-e-Baixo-Nivel": {
        "README": "# 03 - Sistemas e Baixo Nível\n\nMergulhando no controle direto de hardware e recursos do sistema operacional."
    },
    "04-Computacao-Cientifica-e-Analise-de-Dados": {
        "README": "# 04 - Computação Científica e Análise de Dados\n\nAplicando o pensamento computacional para modelar e simular."
    },
    "05-Scripts-Automacao-Web-e-Multimidia": {
        "README": "# 05 - Scripts, Automação, Web e Multimídia\n\nFoco em interação, automação e criatividade."
    },
    "06-InfoSec-e-Privacidade-Computacional": {
        "README": "# 06 - InfoSec e Privacidade Computacional\n\nExplorando o lado da segurança."
    }
}

LANGUAGES = [
    "python", "rust", "c_cpp", "java", "go", "csharp", "ruby",
    "typescript", "dart", "elixir", "haskell", "javascript",
    "julia-lang", "lua-lang", "php", "r-lang"
]

README_EXERCISE_TEMPLATE = """# Exercício: {title}

### 🎯 Objetivo
[Descreva o objetivo do exercício aqui.]

### 📝 Descrição do Problema
[Descreva o problema a ser resolvido aqui.]

### 🧠 Conceitos Chave
- Conceito 1
- Conceito 2

### 📥 Exemplo de Entrada e Saída
- Entrada: `...` -> Saída: `...`

### 🚀 Desafio Adicional (Bônus)
[Adicione um desafio extra aqui.]

### 📚 Discussão
[Discuta as nuances da implementação em diferentes linguagens.]
"""

def create_file(path, content=""):
    """Cria um arquivo com conteúdo, garantindo que o diretório exista."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Created: {path}")

def main():
    """Função principal para gerar a estrutura."""
    for module_name, module_content in REPO_STRUCTURE.items():
        # Cria o README do módulo principal
        create_file(os.path.join(module_name, "README.md"), module_content["README"])

        # Lida com o Language Playground de forma especial
        if module_name == "00-Language-Playground":
            for lang in module_content["languages"]:
                lang_path = os.path.join(module_name, lang)
                create_file(os.path.join(lang_path, ".gitkeep")) # Cria pasta da linguagem
            continue # Pula para o próximo módulo

        # Lida com outros módulos
        if "sub_themes" in module_content:
            for theme_name, theme_content in module_content["sub_themes"].items():
                theme_path = os.path.join(module_name, theme_name)
                create_file(os.path.join(theme_path, "README.md"), theme_content["README"])

                if "exercises" in theme_content:
                    for exercise_name in theme_content["exercises"]:
                        exercise_path = os.path.join(theme_path, exercise_name)
                        readme_title = exercise_name.replace('-', ' ').title()
                        readme_content = README_EXERCISE_TEMPLATE.format(title=readme_title)
                        create_file(os.path.join(exercise_path, "README.md"), readme_content)

                        # Cria as pastas de linguagem para o exercício
                        for lang in LANGUAGES:
                            create_file(os.path.join(exercise_path, lang, ".gitkeep"))

    print("\nEstrutura de diretórios criada com sucesso!")

if __name__ == "__main__":
    main()