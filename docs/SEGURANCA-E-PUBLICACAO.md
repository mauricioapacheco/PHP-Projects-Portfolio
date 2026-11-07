# Cuidados para publicar todos os projetos

O objetivo é ter **as 100 pastas de projetos no mesmo repositório público**, preservando seus códigos e recursos sempre que possível.

A triagem automática identifica riscos, mas **não certifica** que os arquivos estão livres de dados pessoais, credenciais, marcas ou conteúdos de terceiros. Na análise inicial foram encontrados padrões de autenticação/conexão e milhares de e-mails em páginas históricas.

- Substituir senhas, tokens, chaves e credenciais reais antes do primeiro commit público. Se ainda estiverem em uso, revogá-los/rotacioná-los.
- Revisar dumps SQL, bancos e backups antes de decidir se podem ser publicados; preferir esquema e dados fictícios.
- Inspecionar manualmente imagens, PDF, áudios e arquivos Flash SWF/FLA, além da titularidade e licenças de bibliotecas e mídias.
- Manter avisos de segurança: sistemas antigos podem depender de PHP/ASP obsoletos e não foram validados para produção.
- O relatório de pendências gerado no Linux é apenas instrumento de auditoria local e não faz parte do repositório público.
- **Não fazer push antes dessa revisão**, pois apagar segredos em commits posteriores não os remove necessariamente do histórico do Git.
