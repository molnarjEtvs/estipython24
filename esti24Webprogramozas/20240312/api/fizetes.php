<?php
sleep(2);
header('Content-Type: application/json');
$postData = json_decode(file_get_contents('php://input'), true);
$responseData = [
  'id' => rand(100,1234),
  'rendeles_id' => $postData['rendeles_id'],
  'osszeg' => $postData['osszeg'] 
];
echo json_encode($responseData);
?>
