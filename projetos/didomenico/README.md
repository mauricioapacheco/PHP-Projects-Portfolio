# didomenico

**Projeto histórico do acervo Casa da Web (2003–2011).** Esta pasta corresponde ao diretório original `didomenico`, preservado como unidade de catalogação.

> A catalogação é baseada em nomes de arquivos e extensões encontrados nos ZIPs. Módulos indicados abaixo são **indícios**, não funcionalidades testadas ou promessas de funcionamento.

## Inventário

| Indicador | Quantidade |
|---|---:|
| Arquivos | 378 |
| Tamanho descompactado aproximado | 2.5 MiB |
| PHP | 239 |
| ASP Clássico | 0 |
| HTML/HTM | 18 |
| JavaScript | 11 |
| CSS | 2 |
| Flash SWF / FLA | 4 / 6 |

**Tecnologias identificadas:** PHP, HTML, CSS, JavaScript, Flash SWF, Flash FLA.

## Módulos identificados preliminarmente

- Galerias ou fotos (indício pelo nome de arquivos)
- Catálogo ou produtos (indício pelo nome de arquivos)
- Publicação de notícias (indício pelo nome de arquivos)
- Enquetes (indício pelo nome de arquivos)
- Cadastro e formulários (indício pelo nome de arquivos)
- Contato e mensagens (indício pelo nome de arquivos)

## Fluxo técnico referencial

```mermaid
flowchart LR
    A[Visitante no navegador] --> B[Interface HTML e JavaScript]
    B --> C[Rotinas PHP do projeto]
    C --> D{Integrações existentes?}
    D --> E[Banco de dados ou serviços, se configurados]
    D --> F[Conteúdo gerado]
    E --> F
    F --> A
```

O fluxograma representa apenas uma **estrutura técnica possível**, não uma arquitetura de produção auditada.

## Código-fonte

Os fontes históricos serão incorporados em `src/` **depois de revisar credenciais, bancos de dados, dados de terceiros e direitos de distribuição**. A cópia pública não deve conter dados operacionais antigos.

## Estado

- [x] Pastas e tecnologias inventariadas
- [ ] Revisão manual de arquivos potencialmente sensíveis
- [ ] Publicação dos fontes selecionados e revisados
- [ ] Testes de execução no ambiente legado
