<!doctype html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="style.css">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet"
          integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
    <title>Регистрация</title>

</head>
<<!--начало стилей-->
<style>
    /*В общем я решил сделать файл со стилями прямо тут, так как это облегчит вам проверку, так как все будет в одном месте*/

    .form-signin {
        max-width: 50%;
        margin-right: 25%;
        margin-left: 25%;
        margin-bottom: 20px;
    }

    .container {
        margin-top: 50px;
        width: 25% !important;
    }


    p {
        margin-top: 30px;
        font-size: 20px;
    }
</style>
<!--конец стилей-->
<main class="form-signin">

    <form method="post" action="treatment.php">
        <img class="mb-4" src="/docs/5.0/assets/brand/bootstrap-logo.svg" alt="" width="72" height="57">
        <h1 class="h3 mb-3 fw-normal">Регистрация</h1>
        <!--            ввод почты-->
        <label for="inputEmail" class="visually-hidden"></label>
        <input name="all[]" type="email" id="inputEmail" class="form-control mb-2" placeholder="Почта" required=""
               autofocus="">

        <!--        ввод пароля-->
        <label for="inputPassword" class="visually-hidden"></label>
        <input name="all[]" type="password" id="inputPassword" class="form-control mb-2" placeholder="Пароль"
               required="">

        <div class="checkbox mb-3">
        </div>
        <button class="w-100 btn btn-lg btn-primary" type="submit">Создать аккаунт</button>
    </form>

</main>

</html>