
$list =((netsh.exe wlan show profiles) -match '\s{2,}:\s') -replace '.*:\s' , ''

$j=0
$pass= [System.Collections.ArrayList]::new()


do {
    $temp= [System.Collections.ArrayList]::new()
    $i=$list[$j]
    $temp=$pass.Add((((netsh.exe wlan show profiles name=$i key=clear) -match '\s{2,}:\s') -replace '.*:\s' , '')[-6])
    
    $j=$j+1
  

    
} until (
    $i -notin $list
)
Write-Output "`n Username`t`t`tPass"
$k=0
do {
    
    $res= $res+($list[$k]+"`t"+"`t"+"`t"+"`t"+$pass[$k]+"`n")
    $k=$k+1
} until (
    $k -eq $j
)
 
$res