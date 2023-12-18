import chime
import SendMessage as sm


def get_short_entry(macd_values, ema_values, stoch_values, inst_data2, fig, go):
    
    ema_min = ema_values[0][99]-ema_values[0][99]*(0.6/100)
    if(ema_min<=inst_data2['open'][299]<=ema_values[0][99]):
        if(macd_values[0][1][99]<=0 and macd_values[0][0][99]<macd_values[0][0][98] and macd_values[0][1][99]<macd_values[0][1][99]):
            if (stoch_values[0][299] < stoch_values[1][299] and stoch_values[0][298]>stoch_values[1][298]):
        
                entry = inst_data2['open'][299]
                time = inst_data2['time'][299]
                fig.add_trace(go.Scatter(
                     x=[time],
                     y=[entry],
                     mode = "markers",
                     marker_symbol="arrow-down",
                     marker_size=10,
                     marker_line_width=1,
                     marker_line_color ="black",
                     marker_color="red"),row=1,col=2) 
                chime.success()
                      
        
    return
    
def get_long_entry(macd_values, ema_values, stoch_values, inst_data2, fig, go):
    
    ema_min = ema_values[0][99]-ema_values[0][99]*(0.6/100)
    if(ema_min<=inst_data2['open'][299]<=ema_values[0][99]):
        if(macd_values[0][1][99]<=0 and macd_values[0][0][99]<macd_values[0][0][98] and macd_values[0][1][99]<macd_values[0][1][99]):
            if (stoch_values[0][299] > stoch_values[1][299] and stoch_values[0][298]<stoch_values[1][298]):
                entry = inst_data2['open'][299]
                time = inst_data2['time'][299]
                fig.add_trace(go.Scatter(
                                x=[time],
                                y=[entry],
                                mode = "markers",
                                marker_symbol="arrow-up",
                                marker_size=10,
                                marker_line_width=1,
                                marker_line_color ="black",
                                marker_color="green"),row=1,col=2)
                chime.success()
                   
        
    return 


       



