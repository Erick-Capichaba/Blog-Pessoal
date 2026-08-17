# Blog Pessoal

> Projeto desenvolvido originalmente em **2022**, durante meus primeiros estudos de desenvolvimento web com Python.

Este repositório representa uma das minhas primeiras experiências construindo uma aplicação web utilizando **Python, Flask, HTML e CSS**.

O projeto foi preservado em seu estado original como forma de registrar minha evolução como desenvolvedor ao longo dos anos.

---

# Sobre o projeto

A proposta inicial era desenvolver um **blog pessoal utilizando Flask**, explorando conceitos que eu estava aprendendo naquele período, como:

* criação de rotas com Flask;
* renderização de páginas utilizando templates;
* organização de arquivos estáticos;
* integração entre Python e HTML;
* navegação entre diferentes páginas;
* criação inicial de uma área para publicação de posts.

O projeto não chegou a ser finalizado e algumas funcionalidades permaneceram em estágio inicial de desenvolvimento.

Decidi preservar o código como ele foi escrito na época porque acredito que projetos antigos também contam uma parte importante da trajetória de um desenvolvedor.

---

# Tecnologias utilizadas

**Back-end**

`Python` • `Flask`

**Front-end**

`HTML` • `CSS`

**Outros**

`Jinja2` • `Git` • `GitHub`

---

# Estrutura do projeto

```text
Blog-Pessoal/
│
├── Site.py
│
├── static/
│   └── imagens e arquivos estáticos
│
└── templates/
    ├── HomepageViews.html
    ├── ContatosViews.html
    ├── Aboutviews.html
    └── PostViews.html
```

O arquivo `Site.py` contém a aplicação Flask e suas rotas, enquanto os arquivos HTML são renderizados através da pasta `templates`.

---

# Executando o projeto localmente em 2026

Em 2026, recuperei este repositório e executei novamente o projeto pela primeira vez desde sua criação.

Como o projeto foi desenvolvido utilizando versões de Python e Flask disponíveis em 2022, foi necessário preparar um ambiente atual para executá-lo.

# 1. Clone o repositório

```bash
git clone https://github.com/Erick-Capichaba/Blog-Pessoal.git
```

Entre na pasta do projeto:

```bash
cd Blog-Pessoal
```

---

# 2. Crie um ambiente virtual

No Windows:

```bash
py -m venv .venv
```

Ative o ambiente:

```bash
.venv\Scripts\activate
```

Após a ativação, o terminal deverá exibir algo semelhante a:

```text
(.venv) C:\...\Blog-Pessoal>
```

---

# 3. Instale o Flask

Como o projeto original não possui um arquivo `requirements.txt`, o Flask pode ser instalado diretamente:

```bash
py -m pip install flask
```

---

# 4. Compatibilidade com versões atuais do Python

Ao executar o projeto originalmente com:

```bash
py Site.py
```

foi apresentado o seguinte erro:

```text
ModuleNotFoundError: No module named 'distutils'
```

Isso acontece porque o projeto possuía, na primeira linha de `Site.py`:

```python
from distutils.log import debug
```

O módulo `distutils`, disponível quando o projeto foi desenvolvido, foi posteriormente removido das versões modernas do Python.

Essa importação não é utilizada pelo restante da aplicação.

Para conseguir executar o projeto em um ambiente Python atual, foi necessário **remover localmente essa linha**:

```python
from distutils.log import debug
```

> Esse ajuste foi realizado apenas para permitir a execução com uma versão moderna do Python. O objetivo deste repositório continua sendo preservar o projeto e sua estrutura original, e não modernizar seu código.

---

# 5. Execute a aplicação

Com o ambiente virtual ativado:

```bash
py Site.py
```

O Flask inicia o servidor de desenvolvimento:

```text
* Running on http://127.0.0.1:5000
```

A aplicação pode então ser acessada pelo navegador em:

```text
http://127.0.0.1:5000
```

---

# Um projeto preservado no tempo

Este projeto **não representa meu nível técnico atual**.

Ele representa meu conhecimento e minha experiência naquele momento da minha trajetória, em **2022**.

Em vez de reestruturar o código, corrigir sua arquitetura ou transformá-lo em uma aplicação moderna, escolhi preservá-lo.

O objetivo é permitir que este repositório funcione como um registro real da minha evolução.

Não apenas mostrando o que sei fazer hoje, mas também **onde comecei**.

---

# 📈 2022 → 2026

# 2022 — Blog Pessoal

`Python` → `Flask` → `HTML` → `CSS`

Um dos meus primeiros projetos utilizando Python para desenvolvimento web.

Foi aqui que comecei a trabalhar com conceitos como rotas, templates, páginas dinâmicas e estruturação de aplicações Flask.

# ↓

# 2026 — Novo projeto

Em 2026, decidi revisitar esta ideia.

Mas, em vez de reconstruir ou modernizar este repositório, escolhi um caminho diferente:

**preservar o projeto original e desenvolver um novo blog completamente do zero.**

O objetivo será aplicar os conhecimentos, ferramentas e práticas que adquiri ao longo dos anos e permitir uma comparação direta entre dois momentos diferentes da minha trajetória como desenvolvedor.

> O repositório do novo projeto será adicionado aqui quando seu desenvolvimento for iniciado.

---

# Autor

**Erick Capichaba**

GitHub: [github.com/Erick-Capichaba](https://github.com/Erick-Capichaba)

---

# Por que manter este projeto?

Porque um portfólio não precisa mostrar apenas resultados atuais.

Ele também pode mostrar **evolução**.

Este repositório registra onde eu estava em 2022.

O próximo mostrará onde estou agora.
