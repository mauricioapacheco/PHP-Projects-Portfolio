<?php
$recipient = "contato@example.invalid";

$subject = "Formulário Site Agrobio";

$nome1 = utf8_decode($nome);
$email1 = utf8_decode($email);
$mensagem1 = utf8_decode($mensagem);

$msg = "Nome: $nome1\n\nE-mail: $email1\n\nMensagem: $mensagem1";

$mailheaders = "From: contato@example.invalid";

mail("$recipient", "$subject", "$msg", "$mailheaders");
?>