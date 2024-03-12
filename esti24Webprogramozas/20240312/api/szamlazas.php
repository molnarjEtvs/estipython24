<?php

sleep(2);
header('Content-Type: application/json');
$postData = json_decode(file_get_contents('php://input'), true);
$responseData = [
  'fizetes_id' => $postData['fizetes_id'],
  'szamlazasi_osszeg' => $postData['osszeg']
];
echo json_encode($responseData);
?>
