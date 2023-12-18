import chime


def get_short_entry(macd_values, ema_values, stoch_values, inst_data2, fig, go):
    
    ema_min = ema_values[0][98]-ema_values[0][98]*(0.6/100)
    if(ema_min<=inst_data2['open'][298]<=ema_values[0][98]):
        if(macd_values[0][0][98]<=0 and macd_values[0][0][98]<macd_values[0][0][97] and macd_values[0][1][98]<macd_values[0][1][97]):
            if (stoch_values[0][297] >70 and stoch_values[0][298] < stoch_values[1][298] and stoch_values[0][297]>stoch_values[1][297]):
        
                entry = inst_data2['close'][298]
                time = inst_data2['time'][298]
                fig.add_trace(go.Scatter(
                     x=[time],
                     y=[entry],
                     mode = "markers",
                     marker_symbol="arrow-down",
                     marker_size=10,
                     marker_line_width=1,
                     marker_line_color ="black",
                     marker_color="red"),row=1,col=2) 
                chime.error()
                      
        

    
def get_long_entry(macd_values, ema_values, stoch_values, inst_data2, fig, go):
    
    ema_max = ema_values[0][98]+ema_values[0][98]*(0.6/100)
    if(ema_values[0][98]<=inst_data2['open'][298]<=ema_max):
        if(macd_values[0][0][98]<=0 and macd_values[0][0][98]>macd_values[0][0][97] and macd_values[0][1][98]>macd_values[0][1][97]):
            if (stoch_values[0][297] < 30 and stoch_values[0][298] > stoch_values[1][298] and stoch_values[0][297]<stoch_values[1][297]):
                entry = inst_data2['close'][298]
                time = inst_data2['time'][298]
                fig.add_trace(go.Scatter(
                                x=[time],
                                y=[entry],
                                mode = "markers",
                                marker_symbol="arrow-up",
                                marker_size=10,
                                marker_line_width=1,
                                marker_line_color ="black",
                                marker_color="green"),row=1,col=2)
                chime.error()
                   
        
   

       



