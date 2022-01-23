# My model trains?  
We know we can't but... we want. This package allows you to regress your loss function with 2 lines of code:
```
import my_model_trains as mmt

regression = mmt.plot_and_regress(np.arange(1, 1 + len(values)), values, 'SDR estimation 50 points', 'epochs', 'SDR',
                                  regressors=['natural_log', 'power_law'], verbose=True, n_values=1200)
plt.show()
```
```
Natural log: A = 1.8883062635915384, B = 1.7362624973685172, R^2 = 3.744796929596155
Power law: A = 3.169713596274487, B = 0.2575654072696419, R^2 = 7.63353926057481
Natural log: A = 1.191823982143853, B = 4.667963014944526, R^2 = 14.247145407884146
Power law: A = 5.316001879233005, B = 0.13215287499090037, R^2 = 19.166739574852727
```  
![imagen](https://user-images.githubusercontent.com/32466310/150661605-badf20aa-fe55-4289-aa57-c6440454266f.png)  
## Wooow! My metrics are gonna be soo good  
Now we face the reality :D  
![imagen](https://user-images.githubusercontent.com/32466310/150661620-d56fe990-3557-47c6-a124-72192b53f335.png)  
