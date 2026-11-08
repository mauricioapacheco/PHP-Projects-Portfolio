<?
$msg .= "Nome:\t$nome2\n";
$msg .= "E-mail:\t$email2\n";
$msg .= "Mensagem:\t$mensagem2\n";

$cabecalho = "Para: Hotel São Luiz";

mail("contato@example.invalid", "Formulário de Contato do site Hotel São Luiz", $msg, $cabecalho);
?>