<?php
sleep(2);
header('Content-Type: application/json');
$responseData = [
  'id' => 123,
  'termek' => 'termek_neve',
  'osszeg' => 10000
];
echo json_encode($responseData);
?>
