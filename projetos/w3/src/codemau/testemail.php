<?php

$headers = "MIME-Version: 1.0\n";
$headers .= "Content-type: text/html; charset=iso-8859-1\n";
$headers .= "From: WebMaster <contato@example.invalid>\n";
$headers .= "Return-Path: <contato@example.invalid>\n";
mail("contato@example.invalid", "Assunto de teste", "Mensagem de teste", $headers) OR DIE ("Mensagem não enviada");
echo "Mensagem enviada com sucesso";

?>
