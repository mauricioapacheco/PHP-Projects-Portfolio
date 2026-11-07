# Preparar os 100 projetos no repositório público

Os 8 ZIPs foram usados para catalogar o acervo. Os códigos originais já estão em `~/GitHub-Backup/Projetos-PHP`.

## 1. Extrair o catálogo

```bash
mkdir -p ~/MEGA/PROJETOS/php/PHP-Projects-Portfolio
cd ~/MEGA/PROJETOS/php/PHP-Projects-Portfolio
unzip -o ~/Downloads/PHP-Projects-Portfolio_Base_Publica.zip -d .
```

## 2. Incorporar os códigos e mídias em cada pasta pública

```bash
python3 ferramentas/montar_portfolio_php_publico.py \
  ~/GitHub-Backup/Projetos-PHP \
  ~/MEGA/PROJETOS/php/PHP-Projects-Portfolio
```

Serão criadas as pastas `projetos/<nome>/src/`. O script copia todo arquivo que passe nas verificações automáticas, preservando imagens, Flash, CSS, JavaScript, PHP e ASP. E-mails são substituídos por um endereço de demonstração e arquivos com padrões fortes de segredos são bloqueados até correção. Nenhum arquivo original é alterado.

O script também emite um relatório de pendências em `~/Downloads/`, **fora do repositório público**: é só uma lista local de controle para evitar a exposição de segredos. Não será criado um segundo repositório privado.

## 3. Verificar e publicar em lotes

**Não publicar antes de revisar as pendências, as mídias e os direitos de terceiros.** É um acervo histórico volumoso: separar commits e envios por grupos menores de projetos evita um único push grande.
