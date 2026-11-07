#!/usr/bin/env python3
"""Prepara cópia de publicação de TODOS os projetos históricos, sem modificar a origem.

Uso: python3 montar_portfolio_php_publico.py PASTA_ORIGINAL PASTA_PORTFOLIO
O resultado é CANDIDATO à publicação, NÃO uma garantia de anonimização.
"""
from __future__ import annotations

import csv
import os
import re
import shutil
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path

EXTENSOES_BLOQUEADAS = {
    '.mdb', '.accdb', '.db', '.sqlite', '.sqlite3', '.bak', '.backup',
    '.dump', '.log', '.pem', '.key', '.p12', '.pfx', '.kdbx',
    '.zip', '.rar', '.7z', '.tar', '.gz', '.tgz', '.sql.gz',
    '.sql',  # dumps podem incluir dados pessoais; esquemas devem ser revisados separadamente
}
NOMES_BLOQUEADOS = {
    '.env', '.htpasswd', '.npmrc', 'id_rsa', 'id_ed25519',
    'credentials.json', 'secrets.json', 'web.config',
}
DIRETORIOS_BLOQUEADOS = {'.git', '.svn', '.hg', '__pycache__', 'node_modules'}
EXTENSOES_TEXTO = {
    '.php', '.php3', '.php4', '.php5', '.phtml', '.inc', '.asp', '.aspx',
    '.htm', '.html', '.css', '.js', '.json', '.xml', '.txt', '.md', '.ini',
    '.config', '.yml', '.yaml', '.tpl', '.cgi', '.pl', '.py', '.cfm',
    '.htaccess', '.htpasswd', '.sql', '.properties',
}
EMAIL = re.compile(rb'(?i)\b[a-z0-9_.+%-]+@[a-z0-9.-]+\.[a-z]{2,}\b')
SEGREDOS = [
    ('senha_litoral', re.compile(
        rb'''(?ix)\b(?:db_?pass(?:word)?|mysql_?pass(?:word)?|password|passwd|pwd|senha|secret|api_?key|access_?key)\s*(?:=|=>|:)\s*['\"][^'\"\r\n]{2,}['\"]''')),
    ('senha_dsn', re.compile(rb'(?i)\b(?:pwd|password)\s*=\s*[^&;\s\r\n\"\']{3,}')),
    ('login_em_url', re.compile(rb'(?i)(?:mongodb(?:\+srv)?|mysql|postgres(?:ql)?|ftp|sftp)://[^\s/]+:[^\s@/]+@')),
    ('chave_privada', re.compile(rb'-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----')),
]
MAX_ARQUIVO = 95 * 1024 * 1024
MAX_TEXTO = 12 * 1024 * 1024


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit('Uso: python3 montar_portfolio_php_publico.py PASTA_ORIGINAL PASTA_PORTFOLIO')
    origem = Path(sys.argv[1]).expanduser().resolve()
    portfolio = Path(sys.argv[2]).expanduser().resolve()
    if not origem.is_dir():
        raise SystemExit(f'Origem inexistente: {origem}')
    if not (portfolio / 'README.md').is_file() or not (portfolio / 'projetos').is_dir():
        raise SystemExit('Extraia primeiro o pacote de documentação em PASTA_PORTFOLIO.')
    if portfolio == origem or origem in portfolio.parents or portfolio in origem.parents:
        raise SystemExit('Origem e destino devem ser locais separados.')
    projetos = [p for p in sorted(origem.iterdir()) if p.is_dir() and not p.is_symlink() and p.name not in DIRETORIOS_BLOQUEADOS]
    existentes = [p for p in projetos if (portfolio / 'projetos' / p.name / 'src').exists()]
    if existentes:
        raise SystemExit(f'A pasta src já existe em {len(existentes)} projetos. Use uma cópia limpa do catálogo, para não misturar versões.')

    resumo = Counter()
    problemas: list[tuple[str, str]] = []
    relatorio = Path.home() / 'Downloads' / f'PHP_AUDITORIA_LOCAL_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'

    for projeto in projetos:
        destino_raiz = portfolio / 'projetos' / projeto.name / 'src'
        destino_raiz.mkdir(parents=True, exist_ok=True)
        resumo['projetos'] += 1
        for raiz, dirs, arquivos in os.walk(projeto, followlinks=False):
            dirs[:] = [d for d in dirs if d not in DIRETORIOS_BLOQUEADOS and not (Path(raiz) / d).is_symlink()]
            for nome in arquivos:
                arquivo = Path(raiz) / nome
                relativo = arquivo.relative_to(origem).as_posix()
                try:
                    if arquivo.is_symlink():
                        motivos = ['link_simbolico']
                    elif arquivo.stat().st_size > MAX_ARQUIVO:
                        motivos = ['maior_que_95_MiB']
                    elif arquivo.name.lower() in NOMES_BLOQUEADOS or arquivo.suffix.lower() in EXTENSOES_BLOQUEADAS:
                        motivos = ['banco_backup_ou_segredo']
                    else:
                        motivos = []
                    if motivos:
                        resumo['bloqueados'] += 1
                        problemas.append((relativo, '+'.join(motivos)))
                        continue
                    alvo = destino_raiz / arquivo.relative_to(projeto)
                    alvo.parent.mkdir(parents=True, exist_ok=True)
                    if arquivo.suffix.lower() in EXTENSOES_TEXTO and arquivo.stat().st_size <= MAX_TEXTO:
                        dados = arquivo.read_bytes()
                        if b'\0' in dados:
                            resumo['bloqueados'] += 1
                            problemas.append((relativo, 'arquivo_binario_com_extensao_texto'))
                            continue
                        achados = [titulo for titulo, padrao in SEGREDOS if padrao.search(dados)]
                        if achados:
                            resumo['bloqueados'] += 1
                            problemas.append((relativo, ','.join(achados)))
                            continue
                        dados, qtd = EMAIL.subn(b'contato@example.invalid', dados)
                        if qtd:
                            resumo['emails_substituidos'] += qtd
                        alvo.write_bytes(dados)
                        shutil.copystat(arquivo, alvo)
                    else:
                        shutil.copy2(arquivo, alvo)
                        if arquivo.suffix.lower() in {'.swf', '.fla', '.pdf', '.jpg', '.jpeg', '.png', '.gif'}:
                            resumo['midias_para_inspecao'] += 1
                    resumo['copiados'] += 1
                except OSError as exc:
                    resumo['erros'] += 1
                    problemas.append((relativo, f'erro_{type(exc).__name__}'))
    relatorio.parent.mkdir(parents=True, exist_ok=True)
    with relatorio.open('w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['arquivo_original', 'motivo_para_revisar_antes_de_publicar'])
        writer.writerows(problemas)
    print(f"Projetos com pasta pública: {resumo['projetos']}")
    print(f"Arquivos copiados para projeto público: {resumo['copiados']}")
    print(f"Arquivos que exigem correção/seleção: {resumo['bloqueados']}")
    print(f"Endereços de e-mail substituídos: {resumo['emails_substituidos']}")
    print(f"Mídias que exigem inspeção visual/licenciamento: {resumo['midias_para_inspecao']}")
    print(f"Erros de cópia: {resumo['erros']}")
    print(f'Relação de pendências para uso local (NÃO incluída no Git): {relatorio}')
    print('NÃO execute git push ainda. A triagem automatizada não verifica todos os tipos de dados pessoais/credenciais ou direitos de terceiros.')


if __name__ == '__main__':
    main()
