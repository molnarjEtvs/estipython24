<!DOCTYPE html>
<html lang="hu">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script> 
</head>
<body>

    <a href="{{route('fooldal')}}">Főoldal</a>
    <a href="{{route('hellobello')}}">Helló</a>

    <div class="container">
        <div class="row">
            <div class="col-6">
                <div>
                    @yield("bal")
                </div>
            </div>
            <div class="col-6">
                <div>
                    @yield("jobb")
                </div>
            </div>
        </div>
    </div>
    

</body>
</html>