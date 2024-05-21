<?php
session_start();
$szervernev = "localhost";
$felhasznalonev = "root";
$jelszo = "";
$dbnev = "kormos";

$kapcsolat = mysqli_connect($szervernev,$felhasznalonev,$jelszo,$dbnev);

if(!$kapcsolat){
    die("Adatbáziskapcsolódás sikertelen: ".mysqli_connect_error());
}

if($_SERVER['REQUEST_METHOD'] == "POST"){

    $kormosnev = trim($_POST['kormos']);
    $telefonszam = trim($_POST['telefonszam']);
    $foglalasidopont = trim($_POST['idopont']);
    $megjegyzes = trim($_POST['komment']);

    $sql = "INSERT INTO `foglalasok`(`kormos_nev`, `telefonszam`, `foglalas_idopont`, `megjegyezes`) VALUES 
    ('".$kormosnev."',
    '".$telefonszam."',
    '".$foglalasidopont."',
    '".$megjegyzes."');";

    mysqli_query($kapcsolat,$sql);

    $_SESSION['sikeres'] = true;
    header("Location: http://localhost/kormos/");
    exit();
}

$utolsokSql = "SELECT * FROM foglalasok WHERE 1 ORDER BY foglalas_id DESC LIMIT 0,5;";
$utolsoRes = mysqli_query($kapcsolat,$utolsokSql);

?>
<!doctype html>
<html lang="hu">
<head>
    <title>Körmös fogalás</title>
    <!-- Required meta tags -->
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />

    <!-- Bootstrap CSS v5.2.1 -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous" />
</head>

<body>

    <div class="container">
        <div class="row">
            <div class="col-6">
                <div class="rounded p-3" style="background-color: lightpink;">
                <?php
                    if(isset($_SESSION['sikeres']) && $_SESSION['sikeres'] == true){
                        echo "<div class='alert alert-success'>Adatok mentése sikeres!</div>";
                        unset($_SESSION['sikeres']);
                    }
                ?>
                <form method="post">
                        <div>
                            <label for="kormos">Válaszd ki a körmöst:</label>
                            <select name="kormos" id="kormos" class="form-select">
                                <option value="Juci">Juci</option>
                                <option value="Joli">Joli</option>
                                <option value="Bianka">Bianka</option>
                            </select>
                        </div>

                        <div class="mt-2">
                            <label for="telefonszam">Telefonszám: </label>
                            <input type="tel" name="telefonszam" id="telefonszam" class="form-control">
                        </div>

                        <div class="mt-2">
                            <label for="idopont">Válaszd ki az időpontot:</label>
                            <input type="datetime-local" name="idopont" id="idopont" class="form-control">
                        </div>

                        <div class="mt-2">
                            <label for="komment">Írd le mit szeretnél: </label>
                            <textarea name="komment" id="komment" class="form-control"></textarea>
                        </div>

                        <div class="mt-2">
                            <button type="submit" class="btn btn-danger w-100">Foglalás elküldése</button>
                        </div>
                    </form>
                </div>
            </div>
            <div class="col-6">
                <div class="table-responsive">
                    <h2>Eddig rögzített adatok</h2>
                    <table class="table table-light table-striped">
                        <tr>
                            <th>#</th>
                            <th>Körmös neve</th>
                            <th>Telefonszám</th>
                            <th>Időpont</th>
                            <th>Megjegyzés</th>
                        </tr>
                        <?php
                            while($sor = mysqli_fetch_assoc($utolsoRes)){
                                echo "<tr>
                                        <td>".$sor['foglalas_id']."</td>
                                        <td>".$sor['kormos_nev']."</td>
                                        <td>".$sor['telefonszam']."</td>
                                        <td>".$sor['foglalas_idopont']."</td>
                                        <td>".$sor['megjegyezes']."</td>
                                    </tr>";
                            }
                        ?>
                        
                    </table>
                </div>
            </div>
        </div>
    </div>


    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.min.js"
        integrity="sha384-BBtl+eGJRgqQAUMxJ7pMwbEyER4l1g+O15P+16Ep7Q9Q+zqX6gSbd85u4mG4QzX+"
        crossorigin="anonymous"></script>
</body>

</html>