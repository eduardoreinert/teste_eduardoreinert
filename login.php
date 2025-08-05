<?php
    //definir os dados de login (futuramente seria via BD)
    $usuario_correto="admin";
    $senha_correta="123456";

    //dados do formulario
    $usuario=$_POST['username'] ?? '';
    $senha=$_POST['password'] ?? '';

    //verifica se estao corretos
    if($usuario===$usuario_correto && $senha===$senha_correta){
        header("Location: index.html");
        exit;
    } else {
        //redireciona de volta com erro
        header("Location: login.html?error=1");
        exit;
    }
?>