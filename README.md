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
![imagen](https://user-images.githubusercontent.com/32466310/150661695-d0f78a1b-bc09-4075-91d0-6fcf3acba912.png) 
## Wooow! My metrics are gonna be soo good  
Now we face the reality :D  
![imagen](https://user-images.githubusercontent.com/32466310/150661699-20711c52-4da7-4601-bd8e-6635722d8e34.png)  

In fact if we remove the first data points it's more accurate :)  
![imagen](https://user-images.githubusercontent.com/32466310/150661772-f855373d-d5c3-4ea1-b88e-6e3e95a5833f.png)
