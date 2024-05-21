<?php

use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return view('welcome');
})->name('fooldal');

Route::get('/hellodffdg', function () {
    return view('hello');
})->name("hellobello");
