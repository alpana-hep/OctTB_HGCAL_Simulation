#!/bin/bash 

float_scale=3
function float_eval()
{
    local stat=0
    local result=0.0
    if [[ $# -gt 0 ]]; then
        result=$(echo "scale=$float_scale; $*" | bc -q 2>/dev/null)
        stat=$?
        if [[ $stat -eq 0  &&  -z "$result" ]]; then stat=1; fi
    fi
    echo $result
    return $stat
}



energy=( 20 30 50 80 100 120 200 250 300 )

actualEnergy=( 20 30 50 80 100 120 200 250 300 )
spreadE=( 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.  )

beamX=( 32.792465 34.278623 33.846409 33.915978 33.861249 33.819573 33.137400 33.451364 33.216112 )
beamY=( 20.025798 20.452299 20.659685 20.867345 20.796806 20.671064 20.560352 20.424566 20.310643 )
beamSX=( 1.29778 1.091 1.05242 0.944066 0.881709 0.815115 0.375787 0.529465 0.44284 )
beamSY=( 1.37312 1.161 0.942595 0.767335 0.664649 0.5469 0.408783 0.353722 0.358179 )

phi=( 3.659799 3.641493 3.637457 3.636328 3.635932 3.637448 3.641316 3.643557 3.645796 )
theta=( 0.011619 0.012001 0.012071 0.012128 0.012139 0.012171 0.012179 0.012234 0.012223 )

#pid=( 11 211 2212)
#name=( "ele" "pi" "p")

pid=( 2212 )
name=( "p" )


np=${#pid[@]}
ne=${#energy[@]}

for ((ip=0; ip<$np; ip++))
do

    for ((ie=0; ie<$ne; ie++))
    do
#	beamX=$(float_eval "${beamX[$ie]}/10.0")
#	beamY=$(float_eval "${beamY[$ie]}/10.0")
#	beamSX=$(float_eval "${beamSX[$ie]}/10.0")
#	beamSY=$(float_eval "${beamSY[$ie]}/10.0")

	beamX=$(float_eval "${beamX[$ie]}")
	beamY=$(float_eval "${beamY[$ie]}")
	beamSX=$(float_eval "${beamSX[$ie]}")
	beamSY=$(float_eval "${beamSY[$ie]}")
	phi=$(float_eval "${phi[$ie]}") 
	theta=$(float_eval "${theta[$ie]}") 

	part=${pid[$ip]}
	#e=${energy[$ie]}
	e=${actualEnergy[$ie]}
	spreade=$(float_eval "${spreadE[$ie]}*${energy[$ie]}/100")
	#min=${mine[$ie]}
	#max=${maxe[$ie]}
	partname=${name[$ip]}
	echo "particle : energy "$part " "$e
	cp HGCalTBCERN170_cfg.py HGCalTBCERN170_tmp_cfg.py
	#sed s/'MINE'/${min}/g <HGCalTBCERN170_tmp_cfg.py|
	#sed s/'MAXE'/${max}/g | 
	sed s/'MEANP'/${e}/g <HGCalTBCERN170_tmp_cfg.py|
	sed s/'SIGMAP'/${spreade}/g | 
	sed s/'PID'/${part}/g |
	sed s/'PHI'/${phi}/g |
	sed s/'THETA'/${theta}/g |
	sed s/'BEAMX'/${beamX}/g |
	sed s/'BEAMSX'/${beamSX}/g |
	sed s/'BEAMY'/${beamY}/g |
	sed s/'BEAMSY'/${beamSY}/g  > HGCalTBCERN170_${partname}_E${energy[$ie]}_cfg.py
	rm HGCalTBCERN170_tmp_cfg.py 
    
    done
done