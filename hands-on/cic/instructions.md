Instructions to run ROM workflow in MN4
=======================================

1. Select an account

Go to this link and select one account writting your name besides the selected username
  
https://docs.google.com/spreadsheets/d/1rLULEtYyK94wFUAsUVvCOz3LeBOUTVfWNXx2ZCThWSE/edit?usp=sharing

2. Access MN4

```
user@localhost:~> ssh -X nct01XXX@mn1.bsc.es
```

3. Copy the necessary files

```
nct01XXX@login1:~> cp -R /gpfs/projects/nct00/nct00012/mn4 .
```

4. You can overwrite the file with the downloaded image

```
user@localhost:~> scp reduce_order_model_skylake_v_latest.sif nct01XXX@mn1.bsc.es:mn4/
```

5. Run the workflow

```
nct01XXX@login1:~> cd mn4
nct01XXX@login1:~/mn4>./launch_simulation.sh 
```
