# alta
# Copyright © 2023, Jignas Paturu

$list =((netsh.exe wlan show profiles) -match '\s{2,}:\s') -replace '.*:\s' , ''
$j=0
$pass= [System.Collections.ArrayList]::new()

do {
    $temp= [System.Collections.ArrayList]::new()
    $i=$list[$j]
    $temp=$pass.Add((((netsh.exe wlan show profiles name=$i key=clear) -match '\s{2,}:\s') -replace '.*:\s' , '')[-6])
    $j=$j+1  
    
}
until (
    $i -notin $list
)

$data = for($i=0; $i -lt $list.Count; $i++){
    [pscustomobject]@{
        username = $list[$i]
        password = $pass[$i]
    }
}

$data | Format-Table -AutoSize
